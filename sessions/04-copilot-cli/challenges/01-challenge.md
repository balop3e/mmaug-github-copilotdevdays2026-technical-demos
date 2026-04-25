# Challenge 01 - Safer Command Automation with Copilot CLI

**Duration:** 20-25 minutes | **Level:** Beginner to Intermediate

## Challenge Overview

In this hands-on challenge, you'll experience GitHub Copilot CLI as your AI terminal companion. You'll convert natural language intent to shell commands, validate and explain commands before execution, compose safe data-processing pipelines, and generate reusable scripts—all with safety guardrails.

**Core Objectives:**
1. ✅ Convert natural language intent to shell commands
2. ✅ Explain and validate generated commands before running
3. ✅ Compose a safe data-processing pipeline
4. ✅ Generate a reusable script from interactive commands
5. ✅ Add input validation and error handling
6. ✅ Document cross-platform alternatives

---

## Task 1: File Discovery with Natural Language

**Steps:**

1. **Open your terminal** and navigate to the starter folder:
   ```bash
   cd sessions/04-copilot-cli/starter
   ```

2. **Use Copilot CLI** to find markdown files:
   ```bash
   github-copilot find all markdown files in this project and show the 10 largest
   ```
   
   Or use the interactive mode:
   ```bash
   github-copilot
   # Then type: Find all markdown files larger than 200KB and list top 10 by size.
   ```

3. **Review the suggested command:**
   ```bash
   find . -type f -name "*.md" -print0 | xargs -0 du -h | sort -hr | head -n 10
   ```

4. **Ask Copilot to explain it:**
   - What does each part do?
   - Why use `-print0` and `xargs -0`?
   - When would this command fail?

5. **Run the command:**
   ```bash
   find . -type f -name "*.md" -print0 | xargs -0 du -h | sort -hr | head -n 10
   ```

**Success Criteria:**
- [ ] Command successfully lists markdown files
- [ ] Top 10 files by size are displayed
- [ ] You understand each part of the command

---

## Task 2: Pipeline Composition & Dry-Run

**Steps:**

1. **Create sample data** (or use existing data in the starter folder):
   ```bash
   ./setup-demo-data.sh
   ```

2. **Ask Copilot CLI** for a data analysis pipeline:
   ```
   Show me how to find all Python files with the word "import" 
   and count unique imports.
   ```

3. **Review the proposed pipeline:**
   ```bash
   grep -r "import" . --include="*.py" | cut -d: -f2 | sort | uniq -c | sort -rn
   ```

4. **Ask Copilot to explain:**
   - What data passes between each pipe?
   - How does `cut -d: -f2` work?
   - What would happen without `sort | uniq`?

5. **Ask for a safer variant:**
   ```
   Suggest a safer variant of this pipeline with 
   better error handling and performance.
   ```

6. **Test with `--dry-run` equivalent** (preview without modification):
   ```bash
   # First, just count:
   grep -r "import" . --include="*.py" | wc -l
   ```

**Success Criteria:**
- [ ] Pipeline works correctly
- [ ] You understand each step
- [ ] You could modify it for different use cases

---

## Task 3: Archive Script Generation

**Steps:**

1. **Ask Copilot CLI** to help create an archive script:
   ```
   Create a safe bash script to archive completed tasks from tasks.csv.
   The script should:
   - Read tasks.csv with completed/done status
   - Create archive.csv with completed rows
   - Remove archived rows from original
   - Support --dry-run mode to preview changes
   - Support --help to show usage
   - Validate input file exists before proceeding
   - Use clear output messages
   ```

2. **Review the proposed script** that Copilot suggests
3. **Ask for improvements:**
   ```
   Add input validation and error handling to this script.
   Ensure it doesn't crash if:
   - Input file doesn't exist
   - CSV format is invalid
   - Insufficient permissions
   ```

4. **Create the script** (`archive-tasks.sh`):
   ```bash
   cat > starter/archive-tasks.sh << 'EOF'
   #!/bin/bash
   # [Paste Copilot's generated script here]
   EOF
   chmod +x starter/archive-tasks.sh
   ```

5. **Test in dry-run mode first:**
   ```bash
   ./starter/archive-tasks.sh --dry-run
   ```

6. **Test with actual data:**
   ```bash
   ./starter/archive-tasks.sh
   ```

**Success Criteria:**
- [ ] Script creates archive.csv correctly
- [ ] Original file is cleaned (completed rows removed)
- [ ] --dry-run mode shows changes without applying them
- [ ] --help displays usage instructions
- [ ] Script handles errors gracefully

---

## Task 4: Command with Batch Rename

**Steps:**

1. **Ask Copilot CLI** for a safe batch rename approach:
   ```
   Show me how to rename files from draft-*.md to final-*.md with dry-run output.
   I want to see the changes before applying them.
   ```

2. **Review the suggested command:**
   ```bash
   for f in draft-*.md; do
     echo mv "$f" "${f/draft-/final-}"
   done
   ```

3. **Understand this approach:**
   - Why use `echo` first?
   - What does `${f/draft-/final-}` do?
   - How would you actually execute it?

4. **Ask for error handling:**
   ```
   Add error checking to ensure the rename won't fail.
   Handle cases where target file already exists.
   ```

5. **Create a test scenario:**
   ```bash
   # Create test files
   touch draft-example1.md draft-example2.md
   
   # Preview changes
   for f in draft-*.md; do
     echo "Would rename: $f → ${f/draft-/final-}"
   done
   
   # Actually apply (if dry-run looks good)
   for f in draft-*.md; do
     [ -f "${f/draft-/final-}" ] && echo "Target exists: ${f/draft-/final-}" || mv "$f" "${f/draft-/final-}"
   done
   ```

**Success Criteria:**
- [ ] Preview shows all files that would be renamed
- [ ] No files are renamed until you confirm
- [ ] Error handling prevents overwriting existing files

---

## Task 5: Generate Release Notes

**Steps:**

1. **Initialize a sample git repo** (if not already):
   ```bash
   cd starter && git init && cd ..
   # Or use existing repo
   ```

2. **Ask Copilot CLI** to generate release notes:
   ```
   Create grouped release notes from commit messages from the last 2 weeks.
   Group by type: Features, Fixes, Documentation, Other.
   ```

3. **Review the command:**
   ```bash
   git log --since="2 weeks ago" --pretty=format:"- %s (%an)"
   ```

4. **Ask for improvements:**
   ```
   Group these commits by type (feat:, fix:, docs:).
   Create a professional release notes format.
   ```

5. **Generate and save release notes:**
   ```bash
   git log --since="2 weeks ago" --pretty=format:"- %s" | tee release-notes.txt
   ```

**Success Criteria:**
- [ ] Release notes are generated from recent commits
- [ ] Commits are organized by type/category
- [ ] Format is professional and readable

---

## Task 6: Cross-Platform Script Alternative

**Steps:**

1. **Ask Copilot CLI** for a Python alternative:
   ```
   Provide a Python version of the archive script for cross-platform compatibility.
   Should work on Windows, macOS, and Linux.
   ```

2. **Review the Python implementation:**
   - How does it handle file I/O differently?
   - What CSV library does it use?
   - How is dry-run implemented?

3. **Ask about error handling:**
   ```
   Add comprehensive error handling and logging to the Python version.
   Log all operations to archive.log for audit trail.
   ```

4. **Save the Python script** as `starter/archive-tasks.py`

5. **Test it:**
   ```bash
   python starter/archive-tasks.py --dry-run
   python starter/archive-tasks.py
   ```

**Success Criteria:**
- [ ] Python version produces same output as bash
- [ ] Works on multiple platforms (test on your OS)
- [ ] Logging captures all operations
- [ ] Error handling is comprehensive

---

## Task 7: Complex Query & Analysis

**Steps:**

1. **Ask Copilot CLI** for a complex analysis:
   ```
   Find all Python files that import "requests" library, 
   show their size, modification date, and count total lines of code.
   Sort by lines of code descending.
   ```

2. **Review the proposed command:**
   ```bash
   grep -r "import requests" . --include="*.py" -l | \
     while read f; do echo "$f $(du -h "$f" | cut -f1) $(stat -f %Sm -t '%Y-%m-%d' "$f") $(wc -l < "$f" | tr -d ' ')"; done | \
     sort -k4 -rn
   ```

3. **Ask Copilot to explain:**
   - Why use `while read`?
   - What does `tr -d ' '` do?
   - How would you filter by size?

4. **Ask for optimization:**
   ```
   Make this command more efficient. Avoid repeated stat calls.
   Use find with printf if possible.
   ```

5. **Test and refine:**
   ```bash
   # Run the command
   # Observe the output
   # Ask for further improvements
   ```

**Success Criteria:**
- [ ] Command finds all matching files
- [ ] Output includes size, date, and line count
- [ ] Results are sorted correctly
- [ ] You understand each step

---

## Safety Practices Checklist

- [ ] Always inspect commands before execution
- [ ] Use dry-run or echo patterns for destructive operations
- [ ] Validate file paths and permissions
- [ ] Use `find -print0` and `xargs -0` for filenames with spaces
- [ ] Add error handling for missing files or permission issues
- [ ] Log operations for audit trail
- [ ] Test on sample data before production
- [ ] Provide `--help` and `--dry-run` options
- [ ] Quote variables to handle spaces: `"$file"`
- [ ] Use explicit exit codes for error handling

---

## Challenge Wrap-Up

**Reflection Questions:**
1. Which Copilot CLI feature helped you most?
2. How did dry-run patterns help prevent mistakes?
3. What safety practices would you add to your workflows?
4. How could you apply this to your daily development tasks?

**Next Steps:**
- Create wrapper scripts around common complex commands
- Build an internal command library for your team
- Integrate Copilot CLI into your CI/CD workflows
- Explore custom Copilot agents for domain-specific tasks

---

## Resources

- **GitHub Copilot CLI Docs:** https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents
- **Bash Scripting Guide:** https://www.gnu.org/software/bash/manual/bash.html
- **Unix Pipes & Filters:** https://www.gnu.org/software/coreutils/manual/
- **Git Documentation:** https://git-scm.com/doc
- **Python CSV Module:** https://docs.python.org/3/library/csv.html
