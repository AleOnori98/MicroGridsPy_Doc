=========================
Model Structure
=========================

The ``Model`` directory forms the core of the MicroGridsPy application for developers. It contains a set of Python modules that together constitute the architecture of the Pyomo optimization model. Each module is specialized to handle different aspects of the optimization process. Below is a concise overview of each file within the ``Model`` folder:

- ``__pycache__``: A directory that holds the bytecode compiled Python files, which are used to speed up module loading. This directory is automatically generated and should not be altered manually.

- ``Constraints.py``: This file defines the constraints of the optimization problem, ensuring that the solutions conform to the predefined logical and mathematical rules.

- ``Demand.py``: Manages the demand simulation advanced features thorugh build-in demand archetypes.

- ``Grid_Availability.py``: This module generates the electrical grid's availability matrix, crucial for planning around periods when the grid is not operational.

- ``Initialize.py``: Prepares the initial settings and variables necessary for the model, setting the stage for the optimization process.

- ``MicroGrids.py``: Acts as the primary script for developers to run the model, invoking the necessary modules and coordinating the execution flow.

- ``Model_Creation.py``: Entrusted with assembling the model instance, defining the structural elements, and populating initial set, parameters and variables.

- ``Model_Resolution.py``: Dedicated to the resolution of the optimization model, it triggers the solver and oversees the entire solution procedure.

- ``Plots.py``: A utility module aimed at creating graphical representations of the model's outputs.

- ``RE_calculation.py``: Calculates the production of renewable energy, downloading and processing the time series data for sources like wind and solar from the NASA POWER project website. 

- ``Results.py``: Manages the formatting and storage of the model's outcomes, preparing them for analysis or reporting purposes.

- ``tmpjvcss8hv.pyomo.lp``: An intermediary file that represents the linear programming formulation of the model, useful for debugging or in-depth examination by developers.

In the forthcoming sections, we will explore in detail the functionalities and significance of each module, offering insights into their contributions to the model's optimization mechanism.



