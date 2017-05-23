"""Jackalope: a slacky Jamf Pro notification plugin."""
import flask

import config
from .database import db
from .routes import register_routes


__title__ = 'jackalope'
__version__ = '0.1.1'
__author__ = 'Bryson Tyrrell'
__copyright__ = '(c) 2017 Bryson Tyrrell'


def create_app():
    """Create the root application object, configure the database object, and
    register all blueprints from :mod:`jackalope.routes`.
    
    :returns: Flask application
    :rtype: flask.Flask
    """
    app = flask.Flask(__name__, static_url_path='')
    app.config.from_object(config)

    db.init_app(app)

    register_routes(app)

    with app.app_context():
        if app.config['DEBUG']:
            db.engine.echo = 'debug'

        db.create_all()

    return app
