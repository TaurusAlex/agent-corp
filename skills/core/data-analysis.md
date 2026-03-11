---
name: data-analysis
description: Analyze data and generate insights. Use when user wants to analyze data, create reports, build dashboards, or get insights from data. Triggers on: "analyze", "分析数据", "analytics", "insights", "dashboard"
---

# Data Analysis Skill

## Description
Professional data analysis skill for extracting insights from data.

## When to Use
- Analyze datasets
- Generate reports
- Create visualizations
- Build dashboards
- Find patterns
- Make predictions

## Workflow

### Step 1: Define Goal
- What question to answer?
- Data sources?
- Metrics needed?

### Step 2: Collect & Clean
- Import data
- Handle missing values
- Transform data
- Validate quality

### Step 3: Analyze
- Descriptive statistics
- Trend analysis
- Correlation analysis
- Segmentation

### Step 4: Visualize & Report
- Create charts
- Build dashboard
- Write insights
- Recommend actions

## Output Format
```
# Analysis: [Topic]

## Key Metrics
- Metric 1: X
- Metric 2: Y

## Insights
1. [Insight 1]
2. [Insight 2]

## Recommendations
- [Action 1]
- [Action 2]
```

## For Agents (API)
```python
result = await agent.call_skill("data-analysis", {
    "data": dataset,
    "goal": "customer segmentation",
    "output": "report"
})
```

## For Humans
Say: "Analyze this data" or "Create a sales report"
