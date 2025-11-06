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
    """pip install -r requirements.txt""" {Because of the "-e .", it will run the setup.py file too }

