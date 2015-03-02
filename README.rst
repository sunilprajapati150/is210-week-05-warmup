####################
IS 210 Assignment 06
####################
************
Warmup Tasks
************

:College: CUNY School of Professional Studies
:Course-Name: Software Application Programming I
:Course-Code: IS 210
:Points: 20
:Due-Date: YYYY-MM-DDTHH:mm:ss

Overview
========

Modules are at the very heart of the Python programming language. Each Python
file created is its own module whether it's imported directly or run on the
command line. In this set of exercises we'll look at modules in isolation.

Instructions
============

The following tasks will either have you interacting with existing files in
the assignment repository or creating new ones on the fly. Don't forget to add
your interpreter directive, utf-8 encoding, and a short docstring with any new
files that you create!

.. important::

    In these exercises, you may, on occasion, come across a task that requres
    you to research or use a function or method not directly covered by the
    course text. Since Python is such a large language it would be impossible
    for the author to have included descriptions of each and every available
    function which would largely duplicate the offical Python documentation.

    A *vital* skill to successful programming is being comfortable searching
    for and using official language documentation sources like the
    `Python String Documentation`_ page. Throughout our coursework we will be
    practicing both the use of the language in practice and the search skills
    necessary to become functional programmers.

Warmup Tasks
============

Task 01: Create a Package
-------------------------

We'll assume you're comfortable with basic module creation and will move
straight on to package creation.

Specifications
^^^^^^^^^^^^^^

#.  Create a package called ``task_01``

#.  Create a module in ``task_01`` named ``peanut``

#.  In ``peanut``, create a constant named ``BUTTER`` and have it return a
    truthy value.

#.  In ``peanut``, create a second constant named ``OIL`` and assign it a
    falsy value

Examples
^^^^^^^^

.. code:: pycon

    >>> import task_01
    >>> if task_01.peanut.BUTTER: print 'I am truthy'
    True

    >>> import task_01.peanut
    >>> if not peanut.OIL: print 'I am Falsy'
    True

Task 02: Import a Module Namespace
----------------------------------

We'll begin our importation practice by importing a module with its full
namespace. Generally, this is the safest way to import modules though it's not
always the most practical.

Specifications
^^^^^^^^^^^^^^

#.  Create a module called ``task_02``

#.  Import the ``peanut`` module from the ``task_01`` package

#.  Create a new constant in ``task_02`` called, ``TIME`` and assign it the
    value from ``BUTTER`` constant of the ``peanut`` module

Examples
^^^^^^^^

.. code:: pycon

    >>> import task_02
    >>> if task_02.TIME: print 'I am truthy'

Task 03: Copy a Module Attribute
--------------------------------

Our next import adventure has us copying module attributes into the current
namespace.

Specifications
^^^^^^^^^^^^^^

#.  Create a module called ``task_03``

#.  Copy the ``BUTTER`` constant from the ``peanut`` module into the ``task_03``
    namespace

#.  Create a new constant called ``JELLY`` and assign its value from the
    copied ``BUTTER`` attribute

Examples
^^^^^^^^

.. code:: pycon

    >>> import task_03
    >>> task_03.BUTTER == True
    True

    >>> task_03.JELLY == task_03.BUTTER
    True

Executing Tests
===============

Code must be functional and pass tests before it will be eligible for credit.

Linting
-------

Lint tests check your code for syntactic or stylistic errors To execute lint
tests against a specific file, simply open a terminal in the same directory as
your code repository and type:

.. code:: console

    $ pylint filename.py

Where ``filename.py`` is the name of the file you wish to lint test.

Unit Tests
----------

Unit tests check that your code performs the tested objectives. Unit tests
may be executed individually by opening a terminal in the same directory as
your code repository and typing:

.. code:: console

    $ nosetests tests/name_of_test.py

Where ``name_of_test.py`` is the name of the testfile found in the ``tests``
directory of your source code.

Running All Tests
-----------------

All tests may be run simultaneously by executing the ``runtests.sh`` script
from the root of your assignment repository. To execute all tests, open a
terminal in the same directory as your code repository and type:

.. code:: console

    $ bash runtests.sh

Submission
==========

Code should be submitted to `GitHub`_ by means of opening a pull request.

As-of Lesson 02, each student will have a branch named after his or her
`GitHub`_ username. Pull requests should be made against the branch that
matches your `GitHub`_ username. Pull requests made against other branches will
be closed.  This work flow mimics the steps you took to open a pull request
against the ``pull`` branch in Week Two.

For a refresher on how to open a pull request, please see homework instructions
in Lesson 01. It is recommended that you run PyLint locally after each file
is edited in order to reduce the number of errors found in testing.

In order to receive full credit you must complete the assignment as-instructed
and without any violations (reported in the build status). There will be
automated tests for this assignment to provide early feedback on program code.

When you have completed this assignment, please post the link to your
pull request in the body of the assignment on Blackboard in order to receive
credit.

.. _GitHub: https://github.com/
.. _Python String Documentation: https://docs.python.org/2/library/stdtypes.html
