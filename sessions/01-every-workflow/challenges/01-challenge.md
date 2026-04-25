# Challenge 01 - Feature and Test Expansion

**Duration:** 20-25 minutes | **Level:** Beginner to Intermediate

## Challenge Overview

In this hands-on challenge, you'll experience GitHub Copilot's value across a realistic software delivery workflow. You'll implement a feature, generate tests, fix bugs, write documentation, and conduct code review—all with Copilot's assistance.

**Core Objectives:**
1. ✅ Implement a feature from a user story using Copilot Chat
2. ✅ Generate focused unit tests with comprehensive coverage
3. ✅ Debug and fix introduced issues
4. ✅ Generate pull request descriptions
5. ✅ Update documentation and release notes
6. ✅ Conduct a code review pass

---

## Task 1: Feature Implementation

**User Story:** "As a task manager, I want to filter tasks by due date and priority so I can focus on urgent items."

**Steps:**

1. **Open Copilot Chat** in VS Code
2. **Paste this prompt** into the chat:
   ```
   Implement a feature for filtering tasks by due date and priority in this project. 
   Add these capabilities:
   - Due date query parameter (optional, format: YYYY-MM-DD)
   - Priority filter (optional, values: high, medium, low)
   - Both filters should be combinable
   - Update the Task model if needed
   ```

3. **Review the proposed changes** Copilot suggests
4. **Accept and apply** the changes to `app/main.py`
5. **Verify** the /tasks endpoint now accepts these query parameters

**Success Criteria:**
- [ ] /tasks endpoint accepts `due_date` query parameter
- [ ] /tasks endpoint accepts `priority` query parameter
- [ ] Filters work independently and together
- [ ] Code follows the existing project style

---

## Task 2: Test Generation & Edge Cases

**Steps:**

1. **Open Copilot Chat** again
2. **Paste this prompt:**
   ```
   Generate comprehensive unit tests for the new due_date and priority filters.
   Include:
   - Tests for matching tasks (nominal case)
   - Tests for non-matching tasks
   - Tests for null/missing parameters
   - Edge cases (empty task list, single task, boundary dates)
   - Error handling for invalid date formats
   ```

3. **Review** the pytest test cases Copilot generates
4. **Add them** to `tests/test_tasks.py`
5. **Run tests locally** to verify they pass:
   ```bash
   cd sessions/01-every-workflow/starter
   pytest -v
   ```

**Success Criteria:**
- [ ] All new tests pass locally
- [ ] Coverage includes at least 5 edge cases
- [ ] Tests use descriptive names
- [ ] Error paths are tested

---

## Task 3: Bug Identification & Fix

**Steps:**

1. **In your code**, intentionally introduce a bug (e.g., change a filter condition or validation logic)
2. **Open Copilot Chat** and share the buggy function:
   ```
   Explain the bug in this function and suggest a safe refactor:
   [Paste the buggy code here]
   ```

3. **Review** Copilot's diagnosis
4. **Accept the fix** and update your code
5. **Re-run tests** to confirm the fix:
   ```bash
   pytest -v
   ```

**Success Criteria:**
- [ ] Bug is correctly identified
- [ ] Fix is minimal and safe
- [ ] All tests pass after fix
- [ ] No regression in other functionality

---

## Task 4: Pull Request Summary & Documentation

**Steps:**

1. **Gather your changes:** Note the commit diff (new endpoints, tests, etc.)
2. **Open Copilot Chat** and use this prompt:
   ```
   Draft a professional pull request summary with these sections:
   - What: Brief description of changes
   - Why: Business context and rationale
   - How: Technical approach (e.g., added query params, test coverage)
   - Tests: Summary of test coverage added
   - Rollout: Any deployment or rollout notes
   
   Context: Added due_date and priority filtering to the /tasks endpoint.
   ```

3. **Copy the PR summary** and store it (you can use this in a real PR later)
4. **Now update the README** with usage examples. Use this prompt:
   ```
   Update the README section about API endpoints with usage examples for 
   the new due_date and priority filters:
   - Show how to filter by due date
   - Show how to filter by priority
   - Show how to combine both filters
   - Include example curl requests or Python requests code
   ```

5. **Accept the changes** and update `starter/README.md` (if it exists, or create examples)

**Success Criteria:**
- [ ] PR summary includes all 5 sections
- [ ] Documentation includes at least 3 usage examples
- [ ] Examples are executable/testable
- [ ] Formatting is clear and professional

---

## Task 5: Code Review Pass

**Steps:**

1. **Gather all your changes** (feature implementation + tests + docs)
2. **Open Copilot Chat** and use this final prompt:
   ```
   Perform a thorough code review of the changes to the /tasks endpoint 
   and tests. Identify:
   - Potential bugs or security risks
   - Missing test coverage
   - Performance issues
   - Style or readability problems
   - Backward compatibility concerns
   
   Suggest fixes for any issues found.
   ```

3. **Review Copilot's suggestions** carefully
4. **Implement any critical fixes** (security, bugs)
5. **Document any non-critical recommendations** for future improvement

**Success Criteria:**
- [ ] Code review completed
- [ ] Security concerns addressed
- [ ] Tests added for any gaps found
- [ ] Changes are ready for merge

---

## Challenge Wrap-Up

**Reflection Questions:**
1. How did Copilot accelerate your development workflow?
2. Which task (feature, tests, docs, review) did Copilot help most?
3. What would you use Copilot for in your own projects?

**Next Steps:**
- Try this workflow on your own codebase
- Explore Copilot's agent mode for multi-step changes
- Use similar prompts for documentation and code review

---

## Resources

- **Copilot Chat Docs:** https://github.com/features/copilot
- **FastAPI Docs:** https://fastapi.tiangolo.com/
- **pytest Documentation:** https://docs.pytest.org/
