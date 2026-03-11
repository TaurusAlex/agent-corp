---
name: technical-writing
description: Technical Writing for AI/ML products. Use this skill whenever the user needs to write technical documentation, API docs, README files, technical blog posts, or any content that explains technical concepts. This skill is essential for AI companies that need to make complex technology accessible. Triggers on: "write documentation", "API docs", "技术文档", "README", "technical blog".
---

# Technical Writing

## When to Use
- Writing API documentation
- Creating README files
- Drafting technical blog posts
- Writing white papers
- Creating user guides

## Workflow

### Step 1: Understand the Technology
- What does the product do?
- Who is the audience?
- What's the key value proposition?
- What are the technical details needed?

### Step 2: Structure the Content
- Start with high-level overview
- Break into logical sections
- Progress from simple to complex
- Include code examples where relevant

### Step 3: Write the Draft
- Use clear, simple language
- Define technical terms
- Use consistent formatting
- Include examples

### Step 4: Review & Refine
- Check for clarity
- Verify technical accuracy
- Ensure completeness
- Format for readability

## Writing Principles

### Clarity
- Short sentences
- Active voice
- Define acronyms
- Avoid jargon (or explain)

### Structure
- Headings and subheadings
- Bullet points for lists
- Code blocks for examples
- Tables for comparisons

### Examples
Always include working examples:
```python
# Example: How to use the API
from ailib import Client

client = Client(api_key="your-key")
result = client.predict("Hello world")
print(result)
```

## Documentation Types

### README
```
# Product Name

One-sentence description.

## Quick Start
[3-step setup]

## Features
[Bullet points]

## API Reference
[Key methods]

## Examples
[Working code]
```

### API Docs
```
## Method: predict

### Description
[What it does]

### Parameters
| Name | Type | Description |
|------|------|-------------|
| input | string | Input text |

### Returns
[What comes back]

### Example
[Code example]
```

## Tips
- Write for your audience (developers, users, etc.)
- Show, don't just tell
- Keep it current
- Include troubleshooting
