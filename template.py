# this executable file creates your folder structure

import os
from pathlib import Path
import logging

# logging. format curr time in ascii and print log message
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "app.py",
    "research/trials.ipynb",
]


for filepath in list_of_files:
    filepath = Path(filepath) # convert to device os filepath format
    filedir, filename = os.path.split(filepath) # extract file dir and file name

    if filedir !="":
        os.makedirs(filedir,exist_ok=True) # create dir, if exists, ignore
        logging.info(f"Creating directory; {filedir} for the file: {filename}") # log the info
    
    # if file is empty or doesn't exist, create the file and log it
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): 
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")