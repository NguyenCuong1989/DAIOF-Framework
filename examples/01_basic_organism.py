#!/usr/bin/env python3
"""
Basic Digital Organism Example
Demonstrates fundamental organism capabilities: genome, metabolism, decision-making

This is the SIMPLEST example to understand DAIOF Framework.
Perfect for: First-time users, tutorials, quick demos

Creator: Nguyễn Đức Cường (alpha_prime_omega)
Framework: DAIOF (Digital Autonomous Intelligent Organism Framework)
Original Creation: October 30, 2025
"""

from src.digital_organism import DigitalOrganism, DigitalGenome


def main():
    """
    Creates a basic digital organism and demonstrates its core functions.
    
    This example shows:
    1. How to create a genome (DNA)
    2. How to initialize an organism
    3. How metabolism works (energy management)
    4. How organisms make decisions
    5. How to check organism health
    """
    
    print("="*60)
    print("🧬 BASIC DIGITAL ORGANISM EXAMPLE")
    print("="*60)
    print()
    
    # Step 1: Create the Genome (DNA)
    print("Step 1: Creating Genome (DNA)...")
    print("-" * 60)
    
    genome = DigitalGenome(
        traits={
            'learning_rate': 0.5,           # How fast it learns
            'exploration_factor': 0.3,      # How much it explores
            'energy_efficiency': 0.7,       # How well it uses energy
            'memory_retention': 0.8,        # How well it remembers
            'social_tendency': 0.5,         # Social behavior
            'adaptation_speed': 0.6,        # How fast it adapts
            'risk_tolerance': 0.4,          # Risk-taking behavior
            'reproduction_rate': 0.5        # Reproduction capability
        },
        mutation_rate=0.1
    )
    
    print(f"✅ Genome created with {len(genome.traits)} traits")
    print(f"   - Learning Rate: {genome.traits['learning_rate']}")
    print(f"   - Exploration: {genome.traits['exploration_factor']}")
    print(f"   - Energy Efficiency: {genome.traits['energy_efficiency']}")
    print(f"   - Memory Retention: {genome.traits['memory_retention']}")
    print()
    
    # Step 2: Create the Organism
    print("Step 2: Creating Digital Organism...")
    print("-" * 60)
    
    organism = DigitalOrganism(
        organism_id="basic_001",
        genome=genome,
        initial_resources={
            'cpu_cycles': 100,
            'memory_units': 50,
            'network_bandwidth': 30,
            'storage_space': 20,
            'knowledge_points': 10
        }
    )
    
    print(f"✅ Organism '{organism.organism_id}' created")
    print(f"   - Initial Energy: {organism.energy:.1f}")
    print(f"   - Fitness: {organism.fitness:.2f}")
    print(f"   - Generation: {organism.generation}")
    print()
    
    # Step 3: Demonstrate Metabolism
    print("Step 3: Testing Metabolism (Energy Management)...")
    print("-" * 60)
    
    print(f"🔥 Organism performing actions (consuming energy)...")
    
    # Simulate thinking/processing (costs energy)
    initial_energy = organism.energy
    organism.consume_energy(10)
    
    print(f"   Energy before: {initial_energy:.1f}")
    print(f"   Energy consumed: 10")
    print(f"   Energy after: {organism.energy:.1f}")
    print()
    
    # Step 4: Make Decisions
    print("Step 4: Making Decisions...")
    print("-" * 60)
    
    # Simulate environmental input
    environment_data = {
        'challenge_level': 0.6,
        'resource_availability': 0.7,
        'threat_level': 0.3,
        'temperature': 25.0,
        'complexity': 0.6,
        'urgency': 0.8
    }
    
    print(f"📊 Environment: {environment_data}")
    
    # Organism perceives and decides
    decision = organism.perceive_and_decide(environment_data)
    
    print(f"🧠 Decision made:")
    print(f"   - Action: {decision.get('action', 'unknown')}")
    print(f"   - Confidence: {decision.get('confidence', 0.0):.1%}")
    print(f"   - Reasoning: {decision.get('reasoning', 'N/A')}")
    print()
    
    # Step 5: Learn from Experience
    print("Step 5: Learning from Experience...")
    print("-" * 60)
    
    experience = {
        'state': environment_data,
        'action': decision.get('action', 'process'),
        'reward': 0.8,  # How good was the decision
        'next_state': {
            'challenge_level': 0.5,
            'resource_availability': 0.8,
            'threat_level': 0.2
        }
    }
    
    organism.learn_from_experience(experience)
    
    print(f"✅ Organism learned from experience (reward: {experience['reward']:.1%})")
    print(f"   - Memory size: {len(organism.nervous_system.memory)}")
    print()
    
    # Step 6: Evolution - Create Offspring
    print("Step 6: Evolution (Creating Offspring)...")
    print("-" * 60)
    
    offspring = organism.reproduce()
    
    print(f"👶 Offspring created: {offspring.organism_id}")
    print(f"   - Parent generation: {organism.generation}")
    print(f"   - Offspring generation: {offspring.generation}")
    print(f"   - Genome mutated: {offspring.genome != organism.genome}")
    print()
    
    # Compare traits
    print("🔬 Trait comparison (Parent → Offspring):")
    for trait_name in ['learning_rate', 'exploration_factor', 'energy_efficiency']:
        parent_val = organism.genome.traits[trait_name]
        offspring_val = offspring.genome.traits[trait_name]
        change = offspring_val - parent_val
        print(f"   - {trait_name}: {parent_val:.3f} → {offspring_val:.3f} ({change:+.3f})")
    print()
    
    # Step 7: Check Final Status
    print("Step 7: Final Status Check...")
    print("-" * 60)
    
    status = organism.get_status()
    
    print(f"🏥 Organism Status Report:")
    print(f"   - ID: {status['organism_id']}")
    print(f"   - Energy: {status['energy']:.1f}")
    print(f"   - Fitness: {status['fitness']:.2f}")
    print(f"   - Age: {status['age']} cycles")
    print(f"   - Alive: {status['alive']}")
    print(f"   - Generation: {status['generation']}")
    
    # Health assessment
    if status['energy'] >= 80:
        health_status = "💚 EXCELLENT"
    elif status['energy'] >= 60:
        health_status = "💛 GOOD"
    elif status['energy'] >= 40:
        health_status = "🧡 FAIR"
    else:
        health_status = "❤️ NEEDS ATTENTION"
    
    print(f"   - Status: {health_status}")
    print()
    
    # Summary
    print("="*60)
    print("🎉 EXAMPLE COMPLETE")
    print("="*60)
    print()
    print("Key Takeaways:")
    print("1. Genomes define organism characteristics (8 core traits)")
    print("2. Organisms consume energy when performing actions")
    print("3. Decisions are made based on genome + environment")
    print("4. Learning improves decision-making over time")
    print("5. Reproduction creates mutated offspring (evolution!)")
    print()
    print("Next Steps:")
    print("- Try: examples/02_evolution_race.py (see organisms evolve)")
    print("- Try: examples/03_predator_prey.py (ecosystem simulation)")
    print("- Try: examples/04_multi_species.py (complex ecosystems)")
    print("- Read: docs/ for detailed documentation")
    print()
    print("---")
    print("Powered by HYPERAI Framework")
    print("Creator: Nguyễn Đức Cường (alpha_prime_omega)")
    print("Original Creation: October 30, 2025")
    print("---")
    print()


if __name__ == '__main__':
    main()
