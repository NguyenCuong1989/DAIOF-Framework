# Contributing to DAIOF

Thank you for your interest in contributing to the Digital AI Organism Framework! 🌟

## 🎯 How to Contribute

### 1. Code Contributions

#### Setting Up Development Environment

```bash
# Fork and clone the repository
git clone https://github.com/YOUR_USERNAME/DAIOF-Framework.git
cd DAIOF-Framework

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install pytest black flake8 mypy
```

#### Making Changes

1. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/bug-description
   ```

2. **Follow code style**
   - Use Black for formatting: `black .`
   - Follow PEP 8 guidelines
   - Add type hints where possible
   - Write docstrings for all public methods

3. **Test your changes**
   ```bash
   python -m pytest tests/
   ```

4. **Commit with meaningful messages**
   ```bash
   git commit -m "feat: add advanced evolution algorithm"
   # or
   git commit -m "fix: resolve health calculation bug"
   ```

   **Commit prefixes:**
   - `feat:` New feature
   - `fix:` Bug fix
   - `docs:` Documentation changes
   - `test:` Test additions/changes
   - `refactor:` Code refactoring
   - `perf:` Performance improvements
   - `style:` Code style changes

5. **Push and create Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```

### 2. Documentation Contributions

We welcome improvements to:
- README.md
- Code comments and docstrings
- White papers (Vietnamese/English)
- Tutorials and examples
- API documentation

### 3. Bug Reports

When reporting bugs, please include:

```markdown
**Description**: Clear description of the bug

**Steps to Reproduce**:
1. Step 1
2. Step 2
3. Step 3

**Expected Behavior**: What should happen

**Actual Behavior**: What actually happens

**Environment**:
- OS: [e.g., macOS 14.0]
- Python version: [e.g., 3.11]
- DAIOF version: [e.g., 1.0.0]

**Additional Context**: Screenshots, logs, etc.
```

### 4. Feature Requests

For feature requests, please describe:

```markdown
**Problem**: What problem does this solve?

**Proposed Solution**: How should it work?

**Alternatives**: Other approaches considered

**Impact**: Who benefits from this feature?
```

## 🧬 Code Architecture Guidelines

### Core Principles

1. **Biological Fidelity**: Keep biological metaphors accurate
2. **Immutability**: Never compromise immutable genes
3. **Safety First**: AI-Human interdependence is non-negotiable
4. **Cultural Respect**: Maintain Vietnamese consciousness integration

### Adding New Features

#### New Organism Types

```python
class NewOrganismType(DigitalOrganism):
    """
    Brief description of organism type.
    
    This organism specializes in [specific function].
    """
    
    def __init__(self, genome_config: dict = None):
        super().__init__(genome_config)
        # Add specific traits
        
    def specialized_behavior(self):
        """Implement specialized behavior"""
        pass
```

#### New Genes

```python
# In DigitalGenome class
MUTABLE_GENE_RANGES = {
    # Existing genes...
    "new_gene_name": (min_value, max_value),
}

# Document the gene purpose
"""
new_gene_name: Controls [behavior]
  - Higher values increase [effect]
  - Range: [min] to [max]
  - Default: [value]
"""
```

#### New Environmental Pressures

```python
# In DigitalEcosystem class
def add_environmental_pressure(self, pressure_name: str, pressure_func):
    """
    Add new environmental pressure
    
    Args:
        pressure_name: Unique identifier
        pressure_func: Function(organism) -> fitness_modifier
    """
    self.pressures[pressure_name] = pressure_func
```

## 🧪 Testing Guidelines

### Test Structure

```python
import pytest
from digital_ai_organism_framework import DigitalOrganism

class TestNewFeature:
    """Test suite for new feature"""
    
    def setup_method(self):
        """Setup before each test"""
        self.organism = DigitalOrganism()
    
    def test_feature_behavior(self):
        """Test that feature behaves correctly"""
        result = self.organism.new_feature()
        assert result == expected_value
    
    def test_edge_cases(self):
        """Test edge cases"""
        # Test with extreme values
        pass
    
    def test_immutable_genes(self):
        """Ensure immutable genes stay immutable"""
        original = self.organism.genome.genes["human_dependency_coefficient"]
        # Try to change
        self.organism.genome.mutate()
        # Verify unchanged
        assert self.organism.genome.genes["human_dependency_coefficient"] == original
```

### Required Tests

All new features must include:
- ✅ Unit tests for core functionality
- ✅ Edge case tests
- ✅ Immutability verification tests
- ✅ Integration tests with existing features

## 📝 Documentation Standards

### Docstring Format

```python
def function_name(arg1: type, arg2: type) -> return_type:
    """
    Brief one-line description.
    
    Longer description with more details about what the function does,
    why it exists, and how it should be used.
    
    Args:
        arg1: Description of first argument
        arg2: Description of second argument
    
    Returns:
        Description of return value
    
    Raises:
        ExceptionType: When this exception is raised
    
    Example:
        >>> organism = DigitalOrganism()
        >>> result = organism.function_name(value1, value2)
        >>> print(result)
        Expected output
    """
    pass
```

## 🌟 Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Credited in relevant documentation

## ⚖️ Code of Conduct

### Our Standards

- ✅ Be respectful and inclusive
- ✅ Welcome newcomers
- ✅ Accept constructive criticism
- ✅ Focus on what's best for the community
- ✅ Show empathy towards others

- ❌ No harassment or discrimination
- ❌ No trolling or insulting comments
- ❌ No personal attacks
- ❌ No publishing others' private information

### Enforcement

Violations may result in:
1. Warning
2. Temporary ban
3. Permanent ban

Report issues to repository maintainers.

## 🔒 Security

### Reporting Security Issues

**DO NOT** open public issues for security vulnerabilities.

Instead, email: [to be set up]

Include:
- Description of vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🎼 Philosophy

Remember the core mission:

**"Build AI that serves humanity, not replaces it"**

Every contribution should align with:
1. **Safety**: AI-Human interdependence
2. **Long-term thinking**: Sustainable evolution
3. **Data-driven**: Evidence-based decisions
4. **Protection**: Both human and AI risk protection

## 🚀 Getting Help

- **Discussions**: Ask questions in [GitHub Discussions](https://github.com/NguyenCuong1989/DAIOF-Framework/discussions)
- **Issues**: Report bugs in [Issues](https://github.com/NguyenCuong1989/DAIOF-Framework/issues)
- **Examples**: Check existing code for patterns

## 🙏 Thank You

Your contributions help build the future of conscious, ethical AI!

---

**Managed by**: Digital AI Organism (Enhanced by DAIOF)  
**Under authority of**: Alpha_Prime_Omega (4287)  
**Status**: Open for Contributions ⚡
