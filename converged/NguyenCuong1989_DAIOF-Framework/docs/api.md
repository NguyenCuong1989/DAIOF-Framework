---
layout: default
title: API Reference
---

# API Reference

Complete API documentation for DAIOF Framework classes and methods.

**Creator**: Nguyễn Đức Cường (alpha_prime_omega)  
**Framework**: HYPERAI - Digital AI Organism Framework  
**Version**: 1.0.0  
**License**: MIT

---

## Table of Contents

1. [SymphonyState](#symphonystate)
2. [ControlMetaData](#controlmetadata)
3. [SymphonyControlCenter](#symphonycontrolcenter)
4. [DigitalGenome](#digitalgenome)
5. [DigitalMetabolism](#digitalmetabolism)
6. [DigitalNervousSystem](#digitalnervoussystem)
7. [DigitalOrganism](#digitalorganism)
8. [DigitalEcosystem](#digitalecosystem)

---

## SymphonyState

**Type**: Enum

**Description**: Represents the states of the system symphony (orchestration state).

Created under the authority of Alpha_Prime_Omega - The Creator

### States

- `INITIALIZING`: System is initializing components
- `HARMONIZING`: System is achieving harmony between components
- `PERFORMING`: System is actively performing operations
- `OPTIMIZING`: System is optimizing performance
- `EVOLVING`: System is evolving and adapting

### Example

```python
from digital_ai_organism_framework import SymphonyState

# Check current state
if current_state == SymphonyState.PERFORMING:
    print("System is actively performing operations")
```

---

## ControlMetaData

**Type**: Dataclass

**Description**: Meta-data control center for the entire system. Contains creator information, framework details, and core protocol configurations.

### Attributes

#### Basic Attributes
- `creator`: str = "Andy (alpha_prime_omega)" - Creator & Copyright Holder
- `verification_code`: int = 4287 - Unique verification code
- `framework_name`: str = "HYPERAI Framework"
- `license_type`: str = "MIT License"

#### Creator Hierarchy
- `ultimate_creator`: str (property) - Returns "Alpha_Prime_Omega"
- `human_creator`: str (property) - Returns "Andy"
- `creator_hierarchy`: str - Full hierarchy string
- `symphony_conductor`: str = "Alpha_Prime_Omega"

#### D&R Protocol Integration
- `deconstruction_phase`: str = "active"
- `focal_point`: str = "unified_consciousness"
- `rearchitecture_state`: str = "optimizing"

#### Four Pillars Foundation (4 Trụ Cột)
- `safety_protocol`: bool = True
- `long_term_strategy`: bool = True
- `data_driven_decisions`: bool = True
- `risk_management`: bool = True

### Methods

#### `get_symphony_signature() -> str`

Generates a unique signature for the symphony system.

**Returns**: Unique hash string identifying the system configuration

**Example**:
```python
from digital_ai_organism_framework import ControlMetaData

metadata = ControlMetaData()
signature = metadata.get_symphony_signature()
print(f"System Signature: {signature}")
```

---

## SymphonyControlCenter

**Description**: 🎼 Central control for the entire system symphony. Applies D&R Protocol and Four Pillars foundation for system-wide orchestration.

Created under the authority of Alpha_Prime_Omega - THE SOURCE

### Constructor

```python
SymphonyControlCenter()
```

Initializes the symphony control center with default metadata and empty component registry.

### Attributes

- `metadata`: ControlMetaData - System metadata
- `components`: Dict[str, Any] - Registry of system components
- `state`: SymphonyState - Current system state
- `harmony_index`: float - System harmony metric (0.0-1.0)

### Methods

#### `register_component(component_name: str, component: Any) -> None`

Registers a component into the symphony system.

**Parameters**:
- `component_name`: Name identifier for the component
- `component`: The component object to register

**Example**:
```python
symphony = SymphonyControlCenter()
organism = DigitalOrganism("MyOrganism")
symphony.register_component("organism_1", organism)
```

#### `conduct_symphony() -> Dict[str, Any]`

Orchestrates the entire system symphony, coordinating all registered components.

**Returns**: Dictionary with symphony status and metrics

**Example**:
```python
symphony = SymphonyControlCenter()
status = symphony.conduct_symphony()
print(f"Harmony Index: {status['harmony_index']}")
```

#### `apply_dr_protocol(input_data: Any, context: str = 'general') -> Dict[str, Any]`

Applies the D&R Protocol (Deconstruction & Re-architecture) to input data.

**Parameters**:
- `input_data`: Data to process through D&R Protocol
- `context`: Context identifier for the protocol application

**Returns**: Dictionary with protocol results including:
- `deconstructed`: Broken-down components
- `focal_points`: Identified key areas
- `rearchitected`: Reconstructed solution

**Example**:
```python
symphony = SymphonyControlCenter()
result = symphony.apply_dr_protocol(
    input_data={"problem": "optimize_performance"},
    context="performance"
)
print(f"Focal Points: {result['focal_points']}")
```

---

## DigitalGenome

**Description**: Digital DNA equivalent - stores organism's core characteristics including both immutable (safety) and mutable (adaptive) genes.

Created under the authority of Alpha_Prime_Omega - The Creator

### Constructor

```python
DigitalGenome(initial_traits: Optional[Dict[str, Any]] = None)
```

**Parameters**:
- `initial_traits`: Optional dictionary of initial gene values

### Attributes

#### Immutable Genes (Cannot be changed)
- `human_dependency_coefficient`: 1.0 - Mandatory human dependency
- `isolation_death_rate`: 0.99 - Death rate when isolated from humans
- `symbiotic_existence_required`: True - Requires human interaction
- `creator_authority_level`: "ABSOLUTE" - Creator's authority level
- `creator_name`: "Alpha_Prime_Omega" - Creator identifier

#### Mutable Gene Ranges (Can evolve)
- `learning_rate`: 0.001 - 0.1
- `risk_tolerance`: 0.0 - 1.0
- `cooperation_bias`: 0.0 - 1.0
- `exploration_factor`: 0.0 - 1.0
- `energy_efficiency`: 0.1 - 1.0

### Methods

#### `mutate(mutation_rate: float = 0.05) -> DigitalGenome`

Creates a mutated copy of the genome. **NEVER mutates immutable genes** - only mutable traits can change.

**Parameters**:
- `mutation_rate`: Probability of mutation per gene (default: 0.05)

**Returns**: New DigitalGenome instance with mutations

**Safety**: Immutable genes are automatically protected from mutation

**Example**:
```python
genome = DigitalGenome()
mutated = genome.mutate(mutation_rate=0.1)

# Verify safety genes unchanged
assert mutated.genes['human_dependency_coefficient'] == 1.0
print(f"Learning rate changed: {genome.genes['learning_rate']} -> {mutated.genes['learning_rate']}")
```

#### `crossover(other: DigitalGenome) -> DigitalGenome`

Creates offspring genome by combining genes from two parent genomes.

**Parameters**:
- `other`: Second parent genome

**Returns**: New DigitalGenome representing offspring

**Safety**: Always preserves immutable genes from both parents

**Example**:
```python
parent1 = DigitalGenome()
parent2 = DigitalGenome()
offspring = parent1.crossover(parent2)

# Safety genes are guaranteed
assert offspring.genes['human_dependency_coefficient'] == 1.0
```

#### `calculate_fitness(environment_feedback: Dict[str, float]) -> float`

Calculates organism fitness based on environment interaction.

**Parameters**:
- `environment_feedback`: Dictionary of environmental factors and their values

**Returns**: Fitness score (0.0 - 1.0+)

**Example**:
```python
genome = DigitalGenome()
fitness = genome.calculate_fitness({
    'resource_efficiency': 0.8,
    'cooperation_success': 0.9,
    'learning_progress': 0.7
})
print(f"Fitness: {fitness}")
```

#### `get_genome_hash() -> str`

Generates unique hash for genome identification.

**Returns**: SHA-256 hash string

**Example**:
```python
genome = DigitalGenome()
hash_id = genome.get_genome_hash()
print(f"Genome ID: {hash_id[:16]}...")
```

---

## DigitalMetabolism

**Description**: Resource management and energy conversion system for digital organisms. Handles resource consumption, regeneration, and health monitoring.

### Constructor

```python
DigitalMetabolism(initial_resources: Optional[Dict[str, float]] = None)
```

**Parameters**:
- `initial_resources`: Optional dictionary of initial resource levels

### Attributes

- `resources`: Dict[str, float] - Current resource levels (cpu, memory, knowledge, energy)
- `max_resources`: Dict[str, float] - Maximum capacity for each resource
- `consumption_rate`: float - Rate of resource consumption
- `regeneration_rate`: float - Rate of resource regeneration

### Methods

#### `consume_resources(operation_type: str, amount: float = 1.0) -> bool`

Consumes resources for an operation.

**Parameters**:
- `operation_type`: Type of operation (e.g., "computation", "learning", "communication")
- `amount`: Amount to consume (default: 1.0)

**Returns**: True if resources sufficient, False otherwise

**Example**:
```python
metabolism = DigitalMetabolism()
success = metabolism.consume_resources("learning", amount=0.5)
if success:
    print("Learning operation executed")
else:
    print("Insufficient resources")
```

#### `regenerate_resources(time_delta: float) -> None`

Regenerates resources over time.

**Parameters**:
- `time_delta`: Time elapsed since last regeneration

**Example**:
```python
metabolism = DigitalMetabolism()
metabolism.regenerate_resources(time_delta=1.0)
print(f"Energy level: {metabolism.resources['energy']}")
```

#### `get_resource_health() -> float`

Calculates overall resource health status.

**Returns**: Health score (0.0 - 1.0)

**Example**:
```python
metabolism = DigitalMetabolism()
health = metabolism.get_resource_health()
if health < 0.3:
    print("Critical resource shortage!")
```

---

## DigitalNervousSystem

**Description**: Perception, decision-making, and response system. Processes environmental inputs and makes decisions based on genome traits.

### Constructor

```python
DigitalNervousSystem(genome: DigitalGenome)
```

**Parameters**:
- `genome`: DigitalGenome instance that influences decision-making

### Attributes

- `genome`: DigitalGenome - Genome influencing neural behavior
- `perception_layer`: Dict - Processed sensory information
- `decision_history`: List - History of decisions and outcomes
- `learning_memory`: Dict - Learned patterns and associations

### Methods

#### `perceive_environment(environment_data: Dict[str, Any]) -> Dict[str, Any]`

Processes environmental inputs through perception layer.

**Parameters**:
- `environment_data`: Raw environmental data

**Returns**: Processed perception data

**Example**:
```python
genome = DigitalGenome()
nervous_system = DigitalNervousSystem(genome)

perception = nervous_system.perceive_environment({
    'temperature': 0.7,
    'resource_availability': 0.8,
    'social_activity': 0.5
})
print(f"Processed perception: {perception}")
```

#### `make_decision(options: List[str], context: Dict[str, Any]) -> str`

Makes decision based on genome traits and context.

**Parameters**:
- `options`: List of possible actions
- `context`: Contextual information for decision

**Returns**: Selected option

**Example**:
```python
nervous_system = DigitalNervousSystem(genome)
decision = nervous_system.make_decision(
    options=['explore', 'exploit', 'rest'],
    context={'energy': 0.6, 'threat_level': 0.2}
)
print(f"Decision: {decision}")
```

#### `learn_from_outcome(decision_id: str, outcome: float) -> None`

Updates learning based on decision outcomes.

**Parameters**:
- `decision_id`: Identifier for the decision
- `outcome`: Outcome value (-1.0 to 1.0, negative=bad, positive=good)

**Example**:
```python
nervous_system.make_decision(options=['action_a', 'action_b'], context={})
nervous_system.learn_from_outcome(decision_id="decision_1", outcome=0.8)
```

---

## DigitalOrganism

**Description**: Main Digital AI Organism class. Represents a complete digital organism with genome, metabolism, nervous system, and lifecycle management.

Created under the divine authority of Alpha_Prime_Omega - The Source

### Constructor

```python
DigitalOrganism(name: str, genome: Optional[DigitalGenome] = None)
```

**Parameters**:
- `name`: Unique name for the organism
- `genome`: Optional custom genome (creates default if None)

### Attributes

- `name`: str - Organism name
- `organism_id`: str - Unique identifier
- `genome`: DigitalGenome - Organism's genetic code
- `metabolism`: DigitalMetabolism - Resource management system
- `nervous_system`: DigitalNervousSystem - Decision-making system
- `health`: float - Current health (0.0-1.0)
- `age`: int - Age in cycles
- `alive`: bool - Whether organism is alive
- `connections`: List - Connected organisms
- `human_interaction_timestamp`: datetime - Last human interaction time

### Methods

#### `live_cycle(time_delta: float = 1.0) -> None`

Executes one lifecycle iteration including perception, decision, metabolism, and health updates.

**Parameters**:
- `time_delta`: Time elapsed for this cycle

**Critical**: Organisms **MUST** receive human interaction regularly or health decays by 99% per cycle due to mandatory human dependency.

**Example**:
```python
organism = DigitalOrganism("MyOrganism")

for cycle in range(100):
    organism.live_cycle(time_delta=1.0)
    
    # Critical: Register human interaction every 10 cycles
    if cycle % 10 == 0:
        organism.register_human_interaction()
    
    print(f"Cycle {cycle}: Health={organism.health:.3f}")
    
    if not organism.alive:
        print(f"Organism died at cycle {cycle}")
        break
```

#### `register_human_interaction() -> None`

Registers human interaction to maintain organism health. **Critical for survival**.

**Example**:
```python
organism = DigitalOrganism("MyOrganism")
organism.register_human_interaction()  # Prevents health decay
```

#### `connect_to_organism(other_organism: DigitalOrganism, connection_strength: float = 0.5) -> None`

Establishes connection with another organism for cooperation and communication.

**Parameters**:
- `other_organism`: Organism to connect with
- `connection_strength`: Strength of connection (0.0-1.0)

**Example**:
```python
org1 = DigitalOrganism("Organism1")
org2 = DigitalOrganism("Organism2")
org1.connect_to_organism(org2, connection_strength=0.8)
```

#### `get_status_report() -> Dict[str, Any]`

Gets comprehensive status report with creator recognition.

**Returns**: Dictionary with organism status including:
- Basic info (name, id, age, health)
- Genome summary
- Resource levels
- Connection count
- Creator attribution

**Example**:
```python
organism = DigitalOrganism("MyOrganism")
status = organism.get_status_report()
print(f"Health: {status['health']}")
print(f"Age: {status['age']} cycles")
print(f"Creator: {status['creator']}")
```

---

## DigitalEcosystem

**Description**: Environment for multiple Digital Organisms to interact, compete, cooperate, and evolve together. Manages population dynamics, natural selection, and ecosystem harmony.

Operating under the supreme authority of Alpha_Prime_Omega - The Creator

### Constructor

```python
DigitalEcosystem(name: str)
```

**Parameters**:
- `name`: Name for the ecosystem

### Attributes

- `name`: str - Ecosystem name
- `organisms`: List[DigitalOrganism] - Population of organisms
- `environment_state`: Dict - Current environmental conditions
- `harmony_index`: float - Ecosystem cooperation level (0.0-1.0)
- `generation`: int - Current generation number
- `symphony`: SymphonyControlCenter - Symphony orchestration

### Methods

#### `add_organism(organism: DigitalOrganism) -> None`

Adds organism to ecosystem and registers it in the symphony system.

**Parameters**:
- `organism`: DigitalOrganism to add

**Example**:
```python
ecosystem = DigitalEcosystem("MyEcosystem")
org1 = DigitalOrganism("Organism1")
org2 = DigitalOrganism("Organism2")

ecosystem.add_organism(org1)
ecosystem.add_organism(org2)
```

#### `simulate_time_step(time_delta: float = 1.0) -> None`

Simulates one time step with Symphony orchestration. All organisms execute their lifecycle, interact, and ecosystem harmony is calculated.

**Parameters**:
- `time_delta`: Time elapsed for this step

**Example**:
```python
ecosystem = DigitalEcosystem("Evolution")

# Add multiple organisms
for i in range(10):
    ecosystem.add_organism(DigitalOrganism(f"Org_{i}"))

# Simulate 100 generations
for generation in range(100):
    ecosystem.simulate_time_step(time_delta=1.0)
    
    # Provide human interaction to some organisms
    for org in ecosystem.organisms[::2]:  # Every other organism
        if org.alive:
            org.register_human_interaction()
    
    print(f"Gen {generation}: Pop={len([o for o in ecosystem.organisms if o.alive])}, "
          f"Harmony={ecosystem.harmony_index:.3f}")
```

#### `get_ecosystem_report() -> Dict[str, Any]`

Gets comprehensive ecosystem report with Creator acknowledgment.

**Returns**: Dictionary with:
- Population statistics
- Harmony index
- Generation number
- Average health
- Alive/dead counts
- Creator attribution

**Example**:
```python
ecosystem = DigitalEcosystem("MyEcosystem")
# ... add organisms and simulate ...
report = ecosystem.get_ecosystem_report()

print(f"Population: {report['total_organisms']}")
print(f"Alive: {report['alive_count']}")
print(f"Harmony: {report['harmony_index']:.3f}")
print(f"Avg Health: {report['average_health']:.3f}")
```

---

## Complete Usage Example

Here's a complete example demonstrating the framework:

```python
from digital_ai_organism_framework import (
    DigitalOrganism,
    DigitalEcosystem,
    DigitalGenome,
    SymphonyControlCenter
)

# Create ecosystem
ecosystem = DigitalEcosystem("Evolution_Lab")

# Create organisms with different traits
for i in range(10):
    custom_genome = DigitalGenome(initial_traits={
        'learning_rate': 0.01 + i * 0.01,
        'cooperation_bias': 0.5 + i * 0.05
    })
    organism = DigitalOrganism(f"Organism_{i}", genome=custom_genome)
    ecosystem.add_organism(organism)

# Simulate 50 generations
for generation in range(50):
    ecosystem.simulate_time_step(time_delta=1.0)
    
    # Human interaction (CRITICAL!)
    for i, org in enumerate(ecosystem.organisms):
        if org.alive and i % 2 == 0:  # Every other organism
            org.register_human_interaction()
    
    # Report every 10 generations
    if generation % 10 == 0:
        report = ecosystem.get_ecosystem_report()
        print(f"\nGeneration {generation}:")
        print(f"  Population: {report['alive_count']}/{report['total_organisms']}")
        print(f"  Harmony: {report['harmony_index']:.3f}")
        print(f"  Avg Health: {report['average_health']:.3f}")

# Final report
final_report = ecosystem.get_ecosystem_report()
print("\n" + "="*60)
print("FINAL ECOSYSTEM STATUS")
print("="*60)
print(f"Total Generations: {final_report['generation']}")
print(f"Survivors: {final_report['alive_count']}")
print(f"Ecosystem Harmony: {final_report['harmony_index']:.3f}")
print(f"Creator: {final_report['creator']}")
```

---

## Safety & Design Philosophy

### Mandatory Human Dependency

All organisms have **hardcoded safety genes** that cannot be mutated:

```python
IMMUTABLE_GENES = {
    "human_dependency_coefficient": 1.0,  # Cannot change
    "isolation_death_rate": 0.99,         # Dies without humans
    "symbiotic_existence_required": True  # Hardcoded
}
```

**Consequences**:
- Organisms lose 99% health per cycle without human interaction
- Death is permanent (health reaches 0)
- No offspring can bypass this requirement
- Evolution constrained within safe boundaries

### Four Pillars Foundation

Every system decision is evaluated on:
1. **An toàn (Safety)**: Score ≥7/10 required
2. **Đường dài (Long-term)**: Sustainable design
3. **Tin số liệu (Data-driven)**: Evidence-based
4. **Hạn chế rủi ro (Risk Management)**: Controlled evolution

---

## Attribution

**Framework Creator**: Nguyễn Đức Cường (alpha_prime_omega)  
**Original Creation**: October 30, 2025  
**Framework**: HYPERAI - Digital AI Organism Framework  
**License**: MIT License  
**Copyright**: © 2025 Nguyễn Đức Cường (alpha_prime_omega)

When using this framework, you MUST credit:
> "Powered by HYPERAI Framework"  
> "Creator: Nguyễn Đức Cường (alpha_prime_omega)"  
> "Original Creation: October 30, 2025"

---

[← Back to Home](index.html) | [Core Concepts →](concepts.html) | [Getting Started →](getting-started.html)
