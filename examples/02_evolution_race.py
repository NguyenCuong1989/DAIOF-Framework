#!/usr/bin/env python3
"""
Evolution Race Example
Watch multiple organisms compete and evolve over generations

This example demonstrates:
- Population dynamics
- Natural selection
- Genetic mutation
- Survival of the fittest
- Multi-generation evolution
"""

from daiof.core.digital_organism import DigitalOrganism
from daiof.core.digital_genome import DigitalGenome
from daiof.evolution.evolution_engine import EvolutionEngine
import random


def create_random_organism(organism_id: str) -> DigitalOrganism:
    """Create an organism with random genes"""
    genome = DigitalGenome()
    
    # Random traits
    genome.set_gene('speed', random.uniform(0.3, 0.9))
    genome.set_gene('strength', random.uniform(0.3, 0.9))
    genome.set_gene('intelligence', random.uniform(0.3, 0.9))
    genome.set_gene('adaptability', random.uniform(0.3, 0.9))
    
    # Immutable DNA
    genome.set_immutable_gene('human_dependency_coefficient', 1.0)
    
    return DigitalOrganism(genome=genome, organism_id=organism_id)


def fitness_function(organism: DigitalOrganism) -> float:
    """Calculate organism fitness score"""
    speed = organism.genome.get_gene('speed')
    strength = organism.genome.get_gene('strength')
    intelligence = organism.genome.get_gene('intelligence')
    adaptability = organism.genome.get_gene('adaptability')
    
    # Weighted fitness (intelligence and adaptability more important)
    fitness = (
        speed * 0.2 +
        strength * 0.2 +
        intelligence * 0.3 +
        adaptability * 0.3
    )
    
    return fitness


def main():
    print("="*70)
    print("🏁 EVOLUTION RACE - Natural Selection in Action")
    print("="*70)
    print()
    
    # Configuration
    POPULATION_SIZE = 10
    GENERATIONS = 5
    MUTATION_RATE = 0.2
    
    print(f"⚙️  Configuration:")
    print(f"   Population Size: {POPULATION_SIZE}")
    print(f"   Generations: {GENERATIONS}")
    print(f"   Mutation Rate: {MUTATION_RATE}")
    print()
    
    # Create initial population
    print("🧬 Creating initial population...")
    print("-" * 70)
    
    population = [create_random_organism(f"org_{i}") for i in range(POPULATION_SIZE)]
    
    print(f"✅ Created {len(population)} organisms with random genes")
    print()
    
    # Evolution Engine
    evolution = EvolutionEngine(
        mutation_rate=MUTATION_RATE,
        crossover_rate=0.7,
        elite_size=2  # Keep top 2 organisms
    )
    
    # Track best organism across generations
    best_organisms = []
    
    # Evolution loop
    for generation in range(GENERATIONS):
        print(f"🔄 GENERATION {generation + 1}")
        print("-" * 70)
        
        # Evaluate fitness
        fitness_scores = [(org, fitness_function(org)) for org in population]
        fitness_scores.sort(key=lambda x: x[1], reverse=True)
        
        # Show top 3
        print("🏆 Top 3 Organisms:")
        for rank, (org, fitness) in enumerate(fitness_scores[:3], 1):
            speed = org.genome.get_gene('speed')
            strength = org.genome.get_gene('strength')
            intelligence = org.genome.get_gene('intelligence')
            adaptability = org.genome.get_gene('adaptability')
            
            print(f"   #{rank} {org.organism_id}: Fitness = {fitness:.3f}")
            print(f"       Speed: {speed:.2f} | Strength: {strength:.2f} | "
                  f"Intel: {intelligence:.2f} | Adapt: {adaptability:.2f}")
        
        # Track best
        best_org, best_fitness = fitness_scores[0]
        best_organisms.append((generation + 1, best_org, best_fitness))
        
        print(f"\n   📊 Generation Stats:")
        print(f"      Best Fitness: {best_fitness:.3f}")
        print(f"      Avg Fitness: {sum(f for _, f in fitness_scores)/len(fitness_scores):.3f}")
        print(f"      Worst Fitness: {fitness_scores[-1][1]:.3f}")
        print()
        
        # Evolve to next generation
        if generation < GENERATIONS - 1:
            print("   🧬 Evolving to next generation...")
            population = evolution.evolve_population(
                population=[org for org, _ in fitness_scores],
                fitness_scores=[f for _, f in fitness_scores]
            )
            print(f"   ✅ New generation created with mutations")
            print()
    
    # Final summary
    print("="*70)
    print("📊 EVOLUTION COMPLETE - Summary")
    print("="*70)
    print()
    
    print("🏆 Best Organism from Each Generation:")
    for gen, org, fitness in best_organisms:
        print(f"   Gen {gen}: {org.organism_id} - Fitness: {fitness:.3f}")
    
    print()
    print("📈 Evolution Progress:")
    first_best = best_organisms[0][2]
    last_best = best_organisms[-1][2]
    improvement = ((last_best - first_best) / first_best) * 100
    
    print(f"   Generation 1 Best: {first_best:.3f}")
    print(f"   Generation {GENERATIONS} Best: {last_best:.3f}")
    print(f"   Improvement: {improvement:+.1f}%")
    
    if improvement > 0:
        print(f"   ✅ Population IMPROVED through natural selection!")
    else:
        print(f"   ⚠️  Population stable (may need more generations)")
    
    print()
    print("🔬 Key Insights:")
    print("   - Natural selection favors fitter organisms")
    print("   - Mutation introduces variation")
    print("   - Elite preservation maintains good genes")
    print("   - Population improves over generations")
    print()
    print("Next: Try examples/03_predator_prey.py for ecosystem simulation")
    print()


if __name__ == '__main__':
    main()
