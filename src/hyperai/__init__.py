"""
HYPERAI Framework - Digital Organism System
============================================

A framework for creating self-evolving, self-maintaining AI entities
Philosophy: Biological principles applied to digital systems

Creator & Copyright Holder: Nguyễn Đức Cường (alpha_prime_omega)
Verification Code: 4287
Original Creation Date: October 30, 2025

MIT License: https://opensource.org/licenses/MIT
"""

__version__ = "1.0.0"
__author__ = "Nguyễn Đức Cường (alpha_prime_omega)"
__copyright__ = "Copyright (c) 2025 Nguyễn Đức Cường"

# Core imports
from .core.haios_core import HAIOSCore
from .core.haios_runtime import HAIOSRuntime

# Component imports
from .components.genome import DigitalGenome
from .components.metabolism import DigitalMetabolism
from .components.nervous_system import DigitalNervousSystem
from .components.organism import DigitalOrganism

# Ecosystem imports
from .ecosystem.ecosystem import DigitalEcosystem

# Protocol imports
from .protocols.symphony import SymphonyControlCenter, ControlMetaData
from .protocols.dr_protocol import DRProtocol

# Metadata imports
from .protocols.metadata import HAIOSInvariants, CreatorHierarchy

__all__ = [
    # Core
    "HAIOSCore",
    "HAIOSRuntime",
    
    # Components
    "DigitalGenome",
    "DigitalMetabolism",
    "DigitalNervousSystem",
    "DigitalOrganism",
    
    # Ecosystem
    "DigitalEcosystem",
    
    # Protocols
    "SymphonyControlCenter",
    "ControlMetaData",
    "DRProtocol",
    
    # Metadata
    "HAIOSInvariants",
    "CreatorHierarchy",
]
