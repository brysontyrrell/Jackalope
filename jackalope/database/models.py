"""Database models."""
import uuid

from . import db


def _generate_uuid():
    """Returns a UUID string.

    :return: UUID as a string
    :rtype: str
    """
    return str(uuid.uuid4())


class BaseModel(db.Model):
    __abstract__ = True


class SlackChannel(BaseModel):
    """Database model for installed Slack channels.
    
    :param str channel_id: The Slack ID for installed channel.
    :param str jamf_uuid: A randomly generated UUID used for receiving inbound
        webhooks from a Jamf Pro server.
        
    :param str channel_name: The name of the installed channel.
    :param str access_token: The access token provided by Slack upon
        installation.
        
    :param str user_id: The Slack ID of the installing Slack user.
    :param str team_id: The Slack ID of the installing Slack Team.
    :param str team_name: The name of the installing Slack Team.
    
    :param str configuration_url: URL to the Slack app configuration page.
    :param str slack_webhook_url: The inbound Slack webhook URL for the
        installed channel.
        
    """
    __tablename__ = 'slackchannels'

    id = db.Column(db.Integer, primary_key=True)
    channel_id = db.Column(db.String(12), unique=True, index=True)
    jamf_uuid = db.Column(
        db.String(36), unique=True, index=True, default=_generate_uuid)

    channel_name = db.Column(db.String(128))
    access_token = db.Column(db.String(128))

    user_id = db.Column(db.String(12))
    team_id = db.Column(db.String(12))
    team_name = db.Column(db.String(128))

    configuration_url = db.Column(db.String(256))
    slack_webhook_url = db.Column(db.String(256))
