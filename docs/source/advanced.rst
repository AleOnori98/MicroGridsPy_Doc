Advanced Features
=========================
.. role:: raw-html(raw)
    :format: html

Multi-Objective Optimization
------------
A multi-objective two-stage stochastic approach is presented by Gou et al. [1]. The goals are to minimize the net present cost (NPC) and the pollutants emission using chance-constrained programming and a genetic algorithm as optimization techniques.

Multi-Step Investment
--------------------------

RES Time Series Estimation
----------------

RES parameters for production time series estimation in MicroGridsPy:

.. list-table:: 
   :widths: 25 25 50
   :header-rows: 1

   * - Parameter name
     - Unit
     - Description
   * - lat
     - [-° -' -"] (e.g. 'xx xx xx')
     - latitude  [N positive, S negative]
   * - lon
     - [-° -' -"] (e.g. 'xx xx xx')
     - longitude [E positive, O negative]
   * - time_zone
     - (-) (e.g. +2)
     - UTC time zone 
   * - nom_power
     - Power (e.g. W)
     - Solar module nominal power 	
   * - tilt
     - °
     - tilt angle 
   * - azim
     - °
     - azimuth angle [0° south facing, 180° north facing]
   * - ro_ground
     - (-)
     - ground reflectivity  
   * - k_T
     - (e.g. %/°C)
     - power variation coefficient with temperature 
   * - NMOT
     - (e.g. °C)
     - Nominal Module Operating Temperature 
   * - T_NMOT
     - (e.g. °C)
     - Ambient temperature of NMOT conditions
   * - G_NMOT
     - (e.g. W/m^2)
     - Irradiance in NMOT conditions 
   * - turbine_type
     - (e.g. 'HA' or 'VA')
     - Horizontal Axis/Vertical Axis
   * - turbine_model
     - (e.g. 'NPS100c-21')
     - model name of the turbine (turbine data and power curve selected in XXX.csv)
   * - drivetrain_efficiency
     - % (0-1)
     - Average efficiency of turbine drivetrain (gearbox,generator,brake)


Advanced (for developers)


RES parameters (non-editable):

.. list-table:: 
   :widths: 25 25 50
   :header-rows: 1

   * - Parameter name
     - Unit
     - Description
   * - base_URL
     - 'https://power.larc.nasa.gov/api/temporal/'
     - URL base for API 
   * - loc_id
     - 'point'
     - Spatial resolution
   * - parameters_1
     - 'ALLSKY_SFC_SW_DWN'
     - Parameters of daily data with resolution of 1° x 1°
   * - parameters_2
     - 'T2MWET, T2M, WS50M'
     - Parameters of daily data with resolution of 0.5° x 0.625°
   * - parameters_3
     - 'WS50M, WS2M,WD50M, T2M'
     - parameters of hourly data
   * - date_start
     - '20150101'
     - Starting date for dataset (from 2001)
   * - date_end
     - '20201231'
     - Ending date for dataset (until 2020)
   * - community
     - 'RE'
     - Community of data archive
   * - temp_res_1
     - 'daily'
     - Temporal resolution for daily data
   * - temp_res_2
     - 'hourly'
     - Temporal resolution for hourly data
   * - output_format
     - 'JSON'
     - Output format
   * - user
     - 'anonymous'
     - User key



Load Demand Estimation
----------------------



.. list-table:: 
   :widths: 25 25 50
   :header-rows: 1

   * - Parameter name
     - Unit
     - Description
   * - demand_growth
     - % (0-1)
     - yearly expected average percentage variation of the demand [%]
   * - cooling_period
     - (e.g. 'NC' = No Cooling; 'AY' = All Year; 'OM' = Oct-Mar; 'AS' = Apr-Sept)
     - Cooling period 
   * - h_tier1
     - (-)
     - number of households in the wealth tier 1
   * - h_tier2
     - (-)
     - number of households in the wealth tier 2
   * - h_tier3
     - (-)
     - number of households in the wealth tier 3
   * - h_tier4
     - (-)
     - number of households in the wealth tier 4
   * - h_tier5
     - (-)
     - number of households in the wealth tier 5
   * - schools
     - (-)
     - number of schools
   * - hospital_1
     - (-)
     - number of hospitals of type 1
   * - hospital_2
     - (-)
     - number of hospitals of type 2
   * - hospital_3
     - (-)
     - number of hospitals of type 3
   * - hospital_4
     - (-)
     - number of hospitals of type 4
   * - hospital_5
     - (-)
     - number of hospitals of type 5


Generator Partial Load Effect
----------------------
In the present section, the focus is set on the generator models which often neglect decreased part-load efficiencies or minimum load constraints which can lead to significantly overestimated performance and therefore biased system planning. The model is therefore modified to consider more complex operating characteristics of a genset operating in partial load. A diesel genset optimally optimises efficiency in a fixed optimal power output. A reduction in power output results in a reduction in the efficiency. This effect has a non-linear behaviour, although diesel generators are often modelled with constant efficiency due to the limitations of the LP formulation. The MILP approach allows many ways to model these effects: a specific set of equations affecting the total operation costs of the energy produced by the generator has been implemented following the example of Balderrama et al. [42]. This formulation is relatively simple to implement, as it does not disrupt the structure of the entire model in terms of equations, it requires few parameters with an advantage in terms of computational effort, but it is closely linked to costs and not directly to the efficiency value leading to some limitations in case of null operation cost. For comparison, the partial load effect formulation is compared to the original LP model. This is further explained in the following figures.

In the LP formulation, the generator can freely vary its output between 0 and 100% without any penalization for partial load. The only limitation is therefore the maximum capacity of the unit. The slope of the cost curve for the generator system (a_LP), representing the marginal cost, is calculated as shown in equation (3.3) from the price of the fuel (p_fuel), the low heating value of the fuel (〖LHV〗_(fuel )) and the efficiency of the genset (η_gen). To not exceed the generator nominal capacity C, equation (3.4) is necessary, where E(s,t) is the energy output of the genset and Δt_p the hourly timestep. Finally, the total operation cost of the generator in the period t of scenario s (Cost(s,t))is calculated with equation (3.5).

...... Equations

In an isolated system, typically a predetermined number of diesel generators are coordinated to fulfil the fluctuating energy demands. To accurately represent this scenario, as well as account for the part load effect in each generator, the optimization approach is modified to a MILP (Mixed-Integer Linear Programming) formulation. The cost, denoted as Cost and calculated using equation (3.6), considers various factors including the number of generators operating at full load (N_full), the energy output of generators operating at part load (E_part), the slope of the cost curve for part load generators (α_MILP) as defined in equation (3.7), and the origin of the cost curve for part load generators (Cost_part). In this study, the value of Cost_part is determined as a percentage (p_gen) of the total operational cost of the generator system at full load, as elaborated in equation (3.8). Lastly, the binary variable B determines whether a generator operates in part load at a given time t.

......Equations

The minimum and maximum energy output of the generator in partial load is limited as shown in (3.9), where 𝑀𝑖𝑛𝑝𝑎𝑟𝑡 is the minimum percentage of energy output for the generator in part load. In addition, 𝑁 is the number of generators and is determined with the last equation. It is important to note that during the MILP optimization, 𝐶 is defined as a parameter and 𝑁 is the variable to optimize.

......Equations


Grid Availability
----------------------




Brownfield
----------------------

References
----------------------
.. [1] L. Guo, W. Liu, B. Jiao, B. Hong, C. Wang, "Multi-objective stochastic optimal planning method for stand-alone microgrid system", IET Generation
   Transm Distrib, 8 (7) (2014), pp. 1263-1273


