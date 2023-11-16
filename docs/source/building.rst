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

* + Parameters

       * - Parameters.dat

* + Time Series

       * - Demand.csv
       * - RES Time Series.csv
       * - Grid Availability.csv
       * - Direct Emissions.csv
       * - WT Power Curve.csv

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
   * - Step_Duration
     - years
     - Duration of each investment decision step in which the project lifetime will be split
   * - Min_Last_Step_Duration
     - years
     - Minimum duration of the last investment decision step, in case of non-homogeneous divisions of the project lifetime 
   * - StartDate
     - 'DD/MM/YYYY hh:mm:ss'
     - Start date of the project
   * - Delta_Time
     - hours
     - Time step in hours [fixed input]
   * - Scenarios
     - (-)
     - Number of scenarios to consider within the optimisation
   * - Scenario_Weight
     - (-)
     - Occurrence probability of each scenario
   * - Discount_Rate
     - unit
     - Real discount rate accounting also for inflation
   * - Investment_Cost_Limit
     - (e.g. USD)
     - Upper limit to investment cost (considered only in case Optimization_Goal='Operation cost')


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
     - It allows to switch between an NPC-oriented optimization and a NON-ACTUALIZED Operation
   * - MILP_Formulation
     - 1 = MILP / 0 = LP
     - It allows to switch between a MILP (for monodirectional energy flows) and LP formulation

Technology Parameters
----------------------

**RES Technology**

intro

.. list-table:: 
   :widths: 25 25 50
   :header-rows: 1

   * - Parameter name
     - Unit
     - Description
   * - RES_Sources
     - (-)
     - Number of Renewable Energy Sources (RES) types
   * - RES_Names
     - (e.g. PV panels, Wind turbines)
     - Renewable Energy Sources (RES) names
   * - RES_Nominal_Capacity
     - Power (e.g. W)
     - Single unit capacity of each type of Renewable Energy Source (RES)
   * - RES_Inverter_Efficiency
     - % (0-1)
     - Efficiency of the inverter connected to each Renewable Energy Source (RES) (put 1 in case of AC bus)
   * - RES_Specific_Investment_Cost
     - (e.g. USD/W)
     - Specific investment cost for each type of Renewable Energy Source (RES) 
   * - RES_Specific_OM_Cost
     - % (0-1)
     - O&M cost for each type of Renewable Energy Source (RES) as a fraction of the specific investment cost 
   * - RES_Lifetime
     - years
     - Lifetime of each Renewable Energy Source (RES)   
   * - RES_units
     - (-)
     - Existing RES units of nominal capacity (if Brownfield investment activated)
   * - RES_years
     - years
     - How many years ago the component was installed 
   * - RES_unit_CO2_emission
     - [kgCO2/kW]
     - ???



**Generator Technology**


**Battery Technology**

The input parameters for the Battery Energy Storage System (BESS) include:

.. list-table:: 
   :widths: 25 25 50
   :header-rows: 1

   * - Parameter name
     - Unit
     - Description
   * - Battery_Specific_Investment_Cost
     - (e.g. USD/Wh)
     - Specific investment cost of the battery bank [USD/Wh]            
   * - Battery_Specific_Electronic_Investment_Cost
     - (e.g. USD/Wh)
     - Specific investment cost of non-replaceable parts (electronics) of the battery bank
   * - Battery_Specific_OM_Cost
     - (-)
     - O&M cost of the battery bank as a fraction of the specific investment cost
   * - Battery_Discharge_Battery_Efficiency
     - % (0-1)
     - Discharge efficiency of the battery bank
   * - Battery_Charge_Battery_Efficiency
     - % (0-1)
     - Charge efficiency of the battery bank 
   * - Battery_Depth_of_Discharge
     - % (0-1)
     - Depth of discharge of the battery bank (maximum amount of discharge)
   * - Maximum_Battery_Discharge_Time
     - hours
     - Maximum time to discharge the battery bank
   * - Maximum_Battery_Charge_Time
     - hours
     - Maximum time to charge the battery bank
   * - Battery_Cycles
     - (-)
     - Maximum number of cycles before degradation of the battery
   * - Battery_Initial_SOC
     - % (0-1)
     - Battery initial state of charge
   * - Battery_capacity
     - Energy (e.g. Wh)
     - Existing Battery capacity (if Brownfield investment activated)
   * - BESS_unit_CO2_emission
     - (e.g. kgCO2/kWh)
     - ????
   * - Battery_Nominal_Capacity_Milp
     - Energy (e.g. Wh)
     - Nominal Capacity of each battery



(refer to :doc:`advanced`)

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

At the core of the optimization energy modelling process lies the load curve demand. This section aims to explain what load curve demand is, how it is used within MicroGridsPy, and how it can be operated or estimated with external software tools like RAMP or within the model itself using the advanced feature of demand estimation integrated into MicroGridsPy.

**What is the load curve demand?**

Load Curve Demand represents the **time-dependent electricity consumption** of a given area or system. It is typically measured in *Watts* (or kilowatts, megawatts, etc.) and captures how electricity demand varies over years, usually in hourly or sub-hourly intervals. The Load Curve Demand curve illustrates the power required at each point in time, providing insights into when and how much electricity is needed. This curve serves as a foundational data source for MicroGridsPy since the model aims to size and operate mini-grid components, such as renewable energy sources (e.g., solar panels, wind turbines), energy storage systems (e.g., batteries), and backup generators, to meet the electricity demand of a specific area or community. The key role of Load Curve Demand in the model is **optimizing resource allocation**: MicroGridsPy uses the load curve demand to distribute available resources efficiently over the years, balancing the generation and storage resources to minimize costs while meeting the electricity demand throughout the day. In addition to optimizing resource allocation, the software can also predict, along the time horizon of the simulation run, when **investment steps** should be taken to expand the system's capacity to accommodate the projected increase in demand if such an increase is anticipated. 

**Load curve demand estimation**

There are two key methods for operating load curve demand:

*  Using software tools such as `RAMP <https://rampdemand.readthedocs.io/en/stable/intro.html>`_ which is a bottom-up stochastic model for the generation 
   of high-resolution multi-energy profiles, conceived for application in contexts where only rough information about users' behaviour is obtainable. Those 
   may range from remote villages to whole countries as well as informal settlements.

  .. image:: https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/RAMP.png?raw=true
     :width: 150
     :align: center

*  Using the advanced features integrated into MicroGridsPy which allows to use built-in archetypes referring to rural villages in Sub-Saharan 
   Africa at different latitudes (refer to :doc:`advanced`)

**Demand.csv**
The input file, located in the "Time Series" folder within the "Inputs" folder, must have as many numbered columns (excluding the rows labels) as the total years of the project and as many rows (excluding the columns headers) as the periods in which one year is divided (e.g. 1-hour time resolution leads to 8760 rows). 

.. warning::
    The number of columns in the csv file must coincide with the value set for the 'Years' parameter. The same for the number of rows 
    that must coincide with the value set for 'Periods' in the model configuration.csv file! If not properly set and matched, it may arise a 'Key Error'.



.. image:: https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Demand.png?raw=true
     :width: 700
     :align: center



Renewable Energy Production (Generation)
-------

**Introduction**

Electricity needed to meet the demand can be generated using various energy sources. MicroGridsPy considers renewable sources, such as solar and wind, and backup diesel generators as the choices for generating electricity. This section aims to explain what renewable energy production is, how it is used within MicroGridsPy, how it can be estimated with external available web tools like Renewables.ninja and PVGIS or within the model itself using the advanced feature of renewable energy production estimation integrated into MicroGridsPy.

**What is the renewable energy production?**

The renewable energy production represents the estimated electricity production for each unitary generation technology at a given time for a specific location. It is typically measured in *Watts* (or kilowatts, megawatts, etc.) and captures how electricity production varies over time and source, usually in hourly or sub-hourly intervals. The data can be computed into a generation curve which illustrates the produced power at each point in time. This data becomes a fundamental source for MicroGridsPy to size and operate mini-grid components, such as renewable energy sources (e.g., solar panels, wind turbines) based on the unitary production of each source and complement the system with energy storage systems (e.g., batteries), and backup generators, to ensure the necessary electricity of a specific area or community. 

**Renewable Energy Production estimation**

There are two key methods to estimate renewable production:

*  Using web tools such as: 
** Renewables.ninja which provides data and tools for assessing energy generation profiles with simulations and forecasting features. The electricity production is estimated for solar and wind sources and is computed for 1 year with 1-hour time resolution. To cover more years, more requests need to be performed for the same location.

** PVGIS
PVGIS (Photovoltaic Geographical Information System) provides solar radiation data, PV system yield estimations, and solar maps for various regions. It provides data for the typical meteorological conditions over a single year with 1-hour time resolution for a specific location.  

*  Using the advanced features integrated into MicroGridsPy which allows to estimating generation based on VRES parameters, project location, and the specific year in question. The necessary data for solar, wind, and temperature conditions is obtained from the NASA POWER platform through an Application Program Interface (API) integrated into the MGPy software. These data are used to create a Typical Meteorological Year (TMY) dataset, representing typical weather conditions for the project location, with hourly resolution, based on 20 years of historical data. This TMY dataset is then used to calculate energy generation, which is consistent across all project years.
(refer to :doc:`advanced`)

**Generation.csv**
The input file, located in the "Time Series" folder within the "Inputs" folder, must have as many numbered columns (excluding the rows labels) as the total years of the project and as many rows (excluding the columns headers) as the periods in which one year is divided (e.g. 1-hour time resolution leads to 8760 rows). 






