Deploying the Slack App
-----------------------

Jackalope is written in Python using the Flask framework. This
gives a wide variety of options in deploying the application in your environment
from installing onto a standalone server, a cloud instance, or within a
container.

.. note:: If you are testing, skip to :ref:`run-from-application-py` below.

You will need the following components to deploy the application:

   * A web server or load balancer to serve traffic over TLS
   * A WSGI server *(uWSGI or Gunicorn for example)* to run the application code
   * A MySQL server

The application will only connect to a MySQL server if all of the required
:ref:`environment-variables` have been provided. If not, a local SQLite database
will be created within the application directory.

In a cloud instance deployments you can use services such as:

   * `Amazon Elastic Beanstalk <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html>`_
   * `Heroku <https://devcenter.heroku.com/articles/getting-started-with-python#introduction>`_
   * `Google Apps Engine <https://cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env>`_

.. _run-from-application-py:

Run from application.py
^^^^^^^^^^^^^^^^^^^^^^^

.. automodule:: application

.. _testing-with-ngrok:

Testing with ngrok
^^^^^^^^^^^^^^^^^^

For testing, you can use the `ngrok <https://ngrok.com/>`_ secure tunneling
service to expose the application to the internet and access it using both HTTP
and HTTPS.

.. note:: ngrok will create randomized subdomains each time you execute the
    binary (e.g. ``4951502d.ngrok.io``). Custom subdomain names are a part of a
    paid subscription.

Once you have the ``ngrok`` binary you can create your tunnel.

Expose a local port on your client (5000 in this example):

.. code-block:: bash

    $ ngrok http 5000 --bind-tls true

Expose a port on another host from your client (such as a running Docker host):

.. code-block:: bash

    $ ngrok http 192.168.99.100:5000 --bind-tls true

When ``ngrok`` is running you will see the available public endpoints in the
window and a stream of traffic logging. Going to ``http://127.0.0.1:4040`` in
your browser will show the web UI and additional details on the requests that
are being made through the tunnel.

.. _environment-variables:

Environment Variables
^^^^^^^^^^^^^^^^^^^^^

.. automodule:: jackalope.config

Using create_app()
^^^^^^^^^^^^^^^^^^

.. autofunction:: jackalope.create_app
