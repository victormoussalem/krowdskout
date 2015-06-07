import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = '1234567890' #TODO: Consider making this randomly generated every so often for security reasons.

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

ACCESS_TOKEN = '8ee27215f27c6a2d5ce1975abb0c86938e63589e'
SPARK_OCCUPANCY = 'cm'

# pagination
LOCATIONS_PER_PAGE = 5