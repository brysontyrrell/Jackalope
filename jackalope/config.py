"""
.. Configuration settings for the application.

Configuration settings are applied at runtime from the environment variables
detailed below.

.. envvar:: DEBUG

    Run the application in debug mode (additional logging).

    This setting will set to ``True`` if any value is provided. To leave this
    setting disabled do not set it in the environment.

.. envvar:: SECRET_KEY

    The secret key is a value used to secure sessions with the application.

    If a value is not present the application will generate a 16-byte key using
    :func:`os.urandom`.

.. envvar:: SERVER_NAME

    The domain name of the application server.
    
    Example::
    
        jackalope.mydomain.org

.. envvar:: SLACK_CLIENT_ID

    The client ID for the Slack application.
    
    This is obtained during the app creation process at::
    
        https://api.slack.com/apps
    

.. envvar:: SLACK_CLIENT_SECRET

    The client secret key for the Slack application.
    
    This is obtained during the app creation process at::
    
        https://api.slack.com/apps

.. envvar:: SLACK_SHAREABLE_URL

    The URL provided by Slack for installing the application to channels. This
    is used for the installation page's "Add to Slack" button that is provided
    as a part of this application.
    
    This is obtainted during the app create process at::
    
        https://api.slack.com/apps

.. note:: The following database values are required when connecting Jackalope
    to a MySQL server. If they are omitted, a SQLite database will be created
    within the application directory. This is *not* recommended for production
    deployments.

.. envvar:: DATABASE_URL

    The URL to the MySQL server with the port.

    Example::

        localhost:3306
        database.mydomain.org:3306

.. envvar:: DATABASE_NAME

    The name of the MySQL database residing on the server.

.. envvar:: DATABASE_USER

    The username to access the database with.

.. envvar:: DATABASE_PASSWD

    The password to the user accessing the database.

"""
import os

DEBUG = bool(os.getenv('DEBUG', False))

SECRET_KEY = os.getenv('SECRET_KEY', os.urandom(16))

SERVER_NAME = os.getenv('SERVER_NAME')
PREFERRED_URL_SCHEME = 'https'

SLACK_CLIENT_ID = os.getenv('SLACK_CLIENT_ID')
SLACK_CLIENT_SECRET = os.getenv('SLACK_CLIENT_SECRET')

SLACK_SHAREABLE_URL = os.getenv('SLACK_SHAREABLE_URL')

SQLALCHEMY_TRACK_MODIFICATIONS = False

DATABASE_URL = os.getenv('DATABASE_URL')
DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWD = os.getenv('DATABASE_PASSWD')

if not (DATABASE_URL and DATABASE_NAME and DATABASE_USER and DATABASE_PASSWD):
    APP_DIR = os.path.dirname(os.path.realpath(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:////{}'.format(
        os.path.join(APP_DIR, 'jackalope.db'))
else:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}?charset=utf8'.format(
        DATABASE_USER,
        DATABASE_PASSWD,
        DATABASE_URL,
        DATABASE_NAME
    )
