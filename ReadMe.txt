## CODE SETUP

1. Create public repo on Github
2. Create dir on local
3. create venv for project
    """conda create -p venv python==3.9 -y"""
    """conda activate venv/"""
4. Setup Github
    """git init"""
    """git add README.md"""
    """ git commit -m 'first commit' """
    """ git branch -M main """
    """ git remote add origin https://github.com/mohamedomartoure/mlproject.git """
    """ git push -u origin main """
5. Create and commit github new file (gitignore) on github {Indicate the file or folder git hafta ignore}
6. Create local files setup.py {It creates the ML App as a Package} and requirements.txt {with requirtements}
7. Create a local src folder and create a local file name """__init__.py""". {It will transform the dir to an package and able the function find_packages to find It}
8. Install requirements
    """pip install -r requirements.txt""" {Because of the "-e .", it will run the setup.py file too}
    returns """ml_project.egg-info""" folder with all the setup information
9. Push the files on Github
    """git add ."""
    """git status"""
    """git commit -m 'setup' """
    """git push -u origin main"""


    # DAY 2
    PRJECT STRUCTURE - LOGGING - EXCEPTION HANDLING

    1. Create subfolders as PACKAGES into src named 'components', 'pipeline'

        2. Create 'data_ingestion', 'data_transformation', 'model_trainer' modules(files) into `components`
        3. Create 'train_pipeline', 'predict_pipeline' modules(files) into `pipeline`

    4. Create 'logger.py', 'exception.py' 'utils.py' modules(files) into `src`

    5. Write CostumerException class code into exception.py in order to extend Exception Base Class and get a detailled message error along w logs
    6. Create log directory and save logs files within a format. Use a logger to log other modules

    
    # Day 3

    1. Create notebook folder into mlproject for notebook files (eda,trainer)
    2. Create into notebook, folder named data with the csv file
    