
########################################
Building and Running a Model
########################################

MicroGridsPy is a comprehensive energy optimization model designed for the strategic planning and operational management of mini-grid systems. Here below is a general introduction to the different steps in building and running a model:

#. **Time Series Data Input**: Begin by providing specific data, over the lifetime of the project, about the available renewable resources and demand 
   profiles. For sub-Sahara Africa it is also possible to estimate endogenously these time series data based on editable parameters and build-in load 
   demand archetypes

#. **Configuration and Optimization setup**: Set the model's general parameters, such as the number of periods (e.g., 8760 for hourly analysis) and the
   total duration of the project, specific features and modes such as MILP formulation, Multi-Objective optimization, Grid connection etc. as well as 
   specific model's optimization goals and constraints, such as aiming for a minimum renewable penetration or a certain level of battery independence.

#. **Component Selection**: Choose the technologies to include, like PV panels or wind turbines of a specific model, and define their capacities and 
   operational characteristics.


#. **Execution**: Run the model to perform the optimization. MicroGridsPy processes the inputs through its algorithms to find the most cost-effective and 
   efficient system setup.

#. **Output Analysis**: Review the outputs, which include the sizing of system components, financial analyses like NPC and LCOE, and dispatch plots. 


.. image:: https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Mgpy_Simple_Scheme.png?raw=true
   :width: 500
   :align: center

----------------------------

Terminology
==============
The general terminology defined here is used throughout the documentation and the model code and configuration files:

* **Periods**: *units of time* for which the model performs calculations, defining the *temporal resolution* of the model. For example, if 'Periods' is 
  set to 8760, which corresponds to the number of hours in a year, implies that the model calculates energy generation, consumption, and other factors on 
  an hourly basis. Having a high temporal resolution (many periods) allows for a more detailed and accurate simulation of the mini-grid's performance, 
  which is critical for designing an efficient and reliable system. However, more periods also mean more data to process and potentially longer computation 
  times, so there's a trade-off between model detail and computational efficiency.
* **Investment Steps**: Total number of investment steps during project duration. Based on the setp duration of each investment decision in which the project lifetime will be split. (refer to :doc:`advanced`)
* **Scenarios**: Number of scenarios to consider within the optimisation due to the uncertainty associated with the energy generation from renewable sources and the fluctuating energy demand in rural villages. To address this issue, various scenarios are explored aimed at minimizing the overall energy cost for consumers. This involves the creation of diverse and realistic scenarios for both solar power output and energy consumption.
* **Years**: Total duration of the project in years. 
* **RES_Sources**: Number of Renewable Energy Sources (RES) types to consider in the simulation.
* **Generator_Types**: Number of different types of gensets that can be installed in the mini-grid.


.. list-table:: 
   :widths: 25 25
   :header-rows: 1

   * - Parameter name
     - Symbol
   * - Periods
     - t  
   * - Steps
     - ut
   * - Scenarios
     - s
   * - Years
     - yt
   * - RES_Sources
     - r
   * - Generator_Types
     - g



As more generally in constrained optimisation, the following terms are also used:

* Parameter: a fixed coefficient that enters into model equations
* Variable: a variable coefficient (decision variable) that enters into model equations
* Set: an index in the algebraic formulation of the equations
* Constraint: an equality or inequality expression that constrains one or several variables
* Text


--------------------------------------------------------------------------------------------------------------------


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


---------------------------------------------------------------------------------------------------------------

**Model Switches**

This set of parameters allows users to toggle different aspects and features of the model, such as the optimization goal (NPC or operation cost), whether to use a MILP formulation and various operational considerations like partial load effects on generators and multi-objective optimization criteria.

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


(refer to :doc:`advanced`)


----------------------------------------------------------------------------------------------------------------------------------


Technology Parameters
----------------------

**RES Technology**

Defines the types and characteristics of renewable energy sources, like solar PV panels and wind turbines, including their nominal capacities, efficiencies, specific costs, and associated CO2 emissions.


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
     - (e.g. 'PV panels', 'Wind turbines')
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
     - (e.g. kgCO2/kW)
     - ???


----------------------------------------------------------------------------------------------------------


**Generator Technology**

Details the types of generators that can be included in the microgrid, their efficiencies, costs, and lifetime, as well as the fuel they require and associated CO2 emissions.

.. list-table:: 
   :widths: 25 25 50
   :header-rows: 1

   * - Parameter name
     - Unit
     - Description
   * - Generator_Types 
     - (-)
     - Number of different types of gensets 
   * - Generator_Names 
     - (e.g. 'Diesel Genset 1')
     - Generator names
   * - Generator_Efficiency 
     - [%]
     - Average generator efficiency of each generator type
   * - Generator_Specific_Investment_Cost 
     - (e.g. USD/W)
     - Specific investment cost for each generator type 
   * - Generator_Specific_OM_Cost 
     - [%]
     - O&M cost for each generator type as a fraction of specific investment cost [%]
   * - Generator_Lifetime 
     - years
     - Lifetime of each generator type  
   * - Fuel_Names 
     - (e.g. 'Diesel')
     - Fuel names (to be specified for each generator, even if they use the same fuel)
   * - Fuel_Specific_Cost 
     - (e.g. USD/lt)
     - Specific fuel cost for each generator type 
   * - Fuel_LHV 
     - (e.g. Wh/lt)
     - Fuel lower heating value (LHV) for each generator type 
   * - Generator_capacity 
     - Power (e.g. W)
     - Existing Generator capacity (if Brownfield investment activated)
   * - GEN_years 
     - years
     - How many years ago the component was installed 
   * - GEN_unit_CO2_emission 
     - (e.g. kgCO2/kW)
     - ????????
   * - FUEL_unit_CO2_emission 
     - (e.g. kgCO2/lt)
     - ????????
   * - Generator_Min_output 
     - [%]
     - Minimum percentage of energy output for the generator in part load 
   * - Generator_Nominal_Capacity_milp 
     - Power (e.g. W)
     - Nominal capacity of each generator       
   * - Generator_pgen 
     - [%]
     - Percentage of the total operation cost of the generator system at full load 




**Battery Technology**

Specifies the investment and operational costs, efficiencies, and other technical parameters related to battery storage solutions, critical for managing intermittent renewable energy supply.


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
     - [%]
     - Discharge efficiency of the battery bank
   * - Battery_Charge_Battery_Efficiency
     - [%]
     - Charge efficiency of the battery bank 
   * - Battery_Depth_of_Discharge
     - [%]
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
     - [%]
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



**Grid Technology**

Parameters here govern the potential connection to the national grid, including costs, distances, pricing for energy sold to or purchased from the grid, and reliability metrics.


.. list-table:: 
   :widths: 25 25 50
   :header-rows: 1

   * - Parameter name
     - Unit
     - Description
   * - Year_Grid_Connection 
     - (-)
     - Year at which the mini-grid is connected to the national grid (starting from 1)     
   * - Grid_Sold_El_Price 
     - (e.g. USD/kWh)
     - Price at which electricity is sold to the grid
   * - Grid_Purchased_El_Price 
     - (e.g. USD/kWh)
     - Price at which electricity is purchased from the grid 
   * - Grid_Distance 
     - (e.g. km)
     - Distance from grid connection point 
   * - Grid_Connection_Cost 
     - (e.g. USD/km)
     - Investment cost of grid connection, i.e. extension of power line + transformer costs 
   * - Grid_Maintenance_Cost 
     - (-)
     - O&M cost for maintenance of the power line and transformer as a fraction of investment cost
   * - Maximum_Grid_Power 
     - (e.g. kW)
     - Maximum active power that can be injected/withdrawn to/from the grid 
   * - Grid_Average_Number_Outages 
     - (-)
     - Average number of outages in the national grid in a year (0 to simulate ideal power grid)
   * - Grid_Average_Outage_Duration 
     - minutes
     - Average duration of an outage (0 to simulate ideal power grid)
   * - National_Grid_Specific_CO2_emissions 
     - (e.g. kgCO2/kWh)
     - Specific CO2 emissions by the considered national grid



**Lost Load**

Specific parameters for Lost Load regarding maximum value and related costs.

.. list-table:: 
   :widths: 25 25 50
   :header-rows: 1

   * - Parameter name
     - Unit
     - Description
   * - Lost_Load_Fraction 
     - (-)
     - Maximum admittable loss of load          
   * - Lost_Load_Specific_Cost 
     - (e.g. USD/Wh)
     - Value of the unmet load



Plot settings
--------------

These parameters are used for the aesthetic aspects of model outputs, assigning colors to different energy sources, storage options, and other model components for visual representation in plots and charts.


.. note::
  Please refer to the example gallery for a better understanding of the structure of both the set and parameter files.



----------------------------------------------------------------------------------------------------------



Time Series Data
===================

Demand 
-------
**Introduction**

At the core of the optimization energy modelling process lies the load curve demand. This section aims to explain what load curve demand is, how it is used within MicroGridsPy, and how it can be operated or estimated with external software tools like RAMP or within the model itself using the advanced feature of demand estimation integrated into MicroGridsPy.

.. tip::

   **What is the load curve demand?**

   Load Curve Demand represents the *time-dependent electricity consumption* of a given area or system. It is typically measured in Watts (or kilowatts, megawatts, etc.) and captures how electricity demand varies over different periods, usually in hourly or sub-hourly intervals. This curve illustrates the power required at each point in time, providing insights into when and how much electricity is needed.

   MicroGridsPy uses the load curve demand to optimize resource allocation, distributing resources efficiently over the years. It balances generation and storage resources to minimize costs while meeting the electricity demand throughout the day. The software can predict when investment steps should be taken to expand the system's capacity for increasing demand.

   **Load curve demand estimation methods:**

   - Using software tools such as `RAMP <https://rampdemand.readthedocs.io/en/stable/intro.html>`_, a bottom-up stochastic model for generating high-resolution multi-energy profiles.
   - Using the advanced features integrated into MicroGridsPy, which allows the use of built-in archetypes for rural villages in Sub-Saharan Africa at different latitudes.

.. image:: https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/RAMP.png?raw=true
   :width: 150px
   :align: center



**Demand.csv**

The input file, located in the "Time Series" folder within the "Inputs" folder, must have as many numbered columns (excluding the rows labels) as the total years of the project and as many rows (excluding the columns headers) as the periods in which one year is divided (e.g. 1-hour time resolution leads to 8760 rows). 


.. image:: https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Demand.png?raw=true
     :width: 700
     :align: center



.. warning::
    The number of columns in the csv file must coincide with the value set for the 'Years' parameter. The same for the number of rows 
    that must coincide with the value set for 'Periods' in the model configuration.csv file! If not properly set and matched, it may arise a 'Key Error'.



RES Production
----------------

**Introduction**

Electricity needed to meet the demand can be generated using various energy sources. MicroGridsPy considers renewable sources, such as solar and wind, and backup diesel generators as the choices for generating electricity. This section aims to explain what renewable energy production is, how it is used within MicroGridsPy, how it can be estimated with external available web tools like Renewables.ninja and PVGIS or within the model itself using the advanced feature of renewable energy production estimation integrated into MicroGridsPy.

.. tip::

   **What is the renewable energy production?**

   Renewable energy production represents the estimated electricity production for each unitary generation technology at a specific time and location. It is typically measured in Watts (or kilowatts, megawatts, etc.) and illustrates how electricity production varies over time and by source, usually in hourly or sub-hourly intervals.

   MicroGridsPy uses this data to size and operate mini-grid components like renewable energy sources (e.g., solar panels, wind turbines), energy storage systems (e.g., batteries), and backup generators to ensure necessary electricity for a specific area or community.

   **Renewable Energy Production estimation methods:**

   - Using web tools such as `Renewables.ninja <https://www.renewables.ninja/>`_, which provides data and tools for assessing energy generation profiles, including solar and wind energy production estimated for 1 year with 1-hour time resolution.
   - Using the advanced features integrated into MicroGridsPy for estimating generation based on VRES parameters, project location, and the specific year. Data for solar, wind, and temperature conditions are obtained from the NASA POWER platform through an API integrated into the MGPy software, creating a Typical Meteorological Year (TMY) dataset for energy generation calculations.



**Generation.csv**

The input file, located in the "Time Series" folder within the "Inputs" folder, must have as many numbered columns (excluding the rows labels) as the total years of the project and as many rows (excluding the columns headers) as the periods in which one year is divided (e.g. 1-hour time resolution leads to 8760 rows). 


.. image:: https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/RES.png?raw=true
     :width: 200
     :height: 500
     :align: center



