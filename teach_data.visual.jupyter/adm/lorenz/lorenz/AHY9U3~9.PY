
import numpy as np


def simpar_check(simpar):
    """Validates simpar dictionary wrt. type and values.

    Args:
        *simpar* (dict): Simulation parameters. The dictionary is
        composed as {'t_delta': :math:`t_\\delta`, 'N': :math:`N`}.
        Here :math:`t_\delta \in \mathbb{F}_\\mathrm{32} \\vert
        \\mathbb{F}_\\mathrm{64}` is the sampling time, and
        :math:`N \\in \\mathbb{N}_1` is the total number of samples.

    Returns:
        Nothing returned.

    Raises:
        TypeError, ValueError

    Examples:
        >>> from lorenz.aux import simpar_check
        >>> simpar_check({'t_delta': 0.01, 'N': 1000})
        >>> simpar_check({'t_delta': 0.01, 'N': '100'})
        Traceback (most recent call last):
        ...
        TypeError: Input ({'t_delta': 0.01, 'N': '100'}) must be int.

    """
    if not (type(simpar) == dict and len(simpar) == 2):
        st = "Input ({!r}) must be 2-pair dict.".format(simpar)
        raise TypeError(st)
    for key in simpar.keys():
        if not key in ('t_delta', 'N'):
            st = "Input ({!r}) has invalid key.".format(simpar)
            raise ValueError(st)
    if not type(simpar['t_delta']) in (float, ):
        st = "Input ({!r}) must be float.".format(simpar)
        raise TypeError(st)
    if not type(simpar['N']) in (int,):
        st = "Input ({!r}) must be int.".format(simpar)
        raise TypeError(st)


def syspar_check(syspar):
    """Validates *syspar* dictionary wrt. type and values.

    Args:
        *syspar* (dict): System parameters. Dictionary is composed as:
        {'sigma': :math:`\\sigma`, 'rho': :math:`\\rho`,
        'beta': :math:`\\beta`}. Here :math:`\sigma, \\rho, \\beta \\in
        \\mathbb{F}_{32} \\vert \\mathbb{F}_{64} \\vert \mathbb{N}`.

    Returns:
        Nothing returned.

    Raises:
        TypeError, ValueError

    Examples:
        >>> from lorenz.aux import syspar_check
        >>> syspar_check({'sigma': 10, 'rho': 0.2, 'beta': 0.1})

    """
    if not (type(syspar) == dict and len(syspar) == 3):
        st = "Input ({!r}) must be 3-pair dict.".format(syspar)
        raise TypeError(st)
    for key, value in syspar.items():
        if not key in ('sigma', 'rho', 'beta'):
            st = "Input ({!r}) has invalid key.".format(syspar)
            raise ValueError(st)
        if not type(value) in (float, int):
            st = "Input ({!r}) must be float or int.".format(syspar)
            raise TypeError(st)


def xyz0_check(xyz0):
    """Validates xyz0 dictionary wrt. type and values.

    Args:
        *xyz0* (dict): Initial conditions. The dictionary is
        composed as {'x0': :math:`x[0]`, 'y0': :math:`y[0]`,
        'z0': :math:`z[0]`}. Here :math:`x[0], y[0], z[0] \\in
        \\mathbb{F}_{32} \\vert \\mathbb{F}_{64}`
        represent the initial conditions at time :math:`t=0`.

    Returns:
        Nothing returned.

    Raises:
        TypeError, ValueError

    Examples:
        >>> from lorenz.aux import xyz0_check

    """
    if not (type(xyz0) == dict and len(xyz0) == 3):
        st = "Input ({!r}) must be 3-pair dict.".format(xyz0)
        raise TypeError(st)
    for key, value in xyz0.items():
        if not key in ('x0', 'y0', 'z0'):
            st = "Input ({!r}) has invalid key.".format(xyz0)
            raise ValueError(st)
        if not type(value) in (float, int):
            st = "Input ({!r}) must be float or int.".format(xyz0)
            raise TypeError(st)


def xyzd_check(xyzd):
    """Validates xyzd dictionary wrt. type and values.

    Args:
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

    Returns:
        Nothing returned.

    Raises:
        TypeError, ValueError

    Examples:
        >>> from lorenz.aux import xyzd_check

    """
    if not (type(xyzd) == dict and len(xyzd) == 4):
        st = "Input ({!r}) must be 4-pair dict.".format(xyzd)
        raise TypeError(st)
    for key, value in xyzd.items():
        if not key in ('x', 'y', 'z', 'd'):
            st = "Input ({!r}) has invalid key.".format(xyzd)
            raise ValueError(st)
        if not type(value) in (np.ndarray, ):
            st = "Input ({!r}) must be float or int.".format(xyzd)
            raise TypeError(st)
        if not type(value[0]) in (np.float32, np.float64):
            st = "Array elements must be float32 or float64.".format(xyzd)
            raise TypeError(st)
