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

