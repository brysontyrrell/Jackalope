Create the Slack App for Your Team
----------------------------------

Before deploying the app on a server, you will need to create it for your Slack
team at https://api.slack.com/apps .

.. image:: ../images/slack_create_app_1.png
   :align: center
   :width: 400 px

You will need to enable ``Incoming Webhooks``, located at `Features > Incoming Webhooks`...

.. image:: ../images/slack_create_app_2.png
   :align: center
   :width: 500 px

...and set a ``Redirect URL``, located at `Features > OAuth & Permissions` that points to:

   *https://jackalope.mydomain.org/install*

.. image:: ../images/slack_create_app_3.png
   :align: center
   :width: 500 px

With those two steps complete you will be able to copy the following values for
use with the deployed application environment:

* Basic Information/App Credentials/``Client ID``
* Basic Information/App Credentials/``Client Secret``

.. image:: ../images/slack_create_app_4.png
   :align: center
   :width: 500 px

* Manage Distribution/Share Your App with Your Team/``Shareable URL``

.. image:: ../images/slack_create_app_5.png
   :align: center
   :width: 500 px

.. note:: You will need to set these into environment variables details in the
   deployment documentation. See :ref:`environment-variables`.
