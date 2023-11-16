########################################
Building and Running a Model
########################################

.. role:: raw-html(raw)
    :format: HTML

MicroGridsPy is a comprehensive energy optimization model designed for the strategic planning and operational management of mini-grid systems. Here below is a general introduction to the different steps in building and running a model:

#. **Time Series Data Input**: Begin by providing specific data, over the lifetime of the project, about the available renewable resources and demand 
   profiles. For sub-Sahara Africa it is also possible to estimate endogenously these time series data based on editable parameters and build-in load 
   demand archetypes

#. **Configuration and Optimization setup**: Set the model's general parameters, such as the number of periods (e.g., 8760 for hourly analysis) and the 
   the total duration of the project, specific features and modes such as MILP formulation, Multi-Objective optimization, Grid connection etc. as well as 
   specific model's optimization goals and constraints, such as aiming for a minimum renewable penetration or a certain level of battery independence.

#. **Component Selection**: Choose the technologies to include, like PV panels or wind turbines of a specific model, and define their capacities and 
   operational characteristics.


#. **Execution**: Run the model to perform the optimization. MicroGridsPy processes the inputs through its algorithms to find the most cost-effective and 
   efficient system setup.

#. **Output Analysis**: Review the outputs, which include the sizing of system components, financial analyses like NPC and LCOE, and dispatch plots. 


.. image:: https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Mgpy_Simple_Scheme.png?raw=true
   :width: 500
   :align: center


.. |nbsp| unicode:: 0xA0 
   :trim:

|nbsp|

Terminology
===========
The general terminology defined here is used throughout the documentation and the model code and configuration files:

* **Periods**: *units of time* for which the model performs calculations, defining the *temporal resolution* of the model. For example, if 'Periods' is 
  set to 8760, which corresponds to the number of hours in a year, implies that the model calculates energy generation, consumption, and other factors on 
  an hourly basis. Having a high temporal resolution (many periods) allows for a more detailed and accurate simulation of the mini-grid's performance, 
  which is critical for designing an efficient and reliable system. However, more periods also mean more data to process and potentially longer computation 
  times, so there's a trade-off between model detail and computational efficiency.
* **Investment Step**:......
* **Scenario**: 

As more generally in constrained optimisation, the following terms are also used:

* Parameter: a fixed coefficient that enters into model equations
* Variable: a variable coefficient (decision variable) that enters into model equations
* Set: an index in the algebraic formulation of the equations
* Constraint: an equality or inequality expression that constrains one or several variables
* ........

Inputs File
======================
MicroGridsPy models are defined, mainly, through .py files, which are both human-readable and computer-readable, .csv files (simple tabular format) for time series and .dat files for data inputs. All the input files are collected inside a single directory called 'Inputs'. The layout of that directory typically looks roughly like this (> denotes directories, - files):

* >Parameters

       * -Parameters.dat

* >Time Series

       * -Demand.csv
       * -RES Time Series.csv
       * -Grid Availability.csv
       * -Direct Emissions.csv
       * -WT Power Curve.csv


Model Configuration
-------------------------
These settings determine the overall configuration of the optimization model, including the number of periods within a year, the project's total duration, and the time step for the optimization process. It also encompasses financial parameters like the discount rate and investment cost limits.

.. raw:: html

    <div style="overflow-y: auto; height: 350px;">

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
   * - Renewable_Penetration
     - [%]
     - Minimum renewable penetration (fraction of electricity produced by renewable sources) in the final technology mix
   * - Battery_Independence
     - days
     - Number of days of battery independence (working without backup choices)
   * - Lost_Load_Fraction
     - [%]
     - Maximum admittable loss of load
   * - Lost_Load_Specific_Cost
     - [USD/Wh]
     - Value of the unmet load 

.. raw:: html

    </div>

.. |nbsp| unicode:: 0xA0 
   :trim:

|nbsp|

**Model Switches**

This set of parameters allows users to toggle different aspects and features of the model, such as the optimization goal (NPC or operation cost), whether to use a MILP formulation and various operational considerations like partial load effects on generators and multi-objective optimization criteria.

.. raw:: html

    <div style="overflow-y: auto; height: 350px;"> 

.. list-table:: 
   :widths: 25 25 50
   :header-rows: 1

   * - Parameter name
     - Options
     - Description
   * - Optimization_Goal
     - 1 = NPC / 0 = Operation cost
     - It allows to switch between an NPC-oriented optimization and a NON-ACTUALIZED Operation
   * - Multiobjective_Optimization
     - 1 = optimization of NPC/operation cost and CO2 emissions / 0 = optimization of NPC/operation cost
     - It allows to switch between a costs-oriented optimization and a cost and emissions optimization
   * - Plot_Max_Cost
     - 1 = Pareto curve has to include the point at maxNPC/maxOperationCost / 0 = otherwise
     - It allows to shows a specific point on the Pareto curve for multi-objective optimization
   * - MILP_Formulation
     - 1 = MILP / 0 = LP
     - It allows to switch between a MILP (for monodirectional energy flows) and LP formulation
   * - Generator_Partial_Load
     - 1 = Partial load effect / 0 = Constant efficiency
     - It allows to activate the partial load effect on the operation costs of the generator (valid only if MILP Formulation is activated)
   * - RE_Supply_Calculation
     - 1 = Endogenous estimation / 0 = exogenous time series required
     - It allows to select solar PV and wind production time series calculation (using NASA POWER data)
   * - Demand_Profile_Generation
     - 1 = Endogenous estimation / 0 = exogenous time series required
     - It allows to select load demand profile generation (using demand archetypes)
   * - Grid_Connection
     - 1 = Grid connection / 0 = No grid connection
     - It allows to select grid connection during project lifetime
   * - Grid_Availability_Simulation
     - 1 = Endogenous simulation / 0 = exogenous time series required
     - It allows to simulate the grid availability matrix
   * - Grid_Connection_Type
     - 2 = sell/purchase / 0 = purchase only
     - It allows to switch between two different types of grid connections
   * - WACC_Calculation
     - 1 = WACC calculation / 0 = Standard discount rate
     - It allows to calculate and use the Weighted Average Cost of Capital rather than the real discount rate
   * - Model_Components
     - 0 = batteries and generators /1 = batteries only / 2 = generators only
     - It allows to switch between different configuration of technologies (RES are always included)

.. raw:: html

    </div>

.. |nbsp| unicode:: 0xA0 
   :trim:

|nbsp|

(refer to :doc:`advanced`)

Technology Parameters
----------------------

**RES Technology**

Defines the types and characteristics of renewable energy sources, like solar PV panels and wind turbines, including their nominal capacities, efficiencies, specific costs, and associated CO2 emissions.

.. raw:: html

    <div style="overflow-y: auto; height: 350px;">

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
     - [%]
     - Efficiency of the inverter connected to each Renewable Energy Source (RES) (put 1 in case of AC bus)
   * - RES_Specific_Investment_Cost
     - (e.g. USD/W)
     - Specific investment cost for each type of Renewable Energy Source (RES) 
   * - RES_Specific_OM_Cost
     - [%]
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

.. raw:: html

    </div>

.. |nbsp| unicode:: 0xA0 
   :trim:

|nbsp|

**Generator Technology**

Details the types of generators that can be included in the microgrid, their efficiencies, costs, and lifetime, as well as the fuel they require and associated CO2 emissions.

.. raw:: html

    <div style="overflow-y: auto; height: 350px;">

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
     - [%]
     - Efficiency of the inverter connected to each Renewable Energy Source (RES) (put 1 in case of AC bus)
   * - RES_Specific_Investment_Cost
     - (e.g. USD/W)
     - Specific investment cost for each type of Renewable Energy Source (RES) 
   * - RES_Specific_OM_Cost
     - [%]
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

.. raw:: html

    </div>

.. |nbsp| unicode:: 0xA0 
   :trim:

|nbsp|


**Battery Technology**

Specifies the investment and operational costs, efficiencies, and other technical parameters related to battery storage solutions, critical for managing intermittent renewable energy supply.

.. raw:: html

    <div style="overflow-y: auto; height: 350px;">

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

.. raw:: html

    </div>

.. |nbsp| unicode:: 0xA0 
   :trim:

|nbsp|

**Grid Technology**

Parameters here govern the potential connection to the national grid, including costs, distances, pricing for energy sold to or purchased from the grid, and reliability metrics.


Plot settings
--------------

These parameters are used for the aesthetic aspects of model outputs, assigning colors to different energy sources, storage options, and other model components for visual representation in plots and charts.

.. note::
  Please refer to the example gallery for a better understanding of the structure of both the set and parameter files.

Time Series Data
===============

Demand 
-------
**Introduction**

At the core of the optimization energy modelling process lies the load curve demand. This section aims to explain what load curve demand is, how it is used within MicroGridsPy, and how it can be operated or estimated with external software tools like RAMP or within the model itself using the advanced feature of demand estimation integrated into MicroGridsPy.

.. raw:: html

    <div style="margin-bottom: 20px;"> <!-- Adds space below the expand button -->
    <details>
    <summary>Expand for more information</summary>
    <div style="padding-top: 10px;">

    <strong>What is the load curve demand?</strong><br><br>
    Load Curve Demand represents the <strong>time-dependent electricity consumption</strong> of a given area or system. It is typically measured in <em>Watts</em> (or kilowatts, megawatts, etc.) and captures how electricity demand varies over different periods, usually in hourly or sub-hourly intervals. The Load Curve Demand curve illustrates the power required at each point in time, providing insights into when and how much electricity is needed. This curve serves as a foundational data source for MicroGridsPy since the model aims to size and operate mini-grid components, such as renewable energy sources (e.g., solar panels, wind turbines), energy storage systems (e.g., batteries), and backup generators, to meet the electricity demand of a specific area or community. The key role of Load Curve Demand in the model is <strong>optimizing resource allocation</strong>: MicroGridsPy uses the load curve demand to distribute available resources efficiently over the years, balancing the generation and storage resources to minimize costs while meeting the electricity demand throughout the day. In addition to optimizing resource allocation, the software can also predict, along the time horizon of the simulation run, when <strong>investment steps</strong> should be taken to expand the system's capacity to accommodate the projected increase in demand if such an increase is anticipated.<br><br>
    <strong>Load curve demand estimation</strong><br><br>
    There are two key methods for operating load curve demand:<br>
    <ul>
      <li>Using software tools such as <a href="https://rampdemand.readthedocs.io/en/stable/intro.html">RAMP</a> which is a bottom-up stochastic model for the generation of high-resolution multi-energy profiles, conceived for application in contexts where only rough information about users' behaviour is obtainable. Those may range from remote villages to whole countries as well as informal settlements.</li>
      <li>Using the advanced features integrated into MicroGridsPy which allows to use built-in archetypes referring to rural villages in Sub-Saharan Africa at different latitudes (refer to <a href="#">the advanced documentation</a>).</li>
    </ul>
    <img src="https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/RAMP.png?raw=true" style="width: 150px; display: block; margin: auto;">
    </div>
    </details>

.. |nbsp| unicode:: 0xA0 
   :trim:

|nbsp|

**Demand.csv**

The input file, located in the "Time Series" folder within the "Inputs" folder, must have as many numbered columns (excluding the rows labels) as the total years of the project and as many rows (excluding the columns headers) as the periods in which one year is divided (e.g. 1-hour time resolution leads to 8760 rows). 


.. image:: https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Demand.png?raw=true
     :width: 700
     :align: center

.. |nbsp| unicode:: 0xA0 
   :trim:

|nbsp|

.. warning::
    The number of columns in the csv file must coincide with the value set for the 'Years' parameter. The same for the number of rows 
    that must coincide with the value set for 'Periods' in the model configuration.csv file! If not properly set and matched, it may arise a 'Key Error'.




Renewable Energy Production (Generation)
-------

**Introduction**

Electricity needed to meet the demand can be generated using various energy sources. MicroGridsPy considers renewable sources, such as solar and wind, and backup diesel generators as the choices for generating electricity. This section aims to explain what renewable energy production is, how it is used within MicroGridsPy, how it can be estimated with external available web tools like Renewables.ninja and PVGIS or within the model itself using the advanced feature of renewable energy production estimation integrated into MicroGridsPy.

.. raw:: html

    <div style="margin-bottom: 20px;"> <!-- Adds space below the expand button -->
    <details>
    <summary>Expand for more information</summary>
    <div style="padding-top: 10px;">


    <strong>What is the renewable energy production?</strong><br><br>
    The renewable energy production represents the estimated electricity production for each unitary generation technology at a given time for a specific location. It is typically measured in Watts (or kilowatts, megawatts, etc.) and captures how electricity production varies over time and source, usually in hourly or sub-hourly intervals. The data can be computed into a generation curve which illustrates the produced power at each point in time. This data becomes a fundamental source for MicroGridsPy to size and operate mini-grid components, such as renewable energy sources (e.g., solar panels, wind turbines) based on the unitary production of each source and complement the system with energy storage systems (e.g., batteries), and backup generators, to ensure the necessary electricity of a specific area or community. <br><br>
    <strong>Renewable Energy Production estimation</strong><br><br>
    There are two key methods to estimate renewable production::<br>
    <ul>
      <li>Using web tools such as Renewable Ninja and PVGIS. <a href="https://www.renewables.ninja/">Renewables.ninja</a> provides data and tools for assessing energy generation profiles with simulations and forecasting features. The electricity production is estimated for solar and wind sources and is computed for 1 year with 1-hour time resolution. To cover more years, more requests need to be performed for the same location. PVGIS (Photovoltaic Geographical Information System) provides solar radiation data, PV system yield estimations, and solar maps for various regions. It provides data for the typical meteorological conditions over a single year with 1-hour time resolution for a specific location.</li>
      <li>Using the advanced features integrated into MicroGridsPy which allows estimating generation based on VRES parameters, project location, and the specific year in question. The necessary data for solar, wind, and temperature conditions is obtained from the NASA POWER platform through an Application Program Interface (API) integrated into the MGPy software. These data are used to create a Typical Meteorological Year (TMY) dataset, representing typical weather conditions for the project location, with hourly resolution, based on 20 years of historical data. This TMY dataset is then used to calculate energy generation, which is consistent across all project years. (refer to <a href="#">the advanced documentation</a>).</li>
    </ul>
    </div>
    </details>

.. |nbsp| unicode:: 0xA0 
   :trim:

|nbsp|

**Generation.csv**

The input file, located in the "Time Series" folder within the "Inputs" folder, must have as many numbered columns (excluding the rows labels) as the total years of the project and as many rows (excluding the columns headers) as the periods in which one year is divided (e.g. 1-hour time resolution leads to 8760 rows). 






