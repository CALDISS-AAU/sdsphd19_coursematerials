======
Lorenz
======

:Primary developers:
   Torben Larsen
   Thomas Arildsen
   Tobias L. Jensen

:Additional developers:
   None

:Institution:
   Aalborg University,
   Department of Electronic Systems,
   Signal and Information Processing,
   Niels Jernes Vej 12,
   DK-9220 Aalborg,
   Denmark.

:Version:
    1.0.0


Introduction
------------
The Lorenz package supports computation of the 3D-trajectory of the
famous 3 coupled first order differential equations. In addition it
supports 2D-plane plots as well as saving and loading of all system
as simulation data.


Installation
------------
The lorenz package is normally distributed in a zip-file with all
computation, documentation, test files etc. included. Say the name
of the folder you extract the zip-file is **PACKAGE_ROOT** then
extracting lorenz provides you with a structure like:

  PACKAGE_ROOT/__init__.py
              /cases/
              /doc/
              /examples/
              LICENSE.rst
              /lorenz/
              MANIFEST.in
              README.rst
              run_full_doctest.py
              test/

You must then set the PYTHONFOLDER to include 'PACKAGE_ROOT/lorenz' which
in a BASH-shell can be done as:

  export PYTHONPATH=PACKAGE_ROOT

This ensures that the lorenz package can be imported as expected and thus
be used from any place in the directory structure.


Documentation
-------------
The package is documented using **Sphinx** by use of a combination of two
elements:

1. Static ReStrucTured (.rst) text files describing the problem, theory
   etc. which is located in the directory 'PACKAGE_ROOT/doc/source'.

2. Dynamic ReStrucTured (.rst) text files extracted from the docstrings
   in the developed functions.

The documentation can be found as a html file at:

   PACKAGE_ROOT/doc/build/html/index.html


Testing
-------
The lorenz package implements a number of doctests to test against
PEP8, input type and value check for functions, i/o tests etc. The
tests performed are either part of the examples in function
docstrings or part of the 'lorenz/test/' folder with '.dt' doctests.
A full test of all relevant '.py' and '.dt' files are done as either
of the following:

    $ cd PACKAGE_ROOT
    $ python run_full_doctest.py     # quiet
    $ python run_full_doctest.py -v  # verbose

In quiet mode a list is provided of all files containing test scenarios.
If a test is completed without errors nothing is done and if an error
occurs the detailed information is provided. In verbose mode, all the
tests are provided as well as the result. This leads to substantial 
information and should only be done to analyse the details of the tests 
(although it is better to inspect all '.py' and '.dt' files).
