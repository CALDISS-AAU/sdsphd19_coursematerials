
import numpy as np
import os
import matplotlib as mpl
mpl.rcParams['backend'] = 'Agg'
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_2d(abscissa, ordinate, labels, familyname):
    """Plots a 2D-plane of the Lorenz attractor.

    Args:
        *abscissa* (numpy.ndarray): Array used for the abscissa axis,
        which can be :math:`\mathbf{x}` or :math:`\mathbf{y}`.

        *ordinate* (numpy.ndarray): Array used for the ordinate axis,
        which can be :math:`\mathbf{y}` or :math:`\mathbf{z}`.

        *labels* (dict): Labels for the 2D-plot. The dictionary is
        composed as either of {'x': x, 'y': y}, {'x': x, 'z': z}
        and {'y': y, 'z': z}.

        *familyname* (str): High abstraction level name for the simulation
        to be performed. An example could be 'testcase1' or similar.

    Returns:
        Nothing. But a pdf is saved in the directory 'filename'.

    Raises:
        ValueError.

    Examples:
        Examples as part of the :py:mod:`lorenz.run` module.

    """
    # Check that folder familyname exists
    if not os.path.isdir(familyname):
        raise ValueError('{0} is not a directory.'.format(familyname))

    plane = '{0}{1}'.format(labels['abscissa'], labels['ordinate'])

    # Function to make color and b/w plots
    def _local_plot(plottype):
        if plottype == 'col':
            lines = {'xy': 'r-', 'xz': 'b-', 'yz': 'g-'}
        else:
            lines = {'xy': 'k-', 'xz': 'k--', 'yz': '0.7'}

        # Plot and save result
        plt.figure(1, (9.0, 5.0))
        plt.clf()
        plt.plot(abscissa, ordinate, lines[plane], linewidth=1.1)

        plt.xlabel(r'{0}'.format(labels['abscissa']))
        plt.ylabel(r'{0}'.format(labels['ordinate']))
        plt.title(r'{0}-plane'.format(plane))
        plt.grid(True)
        pFname = '{0}/{1}_{2}.pdf'.format(familyname, plane, plottype)
        plt.savefig(pFname, dpi=2400,
                    bbox_inches='tight', pad_inches=0.05)
        plt.close()

    # Make color and b/w plots
    _local_plot('col')
    _local_plot('bw')


def plot_3d(xyzd, familyname):
    """Plots the 3D-trajectory of the Lorenz attractor.

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

        *familyname* (str): High abstraction level name for the simulation
        to be performed. An example could be 'testcase1' or similar.

    Returns:
        Nothing. But a pdf is saved in the directory 'filename'.

    Raises:
        ValueError.

    Examples:
        Tested as part of the :py:mod:`lorenz.run` module.

    """
    # Check that folder familyname exists
    if not os.path.isdir(familyname):
        raise ValueError('{0} is not a directory.'.format(familyname))

    # Make plot
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(xyzd['x'], xyzd['y'], xyzd['z'])
    ax.set_xlabel(r'$x$-axis')
    ax.set_ylabel(r'$y$-axis')
    ax.set_zlabel(r'$z$-axis')
    ax.set_title("Lorenz attractor")
    pFname = '{0}/xyz_{1}.pdf'.format(familyname, 'col')
    plt.savefig(pFname, dpi=2400,
                bbox_inches='tight', pad_inches=0.05)
    plt.close()
