Download and installation
=====

.. _Requirements:

Requirements
------------

MicroGridsPy has been tested on Linux, macOS, and Windows. Running MicroGridsPy requires:

* The Python programming language, version ....
* A number of Python add-on modules (see below for the complete list).
* A solver: MicroGridsPy has been tested with GLPK, Gurobi, and HiGHS. Any other solver that is compatible with Pyomo should also work.

The MicroGrids software itself.

Recommended installation method
----------------

The easiest way to get a working Calliope installation is to use the free conda package manager, which can install all of the four things described above in a single step. To get conda, download and install the “Miniconda” distribution for your operating system (using the version for Python 3).

With Miniconda installed, you can create a new environment called "mgpy" with all the necessary modules, including the free and open source GLPK solver, by running the following command in a terminal or command-line window.
......

