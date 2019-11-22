.. lorenz documentation master file, created by
   sphinx-quickstart on Fri May 23 16:04:19 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Lorenz
======
This package simulates the Lorenz attractor as discovered in 1963. The
package includes a number of modules to assist in the simulation and
generation of 2D and 3D plots of the attractor.

Problem and solution:

.. toctree::
   :maxdepth: 1

   lorenz/_theory.rst
   lorenz/_algorithm.rst
   lorenz/_software.rst
   lorenz/_test.rst
   lorenz/_cases.rst
   lorenz/_references.rst

The modules are:

- **aux** (:py:mod:`lorenz.aux`) A number of functions to validate the input provided to various functions.

- **hdf5** (:py:mod:`lorenz.hdf5`) Interface to saving and loading all relevant data in HDF5 files.

- **plot** (:py:mod:`lorenz.plot`) Plotting functionality of the 3D Lorenz trajectory and the corresponding projections in 2D.

- **run** (:py:mod:`lorenz.run`) Functionality to control the execution of the simulation, handle plotting and saving data.

- **solver** (:py:mod:`lorenz.solver`) A first order Euler ODE solver for the Lorenz problem.

.. toctree::
   :hidden:
   
   lorenz/aux.rst
   lorenz/hdf5.rst
   lorenz/plot.rst
   lorenz/run.rst
   lorenz/solver.rst


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

