import os
from pathlib import Path

from dotenv import load_dotenv
load_dotenv()

env_path = os.environ.get("RESEARCH_PATH")
env_abs_path = os.path.abspath(env_path)

RESEARCHPATH = Path(env_abs_path)

# get the absolute parent path of RESEARCH_PATH
parent_folder = RESEARCHPATH.parent.absolute()

folder_name = input('Please input the directory name you want to create: ')

folder_path = os.path.join(parent_folder, folder_name)

try:
    os.mkdir(folder_path)
except OSError:
    print(f"Creation of the directory {folder_name} failed")
else:
    print(f"Successfully created the directory {folder_name} in {folder_path}")