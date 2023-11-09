########################################
Building and Running a Model
########################################

.. role:: raw-html(raw)
    :format: html


Building a model in MicroGridsPy is very simple and includes the following main steps:

#. Defining the....
#. Delivering the structural inputs (sets) to the model through a number of Excel-based files
#. Delivering the ....

.. image:: https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Mgpy_Simple_Scheme.png?raw=true
   :width: 400
   :align: center

Terminology
===========
The terminology defined here is used throughout the documentation and the model code and configuration files:

* Periods: 

As more generally in constrained optimisation, the following terms are also used:

* Parameter: a fixed coefficient that enters into model equations
* Variable: a variable coefficient (decision variable) that enters into model equations
* Set: an index in the algebraic formulation of the equations
* Constraint: an equality or inequality expression that constrains one or several variables
* ........

Inputs File
======================
MicroGridsPy models are defined, mainly, through PY files, which are both human-readable and computer-readable, and CSV files (a simple tabular format) for time series data and inputs.

All the input files are collected inside a single directory called 'Inputs'. The layout of that directory typically looks roughly like this (+ denotes directories, - files):

* +Parameters

       * -Model Configuration.csv
       * -Model Switches.csv
       * -RES Estimation Parameters.csv
       * -Demand Estimation Parameters.csv
       * -RES Technology.csv
       * -Generator Technology.csv
       * -Battery Technology.csv
       * -Grid Technology.csv
       * -Plot settings.csv

* +Time Series

       * -Demand.csv
       * -Generation.csv

Model Configuration
-------------------------
Intro

**Model Configuration**

Intro

.. list-table:: 
   :widths: 25 25 50
   :header-rows: 1

   * - Parameter name
     - Unit
     - Description
   * - Periods
     - Time unit (e.g. hours/year)
     - Periods considered in one year (e.g. 8760 hours/year)
   * - Years
     - years
     - Total duration of the project (or 'time horizon')

**Model Switches**

Intro

.. list-table:: 
   :widths: 25 25 50
   :header-rows: 1

   * - Parameter name
     - Options
     - Description
   * - Optimization_Goal
     - 1 = NPC / 0 = Operation cost
     - It allows to switch between a NPC-oriented optimization and a NON-ACTUALIZED Operation
   * - MILP_Formulation
     - 1 = MILP / 0 = LP
     - It allows to swtich between a MILP (for monodirectional energy flows) and LP formulation

Technology Parameters
----------------------

**RES Technology**


**Generator Technology**


**Battery Technology**


**Grid Technology**

Plot settings
--------------


  
.. note::
  Please refer to the example gallery for a better understanding of the structure of both the set and parameter files.

Time Series Data
===============
General description of the concept

Demand 
-------
**Introduction**

At the core of the optimization energy modelling process lies the load curve demand. This section aims to explain what load curve demand is, how it is used within MicroGridsPy, how it can be operated or estimated with external software tools like RAMP or within the model itself using the advanced feature of demand estimation integrated into MicroGridsPy.

**What is the load curve demand?**

Load Curve Demand represents the **time-dependent electricity consumption** of a given area or system. It is typically measured in *Watts* (or kilowatts, megawatts, etc.) and captures how electricity demand varies over years, usually in hourly or sub-hourly intervals. The Load Curve Demand curve illustrates the power required at each point in time, providing insights into when and how much electricity is needed. This curve serves as a foundational data source for MicroGridsPy since the model aims to size and operate mini-grid components, such as renewable energy sources (e.g., solar panels, wind turbines), energy storage systems (e.g., batteries), and backup generators, to meet the electricity demand of a specific area or community. The key role of Load Curve Demand in the model is **optimizing resource allocation**: MicroGridsPy uses the load curve demand to distribute available resources efficiently over the years, balancing the generation and storage resources to minimize costs while meeting the electricity demand throughout the day. In addition to optimizing resource allocation, the software can also predict, along the time horizon of the simulation run, when **investment steps** should be taken to expand the system's capacity to accommodate the projected increase in demand if such an increase is anticipated. 

**Load curve demand estimation**

There are two key methods for operating load curve demand:

*  Using software tools such as `RAMP <https://rampdemand.readthedocs.io/en/stable/intro.html>`_ which is a bottom-up stochastic model for the generation 
   of high-resolution multi-energy profiles, conceived for application in contexts where only rough information about users' behaviour is obtainable. Those 
   may range from remote villages to whole countries as well as informal settlements.

  .. image:: https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/RAMP.png?raw=true
     :width: 400
     :align: center

*  Using the advanced features integrated into MicroGridsPy which allows to use built-in archetypes referring to rural villages in Sub-Saharan 
   Africa at different latitudes.


Renewable Energy Sources
-------
Text


Running a model
================
When the inputs of the model are correctly parsed to the model, you can run the model with specifying a couple of parameters:

.. code-block:: python

  model.run(
    solver = 'solver that you prefer'
  )

If model finds an optimum solution, you can have access to the results through :guilabel:`&results` attribute.



