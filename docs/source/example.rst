#################################
Example Gallery
#################################

Default Scenario
----------------
In this basic example run of MicroGridsPy, we demonstrate the foundational capabilities of the tool for microgrids simulation and optimization. The basic configuration for this run is as follows:

- **Time Horizon**: 20 years
- **Renewable Energy Sources (RES)**: Only Photovoltaic (PV) systems available.
- **Formulation**: Linear Programming (LP)
- **Optimization Goal**: Net Present Cost (NPC)
- **Backup Systems**: Both battery storage and diesel generators included.
- **Extra Features**: No extra features or advanced models activated.

The images gallery below visualizes the interface windows, simulation outcomes, displaying the dispatch strategy, and other critical metrics.

.. raw:: html

   <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
     <ol class="carousel-indicators">
       <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
       <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
       <li data-target="#carouselExampleIndicators" data-slide-to="10"></li>
     </ol>
     <div class="carousel-inner">
       <div class="carousel-item active">
         <img src="https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Examples/Default/1.1.png?raw=true" class="d-block w-100" alt="Dispatch Strategy">
       </div>
       <div class="carousel-item">
         <img src="https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Examples/Default/1.2.png?raw=true" class="d-block w-100" alt="Cash Flow Analysis">
       </div>
       <div class="carousel-item">
         <img src="https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Examples/Default/1.3.png?raw=true" class="d-block w-100" alt="Cash Flow Analysis">
       </div>
       <div class="carousel-item">
         <img src="https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Examples/Default/1.4.png?raw=true" class="d-block w-100" alt="Cash Flow Analysis">
       </div>
       <div class="carousel-item">
         <img src="https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Examples/Default/1.5.png?raw=true" class="d-block w-100" alt="Cash Flow Analysis">
       </div>
       <div class="carousel-item">
         <img src="https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Examples/Default/1.6.png?raw=true" class="d-block w-100" alt="Cash Flow Analysis">
       </div>
       <div class="carousel-item">
         <img src="https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Examples/Default/1.7.png?raw=true" class="d-block w-100" alt="Cash Flow Analysis">
       </div>
       <div class="carousel-item">
         <img src="https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Examples/Default/1.8.png?raw=true" class="d-block w-100" alt="Cash Flow Analysis">
       </div>
       <div class="carousel-item">
         <img src="https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Examples/Default/1.9.png?raw=true" class="d-block w-100" alt="Cash Flow Analysis">
       </div>
       <div class="carousel-item">
         <img src="https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Examples/Default/1.10.png?raw=true" class="d-block w-100" alt="Cash Flow Analysis">
       </div>
       <div class="carousel-item">
         <img src="https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Examples/Default/1.11.png?raw=true" class="d-block w-100" alt="Cash Flow Analysis">
       </div>
       <div class="carousel-item">
         <img src="https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Examples/Default/1.12.png?raw=true" class="d-block w-100" alt="Cash Flow Analysis">
       </div>
       <div class="carousel-item">
         <img src="https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Examples/Default/1.13.png?raw=true" class="d-block w-100" alt="Cash Flow Analysis">
       </div>
     </div>
     <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev" style="color: #333;">
       <span class="carousel-control-prev-icon" aria-hidden="true" style="background-image: none;"></span>
       <span class="sr-only">Previous</span>
     </a>
     <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next" style="color: #333;">
       <span class="carousel-control-next-icon" aria-hidden="true" style="background-image: none;"></span>
       <span class="sr-only">Next</span>
     </a>
   </div>

-------------------------------------------------------------------------------------------------------------

**Results Interpretation**

In the default simulation, renewable sources significantly contribute to the energy mix with 77,38% penetration, accompanied by a 34.87% utilization of batteries and a 23,13% share from diesel generators. Notably, as illustrated in the CashFlow Plot, the reliance on generators escalates over the years due to increasing demand, making them a critical component to meet energy requirements in the absence of capacity expansion. The model's settings, including the implementation of the generator's partial load effect, the use of a more realistic MILP formulation, and variable fuel cost considerations, can substantially alter these dynamics. MicroGridsPy also enables setting minimum renewable penetration thresholds, potentially shifting focus towards battery storage, especially under fluctuating fuel prices or supportive renewable energy policies. This feature, along with the observed trend in generator usage, demonstrates the model's capacity to adapt to various scenarios and constraints, highlighting the evolving roles of different technologies as optimal solutions under specific conditions.

Grid Connection
------------------------------

Moving away from the basic example previously discussed, this scenario within MicroGridsPy presents a different configuration where grid connection is enabled starting from year 10. This adjustment aims to explore its influence on the simulation results, offering insights into how integrating with the grid from a specific year affects the overall energy strategy.

- **Grid Connection**: Activated, allowing the microgrid to interact with the main electrical grid. starting from year 10


.. raw:: html

.. raw:: html

   <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
     <ol class="carousel-indicators">
       <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
       <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
       <li data-target="#carouselExampleIndicators" data-slide-to="10"></li>
     </ol>
     <div class="carousel-inner">
       <div class="carousel-item active">
         <img src="https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Examples/1/2.1.png?raw=true" class="d-block w-100" alt="Dispatch Strategy">
       </div>
       <div class="carousel-item">
         <img src="https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Examples/1/2.2.png?raw=true" class="d-block w-100" alt="Cash Flow Analysis">
       </div>
       <div class="carousel-item">
         <img src="https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Examples/1/2.3.png?raw=true" class="d-block w-100" alt="Cash Flow Analysis">
       </div>
       <div class="carousel-item">
         <img src="https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Examples/1/2.4.png?raw=true" class="d-block w-100" alt="Cash Flow Analysis">
       </div>
       <div class="carousel-item">
         <img src="https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Examples/1/2.5.png?raw=true" class="d-block w-100" alt="Cash Flow Analysis">
       </div>
       <div class="carousel-item">
         <img src="https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Examples/1/2.6.png?raw=true" class="d-block w-100" alt="Cash Flow Analysis">
       </div>
       <div class="carousel-item">
         <img src="https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Examples/1/2.7.png?raw=true" class="d-block w-100" alt="Cash Flow Analysis">
       </div>
       <div class="carousel-item">
         <img src="https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Examples/1/2.8.png?raw=true" class="d-block w-100" alt="Cash Flow Analysis">
       </div>
       <div class="carousel-item">
         <img src="https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Examples/1/2.9.png?raw=true" class="d-block w-100" alt="Cash Flow Analysis">
       </div>
       <div class="carousel-item">
         <img src="https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Examples/1/2.10.png?raw=true" class="d-block w-100" alt="Cash Flow Analysis">
       </div>
       <div class="carousel-item">
         <img src="https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Examples/1/2.11.png?raw=true" class="d-block w-100" alt="Cash Flow Analysis">
       </div>
       <div class="carousel-item">
         <img src="https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Examples/1/2.12.png?raw=true" class="d-block w-100" alt="Cash Flow Analysis">
       </div>
       <div class="carousel-item">
         <img src="https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Examples/1/2.13.png?raw=true" class="d-block w-100" alt="Cash Flow Analysis">
       </div>
       <div class="carousel-item">
         <img src="https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Examples/1/2.14.png?raw=true" class="d-block w-100" alt="Cash Flow Analysis">
       </div>
       <div class="carousel-item">
         <img src="https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Examples/1/2.15.png?raw=true" class="d-block w-100" alt="Cash Flow Analysis">
       </div>
       <div class="carousel-item">
         <img src="https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Examples/1/2.16.png?raw=true" class="d-block w-100" alt="Cash Flow Analysis">
       </div>
     </div>
     <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev" style="color: #333;">
       <span class="carousel-control-prev-icon" aria-hidden="true" style="background-image: none;"></span>
       <span class="sr-only">Previous</span>
     </a>
     <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next" style="color: #333;">
       <span class="carousel-control-next-icon" aria-hidden="true" style="background-image: none;"></span>
       <span class="sr-only">Next</span>
     </a>
   </div>

-----------------------------------------------

**Result Interpretaion**

Departing from the basic LP approach, this advanced scenario in the model engages a MILP formulation, significantly refining the model by accurately representing discrete operational choices and system behaviors, albeit with greater computational demands.

MILP Formulation and Partial Load Effect
------------------------------

Moving away from the basic example previously discussed, this scenario within MicroGridsPy presents a different configuration where grid connection is enabled starting from year 10. This adjustment aims to explore its influence on the simulation results, offering insights into how integrating with the grid from a specific year affects the overall energy strategy.

- **MILP Formulation**: technologies are modeled as discrete units of capacity rather than the continuous values used in LP, allowing for a more accurate representation of real-world scenarios where capacity additions occur in quantized increments.
- **Partial Load Effect**: By accounting for the partial load effect on generator operation, the model now reflects the real-world efficiency variations and increased fuel consumption when generators do not operate at optimal levels, potentially altering investment and operational decisions to favor solutions that mitigate these inefficiencies.




