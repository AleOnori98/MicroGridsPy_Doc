########################################
Building and Running a Model
########################################

.. role:: raw-html(raw)
    :format: html

Building a model
==================

Building a model in MicroGridsPy is very simple and includes the following main steps:

#. Defining the....
#. Delivering the structural inputs (sets) to the model through a number of Excel-based files
#. Delivering the ....


Definiton of the model structural inputs 
-------------------------------------------
General introduction and description of the Model data parameters

.. note::
  Testo


.. list-table:: Parameters
   :widths: 20 25 150 20 20 20
   :header-rows: 1

   * - **Parameter**
     - **Sheet Name**
     - **Unit**
     - **Description**
   * - Periods
     - Model data
     - Time unit (e.g. hours/year)
     - Periods considered in one year (e.g. 8760 hours/year)
   * - Years
     - Model data
     - years
     - Total duration of the project

  
.. note::
  Please refer to the example gallery for a better understanding of the structure of both the set and parameter files.

Time Series Data
================
General description of the concept

Demand 
-------
General description of the concept

Renewable Energy Sources
-------
General description of the concept


Running a model
================
When the inputs of the model are correctly parsed to the model, you can run the model with specifying a couple of parameters:

.. code-block:: python

  model.run(
    solver = 'solver that you prefer'
  )

If model finds an optimum solution, you can have access to the results through :guilabel:`&results` attribute. For saving the results to your computer, use :guilabel:`&to_csv` function:

.. code-block:: python

  model.to_csv(
    path = 'path/to/directory'
  )

