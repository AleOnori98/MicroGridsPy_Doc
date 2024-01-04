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

Model Creation Module
=====================

The ``Model_Creation`` module is where the MicroGridsPy's model components are defined and structured. It lays down the framework of parameters, sets, and variables, which are crucial for the optimization process.

Parameters
----------

The module begins by importing necessary Pyomo classes and initialization functions from an external ``Initialize.py`` module:

.. code-block:: python

    from pyomo.environ import Param, RangeSet, Any, NonNegativeReals, NonNegativeIntegers, Var, Set, Reals, Binary
    from Initialize import *

The ``Model_Creation`` function then initializes a series of parameters. Parameters in Pyomo are symbolic representations of values that define the characteristics of the optimization model. They can be mutable or immutable and can be indexed to represent arrays of parameters.

.. code-block:: python

    def Model_Creation(model):
        #%% PARAMETERS
        ############## 

        # RES Time Series Estimation parameters
        model.base_URL= Param(within=Any)
        model.loc_id = Param(within=Any)
        # ...
        # Several other parameters follow here

        # Project parameters
        model.Periods = Param(within=NonNegativeIntegers)
        # ...
        # Additional project parameters follow

Sets
----

After defining parameters, the module creates several sets. Sets are collections of objects, often numbers or strings, that index the model's variables and constraints. For instance, the `periods` set ranges from 1 to the number of periods in each year:

.. code-block:: python

    #%% Sets
    #########

    model.periods = RangeSet(1, model.Periods)
    # ... additional sets follow

Variables
---------

Variables represent the decision variables of the optimization problem. In this module, variables are defined for each component of the energy system, such as the units of renewable energy sources (RES), the energy production from RES, the state of charge (SOC) for batteries, and the energy produced by diesel generators.

.. code-block:: python

    #%% VARIABLES
    #############

    # Variables associated with the RES
    model.RES_Units = Var(model.steps, model.renewable_sources, within=NonNegativeReals)
    # ... additional variables follow

Example Usage
-------------

Here's an example of how a developer might utilize this module to set up an optimization model for a mini-grid:

.. code-block:: python

    from pyomo.environ import ConcreteModel
    from Model_Creation import Model_Creation

    # Create a Pyomo model instance
    model = ConcreteModel()

    # Call the Model_Creation function to set up the model
    Model_Creation(model)

    # The model is now ready to be populated with data and solved.


The ``Model_Creation`` encapsulates the essence of the system being modeled, from the estimation of renewable energy production and demand to the detailed configurations of the project itself.

By structuring the model in this way, MicroGridsPy ensures that the optimization framework is robust, extendable, and maintainable. It also encapsulates complex optimization features like multi-objective optimization and MILP formulations, making it a powerful tool for energy system optimization.



