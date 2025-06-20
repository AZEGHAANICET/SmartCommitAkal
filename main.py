"""
SmartCommit - Générateur simple de messages de commit
"""

import subprocess
import sys
import os
from openai import OpenAI
from utils.generate_message import generate_message
from utils.get_diff import get_diff
from constants import SAFE_EXIT, UNSAFE_EXIT

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <fichier_message>")
        sys.exit(UNSAFE_EXIT)

    diff = get_diff()
    if not diff.strip():
        print("Aucune modification détectée.")
        sys.exit(SAFE_EXIT)

    message = generate_message(diff)
    with open(sys.argv[1], "w") as f:
        f.write(message + "\n")

    print(f"Message généré : {message}")

if __name__ == "__main__":
    main()
