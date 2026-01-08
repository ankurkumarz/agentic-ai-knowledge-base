import os
import subprocess

root = "docs"

md_files = []
for subdir, dirs, files in os.walk(root):
    for f in files:
        if f.endswith(".md"):
            md_files.append(os.path.join(subdir, f))

command = ["pandoc", "-s"] + md_files + ["-o", "AgenticAI_Knowledge.docx"]
subprocess.run(command)

