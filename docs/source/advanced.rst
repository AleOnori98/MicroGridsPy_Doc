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

Generator Partial Load Effect
----------------------

Grid Availability
----------------------

Brownfield
----------------------


