import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO , format = '[%(asctime)s : %(message)s:]' )

project_name = "Chicken-disease-classifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constanta/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "README.md",
    "setup.py",
    "research/trails.ipynb"


]

for file_path in list_of_files:
    # creates a windows file path for overcoming errors
    file_path = Path(file_path)
    filedir , file_name = os.path.split(file_path)

    if filedir != "":
        os.makedirs(filedir , exist_ok=True)
        logging.info(f"{filedir} directory  created for file {file_name}")
    
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path , "w") as f:
            pass
            logging.info(f"Creating an empty file { file_path}")
    else:
        logging.info(f"{file_path} already exists")
