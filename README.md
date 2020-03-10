# Machine Learning
This is my general repository for my files for studying Machine Learning.

## Setup Windows environment

1. Download and install [MiniConda3](https://docs.conda.io/en/latest/miniconda.html).
2. Create a venv using `pipenv` or `MiniConda3`.
```
# For MiniConda3 (Anaconda Prompt (MiniConda3))
conda create --prefix ./env pandas numpy matplotlib scikit-learn jupyter

# For pipenv
pipenv install pandas numpy matplotlib scikit-learn jupyter
```
3. Activate the environment
```
# For MiniConda3
conda activate C:\path\to\your\env\ENV_FOLDER_NAME

# For pipenv
cd C:\path\to\your\project\PROJECT_FOLDER_NAME
pipenv shell
```


## Generate pip dependencies

Activate your venv, then run the commands below on your command line.
```
pipenv shell
pip freeze > requirements.txt
```


## Clone Github repository to your local path

```
git clone REPO_URL
```


## Upload to Git

```
git add -A .
git commit -m "message"
git push
```


## Pull the updates

```
git pull
pip install -r requirements.txt

# If you are using pipenv
pipenv install -r requirements.txt
```