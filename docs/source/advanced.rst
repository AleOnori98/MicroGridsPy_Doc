Advanced Features
=========================
.. role:: raw-html(raw)
    :format: html

Multi-Objective Optimization
------------

Multi-Step Investment
--------------------------

RES Time Series Estimation
----------------

RES parameters for production time series estimation

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
     - azimuth angle [0° south facing]
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
     - 
     - Average efficiency of turbine drivetrain (gearbox,generator,brake)



Load Demand Estimation
----------------------

Generator Partial Load Effect
----------------------

Grid Availability
----------------------

Brownfield
----------------------


