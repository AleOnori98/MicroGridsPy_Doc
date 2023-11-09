Download and installation
=========================
.. role:: raw-html(raw)
    :format: html
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

The easiest way to get a working MicroGridsPy installation is to use the free conda package manager, which can install all of the four things described above in a single step. To get conda, download and install the `Anaconda <https://repo.anaconda.com/archive/>`_ distribution for your operating system (using the version for Python 3). Anaconda is a free and open-source distribution of the Python and R programming languages for data science and machine learning-related applications that aims to simplify package management and deployment.  With Anaconda installed, it is possible to create a new environment (e.g. "mgp"). To create a modelling environment that already contains everything needed to run MicrogridsPy it's suggested to download the environment from `here <https://github.com/SESAM-Polimi/MicroGridsPy-SESAM/tree/Environments>`_ . After placing the mgp_win.yml file in "C:\Users\youruser", it is possible to create and activate the new mgp environment by running the following command in the Anaconda Prompt terminal:

.. code-block:: python

   conda env create -f mgp_win.yml
   conda activate mgp

Solvers
=========================
At least one of the solvers supported by Pyomo is required. HiGHS (open-source) or Gurobi (commercial) are recommended for large problems, and have been confirmed to work with MicroGridsPy. Refer to the documentation of your solver on how to install it.

Gurobi
----------------
Gurobi is commercial but significantly faster than CBC and GLPK, which is relevant for larger problems. It needs a license to work, which can be obtained for free for academic use by creating an account on gurobi.com. Gurobi can be installed via conda by means of the following command:

.. code-block:: python

   conda install -c gurobi gurobi

It's recommended to download and install the installer from the Gurobi website, as the conda package has repeatedly shown various issues. After installing, log on to the Gurobi website and obtain a (free academic or paid commercial) license, then activate it on your system via the instructions given online (using the grbgetkey command).

More info at `Gurobi documentation <https://www.gurobi.com/documentation/>`_


HiGHS
----------------
HiGHS is high-performance serial and parallel software for solving large-scale sparse linear programming (LP), mixed-integer programming (MIP) and quadratic programming (QP) models, developed in C++11, with interfaces to C, C#, FORTRAN, Julia and Python.

HiGHS is freely available under the MIT licence and is downloaded from Github. Installing HiGHS from source code requires CMake minimum version 3.15, but no other third-party utilities. HiGHS can be used as a stand-alone executable on Windows, Linux and MacOS. There is a C++11 library which can be used within a C++ project or, via one of the interfaces, to a project written in other languages.

More info at `HiGHS documentation <https://ergo-code.github.io/HiGHS/dev/>`_



