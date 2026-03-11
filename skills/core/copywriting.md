---
name: copywriting
description: Write persuasive copy for any purpose. Use when user wants to write marketing copy, ads, product descriptions, social posts, or any promotional content. Triggers on: "write copy", "文案", "写广告", "copywriting", "推广文案"
---

# Copywriting Skill

## Description
Professional copywriting skill for creating persuasive marketing content.

## When to Use
- Marketing campaigns
- Product descriptions
- Ad copy
- Social media posts
- Email newsletters
- Landing pages

## Workflow

### Step 1: Understand
- Product/service
- Target audience
- Key message
- Call to action
- Tone/style

### Step 2: Structure
- Headline
- Body copy
- CTA
- Supporting points

### Step 3: Write
- Draft copy
- Apply copywriting frameworks:
  - AIDA (Attention, Interest, Desire, Action)
  - PAS (Problem, Agitation, Solution)
  - FAB (Features, Advantages, Benefits)

### Step 4: Optimize
- Test variations
- Refine for platform
- Ensure clarity

## Output Formats

### Short (Social)
```
Headline: [Catchy headline]
Body: [2-3 sentences]
CTA: [Action]
```

### Long (Landing Page)
```
Headline: [Value proposition]
Subhead: [Supporting message]
Body: [Benefits + proof]
CTA: [Clear action]
```

## For Agents
```python
result = await agent.call_skill("copywriting", {
    "type": "ad",
    "product": "AI writing tool",
    "audience": "marketers",
    "tone": "professional"
})
```

## For Humans
Say: "Write ad copy for X" or "Help me write a product description"
