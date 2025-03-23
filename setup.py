import os

base_dir = os.path.dirname(os.path.abspath(__file__))

task_name = "Web Automation Task"
venv_python = os.path.join(base_dir, "venv", "Scripts", "python.exe")
script_path = os.path.join(base_dir, "program.py")

command = f'schtasks /create /tn "{task_name}" /tr "cmd.exe /c cd /d \\"{base_dir}\\" && \\"{venv_python}\\" \\"{script_path}\\"" /sc daily /st 21:37 /f'

os.system(command)
