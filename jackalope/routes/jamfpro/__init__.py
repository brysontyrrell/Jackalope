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
     
     Inbound webhooks must be in JSON format or a 400 error will be returned.
     
     If a supported webhook event has been received it will be formatted into
     a Slack message via
     :func:`jackalope.routes.jamfpro.webhooks.webhook_notification` and sent via
     :func:`jackalope.slack.send_notification`.
     
     :param str jamf_uuid: The generated UUID for the installed Slack channel.
     
     :raises: SlackChannelLookupError
     :raises: JSONNotProvided
     
     :returns: HTTP 204 success response.
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

    return '', 204
