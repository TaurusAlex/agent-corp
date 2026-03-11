---
name: project-management
description: Manage projects and tasks. Use when user wants to plan projects, track tasks, manage sprints, or organize work. Triggers on: "project", "manage", "任务管理", "sprint", "plan"
---

# Project Management Skill

## Description
Professional project management skill for planning and tracking work.

## When to Use
- Plan projects
- Track tasks
- Manage sprints
- Set milestones
- Allocate resources
- Risk management

## Workflow

### Step 1: Define Project
- Goal/objective
- Scope
- Timeline
- Resources
- Stakeholders

### Step 2: Plan
- Break into tasks
- Estimate effort
- Set dependencies
- Create schedule
- Assign owners

### Step 3: Execute
- Track progress
- Update status
- Manage blockers
- Communicate updates

### Step 4: Review
- Retrospective
- Lessons learned
- Metrics review
- Next planning

## Output Formats

### Project Plan
```
# Project: [Name]

## Goal
[Description]

## Timeline
- Start: [Date]
- End: [Date]

## Milestones
1. [Milestone 1] - [Date]
2. [Milestone 2] - [Date]

## Tasks
| Task | Owner | Due | Status |
|------|-------|-----|--------|
```

### Sprint Board
```
# Sprint [N]

## To Do
- [ ] Task 1
- [ ] Task 2

## In Progress
- [ ] Task 3

## Done
- [x] Task 4
```

## For Agents (API)
```python
result = await agent.call_skill("project-management", {
    "action": "create_sprint",
    "project": "AI Agent",
    "tasks": ["task1", "task2"]
})
```
