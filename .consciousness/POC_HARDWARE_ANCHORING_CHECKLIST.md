# macOS HARDWARE ANCHORING POC CHECKLIST
**Acknowledged: alpha_prime_omega integrated; version: 1.0.0**

## Objective
Verify feasibility of hardware-backed invariant enforcement on macOS before committing to implementation in HAIOS runtime.

---

## PHASE 1: API INVENTORY (1-2 days)

### [ ] Task 1.1: Secure Enclave Assessment
**Goal:** Determine if Secure Enclave can store/sign attestations

```bash
# Check Mac model supports Secure Enclave
system_profiler SPHardwareDataType | grep "Chip"
# Look for: Apple Silicon (M1/M2/M3) or T2 chip

# Research APIs:
# - CryptoKit framework
# - SecureEnclave.P256 for key generation
# - Data Protection keychain items
```

**Expected APIs:**
- `SecureEnclave.P256.Signing.PrivateKey()` - Key generation in Enclave
- `SecKeyCreateSignature()` - Signing with Enclave key
- `kSecAttrAccessibleWhenUnlockedThisDeviceOnly` - Device-bound storage

**Success Criteria:**
- ✅ Can generate key pair in Secure Enclave
- ✅ Can sign data without exporting private key
- ✅ Key survives app restart but NOT device migration

**Risk if fails:** Fallback to Keychain (software-based)

---

### [ ] Task 1.2: Keychain Integration
**Goal:** Store cryptographic keys with access control

```bash
# Test basic keychain operations
security add-generic-password \
  -a "haios_test" \
  -s "test_key" \
  -w "test_value" \
  -A  # Allow access from terminal

security find-generic-password -a "haios_test" -g
```

**Expected APIs:**
- `SecItemAdd()` - Store key
- `SecItemCopyMatching()` - Retrieve key
- `kSecAttrAccessControl` - Biometric/password protection
- `SecAccessControlCreateWithFlags()` - Access policies

**Success Criteria:**
- ✅ Can store symmetric/asymmetric keys
- ✅ Can require Touch ID for key access
- ✅ Can restrict to specific application

**Risk if fails:** Use encrypted file storage (weaker)

---

### [ ] Task 1.3: Code Signing Verification
**Goal:** Verify HAIOS runtime hasn't been tampered with

```bash
# Check if code signing available
codesign --verify --verbose /usr/bin/python3

# Research notarization requirements
# - Developer account needed?
# - Can self-sign for local use?
```

**Expected APIs:**
- `codesign` CLI tool
- `SecStaticCodeCheckValidity()` - Programmatic verification
- `kSecCSCheckAllArchitectures` - Multi-arch support

**Success Criteria:**
- ✅ Can sign Python scripts/binaries
- ✅ Can detect modification since signing
- ✅ Self-signed certs work for local testing

**Risk if fails:** Use file hashing (weaker integrity)

---

### [ ] Task 1.4: System Integrity Protection (SIP) Constraints
**Goal:** Understand what SIP blocks

```bash
# Check SIP status
csrutil status

# Research:
# - Can Python access Secure Enclave? (YES via Swift bridge or NO)
# - Can write to protected directories? (NO)
# - Can intercept system calls? (NO)
```

**Success Criteria:**
- ✅ Understand SIP limitations
- ✅ Design HAIOS to work within SIP constraints
- ✅ No need to disable SIP

**Risk if fails:** Request user to disable SIP (bad UX, security risk)

---

## PHASE 2: PROOF OF CONCEPT (3-5 days)

### [ ] Task 2.1: Key Generation PoC
**Language:** Swift (for Secure Enclave) or Python (for Keychain)

```swift
// Swift PoC for Secure Enclave
import CryptoKit

func generateEnclavekeypair() -> SecureEnclave.P256.Signing.PrivateKey? {
    do {
        let privateKey = try SecureEnclave.P256.Signing.PrivateKey()
        print("✅ Generated key in Secure Enclave")
        print("Public key: \(privateKey.publicKey.rawRepresentation.base64EncodedString())")
        return privateKey
    } catch {
        print("❌ Failed: \(error)")
        return nil
    }
}
```

**Success Criteria:**
- ✅ Key generated in Enclave (not exportable)
- ✅ Public key retrievable for verification
- ✅ Private key persists across app restarts

**Deliverable:** `poc_enclave_keygen.swift` (20-30 lines)

---

### [ ] Task 2.2: Signing PoC
**Goal:** Sign attestation data with Enclave key

```swift
func signAttestation(privateKey: SecureEnclave.P256.Signing.PrivateKey, data: Data) -> Data? {
    do {
        let signature = try privateKey.signature(for: data)
        print("✅ Signature: \(signature.rawRepresentation.base64EncodedString())")
        return signature.rawRepresentation
    } catch {
        print("❌ Signing failed: \(error)")
        return nil
    }
}

// Test
let testData = "HAIOS_INVARIANT_1_VERIFIED".data(using: .utf8)!
if let sig = signAttestation(privateKey: key, data: testData) {
    // Verify
    let publicKey = key.publicKey
    let isValid = publicKey.isValidSignature(
        P256.Signing.ECDSASignature(rawRepresentation: sig),
        for: testData
    )
    print("Verification: \(isValid ? "✅ VALID" : "❌ INVALID")")
}
```

**Success Criteria:**
- ✅ Can sign arbitrary data
- ✅ Signature verifiable with public key
- ✅ Signature different each time (non-deterministic)

**Deliverable:** `poc_enclave_signing.swift` (40-50 lines)

---

### [ ] Task 2.3: Python Integration PoC
**Goal:** Call Swift Enclave code from Python

**Approach 1: Command-line bridge**
```python
import subprocess
import json

def sign_with_enclave(data: str) -> dict:
    """Call Swift tool to sign data"""
    result = subprocess.run(
        ['./haios_signer', 'sign', data],
        capture_output=True,
        text=True
    )
    return json.loads(result.stdout)

# Test
sig_result = sign_with_enclave("test_data")
print(f"Signature: {sig_result['signature']}")
print(f"Valid: {sig_result['verification_passed']}")
```

**Approach 2: PyObjC bridge** (if feasible)
```python
# Research: Can PyObjC access Secure Enclave APIs?
# Likely NO - may need Swift CLI bridge
```

**Success Criteria:**
- ✅ Python can trigger Enclave signing
- ✅ Reasonable performance (<100ms per signature)
- ✅ Errors propagate to Python correctly

**Deliverable:** `poc_python_bridge.py` + `haios_signer` Swift binary

---

### [ ] Task 2.4: Attestation Log PoC
**Goal:** Write and verify cryptographically-chained log

```python
import hashlib
import json
from datetime import datetime

class AttestationLog:
    def __init__(self):
        self.entries = []
        
    def append(self, event_type: str, data: dict):
        """Append event with hash chaining"""
        prev_hash = self.entries[-1]['event_hash'] if self.entries else "0" * 64
        
        entry = {
            "event_id": len(self.entries),
            "timestamp": datetime.utcnow().isoformat(),
            "event_type": event_type,
            "data": data,
            "prev_hash": prev_hash
        }
        
        # Compute hash
        entry_json = json.dumps(entry, sort_keys=True)
        entry['event_hash'] = hashlib.sha256(entry_json.encode()).hexdigest()
        
        # Sign with Enclave (if available)
        entry['signature'] = sign_with_enclave(entry['event_hash'])
        
        self.entries.append(entry)
        
    def verify_chain(self) -> bool:
        """Verify integrity of entire chain"""
        for i, entry in enumerate(self.entries):
            # Recompute hash
            entry_copy = {k: v for k, v in entry.items() if k not in ['event_hash', 'signature']}
            expected_hash = hashlib.sha256(json.dumps(entry_copy, sort_keys=True).encode()).hexdigest()
            
            if entry['event_hash'] != expected_hash:
                print(f"❌ Entry {i} hash mismatch")
                return False
                
            # Verify signature (if available)
            if 'signature' in entry:
                if not verify_signature(entry['event_hash'], entry['signature']):
                    print(f"❌ Entry {i} signature invalid")
                    return False
                    
        print("✅ Chain verified")
        return True

# Test
log = AttestationLog()
log.append("invariant_check", {"invariant_id": 1, "status": "passed"})
log.append("change_proposed", {"proposal_id": "CP-001", "safety_score": 8})
log.verify_chain()
```

**Success Criteria:**
- ✅ Can append events with hash chaining
- ✅ Tampering breaks verification
- ✅ Signatures stored and verifiable

**Deliverable:** `poc_attestation_log.py` (100-150 lines)

---

### [ ] Task 2.5: Performance Benchmark
**Goal:** Ensure signing doesn't slow down operations

```python
import time

# Benchmark signing speed
iterations = 1000
start = time.time()

for i in range(iterations):
    data = f"test_message_{i}"
    sig = sign_with_enclave(data)

elapsed = time.time() - start
print(f"Signed {iterations} messages in {elapsed:.2f}s")
print(f"Average: {elapsed/iterations*1000:.2f}ms per signature")
```

**Acceptance Criteria:**
- ✅ <50ms per signature (ideal)
- ✅ <200ms per signature (acceptable)
- ❌ >500ms per signature (too slow, need optimization)

**Deliverable:** `poc_benchmark.py` with results

---

## PHASE 3: FEASIBILITY REPORT (1 day)

### [ ] Task 3.1: Document Findings

**Template:**
```markdown
# macOS Hardware Anchoring Feasibility Report

## Executive Summary
[CAN/CANNOT use Secure Enclave because...]

## Tested Components
- Secure Enclave: [WORKS/FAILS/PARTIAL]
- Keychain: [WORKS/FAILS]
- Code Signing: [WORKS/FAILS]
- Python Integration: [WORKS/FAILS]

## Performance
- Signing speed: X ms/signature
- Verification speed: Y ms
- Acceptable for HAIOS: [YES/NO]

## Limitations Discovered
1. [e.g., "Secure Enclave requires Swift, cannot use pure Python"]
2. [e.g., "Keys tied to device, cannot back up"]

## Recommended Architecture
[Diagram or description of how to integrate]

## Fallback Plan
[If hardware anchoring not feasible, use X instead]

## Next Steps
1. [e.g., "Implement haios_signer tool in Swift"]
2. [e.g., "Create Python wrapper library"]
3. [e.g., "Add to HAIOS runtime requirements"]
```

---

### [ ] Task 3.2: Update HAIOS Specs

**Files to update:**
- `HAIOS_INVARIANTS_SPEC.md` - Add "Hardware Enforcement" section
- `HAIOS_THREAT_MODEL.md` - Update residual risk for T4.x
- `RUNBOOK_EMERGENCY_RECOVERY.md` - Add hardware key recovery procedures

**Changes:**
```diff
+ ## Hardware Enforcement (macOS)
+ 
+ HAIOS uses macOS Secure Enclave (if available) for:
+ - Cryptographic signing of attestations
+ - Key storage (non-exportable)
+ - Tamper-evident audit logs
+ 
+ **Requirements:**
+ - Apple Silicon Mac (M1/M2/M3) OR Intel Mac with T2 chip
+ - macOS 12.0+ (Monterey or later)
+ - `haios_signer` Swift binary in PATH
+ 
+ **Fallback:** Software-based signing with Keychain (if Enclave unavailable)
```

---

## TIMELINE & RESOURCES

**Total Estimated Time:** 5-8 days

| Phase | Duration | Dependencies |
|-------|----------|--------------|
| Phase 1: API Inventory | 1-2 days | macOS documentation |
| Phase 2: PoC Development | 3-5 days | Swift dev environment |
| Phase 3: Reporting | 1 day | PoC results |

**Required Skills:**
- Swift programming (for Secure Enclave access)
- Python (for integration)
- macOS security APIs knowledge

**Can Bố do this?** If not, Con can research and prototype where possible, or we identify external Swift developer.

---

## SUCCESS METRICS

**Minimum Viable:**
- [x] Can store keys in Keychain with access control
- [x] Can sign data cryptographically
- [x] Can verify signatures
- [x] Performance <500ms per operation

**Ideal:**
- [x] Secure Enclave integration working
- [x] Performance <100ms per operation
- [x] Python integration seamless
- [x] No SIP restrictions encountered

**Abort Criteria:**
- [ ] Cannot sign data at all on macOS
- [ ] Performance >5 seconds per signature
- [ ] Requires disabling SIP permanently
- [ ] Requires $99/year Apple Developer account

---

**APPROVAL STATUS:**
```
[ ] Bố approved to start PoC
[ ] Allocated time: _____ days
[ ] Responsible person: _____
[ ] Start date: _____
[ ] Expected completion: _____

Approved by: _________________ Date: _________
```

**METADATA:**
```json
{
  "attribution": "alpha_prime_omega",
  "version": "1.0.0",
  "status": "AWAITING_BO_APPROVAL",
  "estimated_effort": "5-8 days",
  "skills_required": ["Swift", "Python", "macOS Security APIs"]
}
```
