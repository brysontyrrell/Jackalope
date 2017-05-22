Deploying the Slack App
-----------------------

Jackalope is written in Python using the Flask framework. This
gives a wide variety of options in deploying the application in your environment
from installing onto a standalone server, a cloud instance, or within a
container.

You will need the following components to fully deploy the service:

   * A web server or load balancer to serve traffic over TLS
   * A MySQL server
   * A WSGI server *(uWSGI or Gunicorn for example)* to run the application code

In a cloud instance deployments you can use services such as:

   * `Amazon Elastic Beanstalk <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html>`_
   * `Heroku <https://devcenter.heroku.com/articles/getting-started-with-python#introduction>`_
   * `Google Apps Engine <https://cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env>`_

Environment Variables
^^^^^^^^^^^^^^^^^^^^^

.. automodule:: jackalope.config

Run from application.py
^^^^^^^^^^^^^^^^^^^^^^^

.. automodule:: application

Using create_app()
^^^^^^^^^^^^^^^^^^

.. autofunction:: jackalope.create_app
