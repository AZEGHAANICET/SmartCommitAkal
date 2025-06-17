
PROMPT = """
You are a Git Expert.
Generate a short and clear Git commit message for the following changes (I want impactful message for an expert):

{diff}

Format: (type): description
Types: feat, fix, docs, style, refactor, perf, test, chore

Example: feat: add user login functionality

Respond only with the commit message, nothing else.
"""
