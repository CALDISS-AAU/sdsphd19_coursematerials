
import shutil
from . import hdf5

from . import solver
from . import plot


def run_master(syspar, simpar, xyz0, familyname, save_and_plot=True):
    """Controls the execution of the simulation and data storage.

    This function controls the entire simulation process. The procedure
    is: 1) it first ensures a clean directory for storing plots and data;
    2) the simulation is performed which provides
    :math:`(\mathbf{x},\mathbf{y},\mathbf{z},\mathbf{d}`; 3) data is
    saved in a HDF5 file; 4) 2D- and 3D-plots are made and saved in the
    results directory.

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

        *familyname* (str): High abstraction level name for the simulation
        to be performed. An example could be 'testcase1' or similar.

    Returns:
        Nothing is returned but system and simulation variables are
        stored as well as the results of the simulation.

    Raises:
        Nothing by itself but the inidividual functions called provide
        parameter checks and raise errors when necessary.

    Examples:
        None.

    """

    # Clean any existing directory and make new
    shutil.rmtree('./{0}'.format(familyname), ignore_errors=True)
    shutil.os.mkdir('./{0}'.format(familyname))

    # Solve the Lorenz problem
    xyzd = solver.ode_solver(syspar, simpar, xyz0)

    if save_and_plot:
        # Save data
        hdf5.save_hdf5(syspar, simpar, xyz0, xyzd, familyname)

        # Make plots
        labels = {'abscissa': 'x', 'ordinate': 'y'}
        plot.plot_2d(xyzd['x'], xyzd['y'], labels, familyname)
        
        labels = {'abscissa': 'x', 'ordinate': 'z'}
        plot.plot_2d(xyzd['x'], xyzd['z'], labels, familyname)
        
        labels = {'abscissa': 'y', 'ordinate': 'z'}
        plot.plot_2d(xyzd['y'], xyzd['z'], labels, familyname)

        plot.plot_3d(xyzd, familyname)

    return xyzd
