import os
import subprocess


# subprocess.run(['python', '-V'])
output = 'test.txt'
# subprocess.run(['venv/Scripts/python', 'subprocess_output.py', output])
subprocess.run(['python', 'subprocess_output.py', output], shell=True)
