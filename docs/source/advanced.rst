Advanced Features
=========================
.. role:: raw-html(raw)
    :format: html
    :sphinx.ext.mathbase:

Multi-Objective Optimization
------------


RES Time Series Estimation
----------------


Load Demand Estimation
----------------------

Generator Partial Load Effect
----------------------

Battery Model
----------------------

The operation of the BESS is modelled with simple and straightforward model for batteries with limited complexity. This model relies on both analytical and empirical approaches to estimate the State of Charge (SOC) of the battery based on how energy flows in and out. Importantly, this battery model doesn't account for the battery's degradation over time.

*(equations) - basic energy balance model
.. math::

   (a + b)^2 = a^2 + 2ab + b^2

   (a - b)^2 = a^2 - 2ab + b^2

When it comes to replacing the Battery Energy Storage System (BESS), the calculation is based on data provided by the battery manufacturer regarding the number of charge-discharge cycles the battery can handle before reaching the end of its useful life. This cycle life data, in combination with the investment cost, is used to determine when the battery should be replaced. The battery's capacity is assumed to remain constant, as the model doesn't consider capacity degradation. Therefore, the replacement is solely based on the number of completed cycles. With each cycle, a portion of the initial investment cost is added to the overall project cost, ensuring that the cost of replacing the battery is covered by the time it reaches its End of Life (EOL).

*(equation) - only cost related

