graph
=====

find shortest path in graph

.. image:: https://img.shields.io/badge/Coverage-100%25-brightgreen.svg
    :alt: coverage badge
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style

Settings
--------


Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy graph

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest