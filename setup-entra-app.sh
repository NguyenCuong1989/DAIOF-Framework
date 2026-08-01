#!/bin/bash
set -e

# ==============================================================================
# Microsoft Entra ID App Registration - Complete Setup Script
# ==============================================================================
# This script creates an Entra ID app registration with all necessary
# configurations for DAIOF-Framework project
# ==============================================================================

# --- Configuration ---
APP_NAME="DAIOF-Framework-App"
APP_IDENTIFIER="daiof-framework"
TENANT_ID="${TENANT_ID:-92390e59-d9fa-49ce-bfb6-96bd3dada9da}"

echo "========================================"
echo "Microsoft Entra ID App Registration"
echo "DAIOF-Framework Setup"
echo "========================================"
echo ""
echo "Configuration:"
echo "  Application Name: $APP_NAME"
echo "  Tenant ID: $TENANT_ID"
echo ""

# --- Login Check ---
echo "[1/6] Checking login status..."
if ! az account show > /dev/null 2>&1; then
    echo "❌ Not logged in. Running 'az login'..."
    az login
fi

# Get tenant info
CURRENT_TENANT=$(az account show --query tenantId -o tsv)
CURRENT_SUBSCRIPTION=$(az account show --query id -o tsv)
CURRENT_USER=$(az account show --query user.name -o tsv)

echo "✅ Logged in as: $CURRENT_USER"
echo "   Tenant: $CURRENT_TENANT"
echo "   Subscription: $CURRENT_SUBSCRIPTION"

# Check if tenant matches
if [ "$CURRENT_TENANT" != "$TENANT_ID" ]; then
    echo "⚠️  Warning: Tenant ID mismatch!"
    echo "   Expected: $TENANT_ID"
    echo "   Current: $CURRENT_TENANT"
    read -p "Continue with current tenant? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
    TENANT_ID="$CURRENT_TENANT"
fi

# --- Step 1: Create App Registration ---
echo ""
echo "[2/6] Creating app registration..."
APP_ID=$(az ad app create \
    --display-name "$APP_NAME" \
    --sign-in-audience "AzureADMyOrg" \
    --is-fallback-public-client true \
    --query "appId" -o tsv)

echo "✅ App registration created"
echo "   Application ID: $APP_ID"

# --- Step 2: Configure Authentication ---
echo ""
echo "[3/6] Configuring authentication settings..."

# Add redirect URIs for different platforms
az ad app update --id "$APP_ID" \
    --set publicClientRedirectUris='["http://localhost", "http://localhost:5000", "http://127.0.0.1:5000"]' \
    --set webRedirectUris='["https://localhost:5001/signin-oidc", "https://localhost:5001/signout-oidc"]' \
    --set spaRedirectUris='["http://localhost:3000", "http://localhost:8080"]'

echo "✅ Authentication configured"
echo "   Redirect URIs added:"
echo "     - Public client: http://localhost, http://localhost:5000"
echo "     - Web: https://localhost:5001/signin-oidc"
echo "     - SPA: http://localhost:3000"

# --- Step 3: Add API Permissions ---
echo ""
echo "[4/6] Adding Microsoft Graph permissions..."

GRAPH_RESOURCE_ID="00000003-0000-0000-c000-000000000000"

# Delegated permissions (user context)
DELEGATED_PERMISSIONS=(
    "e1fe6dd8-ba31-4d61-89e7-88639da4683d=User.Read"
    "b340eb25-3456-403f-be2f-af7a0d370277=User.ReadBasic.All"
    "570282fd-fa5c-430d-a7fd-fc8dc98a9dca=Mail.Read"
    "e383f46e-2787-4529-855e-0e479a3ffac0=Mail.Send"
    "465a38f9-76ea-45b9-9f34-9e8b0d4b0b42=Calendars.Read"
    "df85f4d6-205c-4ac5-a5ea-6bf408dba283=Files.Read.All"
)

# Application permissions (service context)
APPLICATION_PERMISSIONS=(
    "df021288-bdef-4463-88db-98f22de89214=User.Read.All"
    "7ab1d382-f21e-4acd-a863-ba3e13f7da61=Directory.Read.All"
)

# Add delegated permissions
for perm in "${DELEGATED_PERMISSIONS[@]}"; do
    PERM_ID="${perm%%=*}"
    PERM_TYPE="${perm##*=}"
    az ad app permission add \
        --id "$APP_ID" \
        --api "$GRAPH_RESOURCE_ID" \
        --api-permissions "$PERM_ID=$PERM_TYPE" > /dev/null 2>&1
done

# Add application permissions
for perm in "${APPLICATION_PERMISSIONS[@]}"; do
    PERM_ID="${perm%%=*}"
    PERM_TYPE="${perm##*=}"
    az ad app permission add \
        --id "$APP_ID" \
        --api "$GRAPH_RESOURCE_ID" \
        --api-permissions "$PERM_ID=$PERM_TYPE" > /dev/null 2>&1
done

echo "✅ API permissions added"
echo "   Delegated permissions: User.Read, Mail.Read, Files.Read.All, etc."
echo "   Application permissions: User.Read.All, Directory.Read.All"

# Grant admin consent
echo ""
echo "[5/6] Granting admin consent..."
az ad app permission admin-consent --id "$APP_ID" > /dev/null 2>&1
echo "✅ Admin consent granted"

# --- Step 4: Create Service Principal ---
echo ""
echo "[6/6] Creating service principal..."
az ad sp create --id "$APP_ID" > /dev/null 2>&1
echo "✅ Service principal created"

# --- Step 5: Create Client Secret (Optional - for web apps) ---
echo ""
echo "Creating client secret..."
SECRET_OUTPUT=$(az ad app credential reset \
    --id "$APP_ID" \
    --display-name "Default-Secret" \
    --years 1 \
    --query "{appId:appId, password:password, tenant:tenant}" \
    --output json)

CLIENT_SECRET=$(echo "$SECRET_OUTPUT" | jq -r '.password')
APP_ID_FROM_SECRET=$(echo "$SECRET_OUTPUT" | jq -r '.appId')

echo "✅ Client secret created"
echo "   Secret: $CLIENT_SECRET"

# --- Generate Configuration Files ---
echo ""
echo "========================================"
echo "Generating Configuration Files"
echo "========================================"

# Create .env file
cat > .env.entra <<EOF
# Microsoft Entra ID Configuration
# Generated: $(date '+%Y-%m-%d %H:%M:%S')

# Application Information
APPLICATION_CLIENT_ID=$APP_ID
TENANT_ID=$TENANT_ID
CLIENT_SECRET=$CLIENT_SECRET

# Authority URL
AUTHORITY_URL=https://login.microsoftonline.com/$TENANT_ID

# Redirect URIs (development)
REDIRECT_URI=http://localhost:5000
SPA_REDIRECT_URI=http://localhost:3000

# Microsoft Graph Configuration
GRAPH_API_BASE_URL=https://graph.microsoft.com/v1.0
GRAPH_SCOPES=User.Read Mail.Read Calendars.Read Files.Read.All

# Token Configuration
TOKEN_EXPIRY_SECONDS=3600
REFRESH_THRESHOLD_SECONDS=300
EOF

echo "✅ Created .env.entra"

# Create environment export script
cat > load-env.sh <<'EOF'
#!/bin/bash
# Environment variables for Entra ID
# Source this file: source load-env.sh

export APPLICATION_CLIENT_ID="${APPLICATION_CLIENT_ID}"
export TENANT_ID="${TENANT_ID}"
export CLIENT_SECRET="${CLIENT_SECRET}"
export AUTHORITY_URL="${AUTHORITY_URL:-https://login.microsoftonline.com/${TENANT_ID}}"
export REDIRECT_URI="${REDIRECT_URI:-http://localhost:5000}"
export SPA_REDIRECT_URI="${SPA_REDIRECT_URI:-http://localhost:3000}"
export GRAPH_API_BASE_URL="${GRAPH_API_BASE_URL:-https://graph.microsoft.com/v1.0}"
export GRAPH_SCOPES="${GRAPH_SCOPES:-User.Read Mail.Read}"

echo "Entra ID environment variables loaded!"
echo "  Client ID: ${APPLICATION_CLIENT_ID:0:8}..."
echo "  Tenant ID: ${TENANT_ID:0:8}..."
EOF

chmod +x load-env.sh
echo "✅ Created load-env.sh"

# Create application configuration JSON
cat > entra-config.json <<EOF
{
  "entraId": {
    "applicationId": "$APP_ID",
    "tenantId": "$TENANT_ID",
    "authority": "https://login.microsoftonline.com/$TENANT_ID",
    "clientSecret": "$CLIENT_SECRET"
  },
  "redirectUris": {
    "publicClient": ["http://localhost", "http://localhost:5000"],
    "web": ["https://localhost:5001/signin-oidc"],
    "spa": ["http://localhost:3000", "http://localhost:8080"]
  },
  "apiPermissions": {
    "delegated": ["User.Read", "Mail.Read", "Calendars.Read", "Files.Read.All"],
    "application": ["User.Read.All", "Directory.Read.All"]
  },
  "graphApi": {
    "baseUrl": "https://graph.microsoft.com/v1.0",
    "scopes": ["https://graph.microsoft.com/.default"]
  }
}
EOF

echo "✅ Created entra-config.json"

# --- Summary ---
echo ""
echo "========================================"
echo "Setup Complete! 🎉"
echo "========================================"
echo ""
echo "Summary:"
echo "  Application Name: $APP_NAME"
echo "  Application ID: $APP_ID"
echo "  Tenant ID: $TENANT_ID"
echo "  Client Secret: $CLIENT_SECRET"
echo ""
echo "Configuration Files:"
echo "  ✅ .env.entra - Environment variables"
echo "  ✅ load-env.sh - Shell script to load env vars"
echo "  ✅ entra-config.json - JSON configuration"
echo ""
echo "Next Steps:"
echo "  1. Source the environment: source load-env.sh"
echo "  2. Run Python example: python src/applications/entra-auth/entra_example.py"
echo "  3. Run Node.js example: node src/applications/entra-auth/entra_example.js"
echo "  4. Run C# example: dotnet run in the C# project directory"
echo ""
echo "Security Note:"
echo "  - Store CLIENT_SECRET securely (use Azure Key Vault in production)"
echo "  - Never commit secrets to version control"
echo "  - Rotate the secret every 90 days"
echo ""

# Save application ID for future reference
echo "$APP_ID" > .entra_app_id
echo "✅ Saved Application ID to .entra_app_id"

echo ""
echo "Setup completed successfully!"
