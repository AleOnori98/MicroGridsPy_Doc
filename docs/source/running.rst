Running the Model
=========================
.. role:: raw-html(raw)
    :format: html

Testo

Scenarios
-----------

Results
-----------

**summary file**
- components size
- cost
- cash flows
- energy parameters

:raw-html:`<br />`

.. container:: scrolling-wrapper

   .. math::
      :nowrap:
        
       \begin{eqnarray}
           Energy\_{Demand}(scenario,year,period) =
           \sum_{res\_{source}} Energy\_{RES}(scenario,res\_{source},year,period) + 
           \sum_{gen\_{type}} Energy\_{Generator}(scenario,gen\_{type},year,period) + 
           Energy\_{Grid}_{from}(scenario,year,period) - Energy\_{Grid}_{to}(scenario,year,period) +
           Energy\_{BESS}_{out}(scenario,year,period) - Energy\_{BESS}_{in}(scenario,year,period) +
           \Lost\_{Load}(scenario,year,period) - Energy\_{Curtailment}(scenario,year,period)
        \end{eqnarray}

:raw-html:`<br />`


**dispatch time series file**
- demand
- components

