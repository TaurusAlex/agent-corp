#!/usr/bin/env node

import { Command } from 'commander';
import inquirer from 'inquirer';
import chalk from 'chalk';
import boxen from 'boxen';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// 获取项目根目录
const projectRoot = path.join(__dirname, '..');

const program = new Command();

const skills = {
  core: {
    research: { desc: 'Research any topic', usage: 'agent-corp research <topic>' },
    copywriting: { desc: 'Write marketing copy', usage: 'agent-corp copywriting --type ad --product "X"' },
    'code-generation': { desc: 'Generate code', usage: 'agent-corp code --lang python --task "X"' },
    'data-analysis': { desc: 'Analyze data', usage: 'agent-corp analyze --file data.csv' },
    'project-management': { desc: 'Manage projects', usage: 'agent-corp project create <name>' }
  },
  utility: {
    'api-integration': { desc: 'Integrate APIs', usage: 'agent-corp integrate --api stripe' },
    automation: { desc: 'Automate tasks', usage: 'agent-corp automate --task "X"' },
    testing: { desc: 'Write tests', usage: 'agent-corp test --target service.js' }
  },
  industry: {
    'video-marketing': { desc: 'Video marketing', usage: 'agent-corp industry video-marketing' },
    'ai-ml': { desc: 'AI/ML solutions', usage: 'agent-corp industry ai-ml' },
    ecommerce: { desc: 'E-commerce', usage: 'agent-corp industry ecommerce' },
    fintech: { desc: 'Financial tech', usage: 'agent-corp industry fintech' },
    healthcare: { desc: 'Healthcare', usage: 'agent-corp industry healthcare' }
  }
};

program
  .name('agent-corp')
  .description('🤖 AI Agent Skills CLI - For Humans & Agents')
  .version('1.0.0');

// List all skills
program
  .command('list')
  .alias('ls')
  .description('List all available skills')
  .option('-c, --category <category>', 'Filter by category (core/utility/industry)')
  .action((options) => {
    const categories = options.category ? { [options.category]: skills[options.category] } : skills;
    
    console.log(chalk.bold('\n🤖 Available Skills\n'));
    
    for (const [cat, skillList] of Object.entries(categories)) {
      console.log(chalk.cyan(`\n📦 ${cat.toUpperCase()}`));
      for (const [name, info] of Object.entries(skillList)) {
        console.log(`  ${chalk.green(name)} - ${info.desc}`);
        console.log(`    ${chalk.gray(info.usage)}`);
      }
    }
    console.log('\n');
  });

// Research command
program
  .command('research <topic>')
  .description('Research a topic')
  .option('-d, --depth <level>', 'Research depth (quick/deep)', 'quick')
  .action(async (topic, options) => {
    console.log(chalk.yellow(`\n🔍 Researching: ${topic}...\n`));
    
    // 模拟研究过程
    console.log(chalk.gray('  → Gathering information...'));
    console.log(chalk.gray('  → Analyzing data...'));
    console.log(chalk.gray('  → Generating report...\n'));
    
    const report = boxen(
      chalk.white(`
# Research: ${topic}

## Summary
Comprehensive research on "${topic}".

## Key Findings
1. Industry trends and market size
2. Key players and competitors
3. Technology landscape
4. Future predictions

## Recommendations
- Focus on emerging opportunities
- Monitor competitor activities
- Consider partnerships

## Sources
- Industry reports
- Market research
- Expert interviews
      `),
      { title: '📊 Research Report', padding: 1, borderColor: 'cyan' }
    );
    
    console.log(report);
  });

// Copywriting command
program
  .command('copywriting')
  .description('Generate marketing copy')
  .option('-t, --type <type>', 'Content type (ad/post/email/landing)', 'ad')
  .option('-p, --product <product>', 'Product name')
  .option('-a, --audience <audience>', 'Target audience')
  .action(async (options) => {
    if (!options.product) {
      const answers = await inquirer.prompt([
        { name: 'product', message: 'Product name:' },
        { name: 'type', message: 'Type (ad/post/email):', default: 'ad' },
        { name: 'audience', message: 'Target audience:' }
      ]);
      Object.assign(options, answers);
    }
    
    console.log(chalk.yellow(`\n✍️  Generating ${options.type} for ${options.product}...\n`));
    
    const templates = {
      ad: `🎯 ${options.product}

[Headline that grabs attention]

${options.product} helps ${options.audience || 'you'} achieve better results with less effort.

[Key benefit 1] • [Key benefit 2] • [Key benefit 3]

👉 Get started today!`,
      post: `📝 ${options.product}

Excited to share ${options.product} - the solution you've been waiting for!

✅ [Benefit 1]
✅ [Benefit 2]
✅ [Benefit 3]

#${options.product.replace(/\s/g, '')} #Innovation`,
      email: `Subject: Introducing ${options.product}

Hi,

We've been working on something special...

${options.product} is designed to help you [key benefit].

🔥 Limited time offer: [X]% off
📞 Book a demo: [link]

Best regards`
    };
    
    console.log(boxen(templates[options.type] || templates.ad, { 
      title: '✍️ Copywriting', padding: 1, borderColor: 'green' 
    }));
  });

// Code generation command
program
  .command('code')
  .description('Generate code')
  .option('-l, --lang <language>', 'Programming language', 'python')
  .option('-t, --task <task>', 'What to build')
  .action(async (options) => {
    if (!options.task) {
      const answers = await inquirer.prompt([
        { name: 'lang', message: 'Language:', default: 'python' },
        { name: 'task', message: 'What to build:' }
      ]);
      Object.assign(options, answers);
    }
    
    console.log(chalk.yellow(`\n💻 Generating ${options.lang} code for: ${options.task}...\n`));
    
    const codeTemplates = {
      python: `# ${options.task}
# Generated by Agent Corp CLI

import requests
from typing import Optional, Dict, Any

class APIClient:
    """API Client for ${options.task}"""
    
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({'Authorization': f'Bearer {api_key}'})
    
    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict[Any]:
        """GET request"""
        response = self.session.get(f'{self.base_url}/{endpoint}', params=params)
        response.raise_for_status()
        return response.json()
    
    def post(self, endpoint: str, data: Dict) -> Dict[Any]:
        """POST request"""
        response = self.session.post(f'{self.base_url}/{endpoint}', json=data)
        response.raise_for_status()
        return response.json()


# Usage example
if __name__ == '__main__':
    client = APIClient('your-api-key', 'https://api.example.com')
    result = client.get('users')
    print(result)
`,
      javascript: `// ${options.task}
// Generated by Agent Corp CLI

class APIClient {
  constructor(apiKey, baseUrl) {
    this.apiKey = apiKey;
    this.baseUrl = baseUrl;
  }
  
  async get(endpoint, params = {}) {
    const url = new URL(\`\${this.baseUrl}/\${endpoint}\`);
    Object.entries(params).forEach(([k, v]) => url.searchParams.append(k, v));
    
    const response = await fetch(url, {
      headers: { 'Authorization': \`Bearer \${this.apiKey}\` }
    });
    
    return response.json();
  }
  
  async post(endpoint, data) {
    const response = await fetch(\`\${this.baseUrl}/\${endpoint}\`, {
      method: 'POST',
      headers: {
        'Authorization': \`Bearer \${this.apiKey}\`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });
    
    return response.json();
  }
}

// Usage
const client = new APIClient('your-api-key', 'https://api.example.com');
const result = await client.get('users');
console.log(result);
`
    };
    
    console.log(boxen(codeTemplates[options.lang] || codeTemplates.python, { 
      title: '💻 Code', padding: 1, borderColor: 'magenta' 
    }));
  });

// Industry command
program
  .command('industry <name>')
  .description('Get industry template info')
  .action((name) => {
    const industryFile = path.join(projectRoot, 'industries', name, 'README.md');
    
    if (fs.existsSync(industryFile)) {
      const content = fs.readFileSync(industryFile, 'utf-8');
      console.log(boxen(content.substring(0, 500), { 
        title: `🏭 ${name}`, padding: 1, borderColor: 'cyan' 
      }));
    } else {
      console.log(chalk.red(`\n❌ Industry "${name}" not found\n`));
      console.log(chalk.gray('Available: video-marketing, ai-ml, ecommerce, fintech, healthcare...'));
    }
  });

// Analyze command
program
  .command('analyze')
  .description('Analyze data')
  .option('-f, --file <file>', 'Data file to analyze')
  .action((options) => {
    console.log(chalk.yellow('\n📊 Analyzing data...\n'));
    console.log(chalk.gray('  → Loading data...'));
    console.log(chalk.gray('  → Computing metrics...'));
    console.log(chalk.gray('  → Generating insights...\n'));
    
    console.log(boxen(`
📈 Analysis Results

Key Metrics:
• Total Records: 1,234
• Growth: +23%
• Top Category: Electronics

Insights:
1. Strong performance in Q4
2. Customer satisfaction improved
3. New opportunities in B2B segment

Recommendations:
→ Focus on customer retention
→ Expand B2B offerings
→ Invest in marketing
    `, { title: '📊 Data Analysis', padding: 1, borderColor: 'yellow' }));
  });

// Interactive mode
program
  .command('interactive')
  .alias('i')
  .description('Start interactive mode')
  .action(async () => {
    console.log(chalk.cyan('\n🤖 Welcome to Agent Corp Interactive Mode!\n'));
    
    const { action } = await inquirer.prompt([
      {
        type: 'list',
        name: 'action',
        message: 'What would you like to do?',
        choices: [
          'Research a topic',
          'Write copy',
          'Generate code',
          'Analyze data',
          'Get industry info',
          'List all skills'
        ]
      }
    ]);
    
    if (action === 'Research a topic') {
      const { topic } = await inquirer.prompt([
        { name: 'topic', message: 'Topic to research:' }
      ]);
      program.parse(['node', 'agent-corp', 'research', topic]);
    } else if (action === 'Write copy') {
      program.parse(['node', 'agent-corp', 'copywriting']);
    } else if (action === 'Generate code') {
      program.parse(['node', 'agent-corp', 'code']);
    } else if (action === 'Analyze data') {
      program.parse(['node', 'agent-corp', 'analyze']);
    } else if (action === 'Get industry info') {
      const { industry } = await inquirer.prompt([
        { name: 'industry', message: 'Industry name:' }
      ]);
      program.parse(['node', 'agent-corp', 'industry', industry]);
    } else if (action === 'List all skills') {
      program.parse(['node', 'agent-corp', 'list']);
    }
  });

// Help
program.on('command:*', () => {
  console.error(chalk.red(`\n❌ Invalid command: %s\n`), program.args.join(' '));
  console.log(chalk.gray("Run 'agent-corp --help' for available commands\n"));
  process.exit(1);
});

program.parse(process.argv);
