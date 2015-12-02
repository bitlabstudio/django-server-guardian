Django Server Guardian
============

A reusable Django app, that fetches and visualizes server health metrics.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install django-server-guardian

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/bitmazk/django-server-guardian.git#egg=server_guardian

TODO: Describe further installation steps (edit / remove the examples below):

Add ``server_guardian`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'server_guardian',
    )

Add the ``server_guardian`` URLs to your ``urls.py``

.. code-block:: python

    urlpatterns = patterns('',
        ...
        url(r'^server-guardian/', include('server_guardian.urls')),
    )

Before your tags/filters are available in your templates, load them by using

.. code-block:: html

	{% load server_guardian_tags %}


Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate server_guardian


Usage
-----

TODO: Describe usage or point to docs. Also describe available settings and
templatetags.


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 django-server-guardian
    make develop

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch

In order to run the tests, simply execute ``tox``. This will install two new
environments (for Django 1.6 and Django 1.7) and run the tests against both
environments.
