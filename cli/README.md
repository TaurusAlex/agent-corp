# 🤖 Agent Corp CLI

> AI Agent Skills Command Line Interface

## 安装

```bash
# 克隆项目
git clone https://github.com/TaurusAlex/agent-corp.git
cd agent-corp/cli

# 安装依赖
npm install

# 链接到全局
npm link
```

## 使用

```bash
# 交互模式 (推荐)
agent-corp interactive
agent-corp i

# 列出所有Skills
agent-corp list
agent-corp ls

# 调研
agent-corp research "AI trends"
agent-corp research "machine learning" --depth deep

# 文案
agent-corp copywriting --product "MyApp" --audience "developers"
agent-corp copywriting

# 代码生成
agent-corp code --lang python --task "API client"
agent-corp code

# 数据分析
agent-corp analyze --file data.csv

# 行业信息
agent-corp industry video-marketing
agent-corp industry ai-ml

# 帮助
agent-corp --help
```

## 命令

| 命令 | 描述 |
|------|------|
| `agent-corp list` | 列出所有Skills |
| `agent-corp research <topic>` | 调研主题 |
| `agent-corp copywriting` | 生成营销文案 |
| `agent-corp code` | 生成代码 |
| `agent-corp analyze` | 分析数据 |
| `agent-corp industry <name>` | 获取行业信息 |
| `agent-corp interactive` | 交互模式 |

## 示例

```bash
# 调研
$ agent-corp research "AI in 2026"
🔍 Researching: AI in 2026...
[生成研究报告]

# 文案
$ agent-corp copywriting --product "AI Writer"
✍️ Generating ad for AI Writer...
[生成广告文案]

# 代码
$ agent-corp code --lang javascript --task "REST API client"
💻 Generating JavaScript code...
[生成API客户端代码]
```

## 作为库使用

```javascript
import { research, copywriting, codeGeneration } from 'agent-corp';

const result = await research({ topic: 'AI trends', depth: 'deep' });
const copy = await copywriting({ type: 'ad', product: 'MyApp' });
const code = await codeGeneration({ language: 'python', task: 'API client' });
```

## License

MIT
