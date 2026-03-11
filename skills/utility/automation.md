---
name: automation
description: Automate repetitive tasks and workflows. Use when user wants to automate tasks, create workflows, or build bots. Triggers on: "automate", "automation", "自动化", "workflow", "bot"
---

# Automation Skill

## Description
Professional skill for automating tasks and creating workflows.

## When to Use
- Automate repetitive tasks
- Create workflows
- Build bots
- Schedule jobs
- Trigger events

## Workflow

### Step 1: Identify
- What to automate?
- Frequency?
- Triggers?
- Inputs/outputs?

### Step 2: Design
- Flow diagram
- Components
- Error handling
- Monitoring

### Step 3: Implement
- Write automation code
- Add scheduling
- Set up triggers
- Logging

### Step 4: Deploy & Monitor
- Deploy
- Monitor
- Handle failures
- Optimize

## Automation Types

### Scheduled Jobs
- Cron jobs
- Time-based triggers

### Event-Driven
- Webhooks
- Message queues
- File changes

### Bot Automation
- Discord/Telegram bots
- Email automation
- Social media bots

## Output Format
```python
# Automation Example
def automation_flow():
    trigger = schedule(cron="0 9 * * *")
    
    @trigger
    def run_task():
        data = fetch_data()
        result = process(data)
        send_notification(result)
    
    return run_task
```

## For Agents (API)
```python
result = await agent.call_skill("automation", {
    "type": "scheduled",
    "task": "daily_report",
    "schedule": "0 9 * * *"
})
```
