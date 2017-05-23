"""Routes for installation of the application to a Slack channel."""
import time

from flask import (
    current_app, redirect, request,
    render_template, url_for, Blueprint
)
import requests

from ..database import db
from ..database.models import SlackChannel
from ..slack import send_notification

blueprint = Blueprint('install', __name__)


@blueprint.route('/')
def root():
    """Renders the "Add to Slack" page."""
    return render_template('add_to_slack.html'), 200


@blueprint.route('/install')
def install():
    """The installation endpoint as set in the "Redirect URLs" for the Slack
    application under "OAuth & Permissions".
    
    A ``code`` parameter will be provided by Slack to this URL once an
    installing user has authorized the application for a channel.
    
    Using the ``code`` along with the application's set ``SLACK_CLIENT_ID`` and
    ``SLACK_CLIENT_SECRET`` values, the application will make a ``POST`` to
    ``https://slack.com/api/oauth.access`` to obtain an ``access_token`` and
    other details for the channel installation.
    
    Upon an ``ok`` response to the request, the details will be saved to the
    database, a UUID will be generated for receiving Jamf Pro webhooks, and a
    success message displayed in the Slack channel.
    
    If the Slack channel already exists in the database its details will be
    updated with those from the response.
    """

    code = request.args.get('code')
    if code:
        url = url_for('install.install', _external=True, _scheme='https')
        params = {
            'code': code,
            'client_id': current_app.config['SLACK_CLIENT_ID'],
            'client_secret': current_app.config['SLACK_CLIENT_SECRET'],
            'redirect_uri': url
        }
        resp = requests.post('https://slack.com/api/oauth.access', data=params)

        data = resp.json()

        if data.get('ok') is True:
            webhook = data.get('incoming_webhook', dict())

            channel_data = {
                'channel_id': webhook.get('channel_id'),
                'channel_name': webhook.get('channel_name'),
                'access_token': data.get('access_token'),
                'user_id': data.get('user_id'),
                'team_id': data.get('team_id'),
                'team_name': data.get('team_name'),
                'configuration_url': webhook.get('configuration_url'),
                'slack_webhook_url': webhook.get('url')
            }

            channel = SlackChannel.query.filter_by(
                channel_id=channel_data['channel_id'],
                team_id=channel_data['team_id']
            ).first()

            if channel:
                for key in channel_data.viewkeys():
                    setattr(channel, key, channel_data[key])

            else:
                channel = SlackChannel(**channel_data)
                db.session.add(channel)

            db.session.commit()

            text = (
                "Jackalope has been installed in this channel! Create webhooks "
                "(in `JSON` format) in your Jamf Pro server using this url:\n"
                "{}\n\nThey will appear here as notifications.".format(
                    url_for(
                        'jamfpro.jamf_webhook',
                        _external=True,
                        _scheme='https',
                        jamf_uuid=channel.jamf_uuid
                    )
                )
            )

            message = {
                "attachments": [
                    {
                        "fallback": text,
                        "color": '#800080',
                        "text": text,
                        "ts": int(time.time()),
                        "mrkdwn_in": ["text", "fallback_text"]
                    }
                ]
            }

            send_notification(channel.slack_webhook_url, message)

        else:
            current_app.logger.error('An error was encountered while attempting'
                                     'to install to a channel:')
            current_app.logger.error(data)

    return redirect(url_for('install.root', _external=True, _scheme='https'))
