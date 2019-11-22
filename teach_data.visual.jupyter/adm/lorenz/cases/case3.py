
# Update path to allow "import lorenz""
import sys
sys.path.insert(0, '../')

import lorenz

# System and simulation parameters
syspar = {'sigma': 10.0, 'rho': 28, 'beta': 8.0/3.0}
simpar = {'t_delta': 0.01, 'N': 10000}
xyz0 = {'x0': 0.1, 'y0': 0.1, 'z0': 0.1}

# Perform simulations
familyname = sys.argv[0].rsplit('.py')[0]
lorenz.run.run_master(syspar, simpar, xyz0, familyname)

