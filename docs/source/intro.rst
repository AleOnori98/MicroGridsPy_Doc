
.. image:: https://raw.githubusercontent.com/SESAM-Polimi/MARIO/767d2c0e9e42ae0b6acf7c3a1cc379d7bcd367fa/doc/source/_static/images/polimi.svg
   :width: 200
   :align: right
   
#######################################
Introduction
#######################################


Energy Optimization Models
=========================================

In rural regions where access to the main power grid is limited and the cost of bringing electricity to each individual can be prohibitively high, it's crucial to use available resources wisely. This means that when planning for rural electrification, one must consider several factors that impact the effectiveness and efficiency of the project. Key considerations include determining the appropriate size and configuration of the system to meet local needs, strategizing the dispatch of electricity to maintain efficiency and reliability, selecting suitable energy generation and storage technologies based on local resources, costs, and technical capabilities, and designing a robust and sustainable network for electricity transmission and distribution. To address these challenges, accurate models for sizing and dispatching mini-grid systems are indispensable. There are three main types of energy optimization methods used for this purpose: intuitive, numerical, and analytical.

* The **intuitive method** is the simplest approach. It calculates the necessary system size using daily electricity demand values and data on available 
  resources. This method is straightforward but may not be as precise as other methods.

* The **numerical method** is more complex. It sizes the system based on hourly demand profiles, energy generation profiles, and specific system parameters. 
  This approach allows for a more nuanced understanding of how the system will operate throughout the day.

* The **analytical method** is the most sophisticated and relies on mathematical optimization techniques such as Linear Programming (LP) or Mixed Integer 
  Linear Programming (MILP). These mathematical models can incorporate a wide range of considerations, including cost, system reliability, and the 
  integration of sustainable technologies. They also have the capacity to take into account various economic, social, and environmental constraints, 
  ensuring that the deployment of the mini-grid system is as effective and sustainable as possible.

Why MicroGridsPy is developed?
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

MicroGridsPy in academic literature
=========================================

Sergio Balderrama, Francesco Lombardi, Fabio Riva, Walter Canedo, Emanuela Colombo, Sylvain Quoilin, A two-stage linear programming optimization framework for isolated hybrid microgrids in a rural context: The case study of the “El Espino” community, Energy **2019**, 188, 116073

Nicolò Stevanato, Francesco Lombardi, Emanuela Colombo, Sergio Balderrama, Sylvain Quoilin, Two-Stage Stochastic Sizing of a Rural Micro-Grid Based on Stochastic Load Generation, **2019** IEEE Milan PowerTech, pp. 1-6

Nicolò Stevanato, Francesco Lombardi, Giulia Guidicini, Lorenzo Rinaldi, Sergio L. Balderrama, Matija Pavičević, Sylvain Quoilin, Emanuela Colombo, Long-term sizing of rural microgrids: Accounting for load evolution through multi-step investment plan and stochastic optimization, Energy for Sustainable Development **2020**, 58, pp. 16-29

Nicolò Stevanato, Gianluca Pellecchia, Ivan Sangiorgio, Diana Shendrikova, Castro Antonio Soares, Riccardo Mereu, Emanuela Colombo, Planning third generation minigrids: Multi-objective optimization and brownfield investment approaches in modelling village-scale on-grid and off-grid energy systems, Renewable and Sustainable Energy Transition **2023**, 3, 100053

Giacomo Crevani, Castro Soares, Emanuela Colombo, Modelling Financing Schemes for Energy System Planning: A Mini-Grid Case Study, ECOS **2023**, pp. 1958-1969 


References
=========================================
.. [1] .... 


