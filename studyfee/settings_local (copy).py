import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

USE_TZ = False

SITE_URL = "http://localhost:8000"
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'ng-bootstrap/dist')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = SITE_URL+"/static/" 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = SITE_URL+"/media/"

# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'ENFORCE_SCHEMA': True
#         'NAME': 'studyfee',
#         'HOST': 'host-name or ip address',
#         'PORT': port_number,
#         'USER': 'db-username',
#         'PASSWORD': 'password',
#         'AUTH_SOURCE': 'db-name',
#         'AUTH_MECHANISM': 'SCRAM-SHA-1',
#         'REPLICASET': 'replicaset',
#         'SSL': 'ssl',
#         'SSL_CERTFILE': 'ssl_certfile',
#         'SSL_CA_CERTS': 'ssl_ca_certs',
#         'READ_PREFERENCE': 'read_preference'
#     }
# }