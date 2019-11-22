
import h5py

from . import aux


def save_hdf5(syspar, simpar, xyz0, xyzd, familyname):
    """Saves system and simulation data to <filename>/<filename>.hdf5.

    *save_hdf5* saves all relevant data regarding system parameters,
    simulation parameters, initial conditions, :math:`(x,y,z)`
    trajectory and Euclidian distance :math:`\\mathbf{d}`. The data is
    saved in the file named *familyname* in the file named
    *familyname.hdf5*.

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

        **familyname** (str): High abstraction level name for the simulation
        to be performed. An example could be 'testcase1' or similar.

    Returns:
        Nothing returned.

    Raises:
        TypeError, ValueError

    Examples:
        >>>

    """
    # Check input parameters
    aux.syspar_check(syspar)
    aux.simpar_check(simpar)
    aux.xyz0_check(xyz0)
    aux.xyzd_check(xyzd)

    # Open HDF5 file
    f5name = "{0}/{1}.hdf5".format(familyname, familyname)
    f5 = h5py.File(f5name, 'w')

    # Save system parameters
    f5.create_dataset('sigma', data=syspar['sigma'])
    f5.create_dataset('rho', data=syspar['rho'])
    f5.create_dataset('beta', data=syspar['beta'])

    # Save simulation parameters
    f5.create_dataset('t_delta', data=simpar['t_delta'])
    f5.create_dataset('N', data=simpar['N'])

    # Save initial conditions
    f5.create_dataset('x0', data=xyz0['x0'])
    f5.create_dataset('y0', data=xyz0['y0'])
    f5.create_dataset('z0', data=xyz0['z0'])

    # Save simulation results
    (x, y, z, d) = xyzd
    f5.create_dataset('x', data=xyzd['x'])
    f5.create_dataset('y', data=xyzd['y'])
    f5.create_dataset('z', data=xyzd['z'])
    f5.create_dataset('d', data=xyzd['d'])

    # Close HDF file
    f5.close()


def load_hdf5(familyname):
    """Loads Lorenz simulation data from file <filename>/<filename>.hdf5.

    Args:
        *familyname* (str): High abstraction level name for the simulation
        to be performed. An example could be 'testcase1' or similar.

    Returns:
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
        Nothing.

    Examples:
        >>>

    """
    # Open HDF5 file
    f5name = "{0}/{1}.hdf5".format(familyname, familyname)
    f5 = h5py.File(f5name, 'r')

    # Load data
    syspar = {}
    syspar['sigma'] = float(f5['sigma'][...])
    syspar['rho'] = float(f5['rho'][...])
    syspar['beta'] = float(f5['beta'][...])
    simpar = {}
    simpar['t_delta'] = float(f5['t_delta'][...])
    simpar['N'] = float(f5['N'][...])
    xyz0 = {}
    xyz0['x0'] = float(f5['x0'][...])
    xyz0['y0'] = float(f5['y0'][...])
    xyz0['z0'] = float(f5['z0'][...])
    xyzd = {}
    xyzd['x'] = f5['x'][...]
    xyzd['y'] = f5['y'][...]
    xyzd['z'] = f5['z'][...]
    xyzd['d'] = f5['d'][...]

    # Close HDF file
    f5.close()

    return syspar, simpar, xyz0, xyzd
