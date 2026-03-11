# 🤖 Agent Corp

> AI Agent知识图谱 - 147个行业 × 3个Agent × 多个Skills

[🌐 在线预览](https://taurusalex.github.io/agent-corp) | [📖 中文文档](./README-ZH.md)

## 📊 项目概览

| 指标 | 数量 |
|------|------|
| 行业/公司 | 147 |
| Agents | 441 |
| Skills | 1556+ |

## 🎯 快速开始

```bash
# Clone项目
git clone https://github.com/TaurusAlex/agent-corp.git

# 本地预览网页
cd agent-corp/web
python3 -m http.server 8080
# 打开 http://localhost:8080
```

## 🏗️ 项目结构

```
agent-corp/
├── web/                    # 🌐 前端知识图谱网页
│   └── index.html         # 交互式行业/Agent/Skill浏览器
│
├── video-marketing/        # 示例：视频营销公司
│   ├── creative-director/ # 🎬 创意导演
│   │   └── en/
│   │       ├── AGENT.md   # Agent定义
│   │       └── skills/    # 技能包
│   │           ├── script-writing.md
│   │           ├── content-planning.md
│   │           └── market-research.md
│   │
│   ├── video-producer/   # 🎥 视频制作
│   │   └── en/skills/
│   │       ├── video-editing.md
│   │       └── thumbnail-design.md
│   │
│   └── distribution-officer/ # 📱 运营分发
│       └── en/skills/
│           ├── social-publishing.md
│           └── analytics-reporting.md
│
├── ai-ml/                 # AI & Machine Learning
├── saas/                  # Software as a Service
├── ecommerce/             # E-commerce
├── healthcare/            # Healthcare
├── fintech/               # Financial Technology
├── gaming/                # Gaming
└── ...                    # 更多行业 (147个)
```

## 🏢 公司架构

每个行业公司采用最小可行架构：

```
┌─────────────────────────────────────────────────┐
│              Company (公司)                      │
├─────────────────────────────────────────────────┤
│  🎬 Creative Director   │ 策略、内容、定位        │
│  🎥 Video Producer     │ 制作、视觉、内容        │
│  📱 Distribution       │ 分发、增长、分析         │
└─────────────────────────────────────────────────┘
         ↓           ↓           ↓
      Skills      Skills      Skills
    (2-6个)     (2-6个)     (2-6个)
```

## 📦 Agent结构

### Creative Director (创意导演)
负责策略和内容规划

**核心技能:**
- Market Research (市场调研)
- Copywriting (文案撰写)
- Brand Strategy (品牌策略)
- Product Marketing (产品营销)
- Content Planning (内容策划)

### Producer (制作)
负责内容创作和制作

**核心技能:**
- Video Editing (视频剪辑)
- Thumbnail Design (封面设计)
- Motion Graphics (动效制作)
- Audio Editing (音频编辑)
- Color Grading (调色)

### Distribution Officer (分发运营)
负责分发和增长

**核心技能:**
- Social Publishing (社媒发布)
- Analytics (数据分析)
- Community Management (社群管理)
- Hashtag Strategy (标签策略)
- Influencer Outreach (红人合作)

## 🔍 浏览方式

### 方式1: 网页预览 (推荐)
```bash
cd web
python3 -m http.server 8080
# 访问 http://localhost:8080
```

### 方式2: 命令行浏览
```bash
# 列出所有行业
ls -d */

# 查看特定行业
ls video-marketing/*/en/

# 查看Skills
ls video-marketing/creative-director/en/skills/
```

## 🌐 支持的语言

- English (英文)
- 中文 (后续添加)

## 🤝 如何贡献

1. Fork本项目
2. 创建新行业分支: `git checkout -b add-new-industry`
3. 添加你的行业模板
4. 提交PR

## 📄 License

MIT License

## 👤 作者

- GitHub: [@TaurusAlex](https://github.com/TaurusAlex)

---

**用AI构建AI，用自动化服务自动化** 🚀
