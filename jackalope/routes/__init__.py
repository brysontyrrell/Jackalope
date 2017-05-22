"""Route blueprints."""
from . import errors, install, jamfpro


def register_routes(app):
    """Registers all imported blueprints to the passed application.
    
    :param flask.Flask app: An instantiated Flask application object.
    """
    app.register_blueprint(errors.blueprint)
    app.register_blueprint(install.blueprint)
    app.register_blueprint(jamfpro.blueprint)
