Theory
------
This file includes functions necessary to simulate the Lorenz attractor [1].
The Lorenz attractor is described by three coupled first order differential
equations as:

.. math::
   
   \dot{x}(t) = \frac{dx}{d\tau}(t) &= \sigma (y(t) - x(t)) \\
   \dot{y}(t) = \frac{dy}{d\tau}(t) &= x(t)\: (\rho - z(t)) - y(t) \\
   \dot{z}(t) = \frac{dz}{d\tau}(t) &= x(t) \: y(t) - \beta z(t)

'dot' indicates the derivative of the variable wrt. time. To simulate such
a set of equations which are continuous in time we need a mapping of the
time variable as:

.. math::

   t \leftarrow n t_\delta

where :math:`t_\delta` is the sampling time used in the simulations. One way
to reformulate the problem in discrete time is to use Euler or Runge-Kutta to
be able to advance time to :math:`n+1` from a solution at :math:`n`. Using a
finite difference as:

.. math::

    \dot{x}((n+1)t_\delta) \simeq \frac{x((n+1)t_\delta) - x(nt_\delta)}
                                    {t_\delta}

or using the formulation :math:`x(nt\delta) = x[n]` leads to the Euler method
as:

.. math::

   \frac{x[n+1] - x[n]}{t_\delta} &= \sigma \: (y[n] - x[n]) \\
   \frac{y[n+1] - y[n]}{t_\delta} &= x[n] \: (\rho - z[n]) - y[n] \\
   \frac{z[n+1] - z[n]}{t_\delta} &= x[n] \: y[n] - \beta \: z[n]

or with the solution at time :math:`n+1` determined from time :math:`n` as:

.. math::

    x[n+1] &= \sigma \: (y[n] - x[n]) \: t_\delta + x[n] \\
    y[n+1] &= x[n] \: (\rho - z[n]) \: t_\delta - y[n] \: t_\delta + y[n] \\
    z[n+1] &= (x[n] \: y[n] - \beta \: z[n]) \: t_\delta + z[n]

with :math:`n=0,1,\ldots,N-1`. Furthermore, we wish to know the change
(Euclidian distance) from one sample, :math:`n`, to another, :math:`n+1`. This
we may use to indicate the 'speed' at which we move through space via for
example colouring of the :math:`(x,y,z)` trajectory in space. The
Euclidian distance can be determined as:

.. math::

   d[n+1] = \sqrt{(x[n+1] - x[n])^2 + (y[n+1] - y[n])^2
            + (z[n+1] - z[n])^2}

Once the signals :math:`(x[n+1], y[n+1], z[n+1], d[n+1])` have been computed
for all :math:`n=0,1,\ldots,N-2` we form the following vectors to obtain a
simple notation:

.. math::

   \mathbf{x} &= \left[x[0], x[1],\ldots, x[N-1] \right]^\mathrm{T} \\
   \mathbf{y} &= \left[y[0], y[1],\ldots, y[N-1] \right]^\mathrm{T} \\
   \mathbf{z} &= \left[z[0], z[1],\ldots, z[N-1] \right]^\mathrm{T} \\
   \mathbf{d} &= \left[d[0], d[1],\ldots, d[N-1] \right]^\mathrm{T}
