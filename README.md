# Cheetsheet pipenv
to install dependencies `pipenv install requests`

Run shell with virtualenv `pipenv shell`

Directly run command/program using virtualenv `pipenv run python`

Migrate existing requirements.txt to Pipfile `pipenv install -r requirements.txt`

print dependency in requirements.txt format `pipeve lock -r`

install dev specific dependency `pipenv install pytest --dev`

Uninstall dependency `pipenv uninstall requests`

Delete and recreate from scratch
```
    pipenv --rm
    pipenv install
```

Location of virtual environment `pipenv --venv`

Vulnerability check `pipenv check`

Dependency graph `pipenv graph`

Production deployment
```
    pipenv lock
    pipenv install --ignore-pipflie
```
System and OS object
```
    os.environ['KEY'] # environment value
    os.getcwd() # get current working directory.
    sys.executable # location of python executable
```

