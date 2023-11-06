
.. image:: https://raw.githubusercontent.com/SESAM-Polimi/MARIO/767d2c0e9e42ae0b6acf7c3a1cc379d7bcd367fa/doc/source/_static/images/polimi.svg
   :width: 200
   :align: right
   
#######################################
Introduction
#######################################
What is MicroGridsPy
=========================================
MicroGridsPy is a bottom-up, open-source optimization model, running on `Pyomo <https://pyomo.readthedocs.io/en/stable/>`_, a Python library used to model optimisation problems, whose primary goal is to offer an open-source approach to the issue of energy scaling and dispatch in mini-grids in remote locations. It was first developed in 2016 by the University of Liege and the code is freely available on GitHub. The model enables the optimization of micro-grid size and its dispatch strategy at the 1-hour temporal resolution, also returning as output the fixed and variable costs associated with each technology and the LCOE of the system. It is based on Linear Programming, and it enables the choice of the installed capacities of batteries, generators, and renewable energy sources that result in the lowest Net Present Cost (NPC) or lowest Operation and Maintenance expenses (O&M) during the project's lifespan while achieving the system limitations. However, in the latest version, it is also possible to consider a multi-objective optimization such as costs and emissions to model different scenarios with different drivers like environmental impact and not only economic parameters. The main inputs required by the tool to initialize the variables and formulate linear constraints, as shown in the figure below, are time series of load demand at 1-hour resolution for one year (or more years); time series of RES production at 1-hour resolution for one year; techno-economic parameters of the technologies and project parameters. In this context, it must be said that in the latest version of MicroGridsPy already structured load demand archetypes referring to rural villages in Sub-Saharan Africa at different latitudes are integrated into the model, from which the code directly derives the time series of load profile. Moreover, an endogenous calculation of RES production times series, solar and wind, relying on the NASA POWER platform is now possible. In the most recent version, there is also the possibility of simulating the connection of the mini-grid with an existing main grid by detailing electricity flows in both directions (electricity taken from the grid or fed into the grid), as well as the availability of the national grid in the event of blackouts.

Why it is developed
=========================================
MicroGridsPy is inspired by the other existing energy system optimization models 
particularly ..... [1]
It is designed to .... by addressing the main 
challenges of ....

* **Electricity Access in rural areas** With the aim of ....



Acknowledgement
=========================================

* The development of MicroGridsPy was not possible without the kind attention and help of Professor
  `Emanuela Colombo <https://www4.ceda.polimi.it/manifesti/manifesti/controller/ricerche/RicercaPerDocentiPublic.do?EVN_DIDATTICA=evento&k_doc=44891&lang=EN&aa=2014&tab_ricerca=1>`_.
  We are fully grateful for having the chance to work under her supervision and would like to express our gratitude for her unwavering support.

* We would also like to acknowledge .... for his kind support and guide that allows us to better understand and use .....
    
License
========

.. image:: https://img.shields.io/badge/License-Apache_2.0-blue.svg
    :target: https://www.apache.org/licenses/


This work is licensed under `Apache 2.0 <https://www.apache.org/licenses/>`_

References
=========================================
.. [1] .... 


