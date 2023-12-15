#################################
Example Gallery
#################################

In this basic example run of MicroGridsPy, we demonstrate the foundational capabilities of the tool for microgrid simulation and optimization. The configuration for this run is as follows:

- **Time Horizon**: 20 years
- **Time Steps**: 4 (5 years each)
- **Renewable Energy Sources (RES)**: Only Photovoltaic (PV) systems available.
- **Formulation**: Linear Programming (LP)
- **Optimization Goal**: Net Present Cost (NPC)
- **Backup Systems**: Both battery storage and diesel generators included.
- **Extra Features**: No extra features or advanced models activated.

Carousel Gallery
----------------

The carousel gallery below visualizes the simulation outcomes, displaying the dispatch strategy, cash flow analysis, and other critical metrics.

.. raw:: html

   <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
     <ol class="carousel-indicators">
       <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
       <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
       <!-- Add more indicators here -->
       <li data-target="#carouselExampleIndicators" data-slide-to="10"></li>
     </ol>
     <div class="carousel-inner">
       <div class="carousel-item active">
         <img src="https://github.com/AleOnori98/MicroGridsPy_Doc/blob/main/docs/source/Images/Examples/Default/1.1.png?raw=true" class="d-block w-100" alt="Dispatch Strategy">
       </div>
       <!-- Add more carousel items here -->
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

To navigate through the gallery, click the previous and next buttons or select the corresponding indicator for the image you wish to view. The images should be observed sequentially from 1.1 to 1.11 to understand the comprehensive visual story of the default run scenario.

Results Interpretation
----------------------

The simulation's parameters in this example favor the diesel generator as the backup technology over the battery system. This preference stems from the higher investment and replacement costs associated with battery storage. The generator primarily ensures reliability and backup power during periods when PV generation is not sufficient.
