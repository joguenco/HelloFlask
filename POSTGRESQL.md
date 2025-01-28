### Installing the PostgreSQL database
* Install
```commandline
sudo apt install postgresql
```
* Create user
```commandline
sudo su - postgres
```
```commandline
psql
```
```commandline
CREATE ROLE hello WITH LOGIN NOSUPERUSER CREATEDB NOCREATEROLE INHERIT NOREPLICATION CONNECTION LIMIT -1 PASSWORD 'h';
```
* Show **pg_hba.conf** path
```commandline
show hba_file;
```
and Ctrl+D to exit psql and postgres user session
* Update pg_hba.conf

Search line
```
local   all             postgres                                peer
```
Add in the next line
```
local   all             hello                                  trust
```
Restart postgresql service
```
sudo systemctl restart postgresql
```
* Test mew hello user
```commandline
psql -d postgres -U odoo15 -W
```
### For access to database from remote host 
* Edit **postgresql.conf** file in the same directory of **pg_hba.conf** file
* Enable or add: listen_addresses = 'ip server'
* or
* Enable or add: listen_addresses = '*'
* In **pg_hba.conf** add the next line:
```
host    all             hello          remote.host.ip/24.mask.number         trust
```
