########################################
Building and Running a Model
########################################

.. role:: raw-html(raw)
    :format: html

Building a model
==================

Building a model in MicroGridsPy is very simple and includes the following main steps:

#. Defining the....
#. Delivering the structural inputs (sets) to the model through a number of Excel-based files
#. Delivering the ....


Definition of the model structural inputs 
-------------------------------------------
General introduction and description of the Model data parameters


.. list-table:: Parameters
   :widths: 20 25 50
   :header-rows: 1

   * - **Parameter**
     - **Sheet Name**
     - **Unit**
     - **Description**
   * - Periods
     - Model data
     - Time unit (e.g. hours/year)
     - Periods considered in one year (e.g. 8760 hours/year)
   * - Years
     - Model data
     - years
     - Total duration of the project

  
.. note::
  Please refer to the example gallery for a better understanding of the structure of both the set and parameter files.

Time Series Data
================
General description of the concept

Demand 
-------
**Introduction**

At the core of the optimization energy modelling process lies the load curve demand, a critical input parameter. This chapter aims to explain what load curve demand is, how it is used within MicroGridsPy, how it can be operated or estimated with external software tools like RAMP or within the model itself using the advanced feature of demand estimation integrated into MicroGridsPy.

**What is the load curve demand?**

Load Curve Demand represents the time-dependent electricity consumption of a given area or system. It is typically measured in Watts (or kilowatts, megawatts, etc.) and captures how electricity demand varies over years, usually in hourly or sub-hourly intervals. The Load Curve Demand curve illustrates the power required at each point in time, providing insights into when and how much electricity is needed. This curve serves as a foundational data source for MicroGridsPy since the model aims to size and operate mini-grid components, such as renewable energy sources (e.g., solar panels, wind turbines), energy storage systems (e.g., batteries), and backup generators, to meet the electricity demand of a specific area or community. The key role of Load Curve Demand in the model is optimizing resource allocation: MicroGridsPy uses the load curve demand to distribute available resources efficiently over the years, balancing the generation and storage resources to minimize costs while meeting the electricity demand throughout the day. In addition to optimizing resource allocation, the software can also predict, along the time horizon of the simulation run, when investment steps should be taken to expand the system's capacity to accommodate the projected increase in demand if such an increase is anticipated. 

**Load curve demand estimation**

There are two key methods for operating load curve demand:

*  Using software tools such as `RAMP <https://rampdemand.readthedocs.io/en/stable/intro.html>`_ which is a bottom-up stochastic model for the generation 
   of high-resolution multi-energy profiles, conceived for 
   application in contexts where only rough information about users' behaviour is obtainable. Those may range from remote villages to whole countries as 
   well as informal settlements.
*  Using the advanced features integrated into MicroGridsPy which allows to use built-in archetypes referring to rural villages in Sub-Saharan 
   Africa at different latitudes.



Renewable Energy Sources
-------
General description of the concept

Technology Parameters
================
General description of the concept

Renewables 
-------
General description of the concept

Generator
-------
General description of the concept

Battery bank
-------
General description of the concept

Main grid
-------
General description of the concept

Running a model
================
When the inputs of the model are correctly parsed to the model, you can run the model with specifying a couple of parameters:

.. code-block:: python

  model.run(
    solver = 'solver that you prefer'
  )

If model finds an optimum solution, you can have access to the results through :guilabel:`&results` attribute. For saving the results to your computer, use :guilabel:`&to_csv` function:

.. code-block:: python

  model.to_csv(
    path = 'path/to/directory'
  )

