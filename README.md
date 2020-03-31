# Machine Learning
This is my general repository for my files for studying Machine Learning.

## Setup Windows environment

1. Download and install [MiniConda3](https://docs.conda.io/en/latest/miniconda.html) or install `pipenv`.
```
$ pip install pipenv
```
2. Create a venv using `pipenv` or `MiniConda3` and install some packages.
```
# For MiniConda3 (using Anaconda Prompt (MiniConda3))
$ conda create --prefix ./env pandas numpy matplotlib scikit-learn jupyter

# For pipenv
$ pipenv install pandas numpy matplotlib scikit-learn jupyter
```
3. Activate the environment
```
# For MiniConda3
$ conda activate C:\path\to\your\env\ENV_FOLDER_NAME

# For pipenv
$ cd C:\path\to\your\project\PROJECT_FOLDER_NAME
$ pipenv shell
```


## Generate pipenv / Miniconda packages

Activate your venv, then run the commands below on your command line.
```
# For MiniConda3
$ conda env export > environment.yml

# For pipenv
$ pipenv shell
$ pipenv lock

# For pipenv (requirements.txt)
## This will generate a Pipfile.lock
$ pipenv lock -r

## This will generate a requirements.txt
$ pipenv run pip freeze > requirements.txt
```

## Install dependencies
```
# If you are using pipenv, this will install packages from the Pipfile.lock
$ pipenv sync

# If you are using MiniConda3
$ conda env create -f environment.yml

# requirements.txt
$ pipenv install -r path/to/requirements.txt
```

## Update pipenv packages
* Check what changed upstream: `$ pipenv update --outdated`
* Two options to update packages:
  * Update all packages: `$ pipenv update`.
  * Specific package: `$ pipenv update <pkg>`.

## Clone Github repository to your local path

```
git clone REPO_URL
```


## Upload to Git

```
git add .
git commit -m "message"
git push
```


## Pull the updates

```
git pull
```