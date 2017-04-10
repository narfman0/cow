===
cow
===

.. image:: https://badge.fury.io/py/cow.png
    :target: https://badge.fury.io/py/cow

.. image:: https://travis-ci.org/narfman0/cow.png?branch=master
    :target: https://travis-ci.org/narfman0/cow

Yuge heifer-like bloated CMS - now with more django, S3, Lambda friendliness!

Documentation
-------------

Cow lives in lambda and breathes S3, and loves to ingest your waste and
uselessly regurgitate your API calls. It provides no end to its own waste,
and offers all the bloat your money can't buy.

Quickstart
----------

Install cow::

    pip install cow

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'rest_framework',
        'cow',
        ...
    )

Add cow's URL patterns:

.. code-block:: python

    from cow import urls as cow_urls


    urlpatterns = [
        ...
        url(r'^', include(cow_urls)),
        ...
    ]

Migrate app::

     ./manage.py migrate cow

Usage
-----

* After installation, add a urls endpoint, and edit menu, page, and plugins
* This should leave you with a hierarchy of pages (and their content)
* The API should give you a sitemap-like structure, and upon navigation,
  a further API call would give all the specific content for plugin
* Check examples for working samples of use!

TODO
----

* Unit tests - menus and some basic view checks
* Add deliciously overweight but relatable cow icon, as an endearing
  and manipulating draw in for suckers wanted to support literal and
  metaphorical dead weight

Features
--------

* Big fat bloated heifer offering content
* Configure menu, page, plugin content for mobile consumption

Running Tests
-------------

Does the code actually work?::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

License
-------

Copyright Jon Robison 2017, see LICENSE for details
