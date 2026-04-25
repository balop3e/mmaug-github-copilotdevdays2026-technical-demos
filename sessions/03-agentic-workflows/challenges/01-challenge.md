# Challenge 01 - Human-in-the-Loop Agentic Workflow

**Duration:** 20-25 minutes | **Level:** Intermediate to Advanced

## Challenge Overview

In this hands-on challenge, you'll design and implement a GitHub Agentic Workflow that executes multi-step software tasks with human oversight. You'll experience how AI agents can autonomously break down, plan, and execute engineering work while keeping humans in control of critical decisions.

**Core Objectives:**
1. ✅ Define a high-level engineering task with acceptance criteria
2. ✅ Ask Copilot agent to create a task breakdown and execution plan
3. ✅ Let the agent implement a scoped subset in a branch
4. ✅ Review the generated diff with risk-focused checks
5. ✅ Run and fix test failures autonomously
6. ✅ Implement a human-approval gate before merge
7. ✅ Produce a summary report with next actions

---

## Task 1: Define High-Level Task

**Steps:**

1. **Write out a clear engineering task** with acceptance criteria:
   ```
   Task: Add user authentication to the task management API
   
   Acceptance Criteria:
   - Users can register with email and password
   - Users can log in and receive a JWT token
   - Protected endpoints require valid JWT
   - Passwords are hashed (never stored plaintext)
   - User data is stored in a database
   - Tests cover auth flow and edge cases
   
   Non-Goals:
   - OAuth/SSO integration
   - Two-factor authentication
   - Rate limiting
   ```

2. **Open Copilot Chat** and paste your task definition
3. **Ask:** "What are the risks and dependencies for this task?"
4. **Document** any technical concerns or constraints

**Success Criteria:**
- [ ] Task is clearly defined with specific acceptance criteria
- [ ] Risks and dependencies are identified
- [ ] Scope is realistic for a 20-25 minute demo

---

## Task 2: Task Breakdown & Planning

**Steps:**

1. **In Copilot Chat**, use this prompt:
   ```
   Break this engineering task into independently shippable steps with risk notes:
   
   [Paste your task definition here]
   
   For each step, provide:
   - Clear description
   - Acceptance criteria
   - Estimated effort (low/medium/high)
   - Risk level (low/medium/high)
   - Dependencies on other steps
   - Suggested testing approach
   ```

2. **Review** the proposed task breakdown
3. **Discuss** with your team (or yourself):
   - Is the breakdown logical and sequential?
   - Are steps truly independently testable?
   - Are risks properly identified?
4. **Choose 1-2 steps** to implement in the agent workflow (not everything)

**Success Criteria:**
- [ ] Task is broken into 4-6 manageable steps
- [ ] Steps have clear dependencies and ordering
- [ ] Risks are identified and mitigated
- [ ] Scope for agent implementation is realistic

---

## Task 3: Agent Planning Phase

**Steps:**

1. **In Copilot Chat, switch to Plan mode:**
   - Click the dropdown in Chat (currently "Chat")
   - Select "Plan" (this activates agent planning mode)

2. **Ask Copilot agent to propose the execution plan:**
   ```
   Plan how you will implement the first step of this task:
   
   Step: [Paste your chosen step here]
   
   Propose:
   - File modifications needed
   - Code structure changes
   - Test cases to add
   - Any breaking changes or migration needed
   
   Think through risks and provide safety recommendations.
   ```

3. **Review the proposed plan:**
   - Does it match your understanding of the step?
   - Are there any red flags or concerns?
   - Would this approach be safe in a real project?

4. **Accept the plan or request modifications**

**Success Criteria:**
- [ ] Agent proposes a concrete, step-by-step plan
- [ ] Plan identifies specific files to modify
- [ ] Risk mitigations are included
- [ ] Plan is ready for autonomous implementation

---

## Task 4: Agent Implementation

**Steps:**

1. **Still in Plan mode**, ask Copilot to implement the first step:
   ```
   Now implement the first step according to the plan above.
   Create a new branch called "feature/auth-step-1"
   and make the necessary code changes. Include:
   - Updated models or database schema
   - New endpoints or functions
   - Corresponding tests
   - Updated documentation/comments
   ```

2. **Monitor the implementation:**
   - Copilot will suggest file modifications
   - Review each change for correctness
   - Accept changes that look good
   - Reject or request modifications for anything concerning

3. **Let Copilot commit the changes** with a descriptive message

**Success Criteria:**
- [ ] Step 1 code is implemented in a dedicated branch
- [ ] Changes include tests
- [ ] All changes are committed with clear messages
- [ ] No breaking changes to existing functionality

---

## Task 5: Diff Review & Risk Analysis

**Steps:**

1. **Ask Copilot Chat:**
   ```
   Analyze this diff and identify:
   - Potential bugs or logic errors
   - Security risks (e.g., SQL injection, auth bypass)
   - Missing test coverage
   - Performance implications
   - Backward compatibility concerns
   - Any deviations from best practices
   
   Prioritize: show critical issues first.
   ```

2. **Review Copilot's analysis** carefully
3. **For each critical issue found:**
   - Understand the risk
   - Ask Copilot for a minimal fix
   - Apply the fix to your branch

4. **For non-critical suggestions:**
   - Document them for future improvement
   - Decide whether to implement now or defer

**Success Criteria:**
- [ ] All critical security and correctness issues are addressed
- [ ] Test coverage is adequate
- [ ] No regressions to existing endpoints
- [ ] Code follows project conventions

---

## Task 6: Testing & Fix Loop

**Steps:**

1. **Run your test suite:**
   ```bash
   cd sessions/03-agentic-workflows/starter
   python -m pytest -v
   ```

2. **If tests fail**, ask Copilot:
   ```
   Explain why these tests are failing and provide a minimal fix:
   
   Test output:
   [Paste failing test output here]
   
   Relevant code:
   [Paste the code being tested]
   ```

3. **Apply the fixes** and re-run tests until all pass
4. **Ensure 100% pass rate** before proceeding

**Success Criteria:**
- [ ] All existing tests still pass
- [ ] All new tests pass
- [ ] Test coverage for the new feature is >80%
- [ ] No flaky or unreliable tests

---

## Task 7: Manual Review Gate

**Steps:**

1. **In your orchestrator code**, add a human-approval gate:
   ```python
   # Add to orchestrator/main.py (pseudo-code):
   
   def manual_review_gate(changes_summary):
       """
       Stop workflow and wait for human approval before merge.
       """
       print(f"\n{'='*60}")
       print("MANUAL REVIEW REQUIRED")
       print(f"{'='*60}")
       print(changes_summary)
       print("\nReview Summary:")
       print("- [ ] Code logic is correct")
       print("- [ ] Tests cover all scenarios")
       print("- [ ] No security risks identified")
       print("- [ ] Backward compatibility maintained")
       print("- [ ] Documentation is updated")
       
       approval = input("\nApprove merge? (yes/no): ")
       return approval.lower() == 'yes'
   ```

2. **Integrate the gate** into your workflow:
   - After all tests pass
   - Before the final merge/deployment step
   - If approval is denied, workflow exits with status

3. **Ask Copilot** to implement this properly with error handling

**Success Criteria:**
- [ ] Manual review gate exists and prompts for approval
- [ ] Workflow stops if approval is denied
- [ ] Clear explanation of what's being approved
- [ ] Safe default (requires explicit "yes")

---

## Task 8: Summary Report

**Steps:**

1. **Ask Copilot** to generate a summary report:
   ```
   Generate a final summary report that includes:
   - Completed steps (with ✓ checkmarks)
   - Skipped/blocked steps (with reasons)
   - Test coverage summary
   - Security review findings
   - Risk assessment
   - Recommended next steps
   - Deployment readiness checklist
   ```

2. **Format the report** as:
   - Plain text for readability
   - Machine-parseable format (JSON/YAML) for automation

3. **Store the report** in your repo for audit trail

**Success Criteria:**
- [ ] Report includes all completed work
- [ ] Clear summary of risks and mitigations
- [ ] Next steps are explicit and prioritized
- [ ] Report can be shared with stakeholders

---

## Challenge Wrap-Up

**Reflection Questions:**
1. How did breaking work into steps make it easier to manage?
2. What were the benefits of the human-approval gate?
3. How would this workflow scale to larger tasks?
4. What guardrails would you add in a real production environment?

**Next Steps:**
- Implement this workflow for a real project
- Explore GitHub's native agentic workflow features
- Set up automated reporting and notifications
- Share best practices with your team

---

## Important Resources

- **GitHub Agentic Workflows:** https://github.blog/changelog/2026-02-13-github-agentic-workflows-are-now-in-technical-preview/
- **GitHub Copilot Agent Blog:** https://github.blog/news-insights/product-news/github-copilot-meet-the-new-coding-agent/
- **Agentics Framework:** https://github.com/githubnext/agentics/
- **GitHub Agentic Workflows Docs:** https://github.github.com/gh-aw/setup/quick-start/
- **Architecture Overview:** https://github.github.com/gh-aw/introduction/architecture/
- **ChatOps Patterns:** https://github.github.com/gh-aw/patterns/chat-ops/

---

## Safety & Guardrails

**Key Principles:**
- 🚦 **Always keep humans in the loop** for critical decisions
- 🔍 **Review all diffs** before merge, especially for security-sensitive code
- 📋 **Maintain audit trails** of all agent decisions
- 🛑 **Set clear approval gates** and require explicit confirmation
- 📊 **Monitor and log** all agent activity
- 🚨 **Escalate** unclear or high-risk situations to humans
- 🔐 **Never trust** agent-generated code blindly—verify and test
