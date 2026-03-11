---
name: code-generation
description: Generate code in any programming language. Use when user wants to write code, create scripts, build applications, or need technical solutions. Triggers on: "write code", "代码", "program", "build", "create function"
---

# Code Generation Skill

## Description
Professional code generation skill for any programming task.

## When to Use
- Write new code
- Fix bugs
- Refactor code
- Create scripts
- Build applications
- API integration

## Workflow

### Step 1: Understand Requirements
- What to build?
- Language/framework?
- Requirements
- Constraints

### Step 2: Plan
- Architecture
- Components
- Dependencies
- Edge cases

### Step 3: Generate
- Write code
- Add comments
- Include error handling
- Follow best practices

### Step 4: Verify
- Review code
- Check syntax
- Ensure it meets requirements

## Supported Languages
- Python, JavaScript, TypeScript
- Go, Rust, Java
- HTML, CSS, SQL
- Shell, YAML, JSON
- And more...

## Output Format
```python
# Code with comments
def example():
    """Function description"""
    pass
```

## For Agents (API)
```python
# Direct API call
result = await agent.call_skill("code-generation", {
    "language": "python",
    "task": "create API client",
    "requirements": ["auth", "retry", "timeout"]
})

# Or use as tool
tool = agent.get_tool("code-generation")
result = tool.execute(language="python", task="...")
```

## For Humans
Say: "Write a Python script to X" or "Create a React component for Y"
