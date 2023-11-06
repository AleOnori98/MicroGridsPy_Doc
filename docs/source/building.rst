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


Definiton of the model structural inputs 
-------------------------------------------
General introduction and description of the Model data parameters

.. note::
  Testo


.. list-table:: Parameters
   :widths: 20 25 150 20 20 20
   :header-rows: 1

   * - Group
     - Sheet Name
     - Description
     - Unit
     - Time dimension
     - Mode
   * - Economic
     - V_OM
     - Specific variable operation and maintenance cost per unit of production of each technology
     - Currency / Production unit (e.g. USD/GWh)
     - Modelling years
     - Planning, Operational
   * - Economic
     - F_OM
     - Specific fixed operation and maintenance cost per unit of total installed capacity of each technology
     - Currency / Capacity unit (e.g. USD/GW)
     - Modelling years
     - Planning, Operational
   * - Economic
     - INV
     - Specific investment cost per unit of new installed capacity of each technology
     - Currency / Capacity unit (e.g. USD/GW)
     - Modelling years
     - Planning
   * - Economic
     - Decom_cost
     - Specific decomissioning cost per unit of dismantled capacity of each technology
     - Currency / Capacity unit (e.g. USD/GW)
     - Modelling years
     - Planning
   * - Economic
     - Economic_lifetime
     - The period over which the investment annuities are spread. In other words, each required investment in a specific year "y" is divided into a stream of annuities during several years starting from "y+1" to "y+economic lifetime"
     - years
     - None
     - Planning
   * - Economic
     - Interest_rate
     - Technology-specific interest rate is required to calculate the depreciation rate of each technology
     - None
     - None
     - Planning
   * - Economic
     - Discount_rate
     - General discount rate for calculating the net present value of the cost components of the objective function
     - None
     - Modelling years
     - Planning
   * - Technical
     - Tech_lifetime
     - The useful operational lifetime of technologies before dismantling
     - years
     - None
     - Planning
   * - Technical
     - Tech_efficiency
     - The ratio between the output activity of the technology to the input activity (Due to the possible difference between the input and output activity units, this parameter can be also higher than one)
     - None
     - Modelling years
     - Planning, Operational
   * - Technical
     - AnnualProd_perunit_capacity
     - The amount of output activity per unit of installed capcity of each technology in each modelling year of the time horizon
     - Activity unit per year / Capacity unit (e.g. GWh/y/GW )
     - Modelling years
     - Planning, Operational
   * - Technical
     - Residual_capacity
     - The total installed capacity of each technology before starting the modelling horizon
     - Capacity unit (e.g. GW)
     - Modelling years
     - Planning, Operational
   * - Technical
     - Capacity_factor_tech
     - Average capacity of a technology over on year divided by its nominal total capacity (allows to consider the planned outages or the operation and maintenance times)
     - None
     - Modelling years
     - Planning, Operational
   * - Technical
     - capacity_factor_resource
     - The max production of one unit capacity of each technology in each time slice based on the variable resource availability (allows to consider the availability of resources especially for renewable technologies in each time slice of the year)
     - None
     - Modelling years & timeslices
     - Planning, Operational
   * - Environmental
     - Specific_emission
     - Specific CO2 or CO2-equivalent emission of each technology per unit of production
     - emission unit / activity unit (e.g. ton/GWh)
     - Modelling years
     - Planning, Operational
   * - Scenario-based
     - Investment_taxsub
     - Taxes and subsidies as a fraction per unit of investment cost
     - Currency / currency (e.g. USD of tax or sub / USD of investment)
     - Modelling years
     - Planning
   * - Scenario-based
     - Fix_taxsub
     - Taxes and subsidies as a fraction per unit of fixed O&M cost
     - Currency / currency (e.g. USD of tax or sub / USD of fixed cost)
     - Modelling years
     - Planning
   * - Scenario-based
     - Carbon_tax
     - The tax defined for each unit of produced CO2 emissions
     - Currency / CO2 emission unit (e.g. USD of tax / tons of CO2 emissions)
     - Modelling years
     - Planning, Operational
   * - Scenario-based
     - Min_newcap
     - The minimum allowed annual new installed capacity of each technology specified in a particular scenario
     - Capacity units (e.g. GW)
     - Modelling year
     - Planning
   * - Scenario-based
     - Max_newcap
     - The maximum allowed annual new installed capacity of each technology specified in a particular scenario
     - Capacity units (e.g. GW)
     - Modelling year
     - Planning
   * - Scenario-based
     - Min_totalcap
     - The minimum allowed annual total installed capacity of each technology specified in a particular scenario
     - Capacity units (e.g. GW)
     - Modelling year
     - Planning
   * - Scenario-based
     - Max_totalcap
     - The maximum allowed annual total installed capacity of each technology specified in a particular scenario
     - Capacity units (e.g. GW)
     - Modelling year
     - Planning
   * - Scenario-based
     - Min_production
     - The minimum allowed annual production of each technology specified in a particular scenario
     - Activity units (e.g. GWh)
     - Modelling years
     - Planning, Operational
   * - Scenario-based
     - Max_production
     - The maximum allowed annual production of each technology specified in a particular scenario
     - Activity units (e.g. GWh)
     - Modelling years
     - Planning, Operational
   * - Scenario-based
     - Emission_cap_annual
     - The allowed cap on the annual CO2 emission production
     - CO2 emission units
     - Modelling years
     - Planning, operational
   * - Demand
     - Demand
     - The final demand specified for each demand technology
     - Activity units (e.g. GWh)
     - Modelling years & timeslices
     - Planning, Operational
  
.. note::
  Please refer to the example gallery for a better understanding of the structure of both the set and parameter files.

Time Series Data
================
General description of the concept

Demand 
-------
General description of the concept

Renewable Energy Sources
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

