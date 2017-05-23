"""Custom application exceptions and error handlers."""
from flask import current_app, Blueprint
from sqlalchemy.exc import SQLAlchemyError

blueprint = Blueprint('errors', __name__)


@blueprint.app_errorhandler(Exception)
def general_exception(err):
    """Catch-all error handler for unhandled exceptions."""
    current_app.logger.exception(err)
    return 'Internal server error (unknown). Check logs.', 500


@blueprint.app_errorhandler(SQLAlchemyError)
def sqlalchemy_error(err):
    """Internal error for database access exceptions."""
    current_app.logger.exception(err)
    return 'Internal server error. Check logs.', 500


class JackalopeException(Exception):
    """Base Jackalope Exception"""


class JSONNotProvided(JackalopeException):
    """A valid JSON body was not provided with a request."""


class SlackChannelLookupError(JackalopeException):
    """Exception raised when performing a lookup of an installed Slack channel.
    """


@blueprint.app_errorhandler(JSONNotProvided)
def json_not_provided(err):
    """No JSON object decoded from the request."""
    current_app.logger.exception(err)
    return 'No JSON found with request', 400


@blueprint.app_errorhandler(SlackChannelLookupError)
def slack_channel_lookup_error(err):
    """'None' or 'Multiple' results were found during a ``one()`` query for
    :class:`jackalope.database.models.SlackChannel``.
    """
    current_app.logger.exception(err)
    return err.message, 404
