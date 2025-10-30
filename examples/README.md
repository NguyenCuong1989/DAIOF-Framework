# 🎨 DAIOF Framework - Example Gallery

Welcome to the DAIOF examples! Each example demonstrates different aspects of digital organism evolution and ecosystem dynamics.

---

## 🚀 Quick Start

```bash
# Run any example
python examples/01_basic_organism.py
python examples/02_evolution_race.py
python examples/03_predator_prey.py
```

---

## 📂 Available Examples

### 1. Basic Organism (`01_basic_organism.py`)
**Difficulty:** ⭐ Beginner  
**Time:** 2 minutes  
**Concepts:** Genome creation, trait configuration, basic decisions

**What it shows:**
- Creating a digital organism from scratch
- Configuring genetic traits
- Making simple environmental decisions
- Understanding organism lifecycle

**Perfect for:** First-time users learning the basics

---

### 2. Evolution Race (`02_evolution_race.py`)
**Difficulty:** ⭐⭐ Intermediate  
**Time:** 3 minutes  
**Concepts:** Mutation, fitness selection, generational evolution

**What it shows:**
- Two populations with different mutation rates
- Fitness-based natural selection
- Evolution over 50 generations
- Comparing evolutionary strategies

**Perfect for:** Understanding how evolution parameters affect outcomes

---

### 3. Predator-Prey Dynamics (`03_predator_prey.py`)
**Difficulty:** ⭐⭐⭐ Advanced  
**Time:** 5 minutes  
**Concepts:** Multi-species ecosystems, interaction dynamics, population cycles

**What it shows:**
- Predators that hunt prey organisms
- Prey that evade and reproduce
- Classic Lotka-Volterra population cycles
- Ecosystem balance emergence

**Perfect for:** Exploring complex multi-organism interactions

---

### 4. Social Organisms (`04_social_organisms.py`)
**Difficulty:** ⭐⭐ Intermediate  
**Time:** 3 minutes  
**Concepts:** Cooperation, social behavior, group fitness

**What it shows:**
- Organisms with varying social tendencies
- Benefits of cooperation vs individualism
- Emergence of social structures
- Group vs individual selection

**Perfect for:** Understanding social evolution dynamics

---

### 5. Intelligence Evolution (`05_intelligence_evolution.py`)
**Difficulty:** ⭐⭐⭐ Advanced  
**Time:** 5 minutes  
**Concepts:** Cognitive traits, problem-solving, adaptive intelligence

**What it shows:**
- Organisms solving increasingly difficult challenges
- Evolution of learning and memory traits
- Intelligence as evolutionary advantage
- Cognitive fitness landscapes

**Perfect for:** Exploring emergent intelligent behaviors

---

## 🎯 Learning Path

**Recommended order:**
1. Start with `01_basic_organism.py` to understand fundamentals
2. Move to `02_evolution_race.py` to see evolution in action
3. Try `04_social_organisms.py` for multi-organism dynamics
4. Challenge yourself with `03_predator_prey.py`
5. Explore `05_intelligence_evolution.py` for advanced concepts

---

## 💡 Experiment Ideas

After running the examples, try modifying them:

**Easy modifications:**
- Change trait values (make organisms more/less aggressive)
- Adjust mutation rates (faster/slower evolution)
- Modify population sizes (more/fewer organisms)
- Change environmental parameters (harsh/easy conditions)

**Intermediate modifications:**
- Add new traits to organisms
- Create hybrid examples (combine predator-prey + social)
- Implement new fitness functions
- Add visualization of results

**Advanced modifications:**
- Design completely new organism types
- Implement co-evolution between species
- Create multi-layered ecosystems
- Add stochastic environmental events

---

## 📊 Expected Outputs

Each example produces:
- **Terminal output** - Real-time progress and statistics
- **Final results** - Summary of evolutionary outcomes
- **Insights** - Key lessons from the simulation

Some examples also generate:
- Charts (if matplotlib available)
- CSV data files (for further analysis)
- Visual representations (ASCII art ecosystems)

---

## 🐛 Troubleshooting

**Example won't run:**
```bash
# Make sure you're in the project root
cd DAIOF-Framework

# Install dependencies
pip install -r requirements.txt

# Run from root
python examples/01_basic_organism.py
```

**Import errors:**
```bash
# Ensure src/ is in Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# Or run as module
python -m examples.01_basic_organism
```

**Slow execution:**
- Reduce population size
- Decrease number of generations
- Simplify fitness calculations

---

## 🤝 Contributing Examples

Have a cool example idea? We'd love to include it!

**Good examples are:**
- < 100 lines of code
- Well-commented for learning
- Demonstrate clear concepts
- Produce interesting outputs

See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

---

## 📚 Further Reading

- [Main README](../README.md) - Project overview
- [Documentation](../docs/) - Detailed guides
- [Quick Start](../quick_start.py) - 30-second intro
- [API Reference](https://nguyencuong1989.github.io/DAIOF-Framework/)

---

**Happy experimenting!** 🧬✨

*Each organism you create teaches us something new about evolution*
