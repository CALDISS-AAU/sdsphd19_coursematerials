Test
----
The Lorenz package contains a number of tests all written using the
Python standard library named 'doctest'. Doctest provides and easy and
efficient way of doing tests of various type. In Lorenz the tests are
implemented in two ways:

1. As examples in the docstring of the functions that constitute
   Lorenz.

2. As special '.dt' (DocTest) files which are not included as the
   function docstrings. This is a convenient way to include tests
   that are not a natural part of the function docstring.

The tests included do not cover all aspects. They have been included to
provide an idea of the capabilities and immense power of doctest and how
it can be used in practical software development.

A script has been provided as 'PACKAGE_ROOT/run_full_doctest.py' which
executes are doctest files in the package - i.e. files with extensions
'.py' and '.dt'. The full test can be run as:

.. code-block:: python

   $ cd PACKAGE_ROOT
   $ python run_full_doctest      # quiet test if all is ok
   $ python run_full_doctest -v   # to print all intermediate results


