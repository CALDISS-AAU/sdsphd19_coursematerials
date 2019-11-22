"""
This file includes functions necessary to simulate the Lorenz attractor [1].
The Lorenz attractor is described by three coupled first order differential
equations as:

    x_dot = sigma * (y - x)
    y_dot = x * (rho - z) - y
    z_dot = x * y - beta * z

'dot' indicates the derivative of the variable wrt. time. To simulate such
a set of equations which are continuous in time we need a mapping of the
time variable as:

    t <- n * t_delta

where t_delta is the sampling time used in the simulations. One way to
reformulate the problem in discrete time is to use Euler or Runge-Kutta
to be able to advance time to n+1 from a solution at n. Using a finite
difference as:

    v_dot[n] = (v[n+1] - v[n]) / t_delta

leads to the Euler method as:

    (x[n+1] - x[n]) / t_delta = sigma * (y[n] - x[n])
    (y[n+1] - y[n]) / t_delta = x[n] * (rho - z[n]) - y[n]
    (z[n+1] - z[n]) / t_delta = x[n] * y[n] - beta * z[n]

or with the solution at time n+1 determined from time n as:

    x[n+1] = sigma * (y[n] - x[n]) * t_delta + x[n]
    y[n+1] = x[n] * (rho - z[n]) * t_delta - y[n] * t_delta + y[n]
    z[n+1] = (x[n] * y[n] - beta * z[n]) * t_delta + z[n]

Furthermore, we wish to know the change (Euclidian distance) from one
sample, n, to another, n+1. This we may use to indicate the 'speed'
at which we move through space via for example colouring of the
(x,y,z) trajectory in space.

    d[n+1] = sqrt(x[n+1] - x[n])**2 + (y[n+1] - y[n])**2
             + (z[n+1] - z[n])**2)


[1] Edward N. Lorenz: "Deterministic Nonperiodic Flow",
    Journal of Atmospheric Sciences, vol. 20, pp. 130-141, 1963.
    DOI: 10.1175/1520-0469(1963)020<0130:DNF>2.0.CO;2.


"""

import lorenz
