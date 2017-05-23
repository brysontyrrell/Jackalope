Docker Example
--------------

The ``docker`` directory within the Github repository is an example of deploying
Jackalope using Docker containers and the ``docker-compose`` utility.

.. warning:: This example is not configured for HTTPS traffic - only HTTP over
    port 80. A production deployment should be configured with a certificate
    to encrypt traffic using TLS.

``docker-compose`` will start three containers (``nginx``, ``web`` - the
application - and ``mysql``) on the host. It will also create a volume attached
to the ``mysql`` container to persist the database between container tear-downs
(but be warned: if the volume is deleted the database will be lost!).

In your shell/Terminal, ``cd`` into the ``docker`` directory before continuing.

Connect to a Docker Host
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ eval $(docker-machine env yourhost)

Docker Environment Variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set the following environment variables within your shell/Terminal:

    * DEBUG
    * SECRET_KEY
    * SERVER_NAME
    * SLACK_CLIENT_ID
    * SLACK_CLIENT_SECRET
    * SLACK_SHAREABLE_URL
    * MYSQL_ROOT_PASSWORD
    * MYSQL_DATABASE
    * MYSQL_USER
    * MYSQL_PASSWORD

Build and Run the Containers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ docker-compose build
    $ docker-compose up -d

You will be able to access the application at the IP address of the Docker host.

.. note:: You can use ``ngrok`` to create a secure tunnel to the Docker host
    and expose it on the public internet to test with Slack. See
    :ref:`testing-with-ngrok` for more details.
