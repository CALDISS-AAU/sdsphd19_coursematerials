"""

Algorithm
---------

The algorithm to perform the key computations can be expressed via the theory
above as:

1. Input parameters:

   * System parameters: :math:`\sigma`, :math:`\rho` and :math:`\beta`.

   * Simulation parameters: :math:`t_\delta` and :math:`N`.

   * Initial conditions: (:math:`x[0]`, :math:`y[0]`, :math:`z[0]`).

2. Compute :math:`x[n+1]`, :math:`y[n+1]` and :math:`z[n+1]` for
   :math:`n=0,1,\ldots,N-2` from:

.. math::

   x[n+1] &= \sigma \: (y[n] - x[n]) \: t_\delta + x[n] \\
   y[n+1] &= x[n] \: (\rho - z[n]) \: t_\delta - y[n] \: t_\delta + y[n] \\
   z[n+1] &= (x[n] \: y[n] - \beta \: z[n]) \: t_\delta + z[n]

3. Compute the Euclidian distance :math:`d[n+1]` for
   :math:`n=0,1,\ldots,N-2` from:

   .. math::

      d[n+1] = \sqrt{(x[n+1] - x[n])^2 + (y[n+1] - y[n])^2
               + (z[n+1] - z[n])^2}

4. Save the following data:

   * System parameters :math:`\sigma`, :math:`\rho` and :math:`\beta`.
   
   * Simulation parameters: :math:`t_\delta` and :math:`N`.

   * Initial conditions: (:math:`x[0]`, :math:`y[0]`, :math:`z[0]`).

   * Trajectory: :math:`\mathbf{x}`, :math:`\mathbf{y}` and
     :math:`\mathbf{z}`.

   * Euclidian distance: :math:`\mathbf{d}`.

5. Plot:

   * 2D-trajectories of planes: :math:`(x[n],y[n])`, :math:`(x[n],z[n])`
     and :math:`(y[n],z[n])` for :math:`n=0,1,\ldots,N-1`.

   * 3D-trajectory space curve: :math:`(x[n],y[n],z[n])` for
     :math:`n=0,1,\ldots,N-1`.


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


References
----------

1. Edward N. Lorenz: "Deterministic Nonperiodic Flow",
   Journal of Atmospheric Sciences, vol. 20, pp. 130-141, 1963.
   DOI: 10.1175/1520-0469(1963)020<0130:DNF>2.0.CO;2.


"""

from . import aux
from . import plot
from . import hdf5
from . import run
from . import solver
