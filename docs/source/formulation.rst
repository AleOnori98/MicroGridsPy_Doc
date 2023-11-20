#######################################
Mathematical Formulation
#######################################
.. role:: raw-html(raw)
    :format: html


Two-stage optimization mixed integer linear programming sizing model
======================================================================

The considered system comprises an electrical load supplied by renewable sources, an inverter, a battery bank and backup generators (Fig. 1). The main optimization variables are divided into first-stage variables (rated capacities of each energy source) and second-stage variables (energy flows from the different components). The optimization is implemented in Python using Pyomo Library. 

.. image:: https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Minigrid%20components.jpg?raw=true
   :width: 500
   :align: center

.. |nbsp| unicode:: 0xA0 
   :trim:

|nbsp|

Objective function
===================
 
The choice of the objective function is guided by the **"Optimization_Goal"** parameter, which allows users to specify the primary focus of the optimization process as well as the **Multiobjective** parameter that introduces a multi-objective optimization option to the model adding CO2 emissions of generation technologies to the already existing NPC objective function.

* **Net Present Cost (NPC) Minimization** ("Optimization_Goal" = 1): When the "Optimization_Goal" parameter is set to 1, the optimization model prioritizes 
  the minimization of the Net Present Cost. The NPC is a comprehensive measure that represents the total cost of the microgrid over its entire lifespan, 
  discounted to the present value. This includes initial capital investments, operation and maintenance costs, fuel costs, and any other expenses, minus 
  the salvage value at the end of the microgrid's life. By minimizing the NPC, the model ensures that the microgrid is not only economically viable but 
  also cost-effective in the long term, making it an essential consideration for investors and policymakers focusing on financial sustainability.

* **Total Variable Cost (TVC) Minimization** ("Optimization_Goal" = 2): If the "Optimization_Goal" is set to 2, the model's objective shifts to minimizing 
  the Total Variable Cost. TVC encompasses all costs that vary directly with the level of energy production or consumption. This typically includes the 
  costs of operating and maintaining energy production facilities, the cost of fuel for generators, and any other costs that are not fixed. Minimizing TVC 
  is particularly important for the operational budgeting and planning of a microgrid, as it directly impacts the cost-effectiveness of its day-to-day 
  operations.

* **CO2 Emissions Minimization** (Multi-objective Optimization): In scenarios where environmental sustainability is as important as economic viability, the 
  MicroGridspy model can be set to perform multi-objective optimization. This approach includes minimizing CO2 emissions as one of the objectives, 
  reflecting the need to reduce the environmental impact of energy production. Minimizing CO2 emissions is aligned with global efforts to combat climate 
  change and is particularly relevant for projects that aim to meet certain environmental standards or qualifications for green funding.

The flexibility in choosing the objective function allows MicroGridspy to be adapted to a wide range of scenarios and policy goals, ensuring that the microgrid design is optimized not just for cost or environmental impact, but for the specific priorities of the project at hand.

Net Present Cost (NPC)
----------------------

The objective function for minimizing the Net Present Cost (NPC) is defined as the weighted sum of the scenario-specific NPC. This function aims to minimize the total cost of the microgrid over its lifecycle, accounting for the time value of money. It captures the comprehensive cost of the microgrid for a given scenario, including investment, operational costs, and salvage value.

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

    \text{NPC}(s) = \text{Investment Cost}(s) + \text{TVC}_{\text{Act}}(s) - \text{Salvage Value}


.. raw:: html

    </div>
    </div>

Total Variable Cost
----------------------

The Total Variable Cost (TVC) is a sum of the weighted scenario-specific variable costs. It reflects the operational expenses that fluctuate with the energy output.

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

    \text{TVC} = \sum_{s \in \text{Scenarios}} (\text{TVC}_{\text{NonAct}}(s) \times \text{Scenario Weight}(s))

.. raw:: html

    </div>
    </div>

Total CO2 emissions
--------------------

The total CO2 emissions are calculated as the sum of the weighted scenario-specific emissions. This equation is relevant for environmental impact assessments.

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

    \text{CO2 emissions} = \sum_{s \in \text{Scenarios}} (\text{CO2 emission}(s) \times \text{Scenario Weight}(s))

.. math::

    \text{CO2 emissions}(s) = 
    \begin{cases}
    \text{RES emission} + \text{GEN emission} + \text{BESS emission} + \text{FUEL emission}(s) + \text{GRID emission}(s), & \text{if Model_Components} = 0 \\
    \text{RES emission} + \text{BESS emission} + \text{GRID emission}(s), & \text{if Model_Components} = 1 \\
    \text{RES emission} + \text{GEN emission} + \text{FUEL emission}(s) + \text{GRID emission}(s), & \text{if Model_Components} = 2 \\
    \end{cases}

.. raw:: html

    </div>
    </div>

- **Emissions**




Cost
====

Investment
--------------------
Fixed Costs
--------------------
Variable Costs 
--------------------
- **Battery replacement**
When it comes to replacing the Battery Energy Storage System (BESS), the calculation is based on data provided by the battery manufacturer regarding the number of charge-discharge cycles the battery can handle before reaching the end of its useful life. This cycle life data, in combination with the investment cost, is used to determine when the battery should be replaced. The battery's capacity is assumed to remain constant, as the model doesn't consider capacity degradation. Therefore, the replacement is solely based on the number of completed cycles. With each cycle, a portion of the initial investment cost is added to the overall project cost, ensuring that the cost of replacing the battery is covered by the time it reaches its End of Life (EOL).


Salvage value
--------------------

Energy
======

Energy Balance
--------------------

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


RES
--------------------

Storage system - BESS 
--------------------
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



Other constraints are enforced in order to model a more realistic BESS operation. The SOC must operate between the defined range of the battery parameters. As the maximum is achieved at full battery capacity while the lower threshold is reached when discharging the percentage of the battery defined in the beginning as DOD. 

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


The maximum possible power when charging or discharging is also constrainted into the model assuming a maximum time for charging or discharging the BESS constinuously. While the maximum energy for the battery inflow or outflow are directly related to the maximum power value for the {\delta t} of the model (time step of 1-hour).

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

    P_{\text{BESS}}(ut) = \frac{Units_{\text{BESS}}(ut) \times C_{\text{BESS}}}{time_{\text{max}}}

.. math::

    E_{\text{BESS}}(s,yt,t) \leq = P_{\text{BESS}}(ut) \times \delta t

.. raw:: html

    </div>
    </div>





Diesel generator
--------------------
Lost Load
--------------------
National Grid
--------------------


