# HelloFlask
Example for Flask and Fly.io in Python

## Content
- Flask
- Add endpoint ping


## Create python virtual environment
```
virtualenv venv
```
or
```
virtualenv -p python3.12 venv
```
or
```
python3.12 -m venv venv
```
## Activate python virtual environment
```
source venv/bin/activate
```
or
```
. ./venv/bin/activate
```

## Update pip and tools
```
pip install -U pip
pip install --upgrade wheel
pip install --upgrade setuptools
```

### Check syntax
```
ruff check .
```
### Format
```
ruff format .
```
## Install dependencies
```
pip install -r requirements.txt
```
## Run
```
flask --app flaskr run --debug
```
