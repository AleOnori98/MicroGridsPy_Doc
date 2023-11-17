#######################################
Mathematical Formulation
#######################################
.. role:: raw-html(raw)
    :format: html

**Summary of Nomenclature**


.. list-table:: 
   :widths: 25 25
   :header-rows: 1

   * - Parameter name
     - Symbol
   * - Scenarios
     - s
   * - Periods
     - t  
   * - Years
     - yt
   * - Steps
     - ut
   * - RES_Sources
     - r
   * - Generator_Types
     - g


Two-stage optimization mixed integer linear programming sizing model
-------------------------------------------------------------------
The considered system comprises an electrical load supplied by renewable sources, an inverter, a battery bank and backup generators (Fig. 1). The main optimization variables are divided into first-stage variables (rated capacities of each energy source) and second-stage variables (energy flows from the different components). The optimization is implemented in Python using Pyomo Library. 

.. image:: https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Minigrid%20components.jpg?raw=true
   :width: 500
   :align: center

.. |nbsp| unicode:: 0xA0 
   :trim:

|nbsp|

Objective function
===================
 
The objective function equation of the planning mode is the sum of all the regional costs
in addition to the inter-regional transmission link costs discounted to the reference year.
While, in the operational mode, the objective function is just the sum of the
fixed and variable costs with their related taxes within the modeled year.

Cost
====

- investment
- fixed o&m cost
- variable cost (battery replacement ...)
- salvage value

Energy
======

- Energy Balance


.. raw:: html

    <style>
    .equation-container {
        overflow-x: auto;
        width: 100%;
        display: block;
    }
    .scrollable-equation {
        white-space: nowrap;
        overflow-x: scroll;
        display: block;
    }
    </style>
    <div class="equation-container">
    <div class="scrollable-equation">

.. math::

    E_{\text{demand}}(s,yt,t) = 
    \sum_{r} E_{\text{RES}}(s,r,yt,t) + 
    \sum_{g} E_{\text{generator}}(s,g,yt,t) + E_{\text{from grid}}(s,yt,t) -
    E_{\text{to grid}}(s,yt,t) + E_{\text{BESS charge}}(s,yt,t) - 
    E_{\text{BESS discharge}}(s,yt,t) +
    \text{Lost Load}(s,yt,t) - E_{\text{curtailment}}(s,yt,t)

.. raw:: html

    </div>
    </div>

    </div>
    </div>






- RES

- Storage system (BESS - Battery Energy Storage System)
The operation of the BESS is modelled with simple and straightforward model with low complexity. This model relies on both analytical and empirical approaches to estimate the State of Charge (SOC) of the battery based on how energy flows in and out. Importantly, this battery model doesn't account for the battery's degradation over time.

.. raw:: html

    <style>
    .equation-container {
        overflow-x: auto;
        width: 100%;
        display: block;
    }
    .scrollable-equation {
        white-space: nowrap;
        overflow-x: scroll;
        display: block;
    }
    </style>
    <div class="equation-container">
    <div class="scrollable-equation">

.. math::

    SOC(s,yt,t) = 
    SOC(s,yt,t-1) + 
    E_{\text{BESS charge}}(s,yt,t) \times \eta_{\text{BESS charge}} -
    \frac{E_{\text{BESS discharge}}(s,yt,t)}{\eta_{\text{BESS discharge}}}

.. raw:: html

    </div>
    </div>

Other constraints are enforced in order to model a more realistic BESS operation.

mention DOD and what means when used here. Maximum discharge of the battery.

.. raw:: html

    <style>
    .equation-container {
        overflow-x: auto;
        width: 100%;
        display: block;
    }
    .scrollable-equation {
        white-space: nowrap;
        overflow-x: scroll;
        display: block;
    }
    </style>
    <div class="equation-container">
    <div class="scrollable-equation">

.. math::

    Units_{\text{BESS}}(ut) \times C_{\text{BESS}} \times (1 - DOD) \leq SOC(s,yt,t) \leq Units_{\text{BESS}}(ut) \times C_{\text{BESS}}

.. raw:: html

    </div>
    </div>


When it comes to replacing the Battery Energy Storage System (BESS), the calculation is based on data provided by the battery manufacturer regarding the number of charge-discharge cycles the battery can handle before reaching the end of its useful life. This cycle life data, in combination with the investment cost, is used to determine when the battery should be replaced. The battery's capacity is assumed to remain constant, as the model doesn't consider capacity degradation. Therefore, the replacement is solely based on the number of completed cycles. With each cycle, a portion of the initial investment cost is added to the overall project cost, ensuring that the cost of replacing the battery is covered by the time it reaches its End of Life (EOL).


- Diesel generator
- lost load
- grid


others
- emissions


