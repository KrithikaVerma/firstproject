import os
from pathlib import Path

# this template file is keeping all in one file and it will automate the creation of all these files and folders lsited below

list_of_files = [  # required for project development

    ".github/workflows/.gitkeep", # empty folder will not be visible in Github when pushed, hence creating this gitkeep (provided by Github) as a convention if you are not sure about the file that will go inside this 
    # This workflow folder is used for deployment i.e. CI/CD Integration, write down entire configuration 

    "src/__init__.py", # src is where we have all the  source code
    "src/components/__init__.py", # components are part of pipelines (one is training pipeline and other is prediction pipeline)
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception.py",


    "tests/unit/__init__.py",
    "tests/integration/__init__.py",


    "init_setup.sh",
    "requirements.txt",  # This will contain what all requirements are needed to deploy the project in production
    "requirements_dev.txt",  # this is for Dev
    "setup.py",
    "setup.cfg", 
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb" # to do your own experiments with small codes smippets 

]

for filepath in list_of_files:
    filepath = Path(filepath)  # this will make a system compatible path
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file
