aux
===
Auxcillary files which all are part of validating the input to various
functions. The main objective across the functions is to do type and
value checking of the system parameters, simulation parameters,
initial conditions and the generated output for the trajectory and
Euclidian solutions.


Functions
---------

.. automodule:: lorenz.aux
   :members: simpar_check, syspar_check, xyz0_check, xyzd_check


Code
----

.. literalinclude:: ../../../lorenz/aux.py


Test
----

PEP8
++++

.. literalinclude:: ../../../test/lorenz/aux/test_aux_pep8.dt