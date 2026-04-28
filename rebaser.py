import subprocess
import os

env = os.environ.copy()
env['GIT_SEQUENCE_EDITOR'] = 'python editor.py'

print("Starting rebase...")
subprocess.run(["git", "rebase", "-i", "--root"], env=env)

while True:
    res = subprocess.run(["git", "status"], capture_output=True, text=True)
    if "interactive rebase in progress" not in res.stdout:
        break
    
    print("Amending commit...")
    subprocess.run(["git", "commit", "--amend", "--author=Ankit Raj <ankitsingh154760@gmail.com>", "--no-edit"])
    print("Continuing rebase...")
    subprocess.run(["git", "rebase", "--continue"])

print("Done!")
