# 🤖 Agent Corp

> AI Agent知识图谱 + 技能市场 | For Humans & Agents

[🌐 Web Dashboard](https://taurusalex.github.io/agent-corp) | [📦 npm](https://npmjs.com/package/agent-corp) | [💻 GitHub](https://github.com/TaurusAlex/agent-corp)

## 📊 Overview

Agent Corp 是一个面向 **人类** 和 **AI Agents** 的双端产品：

| 用户类型 | 使用方式 |
|----------|----------|
| 👤 人类 | 通过对话描述需求，Agent自动匹配Skills完成任务 |
| 🤖 Agent | 直接调用Skill API，程序化完成任务 |

## 🏗️ 产品架构

```
┌─────────────────────────────────────────────────────┐
│                   Agent Corp                         │
├─────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐ │
│  │   Web UI    │  │   REST API  │  │   CLI Tool  │ │
│  │  (Dashboard)│  │  (Agent用)  │  │  (人类用)   │ │
│  └─────────────┘  └─────────────┘  └─────────────┘ │
├─────────────────────────────────────────────────────┤
│                    Skills Engine                     │
│  ┌──────────────────────────────────────────────┐  │
│  │  Core Skills  │  Industry Skills  │ Utility   │  │
│  │  - research  │  - video-marketing │ - api    │  │
│  │  - copywriting│  - ai-ml        │ - automation│  │
│  │  - code-gen  │  - ecommerce     │ - testing  │  │
│  │  - analytics │  - healthcare    │ - ...      │  │
│  └──────────────────────────────────────────────┘  │
├─────────────────────────────────────────────────────┤
│                  Industry Templates                   │
│            147 Industries × 3 Agents                │
└─────────────────────────────────────────────────────┘
```

## 📦 Skills (双重模式)

### 人类模式 (Natural Language)
```
用户: "帮我写个产品广告"
Agent: 调用 copywriting skill → 生成文案
```

### Agent模式 (API调用)
```python
# 直接调用Skills
result = await agent.call_skill("copywriting", {
    "type": "product_ad",
    "product": "AI Tool",
    "audience": "developers"
})
```

## 🛠️ 核心Skills (Core)

| Skill | 描述 | 人类用法 | Agent用法 |
|-------|------|----------|----------|
| `research` | 调研 | "调研AI趋势" | `call_skill("research", {...})` |
| `copywriting` | 文案 | "写个广告" | `call_skill("copywriting", {...})` |
| `code-generation` | 写代码 | "写个爬虫" | `call_skill("code-generation", {...})` |
| `data-analysis` | 分析 | "分析销售数据" | `call_skill("data-analysis", {...})` |
| `project-management` | 项目管理 | "规划项目" | `call_skill("project-management", {...})` |

## 🏭 行业Skills (Industry)

| 行业 | Agent 1 | Agent 2 | Agent 3 |
|------|---------|---------|---------|
| Video Marketing | 🎬 创意导演 | 🎥 制作 | 📱 分发 |
| AI/ML | 产品策略 | 技术实现 | 社区运营 |
| Ecommerce | 品牌策略 | 视觉创作 | 用户增长 |
| Healthcare | 内容策略 | 教育制作 | 患者获取 |

## 🔌 Agent集成

### Python
```python
from agent_corp import Agent

agent = Agent(api_key="your-key")

# 调用Skill
result = agent.execute(
    skill="research",
    params={"topic": "AI trends"}
)

# 或直接
result = await agent.skills.copywriting.write(
    type="ad",
    product="MyApp"
)
```

### JavaScript
```javascript
const { Agent } = require('agent-corp');

const agent = new Agent({ apiKey: 'your-key' });

// 调用Skill
const result = await agent.execute('research', {
  topic: 'AI trends'
});
```

### CLI (人类使用)
```bash
# 安装
npm install -g agent-corp

# 使用
agent-corp research "AI trends"
agent-corp copywriting --type ad --product "MyApp"
agent-corp code-generation --language python --task "API client"
```

## 🌐 Web Dashboard

访问 [Web Dashboard](https://taurusalex.github.io/agent-corp) 浏览：
- 147个行业模板
- 441个Agents
- 1556+个Skills
- 知识图谱可视化

## 📁 项目结构

```
agent-corp/
├── skills/                    # Skills库
│   ├── core/                # 核心Skills
│   │   ├── research.md
│   │   ├── copywriting.md
│   │   ├── code-generation.md
│   │   ├── data-analysis.md
│   │   └── project-management.md
│   ├── industry/            # 行业Skills
│   └── utility/            # 工具Skills
│       ├── api-integration.md
│       ├── automation.md
│       └── testing.md
│
├── industries/              # 行业模板 (147个)
│   ├── video-marketing/
│   ├── ai-ml/
│   ├── ecommerce/
│   └── ...
│
├── web/                     # 前端Dashboard
│   └── index.html
│
├── sdk/                     # SDK开发中
│   ├── python/
│   └── javascript/
│
└── README.md
```

## 🚀 快速开始

### 人类
```bash
# 安装CLI
npm install -g agent-corp

# 使用
agent-corp --help
agent-corp research "AI in 2026"
```

### Agent
```python
pip install agent-corp

# 使用
from agent_corp import AgentCorp
agent = AgentCorp()
result = agent.execute("research", topic="AI")
```

## 🤝 贡献

欢迎贡献Skills！

1. Fork项目
2. 添加新Skill到 `skills/` 目录
3. 提交PR

## 📄 License

MIT

---

**Built with ❤️ for both Humans and Agents** 🌐
