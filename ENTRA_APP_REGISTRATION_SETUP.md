# Microsoft Entra ID App Registration - Complete Setup Guide

This guide helps you set up Microsoft Entra ID app registration for any use case (Web, SPA, Console, or Service applications).

## 📋 Quick Start: Which Method Should You Use?

| Your Need | Recommended Method |
|-----------|-------------------|
| **I want to use Azure Portal (GUI)** | Follow [Step-by-Step Guide](#step-by-step-azure-portal-method) below |
| **I want to use Azure CLI** | Follow [CLI Method](#azure-cli-method) below |
| **I want Infrastructure as Code (BiceP)** | Follow [IaC Method](#infrastructure-as-code-bicep-method) below |
| **I need code examples** | See [Application Examples](#application-examples) section |

---

## Method 1: Step-by-Step (Azure Portal Method)

### Prerequisites
- Azure subscription (free tier works)
- Azure Portal access: https://portal.azure.com

### Step 1: Navigate to App Registrations
1. Open [Azure Portal](https://portal.azure.com)
2. Search for **"Microsoft Entra ID"**
3. In the left menu, click **"App registrations"**
4. Click **"+ New registration"** at the top

### Step 2: Register Your Application

**Application Name:**
- Enter a descriptive name (e.g., "DAIOF Application")

**Supported Account Types:**
- Choose based on your needs:
  - **Single tenant** - Only users from your organization
  - **Multi-tenant** - Users from multiple organizations
  - **Personal + Org** - Both personal and work accounts

**Redirect URI:**
- **Console/Desktop:** `http://localhost`
- **SPA:** `http://localhost:3000`
- **Web App:** `https://localhost:5001/signin-oidc`

**Click "Register"**

### Step 3: Save Critical Information
On the **Overview** page, copy and save:
- **Application (client) ID** (GUID format)
- **Directory (tenant) ID** (GUID format)

### Step 4: Configure Authentication
1. Click **"Authentication"** in left menu
2. For console apps: Enable **"Allow public client flows"** = YES
3. Add redirect URIs as needed
4. Click **"Save"**

### Step 5: Add API Permissions
1. Click **"API permissions"** in left menu
2. Click **"+ Add a permission"**
3. Select **"Microsoft Graph"**
4. Choose **"Delegated permissions"**:
   - `User.Read` (read user profile) - Already added by default
   - `Mail.Read` (read email)
   - `Calendars.Read` (read calendar)

5. For application permissions (no user context):
   - Click **"Application permissions"**
   - `User.Read.All` (read all users)
   - `Directory.Read.All` (read directory)

6. Click **"Grant admin consent"** if you're an admin

### Step 6: Create Client Secret (For Web Apps/Services)
1. Click **"Certificates & secrets"**
2. Click **"+ New client secret"**
3. Add description and choose expiration (6 months recommended for dev)
4. **Copy the value immediately** - It's only shown once!

### Step 7: Test Your Setup
Open Azure Cloud Shell and run:
```bash
# Set your values
CLIENT_ID="your-client-id-here"
TENANT_ID="your-tenant-id-here"

# Interactive login
az login --scope "https://graph.microsoft.com/.default"

# Get an access token
az account get-access-token --resource "https://graph.microsoft.com"
```

---

## Method 2: Azure CLI Method

### Prerequisites
```bash
# Install Azure CLI if not already installed
# macOS
brew install azure-cli

# Or download from https://aka.ms/installazurecli
```

### Complete Setup Script
Save this as `setup_entra_app.sh`:

```bash
#!/bin/bash

# Configuration
APP_NAME="DAIOF-Application"
REDIRECT_URI="http://localhost"
TENANT_ID="your-tenant-id-here"  # Optional - uses current tenant if omitted

echo "=== Microsoft Entra App Registration Setup ==="

# Login to Azure
echo "Step 1: Logging in..."
az login

# Get current tenant
CURRENT_TENANT=$(az account show --query tenantId -o tsv)
echo "Current Tenant ID: $CURRENT_TENANT"

# Create app registration
echo "Step 2: Creating app registration..."
APP_ID=$(az ad app create \
  --display-name "$APP_NAME" \
  --public-client-redirect-uris "$REDIRECT_URI" \
  --query "appId" -o tsv)

echo "App created with ID: $APP_ID"

# Add Microsoft Graph permissions
echo "Step 3: Adding Microsoft Graph permissions..."
GRAPH_RESOURCE_ID="00000003-0000-0000-c000-000000000000"
USER_READ_ID="e1fe6dd8-ba31-4d61-89e7-88639da4683d"

az ad app permission add --id $APP_ID \
  --api $GRAPH_RESOURCE_ID \
  --api-permissions "$USER_READ_ID=Scope"

# Grant admin consent
echo "Step 4: Granting admin consent..."
az ad app permission admin-consent --id $APP_ID

# Create service principal
echo "Step 5: Creating service principal..."
az ad sp create --id $APP_ID

# Create client secret (for web apps/services)
echo "Step 6: Creating client secret..."
SECRET_OUTPUT=$(az ad app credential reset --id $APP_ID --display-name "cli-secret" --years 1)
CLIENT_SECRET=$(echo "$SECRET_OUTPUT" | jq -r '.password')
echo "Client secret created (save this securely!)"
echo "Secret: $CLIENT_SECRET"

# Save configuration
echo "Step 7: Saving configuration..."
cat > app-registration-config.env <<EOF
APPLICATION_CLIENT_ID=$APP_ID
TENANT_ID=$CURRENT_TENANT
CLIENT_SECRET=$CLIENT_SECRET
REDIRECT_URI=$REDIRECT_URI
EOF

echo "Configuration saved to app-registration-config.env"

# Display summary
echo "=== Setup Complete! ==="
echo "Application (Client) ID: $APP_ID"
echo "Tenant ID: $CURRENT_TENANT"
echo "Redirect URI: $REDIRECT_URI"
echo ""
echo "Next: Configure your application with these values"
```

### Run the Script
```bash
chmod +x setup_entra_app.sh
./setup_entra_app.sh
```

---

## Method 3: Infrastructure as Code (BiceP Method)

### Prerequisites
- Bicep v0.21.1+
- Azure subscription

### Complete BiceP Template
Save this as `entra-app.bicep`:

```bicep
// Entra ID App Registration Template
// Deployment: az deployment sub create --template-file entra-app.bicep

extension 'br:mcr.microsoft.com/bicep/extensions/microsoftgraph/v1.0:1.0.0'

@description('Display name for the application')
param appDisplayName string = 'DAIOF-Application'

@description('Sign-in audience')
@allowed([
  'AzureADMyOrg'
  'AzureADMultipleOrgs'
])
param signInAudience string = 'AzureADMyOrg'

// App Registration
resource appRegistration 'Microsoft.Graph/applications@v1.0' = {
  displayName: appDisplayName
  signInAudience: signInAudience
  
  publicClient: {
    redirectUris: [
      'http://localhost'
    ]
  }
  
  requiredResourceAccess: [
    {
      resourceAppId: '00000003-0000-0000-c000-000000000000' // Microsoft Graph
      resourceAccess: [
        {
          id: 'e1fe6dd8-ba31-4d61-89e7-88639da4683d' // User.Read
          type: 'Scope'
        }
      ]
    }
  ]
}

// Service Principal
resource servicePrincipal 'Microsoft.Graph/servicePrincipals@v1.0' = {
  appId: appRegistration.appId
  displayName: appRegistration.displayName
}

// Outputs
output applicationId string = appRegistration.appId
output objectId string = appRegistration.id
```

### Deploy with Azure CLI
```bash
# Deploy to subscription
az deployment sub create \
  --name "entra-app-deployment" \
  --template-file entra-app.bicep \
  --parameters appDisplayName="DAIOF-Application"

# Get deployment outputs
az deployment sub show \
  --name "entra-app-deployment" \
  --query "properties.outputs"
```

---

## Application Examples

### Python Console App Example

Install dependencies:
```bash
pip install msal requests
```

Create `app.py`:
```python
import msal
import requests
import os

# Configuration from your app registration
CLIENT_ID = os.getenv("APPLICATION_CLIENT_ID", "your-client-id-here")
TENANT_ID = os.getenv("TENANT_ID", "your-tenant-id-here")
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPES = ["User.Read"]

def main():
    # Create MSAL client
    app = msal.PublicClientApplication(
        CLIENT_ID,
        authority=AUTHORITY
    )
    
    # Try to get token from cache
    accounts = app.get_accounts()
    result = None
    
    if accounts:
        result = app.acquire_token_silent(SCOPES, account=accounts[0])
    
    if not result:
        # Interactive authentication
        result = app.acquire_token_interactive(scopes=SCOPES)
    
    if "access_token" in result:
        # Call Microsoft Graph API
        headers = {
            'Authorization': f'Bearer {result["access_token"]}'
        }
        response = requests.get('https://graph.microsoft.com/v1.0/me', headers=headers)
        print("User profile:", response.json())
    else:
        print("Error acquiring token:", result.get("error_description"))

if __name__ == "__main__":
    main()
```

### Node.js Console App Example

Install dependencies:
```bash
npm install @azure/msal-node axios
```

Create `app.js`:
```javascript
const msal = require('@azure/msal-node');
const axios = require('axios');

const config = {
    auth: {
        clientId: process.env.APPLICATION_CLIENT_ID || 'your-client-id-here',
        authority: `https://login.microsoftonline.com/${process.env.TENANT_ID || 'your-tenant-id-here'}`,
    }
};

const scopes = ["User.Read"];

async function main() {
    const pca = new msal.PublicClientApplication(config);
    
    const interactiveRequest = {
        scopes: scopes,
        redirectUri: "http://localhost",
    };
    
    const response = await pca.acquireTokenInteractive(interactiveRequest);
    
    if (response.accessToken) {
        const options = {
            headers: {
                Authorization: `Bearer ${response.accessToken}`
            }
        };
        
        const result = await axios.get('https://graph.microsoft.com/v1.0/me', options);
        console.log("User profile:", result.data);
    }
}

main().catch(err => console.error(err));
```

### C# (.NET) Console App Example

Install package:
```bash
dotnet add package Microsoft.Identity.Client
```

Create `Program.cs`:
```csharp
using Microsoft.Identity.Client;
using System;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    private const string ClientId = "your-client-id-here";
    private const string TenantId = "your-tenant-id-here";
    private static readonly string[] Scopes = new[] { "User.Read" };

    static async Task Main(string[] args)
    {
        var app = PublicClientApplicationBuilder
            .Create(ClientId)
            .WithAuthority(AzureCloudInstance.AzurePublic, TenantId)
            .WithRedirectUri("http://localhost")
            .Build();

        var accounts = await app.GetAccountsAsync();
        AuthenticationResult result;

        try
        {
            result = await app.AcquireTokenSilent(Scopes, accounts.FirstOrDefault())
                .ExecuteAsync();
        }
        catch (MsalUiRequiredException)
        {
            result = await app.AcquireTokenInteractive(Scopes)
                .WithPrompt(Prompt.SelectAccount)
                .ExecuteAsync();
        }

        // Call Microsoft Graph
        var httpClient = new HttpClient();
        httpClient.DefaultRequestHeaders.Authorization 
            = new System.Net.Http.Headers.AuthenticationHeaderValue("Bearer", result.AccessToken);
        
        var response = await httpClient.GetAsync("https://graph.microsoft.com/v1.0/me");
        Console.WriteLine(await response.Content.ReadAsStringAsync());
    }
}
```

---

## Environment Configuration

### Set Environment Variables

**macOS/Linux:**
```bash
# Add to ~/.bashrc, ~/.zshrc, or ~/.profile
export APPLICATION_CLIENT_ID="your-client-id"
export TENANT_ID="your-tenant-id"
export CLIENT_SECRET="your-client-secret"  # For web apps
```

**Windows (PowerShell):**
```powershell
# Add to profile.ps1
$env:APPLICATION_CLIENT_ID="your-client-id"
$env:TENANT_ID="your-tenant-id"
$env:CLIENT_SECRET="your-client-secret"
```

---

## Security Best Practices

✅ **DO:**
- Store secrets in Azure Key Vault
- Use environment variables or secure config
- Rotate secrets regularly (every 90 days)
- Use managed identity for Azure-hosted apps
- Grant minimal required permissions
- Monitor sign-in logs for anomalies

❌ **DON'T:**
- Hardcode secrets in source code
- Commit secrets to version control
- Use client secrets in public clients (SPA, mobile)
- Grant excessive permissions "just in case"
- Disable token validation in production

---

## Troubleshooting

### Common Issues

**Redirect URI mismatch:**
- Check the exact URI in app registration settings
- Ensure platform type matches (Web vs SPA vs Public client)

**Insufficient privileges:**
- Grant admin consent for permissions
- Verify user has appropriate directory rights

**Token validation errors:**
- Check token expiration
- Verify issuer and audience claims
- Use https://jwt.ms to decode and inspect tokens

**Consent required:**
- For delegated permissions: User can consent or admin grants
- For application permissions: Admin must grant consent

---

## Quick Reference

| Task | Command |
|------|---------|
| List apps | `az ad app list --output table` |
| Show app details | `az ad app show --id "APP_ID"` |
| Add permission | `az ad app permission add --id $APP_ID --api $GRAPH_ID --api-permissions "$PERM_ID=Scope"` |
| Grant admin consent | `az ad app permission admin-consent --id $APP_ID` |
| Create secret | `az ad app credential reset --id $APP_ID` |
| Get tenant ID | `az account show --query tenantId -o tsv` |

---

## Additional Resources

- [Microsoft Entra ID Documentation](https://learn.microsoft.com/entra/identity-platform/)
- [OAuth 2.0 Flows](https://learn.microsoft.com/entra/identity-platform/v2-protocols)
- [MSAL Libraries](https://learn.microsoft.com/entra/msal/)
- [Microsoft Graph API](https://learn.microsoft.com/graph/)

---

**Generated:** July 13, 2026
**For:** DAIOF-Framework Project
