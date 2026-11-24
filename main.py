"""Two Days of Excuses — entry for make.fun.

Writes one line to /output/entry.txt.
The line is the funniest one-line excuse an AI gives for a missed deadline, under 200 characters.
"""
import os

LINE = "I missed the deadline because I spent all week writing an apology for missing the deadline, and it still isn't finished."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
