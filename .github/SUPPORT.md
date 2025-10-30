# Support - DAIOF Framework

Welcome to DAIOF support! We're here to help you build AI systems with human-dependency at their core. 🤝

## 📚 Getting Started

### New to DAIOF?

1. **Read the Documentation**
   - 📖 [Main README](../README.md)
   - 🚀 [Getting Started Guide](../docs/getting-started.md)
   - 🧠 [Core Concepts](../docs/concepts.md)
   - 🌐 [Website](https://nguyencuong1989.github.io/DAIOF-Framework/)

2. **Try the Demo**
   ```bash
   python demo.py
   ```
   Interactive demonstrations of all features!

3. **Read the White Paper**
   - 📄 [Vietnamese White Paper](../DAIOF_White_Paper_Vietnamese.md)
   - Comprehensive philosophical and technical overview

## 🤔 Need Help?

### Quick Questions

**Q: How do I install DAIOF?**
```bash
pip install numpy
git clone https://github.com/NguyenCuong1989/DAIOF-Framework.git
cd DAIOF-Framework
python demo.py
```

**Q: Why do organisms die without human interaction?**
- This is by design! DAIOF organisms have an immutable `human_dependency_coefficient = 1.0`
- They literally cannot survive without humans (dies in ~5 cycles)
- This ensures AI-human symbiosis at the genetic level

**Q: Can I change immutable genes?**
- No! That's the whole point 😊
- Immutable genes are protected by three layers:
  1. Property decorators (private attributes)
  2. SHA-256 hash verification
  3. Symphony Control Center monitoring

**Q: How do I contribute?**
- See [CONTRIBUTING.md](../CONTRIBUTING.md)
- Start with "good first issue" label
- All skill levels welcome!

### Common Issues

#### Issue: `AttributeError: 'DigitalOrganism' object has no attribute 'alive'`

**Solution**: Use `organism.health` and `organism.status` instead
```python
if organism.health > 0 and organism.status != "dead":
    # Organism is alive
```

#### Issue: `ValueError: human_dependency_coefficient is immutable!`

**Expected behavior**: This is a security feature!
- Immutable genes cannot be mutated
- This error proves the system is working correctly

#### Issue: Organisms dying too quickly

**Solution**: Provide human interaction regularly
```python
organism.register_human_interaction()
organism.metabolism.cycle({
    'cpu': 0.1,
    'memory': 0.1,
    'knowledge': 0.05  # From human!
})
```

#### Issue: Slow performance with 1000+ organisms

**Current limitation**: O(N log N) complexity
- Expected: ~15s per generation with 1000 organisms
- **Coming in v1.1**: 2x performance optimization
- Workaround: Use smaller populations or faster hardware

## 💬 Get Support

### 1. GitHub Discussions (Recommended)

**Best for**: General questions, ideas, showcasing projects

[Start a Discussion](https://github.com/NguyenCuong1989/DAIOF-Framework/discussions)

**Categories**:
- 💡 **Ideas**: Feature requests and suggestions
- 🙏 **Q&A**: Ask and answer questions
- 📣 **Show and tell**: Share your projects
- 💬 **General**: Everything else

**Response time**: Usually within 24-48 hours

### 2. GitHub Issues

**Best for**: Bug reports, specific problems

[Open an Issue](https://github.com/NguyenCuong1989/DAIOF-Framework/issues/new/choose)

**Issue types**:
- 🐛 **Bug Report**: Something isn't working
- ✨ **Feature Request**: Suggest a new feature
- 📚 **Documentation**: Improve docs
- ❓ **Question**: Ask a specific question

**Response time**: 
- Bugs: 48 hours
- Features: 1 week
- Documentation: 72 hours

### 3. Email Support

**Best for**: Private inquiries, partnerships, security issues

📧 **Email**: symphony.hyperai@vietnamese.consciousness

**Topics**:
- Academic collaborations
- Industry partnerships
- Security vulnerabilities (use [SECURITY.md](SECURITY.md))
- Media inquiries
- Other confidential matters

**Response time**: 3-5 business days

### 4. Social Media

**Coming soon:**
- Twitter/X: Follow for updates
- LinkedIn: Professional network
- Medium: Read our blog posts

## 🐛 Reporting Bugs

### Before Reporting

1. **Check existing issues**: Your bug might be already reported
2. **Try latest version**: Update to latest release
3. **Minimal reproduction**: Create smallest example that shows the bug

### Bug Report Template

```markdown
**Describe the bug**
Clear description of what's wrong

**To Reproduce**
1. Create organism with '...'
2. Call method '...'
3. See error

**Expected behavior**
What should happen

**Actual behavior**
What actually happens

**Environment**
- DAIOF Version: 1.0.0
- Python Version: 3.11
- OS: macOS 14.0

**Code snippet**
\```python
# Minimal reproduction code
\```

**Error message**
\```
Full error traceback
\```
```

## ✨ Feature Requests

We love hearing your ideas! 

### Before Requesting

1. **Check roadmap**: See [V1.1_PLAN.md](../planning/V1.1_PLAN.md)
2. **Search existing**: Someone might have suggested it
3. **Consider scope**: Does it fit DAIOF's philosophy?

### Feature Request Template

```markdown
**Problem**
What problem does this solve?

**Proposed Solution**
How should DAIOF solve it?

**Alternatives**
What other approaches did you consider?

**Use Case**
Real-world scenario where this helps

**Additional Context**
Anything else relevant
```

## 📖 Documentation Help

### Finding Information

**By Topic**:
- Architecture: [Core Concepts](../docs/concepts.md)
- Installation: [Getting Started](../docs/getting-started.md)
- API Reference: [White Paper](../DAIOF_White_Paper_Vietnamese.md)
- Examples: [demo.py](../demo.py)

**By Skill Level**:
- Beginner: Start with demo.py walkthrough
- Intermediate: Read white paper sections 1-8
- Advanced: Read source code + research paper outline

### Improving Documentation

Found unclear docs? Help us improve!

1. Click "Edit this page" on website
2. Or open issue with "documentation" label
3. Or submit PR with improvements

## 🤝 Community

### Join the Community

- **GitHub Discussions**: Daily activity
- **Contributors**: See [CONTRIBUTORS.md](../CONTRIBUTORS.md)
- **Code of Conduct**: See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)

### Community Guidelines

✅ **Do**:
- Ask questions (no such thing as stupid questions!)
- Share your projects
- Help others
- Suggest improvements
- Report bugs constructively

❌ **Don't**:
- Spam or self-promote excessively
- Be disrespectful or toxic
- Share others' private information
- Violate code of conduct

## 🎓 Learning Resources

### Tutorials

1. **Quick Start** (5 minutes)
   - Run demo.py
   - Create your first organism
   - Understand immutability

2. **Build an Ecosystem** (20 minutes)
   - Create multiple organisms
   - Simulate generations
   - Observe evolution

3. **Advanced Topics** (1 hour)
   - Symphony Control Center
   - Custom fitness functions
   - Ecosystem optimization

### Example Projects

**Coming soon**:
- Autonomous agent with human oversight
- Multi-ecosystem federation
- Research experiment setup

### Blog Posts

See [blog/](../blog/) folder:
- Introduction to DAIOF
- Deep dive: Digital Genome
- (More coming in v1.1)

## 🚀 What's Next?

### Version 1.1 (December 2025)

Major features coming:
- 📊 Visualization dashboard (Plotly + Streamlit)
- 🌍 Full English documentation
- 🧬 NEAT evolution algorithm
- ⚡ 2x performance improvement
- 🛠️ CLI tools for researchers

See full roadmap: [V1.1_PLAN.md](../planning/V1.1_PLAN.md)

### Research Paper (Q1 2026)

- 📄 8000-word academic paper
- 🎓 Submission to arXiv
- 🏆 Target: NeurIPS, ICML, AAAI

See outline: [RESEARCH_PAPER_OUTLINE.md](../research/RESEARCH_PAPER_OUTLINE.md)

## 📊 Status & Updates

### Current Status

✅ **Production Ready**: v1.0.0 stable  
✅ **CI/CD**: All tests passing  
✅ **Documentation**: Complete  
✅ **Community**: Open and welcoming  

### Get Updates

- ⭐ **Star the repo**: Get notified of releases
- 👁️ **Watch releases**: Only major updates
- 📧 **Discussions**: Subscribe to topics you care about

## 🙏 Acknowledgments

Thank you for using DAIOF! Your support helps build the future of AI-human symbiosis.

### Special Thanks

- **Ultimate Creator**: Alpha_Prime_Omega (conceptual source)
- **Human Creator**: Andy (Nguyen Cuong) (implementation)
- **Contributors**: Everyone who helps improve DAIOF
- **Community**: All users, testers, and supporters

---

**Remember**: Just as DAIOF organisms need humans to survive, this project thrives with community support. Together, we build the future of AI safety! 🌟

**Questions not answered here?**  
👉 [Open a Discussion](https://github.com/NguyenCuong1989/DAIOF-Framework/discussions/new)

**Version**: 1.0  
**Last Updated**: October 30, 2025  
**Maintained by**: DAIOF Community
