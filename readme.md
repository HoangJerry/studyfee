# Study Fee

Study fee system

## Installation
Before you start make sure install python3 and virtualenv [pip](https://pip.pypa.io/en/stable/) to install Studyfee.

[mongoDB on Ubuntu18](https://www.digitalocean.com/community/tutorials/how-to-install-mongodb-on-ubuntu-18-04)

```
virtualenv -p python3 env
source env/bin/activate
```

```
pip install -r requirements.txt
```

Change the study/setting_local (copy).py -> setting_local.py
Change setting with your database

```python3
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'ENFORCE_SCHEMA': True
        'NAME': 'studyfee',
        'HOST': 'host-name or ip address',
        'PORT': port_number,
        'USER': 'db-username',
        'PASSWORD': 'password',
        'AUTH_SOURCE': 'db-name',
        'AUTH_MECHANISM': 'SCRAM-SHA-1',
        'REPLICASET': 'replicaset',
        'SSL': 'ssl',
        'SSL_CERTFILE': 'ssl_certfile',
        'SSL_CA_CERTS': 'ssl_ca_certs',
        'READ_PREFERENCE': 'read_preference'
    }
}
```

```python3
# to make migrations:
python manage.py makemigrations 

# to migrate
python manage.py migrate
```

```
#create superuser login admin add first time
python manage.py createsuperuser
```

```
# collectstatic
python manage.py collectstatic
```

```
# runserver
python manage.py runserver

# go to localhost:8000/admin to login
```

## Build angular to js files
```
cd ng-bootstrap
```

```
ng build

or

ng build --env=prod --output-hashing

```
Tại django server
```
(env) python manage.py collectstatic
yes
(env) python manage.py runserver
```
#go to localhost:8000

