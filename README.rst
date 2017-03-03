===
cow
===

.. image:: https://badge.fury.io/py/cow.png
    :target: https://badge.fury.io/py/cow

.. image:: https://travis-ci.org/narfman0/cow.png?branch=master
    :target: https://travis-ci.org/narfman0/cow

Django mobile S3+Lambda friendly CMS

Documentation
-------------

Cow lives in lambda and breathes S3, and loves to serve API calls

Quickstart
----------

Install cow::

    pip install cow

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'tinymce',
        'cow',
        ...
    )

Add cow's URL patterns:

.. code-block:: python

    from cow import urls as cow_urls


    urlpatterns = [
        ...
        url(r'^', include(cow_urls)),
        url(r'^tinymce/', include('tinymce.urls')),
        ...
    ]

Migrate app::

     ./manage.py migrate cow

Usage
-----

TODO

TODO
----

* Usage :)
* Plugin based text, link, map references
* Images uploads, referencing via plugin :(

Features
--------

* Stores users and shows list view of metrics hit

Running Tests
-------------

Does the code actually work?::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

License
-------

Copyright Jon Robison 2017, see LICENSE for details
