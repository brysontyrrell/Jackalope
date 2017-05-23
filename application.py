"""This script creates the root application object from the
:func:`jackalope.create_app` application factory function. If the script has
been called from the command line an instance will be launched in a local
development server.

.. code-block:: bash

    $ python application.py

The development server will be accessible at::

    http://localhost:5000

If the application is being deployed with a WSGI framework, configure the WSGI
server to point to the ``application.py`` file and the ``application`` object.

Alternatively, the WSGI framework can instantiate and customize an application
object using :func:`jackalope.create_app`.
"""

from jackalope import create_app

application = create_app()

if __name__ == '__main__':
    application.run(threaded=True)
