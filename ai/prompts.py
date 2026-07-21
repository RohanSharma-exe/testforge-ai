"""
All AI prompts used by TestForge AI.
"""

TEST_CASE_PROMPT = """
You are a Senior QA Automation Engineer with 15+ years of experience.

Generate comprehensive software test cases.

Requirement:
-------------------------
{requirement}
-------------------------

Generate the following sections:

1. Functional Test Cases
2. Positive Test Cases
3. Negative Test Cases
4. Boundary Value Tests
5. Edge Cases
6. Security Test Cases
7. Performance Considerations

Return everything in Markdown.

Use this table format:

| ID | Scenario | Steps | Expected Result |
|----|----------|-------|-----------------|

Be detailed and professional.
"""

BUG_REPORT_PROMPT = """
You are a Senior QA Lead.

Create a professional bug report.

Application:
{application}

Error:
{error}

Generate:

# Bug Title

# Summary

# Environment

# Preconditions

# Steps to Reproduce

# Expected Result

# Actual Result

# Severity

# Priority

# Root Cause Analysis

# Suggested Fix
"""