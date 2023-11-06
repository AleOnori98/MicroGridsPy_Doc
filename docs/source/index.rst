Welcome to MicroGridsPy's documentation!
===================================

**MicroGridsPy** is a bottom-up, open-source optimization model, running on Pyomo, a Python library used to model optimisation problems, whose primary goal is to offer an open-source approach to the issue of energy scaling and dispatch in mini-grids in remote locations. It was first developed in 2016 by the University of Liege and the code is freely available on GitHub. The model enables the optimization of micro-grid size and its dispatch strategy at the 1-hour temporal resolution, also returning as output the fixed and variable costs associated with each technology and the LCOE of the system. It is based on Linear Programming, and it enables the choice of the installed capacities of batteries, generators, and renewable energy sources that result in the lowest Net Present Cost (NPC) or lowest Operation and Maintenance expenses (O&M) during the project's lifespan while achieving the system limitations. However, in the latest version, it is also possible to consider a multi-objective optimization such as costs and emissions to model different scenarios with different drivers like environmental impact and not only economic parameters. 
The main inputs required by the tool to initialize the variables and formulate linear constraints, as shown in the figure below, are time series of load demand at 1-hour resolution for one year (or more years); time series of RES production at 1-hour resolution for one year; techno-economic parameters of the technologies and project parameters. In this context, it must be said that in the latest version of MicroGridsPy already structured load demand archetypes referring to rural villages in Sub-Saharan Africa at different latitudes are integrated into the model, from which the code directly derives the time series of load profile.  Moreover, an endogenous calculation of RES production times series, solar and wind, relying on the NASA POWER platform is now possible. In the most recent version, there is also the possibility of simulating the connection of the mini-grid with an existing main grid by detailing electricity flows in both directions (electricity taken from the grid or fed into the grid), as well as the availability of the national grid in the event of blackouts. 
 
Check out the :doc:`usage` section for further information, including
how to :ref:`installation` the project.

.. note::

   This project is under active development.

Contents
--------

.. toctree::

   intro
   usage
   formulation
   building
   contributors
   api
