---
name: testing
description: Write tests and ensure quality. Use when user wants to write tests, debug issues, or ensure code quality. Triggers on: "test", "测试", "debug", "quality", "spec"
---

# Testing Skill

## Description
 tests and ensuring code qualityProfessional skill for writing.

## When to Use
- Write unit tests
- Integration tests
- E2E tests
- Debug issues
- Code review
- Quality assurance

## Workflow

### Step 1: Analyze
- What to test?
- Test strategy
- Coverage goals
- Edge cases

### Step 2: Write Tests
- Unit tests
- Integration tests
- Mock/stub
- Fixtures

### Step 3: Run & Fix
- Run tests
- Fix failures
- Debug issues
- Improve coverage

### Step 4: Report
- Test report
- Coverage report
- Issues found

## Test Types
- Unit Tests
- Integration Tests
- E2E Tests
- Performance Tests
- Security Tests

## Output Format
```python
# Test Example
def test_user_creation():
    # Arrange
    user_data = {"name": "Test", "email": "test@example.com"}
    
    # Act
    user = create_user(user_data)
    
    # Assert
    assert user.id is not None
    assert user.name == "Test"
```

## For Agents (API)
```python
result = await agent.call_skill("testing", {
    "type": "unit",
    "target": "user_service",
    "coverage": 80
})
```
