Analysing the Results
=========================
.. role:: raw-html(raw)
    :format: html

Testo

Scenarios
-----------

Results
-----------

LP/MILP

The **Results_Summary** is a spreadsheet containing:
- The grid components **Size**: Installed capacity of each component. In case of capacity expansion, it shows the size of each component after every investment step.


- The project **Cost**: Economic breakdown of the system. All the costs are actualized to the year at which they occur.


- The **Yearly cash flows**: Breakdown of yearly non-actualised costs (fixed O&M, fuel cost, battery replacement, lost load), grouped by component type (battery, generators, renewable technologies)


- The **Yearly energy parameters**: 
            * Generators share: total energy provided by generators divided by total electric demand
            * Renewables penetration: total energy provided by renewables divided by the sum of total energy provided by both renewables and generators
            * Curtailment share: total energy curtailed divided by the sum of total energy provided by both renewables and generators  
            * Battery usage: total energy discharged by the batteries divided by total electric demand
            * Grid usage: total energy withdrawn from the national grid divided by total electric demand



- sheet 'Yearly energy parameters SC': 
            * Generators share: total energy provided by generators divided by total electric demand for each scenario.
            * Renewables penetration: total energy provided by renewables divided by the sum of total energy provided by both renewables and generators for each scenario.
            * Curtailment share: total energy curtailed divided by the sum of total energy provided by both renewables and generators for each scenario.
            * Battery usage: total energy discharged by the batteries divided by total electric demand for each scenario.
            * Grid usage: total energy withdrawn from the national grid divided by total electric demand for each scenario.



The **Time_Series** is a spreadsheet containing:
- hourly energy balance of the system (technologies energy production, battery energy flows, demand, lost load, curtailment) + state of charge of the batteries and fuel consumed by the generators
- each year of the time horizon is reported on a different sheet







**Plots**/: 
DispatchPlot: image print-out of system energy dispatch and load demand for the selected date(s)


- size
- cost

