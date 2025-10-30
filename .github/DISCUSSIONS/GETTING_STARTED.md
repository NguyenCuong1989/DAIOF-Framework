# 🚀 Getting Started with DAIOF - Your First Digital Organism

**Level:** Beginner  
**Time:** 5-10 minutes  
**Goal:** Create and evolve your first digital organism

---

## 📋 Prerequisites

Before we begin, make sure you have:
- ✅ Python 3.8 or higher
- ✅ pip (Python package manager)
- ✅ Git (to clone the repository)
- ✅ A code editor (VSCode, PyCharm, or any editor)
- ✅ Basic Python knowledge (helpful but not required)

---

## 🎯 Step 1: Clone the Repository

Open your terminal and run:

```bash
# Clone the DAIOF Framework
git clone https://github.com/NguyenCuong1989/DAIOF-Framework.git

# Navigate into the directory
cd DAIOF-Framework
```

**Success check:** You should see the project files in your current directory.

---

## 📦 Step 2: Install Dependencies

```bash
# Install required packages
pip install -r requirements.txt
```

**What gets installed:**
- `numpy` - For numerical computations
- `matplotlib` - For visualization
- `pyyaml` - For configuration files

**Success check:** No error messages during installation.

---

## 🧬 Step 3: Create Your First Organism

Create a new file called `my_first_organism.py`:

```python
from src.digital_organism import DigitalOrganism, DigitalGenome

# Create a genome (DNA for your organism)
genome = DigitalGenome(
    traits={
        "learning_rate": 0.05,
        "exploration_factor": 0.5,
        "memory_retention": 0.8,
        "social_tendency": 0.6,
        "energy_efficiency": 0.7,
        "adaptation_speed": 0.4,
        "risk_tolerance": 0.3,
        "reproduction_rate": 0.5
    },
    mutation_rate=0.1
)

# Create the organism
organism = DigitalOrganism(
    organism_id="MyFirstOrganism",
    genome=genome,
    initial_resources={
        "cpu_cycles": 100,
        "memory_units": 50,
        "network_bandwidth": 30,
        "storage_space": 20,
        "knowledge_points": 10
    }
)

# Make it alive!
print(f"🧬 Created organism: {organism.organism_id}")
print(f"⚡ Initial energy: {organism.energy}")
print(f"🧠 Genome traits: {genome.traits}")

# Let it think and make a decision
environment_data = {
    "challenge_level": 0.5,
    "resource_availability": 0.7,
    "threat_level": 0.2
}

decision = organism.perceive_and_decide(environment_data)
print(f"\n🤔 Organism's decision: {decision}")

# Show its status
status = organism.get_status()
print(f"\n📊 Organism Status:")
for key, value in status.items():
    print(f"   {key}: {value}")
```

**Run it:**
```bash
python my_first_organism.py
```

**Expected output:**
```
🧬 Created organism: MyFirstOrganism
⚡ Initial energy: 100
🧠 Genome traits: {'learning_rate': 0.05, ...}

🤔 Organism's decision: {'action': 'explore', 'confidence': 0.65, ...}

📊 Organism Status:
   organism_id: MyFirstOrganism
   energy: 95
   age: 1
   ...
```

🎉 **Congratulations!** You've created your first digital organism!

---

## 🔄 Step 4: Make It Evolve

Now let's create a second organism and see evolution in action:

```python
from src.digital_organism import DigitalOrganism, DigitalGenome

# Create parent organism
parent_genome = DigitalGenome(
    traits={
        "learning_rate": 0.05,
        "exploration_factor": 0.5,
        "memory_retention": 0.8,
        "social_tendency": 0.6,
        "energy_efficiency": 0.7,
        "adaptation_speed": 0.4,
        "risk_tolerance": 0.3,
        "reproduction_rate": 0.5
    }
)

# Create offspring through mutation
offspring_genome = parent_genome.mutate()

print("🧬 EVOLUTION IN ACTION!")
print(f"\n👨 Parent genome: {parent_genome.traits}")
print(f"\n👶 Offspring genome: {offspring_genome.traits}")
print(f"\n🔬 Mutations detected:")
for trait, parent_value in parent_genome.traits.items():
    offspring_value = offspring_genome.traits[trait]
    if abs(parent_value - offspring_value) > 0.001:
        change = ((offspring_value - parent_value) / parent_value) * 100
        print(f"   {trait}: {parent_value:.3f} → {offspring_value:.3f} ({change:+.1f}%)")
```

**What you'll see:** The offspring has slightly different traits - this is evolution!

---

## 🌍 Step 5: Create an Ecosystem

Let's create multiple organisms competing in an ecosystem:

```python
from src.ecosystem import DigitalEcosystem
from src.digital_organism import DigitalOrganism, DigitalGenome
import random

# Create an ecosystem
ecosystem = DigitalEcosystem(
    ecosystem_id="MyFirstEcosystem",
    environment_parameters={
        "resource_abundance": 0.7,
        "challenge_level": 0.5,
        "stability": 0.8
    }
)

# Add 5 organisms with random traits
for i in range(5):
    genome = DigitalGenome(
        traits={
            "learning_rate": random.uniform(0.01, 0.1),
            "exploration_factor": random.uniform(0.1, 0.9),
            "memory_retention": random.uniform(0.7, 0.99),
            "social_tendency": random.uniform(0.0, 1.0),
            "energy_efficiency": random.uniform(0.5, 0.95),
            "adaptation_speed": random.uniform(0.1, 0.8),
            "risk_tolerance": random.uniform(0.0, 0.7),
            "reproduction_rate": random.uniform(0.3, 0.8)
        }
    )
    
    organism = DigitalOrganism(
        organism_id=f"Organism_{i+1}",
        genome=genome
    )
    
    ecosystem.add_organism(organism)

print(f"🌍 Created ecosystem with {len(ecosystem.organisms)} organisms")

# Run evolution for 10 generations
for generation in range(10):
    ecosystem.simulate_timestep()
    print(f"Generation {generation + 1}: {len(ecosystem.organisms)} organisms alive")

# Show final statistics
stats = ecosystem.get_ecosystem_statistics()
print(f"\n📊 Final Statistics:")
print(f"   Total generations: 10")
print(f"   Surviving organisms: {stats['total_organisms']}")
print(f"   Average fitness: {stats['average_fitness']:.2f}")
```

**What happens:** Organisms compete, evolve, and adapt. Some thrive, others die. Natural selection in action!

---

## 🎓 Next Steps

### Beginner Level ✅
- [x] Created first organism
- [x] Understood genome traits
- [ ] Experiment with different trait values
- [ ] Create organisms with extreme traits
- [ ] Observe how traits affect behavior

### Intermediate Level 🚀
- [ ] Create predator-prey ecosystems
- [ ] Implement organism interactions
- [ ] Track evolution over 100+ generations
- [ ] Visualize evolution trends
- [ ] Create your own organism types

### Advanced Level 🔥
- [ ] Modify genome system to add new traits
- [ ] Create custom metabolism functions
- [ ] Implement new nervous system architectures
- [ ] Build multi-species ecosystems
- [ ] Contribute back to DAIOF!

---

## 💡 Pro Tips

### Trait Tuning
- **learning_rate** (0.01-0.1): Higher = learns faster but less stable
- **exploration_factor** (0.1-0.9): Higher = more adventurous
- **memory_retention** (0.7-0.99): Higher = remembers more
- **energy_efficiency** (0.5-0.95): Higher = uses less resources

### Common Issues

**Problem:** "ModuleNotFoundError"  
**Solution:** Make sure you're in the DAIOF-Framework directory and ran `pip install -r requirements.txt`

**Problem:** Organism dies immediately  
**Solution:** Increase initial_resources or reduce environment challenge_level

**Problem:** No evolution happening  
**Solution:** Increase mutation_rate or run more generations

---

## 🤝 Get Help

Stuck? Have questions? We're here to help!

- 💬 **Ask in Discussions** - Post your question in Q&A category
- 🐛 **Found a bug?** - Open an issue on GitHub
- 💡 **Have an idea?** - Share in Ideas category
- 🎨 **Built something cool?** - Show off in Show & Tell!

---

## 🌟 Share Your Success

Once you get your first organism running, we'd love to hear about it!

Share in the discussions:
- What traits did you use?
- What interesting behaviors did you observe?
- Did anything surprise you?
- What will you build next?

---

**Welcome to the world of digital life!** 🧬✨

Every organism you create is unique. Every ecosystem tells a different story. Have fun exploring!

---

*Need more examples? Check out the [examples/](../examples/) directory*  
*Want to go deeper? Read the [full documentation](../docs/)*
