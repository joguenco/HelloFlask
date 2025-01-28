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

## Run with a Production Server
```
pip install waitress
```
```
waitress-serve --call 'flaskr:create_app'
```

## Deploy in Fly.io
### Create database named <helloflaskdb>
```
fly postgres create
```
### Application status
```
fly status --app helloflaskdb
```
### List users of database
```
fly postgres users list --app helloflaskdb
```
### Connect to database
```
fly postgres connect -a helloflaskdb
```
### Create user
```
CREATE ROLE hello WITH LOGIN NOSUPERUSER CREATEDB NOCREATEROLE INHERIT NOREPLICATION CONNECTION LIMIT -1 PASSWORD 'N0PiratearXfavor';
```
### Create proxy
```
fly proxy 5432 -a helloflaskdb
```
### Connect with pgcli
```
pgcli -h localhost -d postgres -U hello -W
```
and
```
pgcli -h localhost -d hello -U hello -W
```
### Create database
```
create database hello
```
### List applications
```
fly app list
```
### Attach or Detach
Check
```
 fly postgres users list --app helloflaskdb
```
Attach
```
fly postgres attach helloflaskdb --app helloflask
```
Detach
```
fly postgres detach helloflaskdb --app helloflask
```

### Launch and Deploy
```
fly launch
```
```
fly deploy
```

### Destroy
```
fly app destroy helloflask
```
```
fly app destroy helloflaskdb
```