Software
--------
The algorithm described in the previous section clearly outlines the necessary
components for doing the task. We should note that 5 different test cases for
different combinations of system parameters must be handled and that these
results must be stored in separate directories. This means that one simple way
of handling this is to have a configuration and execution script for each test
case. Also we should note that some testing must be provided. These
considerations combined with the teory and algorithm means that the following
modules would make sense:

1. **aux**: A module containing a number of tests for valid input. This
   should cover valid system parameters (type and value), simulation
   parameters (type and value) and initial conditions (type). These
   parameters are contained in dictionaries to protect against 'stupid'
   misplacement errors.

2. **hdf5**: A module to save and load data for system parameters
   (:math:`\sigma`, :math:`\rho` and :math:`\beta`), simulation parameters,
   (:math:`t_\delta` and :math:`N`), initial conditions
   (:math:`x[0]`, :math:`y[0]`, :math:`z[0]`), trajectory
   :math:`(\mathbf{x}, \mathbf{y}, \mathbf{z})` and Euclidian distance
   :math:`\mathbf{d}`.

3. **plot**: A module to do 2D-trajectory plots of
   :math:`(\mathbf{x}, \mathbf{y})`, :math:`(\mathbf{x}, \mathbf{z})`
   and :math:`(\mathbf{y}, \mathbf{z})` as well as 3D-trajectory in
   space :math:`(\mathbf{x}, \mathbf{y}, \mathbf{z})`. Also the
   Euclidian distance :math:`\mathbf{d}` may be used to indicate the
   speed at which the change between samples happens.

4. **run**: A module to control the execution of the different other
   modules to ensure an easy user interface.

5. **solver**: A module to provide a solver to compute the key
   computational part to determine the trajectories
   :math:`(\mathbf{x}, \mathbf{y}, \mathbf{z})` and the
   Euclidian distance :math:`\mathbf{d}`.

