"""
Script to automatically launch all doctests from working directory and below
(in sub-directories). All files with ".py" and ".dt" extensions are found and
are used as argument to the doctest command doctest.testfile(). When writing
the doctests it must be remembered that each doctest containing file must
import the function being tested. As as example we have a file named "test.py"
in the directory "cold" located in the root of the installation (in the same
folder as the master file "run_full_doctest.py") - we wish to test the
function "wild". In this case we must ensure the following line
'>>> from cold.test import wild' is present before any doctest.

It is recommended to only include examples (thus doctests) in the ".py" file
which makes sense to demonstrate the capabilities of that given function. If a
more comprehensive test is desired besides that it is better placed in a file
of the same name but with extension ".dt" (for "DocTest"). If a test should
appear in both files it does not hurt as such - it is obviously not necessary
but it does not give any problems.

The script is executed as:

    $ python run_full_doctest      # quiet test if all is ok
    $ python run_full_doctest -v   # to print all intermediate results

Author:
    Torben Larsen, Aalborg University, Denmark.
Version:
    0.0.1 | 20-APR-2014 : * Initial version.
    0.0.2 | 08-MAY-2014 : * Introduced omit_files tuple including files not to
                            be included in the test.
License:
    BSD 2-Clause
    
"""

import os
import doctest

# Files not included in the test
omit_files = ('run_full_doctest.py', 'run_single_doctest.py', '__init__.py')

# Perform test
path = '.'
print('{0}'.format(78*'='))
for (dirpath, dirnames, filenames) in os.walk(path):
    for filename in filenames:
        # Extract filename extension
        ext_name = os.path.splitext(filename)[1][1:].strip().lower()

        # Perform doctest for all relevant .py and .dt files
        go = filename not in omit_files
        if ext_name in ('py', 'dt') and go:
            full_filename = os.sep.join([dirpath, filename])
            #disp_str = "File under doctest:   {0}".format(filename)
            #print("{0}\n{1}".format(disp_str, len(disp_str)*'-'))
            disp_str = "File under doctest:   {0}".format(filename)
            print("{0}\n".format(disp_str))
            doctest.testfile(full_filename)
            print('{0}'.format(78*'='))
