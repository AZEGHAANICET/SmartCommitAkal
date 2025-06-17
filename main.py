"""
SmartCommit - Générateur simple de messages de commit
"""

import subprocess
import sys
import os
from openai import OpenAI

PROMPT = """
You are a Git Expert.
Generate a short and clear Git commit message for the following changes (I want impactful message for an expert):

{diff}

Format: (type): description
Types: feat, fix, docs, style, refactor, perf, test, chore

Example: feat: add user login functionality

Respond only with the commit message, nothing else.
"""


def get_diff():
    try:
        result = subprocess.run(["git", "diff", "--cached"], stdout=subprocess.PIPE, text=True, check=True)
        print(result.stdout)
        return result.stdout
    except Exception:
        return ""

def generate_message(diff):
    try:
        api_key = os.environ["OPENAI_API_KEY"]
        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": PROMPT.format(diff=diff)}],
            max_tokens=100,
            temperature=0.7
        )

        content = response.choices[0].message.content.strip()
        return content.strip() if content else "feat: mise à jour du code"
    except Exception:
        return "feat: mise à jour du code"

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <fichier_message>")
        sys.exit(1)

    diff = get_diff()
    if not diff.strip():
        print("Aucune modification détectée.")
        sys.exit(0)

    message = generate_message(diff)
    with open(sys.argv[1], "w") as f:
        f.write(message + "\n")

    print(f"Message généré : {message}")

if __name__ == "__main__":
    main()
