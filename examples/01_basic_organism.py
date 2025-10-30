#!/usr/bin/env python3
"""
Basic Digital Organism Example
Demonstrates fundamental organism capabilities: genome, metabolism, decision-making

This is the SIMPLEST example to understand DAIOF Framework.
Perfect for: First-time users, tutorials, quick demos
"""

from daiof.core.digital_organism import DigitalOrganism
from daiof.core.digital_genome import DigitalGenome
from daiof.core.digital_metabolism import DigitalMetabolism


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
    
    genome = DigitalGenome()
    
    # Set basic traits
    genome.set_gene('learning_rate', 0.5)          # How fast it learns
    genome.set_gene('exploration_factor', 0.3)     # How much it explores
    genome.set_gene('energy_efficiency', 0.7)      # How well it uses energy
    
    # Immutable genes (cannot be changed)
    genome.set_immutable_gene('human_dependency_coefficient', 1.0)
    genome.set_immutable_gene('symbiotic_existence_required', True)
    
    print(f"✅ Genome created with {len(genome.genes)} genes")
    print(f"   - Learning Rate: {genome.get_gene('learning_rate')}")
    print(f"   - Exploration: {genome.get_gene('exploration_factor')}")
    print(f"   - Energy Efficiency: {genome.get_gene('energy_efficiency')}")
    print(f"   - Human Dependency: {genome.get_gene('human_dependency_coefficient')} (immutable)")
    print()
    
    # Step 2: Create the Organism
    print("Step 2: Creating Digital Organism...")
    print("-" * 60)
    
    organism = DigitalOrganism(
        genome=genome,
        organism_id="basic_001",
        name="Alpha"
    )
    
    print(f"✅ Organism '{organism.name}' created (ID: {organism.organism_id})")
    print(f"   - Initial Health: {organism.get_health():.1%}")
    print(f"   - Initial Energy: {organism.metabolism.get_energy_level():.1f}")
    print()
    
    # Step 3: Demonstrate Metabolism
    print("Step 3: Testing Metabolism (Energy Management)...")
    print("-" * 60)
    
    # Consume resources (like thinking or processing)
    print("🔥 Organism consuming energy for processing...")
    organism.metabolism.consume_resource('cpu_cycles', 10)
    organism.metabolism.consume_resource('memory_units', 5)
    
    print(f"   Energy after consumption: {organism.metabolism.get_energy_level():.1f}")
    print()
    
    # Regenerate resources (like resting or recharging)
    print("🔋 Organism regenerating energy...")
    organism.metabolism.regenerate(amount=20)
    
    print(f"   Energy after regeneration: {organism.metabolism.get_energy_level():.1f}")
    print()
    
    # Step 4: Make Decisions
    print("Step 4: Making Decisions...")
    print("-" * 60)
    
    # Simulate environmental input
    environment_data = {
        'temperature': 25.0,
        'complexity': 0.6,
        'urgency': 0.8
    }
    
    print(f"📊 Environment: {environment_data}")
    
    # Organism decides based on genome and environment
    decision = organism.decide(environment_data)
    
    print(f"🧠 Decision made: {decision}")
    print(f"   - Action: {decision.get('action', 'process')}")
    print(f"   - Confidence: {decision.get('confidence', 0.0):.1%}")
    print()
    
    # Step 5: Learn from Experience
    print("Step 5: Learning from Experience...")
    print("-" * 60)
    
    experience = {
        'input': environment_data,
        'output': decision,
        'reward': 0.8  # How good was the decision
    }
    
    organism.learn(experience)
    
    print(f"✅ Organism learned from experience (reward: {experience['reward']:.1%})")
    print(f"   - Learning buffer size: {len(organism.nervous_system.learning_buffer)}")
    print()
    
    # Step 6: Check Final Health
    print("Step 6: Final Health Check...")
    print("-" * 60)
    
    final_health = organism.get_health()
    final_energy = organism.metabolism.get_energy_level()
    
    print(f"🏥 Organism Health Report:")
    print(f"   - Overall Health: {final_health:.1%}")
    print(f"   - Energy Level: {final_energy:.1f}")
    print(f"   - Age: {organism.age} cycles")
    print(f"   - Experiences: {len(organism.nervous_system.learning_buffer)}")
    
    # Health assessment
    if final_health >= 0.8:
        status = "💚 EXCELLENT"
    elif final_health >= 0.6:
        status = "💛 GOOD"
    elif final_health >= 0.4:
        status = "🧡 FAIR"
    else:
        status = "❤️ NEEDS ATTENTION"
    
    print(f"   - Status: {status}")
    print()
    
    # Summary
    print("="*60)
    print("🎉 EXAMPLE COMPLETE")
    print("="*60)
    print()
    print("Key Takeaways:")
    print("1. Genomes define organism characteristics (like DNA)")
    print("2. Metabolism manages energy (like eating/resting)")
    print("3. Organisms make decisions based on genome + environment")
    print("4. Learning improves decision-making over time")
    print("5. Health depends on energy, age, and experiences")
    print()
    print("Next Steps:")
    print("- Try: examples/02_evolution_race.py (see organisms evolve)")
    print("- Try: examples/03_predator_prey.py (ecosystem simulation)")
    print("- Read: docs/ for detailed documentation")
    print()


if __name__ == '__main__':
    main()
