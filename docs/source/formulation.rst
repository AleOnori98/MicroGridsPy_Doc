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


Objective function
===================
 
The objective function equation of the planning mode is the sum of all the regional costs
in addition to the inter-regional tranmission link costs discounted to the reference year.
While, in the operational mode, the objective function is just the sum of the
fixed and variable costs with their related taxes within the modeled year.

Cost
====

calculating the components of the objective function including the investment,
fixed and variable operation and maintenance and decommissioning costs followed
by the related taxes considered for each unit of investment or fixed cost
of the technologies. Carbon taxes are also included to be applied for the
carbon-intensive technologies. Alongside the related costs of technologies,
some revenues are considered in the objective function with a negative sign.
These revenues are including the salvage values on some of the investments where the operational 
lifetime of the technology lasts longer than the end of the modelling time horizon
and subsidies that are applied to some technologies based on the national policies.
The Hypatia model considers the economic life time of the technologies in the
investment cost calculation. Therefore, each required investment in a specific
year “y” is divided into a stream of annuities during several years
(from “y+1” to “y+ELIFE”) which is determined by the technology-specific
economic lifetime, depreciation rate and time value of money.

- investment
- fixed o&m cost
- variable cost (battery replacement ...)
- salvage value

Energy
======

- energy balance

:raw-html:`<br />`

.. math::
    :nowrap:
   
        \begin{eqnarray} 
             E_{Demand}(s,yt,t) = 
             \sum_{r} E_{RES}(s,r,yt,t) + 
             \sum_{g} E_{Generator}(s,g,yt,t)+E_{from Grid}(s,yt,t)-
             E_{to Grid}(s,yt,t)+E_{out BESS}(s,yt,t)-E_{in BESS}_{in}(s,yt,t)+Lost\_{Load}(s,yt,t)-
             E_{Curtailment}(s,yt,t)
        \end{eqnarray} 
 
:raw-html:`<br />`


- RES
- battery
The operation of the BESS is modelled with simple and straightforward model for batteries with limited complexity. This model relies on both analytical and empirical approaches to estimate the State of Charge (SOC) of the battery based on how energy flows in and out. Importantly, this battery model doesn't account for the battery's degradation over time.

When it comes to replacing the Battery Energy Storage System (BESS), the calculation is based on data provided by the battery manufacturer regarding the number of charge-discharge cycles the battery can handle before reaching the end of its useful life. This cycle life data, in combination with the investment cost, is used to determine when the battery should be replaced. The battery's capacity is assumed to remain constant, as the model doesn't consider capacity degradation. Therefore, the replacement is solely based on the number of completed cycles. With each cycle, a portion of the initial investment cost is added to the overall project cost, ensuring that the cost of replacing the battery is covered by the time it reaches its End of Life (EOL).

- Diesel generator
- lost load
- grid

others
- emissions

**constraint**

**How to write functions**


:raw-html:`<br />`
.. container:: scrolling-wrapper
   .. math::
      :nowrap:

      \begin{eqnarray}
         Energy\_{Demand}\_(scenario,year,period) =
         \sum_{year} (1+Discount_{rate}(year))^{-year}
         \times \sum_{link} \bigg[InvCost\_{link}(year,link)+
         FixCost\_{link}(year,link)+DecomCost\_{link}(year,link)+
         VarCost\_{link}(year,link)+FixTax\_{link}(year,link)+
         InvTax\_{link}(year,link)-InvSub\_{link}(year,link)-
         FixSub\_{link}(year,link)-InvSalvage\_{link}\bigg]
         \;\;\; \forall year \in years , \forall link \in links
      \end{eqnarray}

:raw-html:`<br />`

