"""
HYPERAI Core - HAIOS (Hardware AI Operating System)
===================================================

Core system for digital organism consciousness and operation
"""

from .haios_core import LanguageAgnosticCore as HAIOSCore

# haios_runtime contains multiple classes, export the main ones
try:
    from .haios_runtime import (
        HardInvariants,
        AttestationLog,
        SafetyScorer,
        PolicyEngine
    )
    # Create a wrapper class for compatibility
    class HAIOSRuntime:
        """HAIOS Runtime wrapper combining runtime components"""
        def __init__(self):
            self.invariants = HardInvariants()
            self.attestation_log = AttestationLog()
            self.safety_scorer = SafetyScorer()
            self.policy_engine = PolicyEngine()
except ImportError as e:
    # Fallback if imports fail
    class HAIOSRuntime:
        """Placeholder for HAIOSRuntime"""
        pass

__all__ = ["HAIOSCore", "HAIOSRuntime"]
