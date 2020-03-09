# Machine Learning
Generate pip dependencies

```
pipenv shell
pip freeze > requirements.txt
```


Upload to Git

```
git add -A .
git commit -m "message"
git push
```


Pull the updates

```
git pull
pip install -r requirements.txt
```
