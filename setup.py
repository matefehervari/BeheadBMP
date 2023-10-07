import os
import pathlib

os.system("python -m venv venv")
os.system("venv\Scripts\\activate & pip install -r requirements.txt")
cwd = pathlib.Path(__file__).parent.resolve()
with open("run.bat", "w") as f:
    f.write(f'cd "{cwd}" & venv\\Scripts\\activate & pythonw run.py')
