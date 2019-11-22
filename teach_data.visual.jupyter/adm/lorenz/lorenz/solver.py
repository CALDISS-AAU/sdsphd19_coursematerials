
import numpy as np

import lorenz


def ode_solver(syspar, simpar, xyz0):
    """Computes (x,y,z) trajectory for Lorenz attractor.

    Args:
        *syspar* (dict): System parameters. Dictionary is composed as:
        {'sigma': :math:`\\sigma`, 'rho': :math:`\\rho`,
        'beta': :math:`\\beta`}. Here :math:`\sigma, \\rho, \\beta \\in
        \\mathbb{F}_{32} \\vert \\mathbb{F}_{64} \\vert \mathbb{N}`.

        *simpar* (dict): Simulation parameters. The dictionary is
        composed as {'t_delta': :math:`t_\\delta`, 'N': :math:`N`}.
        Here :math:`t_\delta \in \mathbb{F}_\\mathrm{32} \\vert
        \\mathbb{F}_\\mathrm{64}` is the sampling time, and
        :math:`N \\in \\mathbb{N}_1` is the total number of samples.

        *xyz0* (dict): Initial conditions. The dictionary is
        composed as {'x0': :math:`x[0]`, 'y0': :math:`y[0]`,
        'z0': :math:`z[0]`}. Here :math:`x[0], y[0], z[0] \\in
        \\mathbb{F}_{32} \\vert \\mathbb{F}_{64}`
        represent the initial conditions at time :math:`t=0`.

    Returns:
        *xyzd* (dict): Dictionary containing the trajectory solution
        given by {'x': :math:`\\mathbf{x}`, 'y': :math:`\\mathbf{y}`,
        'z': :math:`\\mathbf{z}`}` where :math:`\\mathbf{x} =
        [x[0],...,x[N-1]]^\\mathrm{T}`, :math:`\\mathbf{y} =
        [y[0],...,y[N-1]]^\\mathrm{T}` and :math:`\\mathbf{z} =
        [z[0],...,z[N-1]]^\\mathrm{T}` with :math:`N` being the
        number of samples. The vector :math:`\\mathbf{d} =
        [d[0],...,d[N-1]]^\\mathrm{T}` contains the Euclidian
        distance between points - such that :math:`d[n+1]` is the distance
        between points :math:`(x[n], y[n], z[n])` and :math:`(x[n+1], y[n+1],
        z[n+1])`. The vectors :math:`\\mathbf{x}, \\mathbf{y}, \\mathbf{z},
        \\mathbf{d}` are all of type **numpy.ndarray** and array elements
        :math:`x[n], y[n], z[n], d[n] \\in \\mathbb{F}_\\mathrm{32} \\vert
        \\mathbb{F}_{64}`.

    Raises:
        TypeError, ValueError via :py:mod:`lorenz.aux.syspar_check`,
        :py:mod:`lorenz.aux.simpar_check` and
        :py:mod:`lorenz.aux.xyz0_check`.

    Examples:
        Examples as part of the :py:mod:`lorenz.run` module.

    """
    # Check input parameters
    lorenz.aux.syspar_check(syspar)
    lorenz.aux.simpar_check(simpar)
    lorenz.aux.xyz0_check(xyz0)

    # Solve ODE for Lorenz attractor
    x, y = np.empty(simpar['N']), np.empty(simpar['N'])
    z, d = np.empty(simpar['N']), np.zeros(simpar['N'])
    x[0], y[0], z[0] = xyz0['x0'], xyz0['y0'], xyz0['z0']
    for n in range(simpar['N']-1):
        dx = syspar['sigma'] * (y[n] - x[n]) * simpar['t_delta']
        dy = (x[n] * (syspar['rho'] - z[n]) - y[n]) * simpar['t_delta']
        dz = (x[n] * y[n] - syspar['beta'] * z[n]) * simpar['t_delta']
        x[n+1] = x[n] + dx
        y[n+1] = y[n] + dy
        z[n+1] = z[n] + dz
        d[n+1] = np.sqrt(dx**2 + dy**2 + dz**2)

    xyzd = {'x': x, 'y': y, 'z': z, 'd': d}

    return xyzd
