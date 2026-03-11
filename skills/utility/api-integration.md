---
name: api-integration
description: Integrate with external APIs and services. Use when need to connect to external services, build webhooks, or create integrations. Triggers on: "integrate", "API", "webhook", "连接", "对接"
---

# API Integration Skill

## Description
Professional skill for integrating with external APIs and services.

## When to Use
- Connect to APIs
- Build webhooks
- Create integrations
- Authenticate
- Handle errors
- Rate limiting

## Workflow

### Step 1: Understand API
- API documentation
- Authentication
- Endpoints
- Rate limits
- Error codes

### Step 2: Design Integration
- Architecture
- Data flow
- Security
- Error handling

### Step 3: Implement
- Write client code
- Add authentication
- Handle errors
- Add retries
- Logging

### Step 4: Test & Deploy
- Unit tests
- Integration tests
- Deploy
- Monitor

## Supported Integrations
- REST APIs
- GraphQL
- Webhooks
- OAuth
- SDKs

## Output Format
```javascript
// API Client Example
class APIClient {
  constructor(apiKey) {
    this.baseURL = 'https://api.example.com';
    this.client = axios.create({...});
  }
  
  async get(endpoint) {
    return this.client.get(`${this.baseURL}/${endpoint}`);
  }
}
```

## For Agents (API)
```python
# Direct tool call
result = await agent.call_skill("api-integration", {
    "api": "stripe",
    "action": "create_payment",
    "params": {"amount": 1000}
})
```
