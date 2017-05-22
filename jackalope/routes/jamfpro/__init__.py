"""Routes for receiving and processing Jamf Pro webhooks and send notifications
into the associated Slack channel.
"""
import flask
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound

from ...database.models import SlackChannel
from ...slack import send_notification
from ..errors import JSONNotProvided, SlackChannelLookupError
from .webhooks import webhook_notification

blueprint = flask.Blueprint('jamfpro', __name__)


@blueprint.route('/jamf/<jamf_uuid>', methods=['POST'])
def jamf_webhook(jamf_uuid):
    """The receiver endpoint where ``jamf_uuid`` is the auto-generated UUID for
     and installed Slack channel.
     
     :param str jamf_uuid: The generated UUID for the installed Slack channel.
     """
    try:
        channel = SlackChannel.query.filter_by(jamf_uuid=jamf_uuid).one()
    except (NoResultFound, MultipleResultsFound) as err:
        raise SlackChannelLookupError(err)

    if not flask.request.json:
        raise JSONNotProvided

    message = webhook_notification(flask.request.json)

    if message:
        send_notification(channel.slack_webhook_url, message)

    return '', 200
