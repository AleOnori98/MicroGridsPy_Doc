
=======================================
MicroGridsPy's Documentation
=======================================

**MicroGridsPy** is a bottom-up, open-source optimization model, running on `Pyomo <https://pyomo.readthedocs.io/en/stable/>`_ , a Python library used to model optimisation problems, whose primary goal is to offer an open-source approach to the issue of *energy scaling and dispatch* in mini-grids in remote locations. It was first developed in 2016 by the University of Liege and the code is freely available on `GitHub <https://github.com/SESAM-Polimi/MicroGridsPy-SESAM/tree/Development_MILP>`_  . The model enables the **optimization of micro-grid size** and its **dispatch strategy** at the *1-hour temporal resolution*, also returning as output the fixed and variable costs associated with each technology and the LCOE of the system. It is based on **Linear Programming**, and it enables the choice of the installed capacities of batteries, generators, and renewable energy sources that result in the lowest **Net Present Cost (NPC)** or lowest **Operation and Maintenance expenses (O&M)** during the project's lifespan while achieving the system limitations. 



.. figure:: https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Mgpy_Scheme.png?raw=true
   :width: 500
   :align: center

   Visualization of the model conceptual structure



The main inputs required by the tool to initialize the variables and formulate linear constraints are **time series of load demand** at 1-hour resolution for one year (or more years); **time series of RES production** at 1-hour resolution for one year; **techno-economic parameters** of the technologies and project parameters. 
The approach of the model focuses on addressing the issue of load evolution in the long term. This model is designed to make informed decisions about expanding capacity throughout the specified time horizon. To simulate realistic load profiles, the model is integrated with a tool for generating stochastic load profiles. This formulation demonstrates advantages in making robust investment decisions under different load evolution scenarios.

In the latest version of MicroGridsPy the following advanced features (:doc:`advanced`) have been implemented:

* **Multi-Year Formulation**: The system has the capability to take into account changes in energy demand over time (Multi-Year formulation). Each year in the planning period corresponds to a unique load curve, allowing for the analysis of various patterns. This includes factors like population growth, more connections to the network, which affect overall demand but not necessarily daily load profiles. Additionally, variations in consumption habits and the use of new appliances can cause shifts in the daily load curve. In essence, the model is flexible enough to adapt to different dynamics, considering both global demand changes and shifts in daily energy usage patterns.
* **Capacity Expansion**: the model can consider the possibility to expand capacity during the time horizon of the project. This allows for strategic planning of infrastructure enhancements and investments, ensuring that the system can meet rising demand effectively. Capacity expansion could include the addition of new generation facilities, upgrading existing ones, or incorporating renewable energy sources. These adaptations not only meet the growing demand but also can lead to improved efficiency, reduced emissions, and enhanced reliability of the energy supply. By anticipating future needs and planning for capacity expansion, the model aids in making informed, cost-effective decisions that align with long-term energy goals and sustainability objectives. 
* **Multi-objective Optimization** such as costs and emissions to model different scenarios with different drivers like environmental impact
* **Mixed-Integer Linear Programming (MILP) formulation** with an integrated *unit commitment approach* to determine the optimal operating schedule of power generation units over a given time horizon to meet the electricity demand while minimizing operational costs. The MILP formulation offers the chance to keep the main advantages of LP whilst offering a satisfying approximation of *non-linear behaviour*, at the expense of a *lower computational efficiency*. Nonetheless, an accurate MILP characterization of components such as diesel generators requires high-quality data regarding their real-life and site-specific operation, preferably based on real measurements. 
* Modeling of the **Generator Partial Load Effect**;
* **Endogenous Load Curve Estimation** based on structured *archetypes* referring to **rural villages in Sub-Saharan Africa** at different latitudes;
* **Endogenous calculation of RES production times series**, solar and wind, relying on the `NASA POWER platform <https://power.larc.nasa.gov/api/temporal/>`_;
* **Brownfield** feature which allows to perform the optimization of the microgrid taking into consideration the availability of technologies previously 
  installed in the field;
* Possibility of simulating the connection of the mini-grid with an **existing main grid** by detailing electricity flows in both directions (electricity 
  taken from the grid or fed into the grid), as well as the **availability of the national grid** in the event of blackouts. 

MicroGridsPy is developed in the open on `GitHub <https://github.com/SESAM-Polimi/MicroGridsPy-SESAM>`_ and contributions are very welcome: check out the :doc:`formulation`

.. note::

   This project is under active development.

Table of Contents
-------------------

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   intro
   installation
   building
   running
   advanced
   example

.. toctree::
   :maxdepth: 2
   :caption: Developers Guide

   folder
   model_structure
   formulation
   model_results
   troubleshooting
   API

