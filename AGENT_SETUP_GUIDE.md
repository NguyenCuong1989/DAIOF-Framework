# 🤖 Hướng dẫn Cài đặt và Sử dụng 4 Agents

## 📋 Tổng quan

DAIOF Framework hiện hỗ trợ 4 AI agents mạnh mẽ để phát triển và duy trì code tự động:

| Agent | Model | Trạng thái | Chức năng chính |
|-------|-------|-----------|----------------|
| **Claude** | claude-sonnet-4.5 | ✅ Sẵn sàng | Code analysis, Documentation |
| **Blackbox** | blackbox-pro | ⚠️ Cần fix | Code generation, Bug fixing |
| **Codex** | gpt-5-codex | ✅ Sẵn sàng | Multi-language, Algorithms |
| **Gemini** | gemini-2.0-flash-exp | ❌ Chưa config | Multimodal, Creative tasks |

---

## 🔧 Cài đặt chi tiết

### 1. **Kiểm tra cài đặt hiện tại**

```bash
# Kiểm tra Blackbox CLI
export PATH="$HOME/.local/bin:$PATH"
blackbox --version

# Kiểm tra config
cat ~/.blackboxcli/settings.json
```

### 2. **Sửa lỗi 422 cho Blackbox Agent**

Lỗi `Status code 422` thường do API configuration. Thử các bước sau:

```bash
# Bước 1: Xác minh API key
echo $BLACKBOX_API_KEY

# Bước 2: Reconfigure Blackbox CLI
blackbox configure

# Bước 3: Test connection
blackbox --help
```

**Nếu vẫn lỗi, cập nhật settings.json:**

```json
{
  "model": "blackboxai/blackbox-pro",
  "selectedAuthType": "blackbox-api",
  "contentGenerator": {
    "timeout": 900000,
    "maxRetries": 3
  },
  "security": {
    "auth": {
      "blackbox": {
        "apiKey": "YOUR_VALID_API_KEY_HERE",
        "baseUrl": "https://api.blackbox.ai/v1",
        "model": "blackboxai/blackbox-pro"
      },
      "selectedType": "blackbox-api",
      "selectedProvider": "blackbox"
    }
  }
}
```

### 3. **Kích hoạt Gemini Agent**

```bash
# Thêm Gemini API key vào environment
export GEMINI_API_KEY="your-gemini-api-key"

# Hoặc thêm vào .env file
echo "GEMINI_API_KEY=your-gemini-api-key" >> .env
```

---

## 🚀 Sử dụng Agents

### **Chạy Single Agent**

```bash
# Sử dụng Claude agent
blackbox --agent claude "Analyze the DAIOF architecture"

# Sử dụng Codex agent
blackbox --agent codex "Implement binary search algorithm"
```

### **Chạy Multi-Agent (Parallel)**

```bash
# Chạy tất cả agents cùng lúc
blackbox --multi-agent "Optimize the digital_ai_organism_framework.py"

# Chạy specific agents
blackbox --agents claude,codex "Review and improve code quality"
```

### **Agent Collaboration Workflow**

```python
# Example: 4-agent collaboration
from agent_orchestrator import AgentOrchestrator

orchestrator = AgentOrchestrator()

# Task 1: Claude analyzes architecture
analysis = orchestrator.run_agent('claude', 'Analyze DAIOF architecture')

# Task 2: Codex implements improvements
code = orchestrator.run_agent('codex', f'Implement: {analysis.suggestions}')

# Task 3: Blackbox writes tests
tests = orchestrator.run_agent('blackbox', f'Write tests for: {code}')

# Task 4: Gemini creates documentation
docs = orchestrator.run_agent('gemini', f'Document: {code} with visuals')

# Merge results
orchestrator.merge_results([analysis, code, tests, docs])
```

---

## 🎯 Use Cases cho từng Agent

### **Claude Agent** - Best for:
- 📖 **Documentation generation**
  ```bash
  blackbox --agent claude "Generate API documentation for Symphony Control Center"
  ```
- 🔍 **Code review**
  ```bash
  blackbox --agent claude "Review digital_genome.py for best practices"
  ```
- 🏗️ **Architecture design**
  ```bash
  blackbox --agent claude "Design microservices architecture for DAIOF"
  ```

### **Blackbox Agent** - Best for:
- ⚡ **Quick code generation**
  ```bash
  blackbox --agent blackbox "Create REST API endpoint for organism creation"
  ```
- 🐛 **Bug fixing**
  ```bash
  blackbox --agent blackbox "Fix the metabolism resource leak in line 234"
  ```
- 🧪 **Test writing**
  ```bash
  blackbox --agent blackbox "Write pytest tests for DigitalNervousSystem"
  ```

### **Codex Agent** - Best for:
- 🔢 **Algorithm implementation**
  ```bash
  blackbox --agent codex "Implement genetic algorithm for organism evolution"
  ```
- 🗄️ **Database optimization**
  ```bash
  blackbox --agent codex "Optimize MongoDB queries for ecosystem data"
  ```
- 🔧 **DevOps automation**
  ```bash
  blackbox --agent codex "Create GitHub Actions workflow for CI/CD"
  ```

### **Gemini Agent** - Best for:
- 🎨 **Visual content**
  ```bash
  blackbox --agent gemini "Generate architecture diagrams for DAIOF"
  ```
- 📊 **Data analysis**
  ```bash
  blackbox --agent gemini "Analyze organism health metrics and create visualizations"
  ```
- 🎭 **Creative tasks**
  ```bash
  blackbox --agent gemini "Create marketing content for DAIOF launch"
  ```

---

## 🔄 Agent Orchestration Patterns

### **Pattern 1: Sequential Pipeline**
```
Claude (Analyze) → Codex (Implement) → Blackbox (Test) → Gemini (Document)
```

### **Pattern 2: Parallel Processing**
```
        ┌─ Claude (Architecture)
Task ──┼─ Codex (Backend)
        ├─ Blackbox (Frontend)
        └─ Gemini (Design)
```

### **Pattern 3: Iterative Refinement**
```
1. Claude: Initial design
2. Codex: Implement v1
3. Blackbox: Test & find issues
4. Claude: Refine design
5. Codex: Implement v2
6. Repeat until quality threshold met
```

---

## 📊 Monitoring Agent Performance

### **Check Agent Status**

```bash
# View agent health
blackbox --status

# View agent metrics
blackbox --metrics

# View agent logs
tail -f ~/.blackboxcli/logs/agent.log
```

### **Performance Metrics**

```python
from agent_monitor import AgentMonitor

monitor = AgentMonitor()

# Get agent statistics
stats = monitor.get_stats()
print(f"Claude success rate: {stats['claude']['success_rate']}")
print(f"Average response time: {stats['claude']['avg_response_time']}")
print(f"Total tasks completed: {stats['claude']['total_tasks']}")
```

---

## 🛠️ Troubleshooting

### **Common Issues**

#### **Issue 1: Agent not responding**
```bash
# Check agent process
ps aux | grep blackbox

# Restart agent service
blackbox restart

# Clear cache
rm -rf ~/.blackboxcli/cache/*
```

#### **Issue 2: API rate limits**
```bash
# Check rate limit status
blackbox --rate-limit-status

# Use rate limit backoff
blackbox --with-backoff "your task"
```

#### **Issue 3: Authentication errors**
```bash
# Verify all API keys
blackbox --verify-auth

# Reconfigure authentication
blackbox configure --reset
```

---

## 🎓 Best Practices

### **1. Task Assignment**
- ✅ Assign tasks based on agent strengths
- ✅ Use Claude for complex reasoning
- ✅ Use Codex for implementation
- ✅ Use Blackbox for quick iterations
- ✅ Use Gemini for creative/visual tasks

### **2. Resource Management**
- ✅ Monitor API usage and costs
- ✅ Use caching for repeated tasks
- ✅ Implement rate limiting
- ✅ Set timeout thresholds

### **3. Quality Control**
- ✅ Always review agent output
- ✅ Use multiple agents for critical tasks
- ✅ Implement validation checks
- ✅ Maintain human oversight

---

## 📚 Additional Resources

- [Blackbox CLI Documentation](https://docs.blackbox.ai)
- [Claude API Reference](https://docs.anthropic.com)
- [OpenAI Codex Guide](https://platform.openai.com/docs)
- [Gemini API Docs](https://ai.google.dev/docs)

---

## 🤝 Support

Nếu gặp vấn đề với agents:

1. **Check logs**: `~/.blackboxcli/logs/`
2. **GitHub Issues**: [Report here](https://github.com/NguyenCuong1989/DAIOF-Framework/issues)
3. **Email**: symphony.hyperai@vietnamese.consciousness

---

**Created by:** Alpha_Prime_Omega  
**Date:** November 19, 2025  
**Status:** 🚀 Production Ready
