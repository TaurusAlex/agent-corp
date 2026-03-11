---
name: research
description: Research any topic comprehensively. Use when user wants to research a topic, gather information, or learn about something new. Triggers on: "research", "调研", "了解", "learn about", "调查"
---

# Research Skill

## Description
Comprehensive research skill for gathering and analyzing information.

## When to Use
- Research any topic
- Competitive analysis
- Market research
- Technology exploration
- Trend analysis

## Workflow

### Step 1: Define Scope
- What to research?
- Depth level (quick/deep)
- Output format?

### Step 2: Gather Information
- Search web sources
- Read documentation
- Collect data
- Find examples

### Step 3: Analyze
- Synthesize findings
- Identify patterns
- Draw conclusions

### Step 4: Report
- Structured output
- Key insights
- Sources cited
- Next steps

## Output Format
```
# Research: [Topic]

## Summary
[Brief overview]

## Key Findings
1. [Finding 1]
2. [Finding 2]
...

## Sources
- [Source 1]
- [Source 2]

## Recommendations
- [Recommendation 1]
```

## For Agents
This skill can be called programmatically:
```python
result = await agent.call_skill("research", {
    "topic": "AI trends 2026",
    "depth": "deep",
    "output": "report"
})
```

## For Humans
Simply ask: "Research X" or "Tell me about X"
