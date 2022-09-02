# Welcome to Olinto's bike shop
*This app is named after Antonio Olinto Ferreira, an awesome brazilian traveling cyclist. see more at https://www.olinto.com.br*
___
## About the app
A python application that simulates a bike rental shop system. The user chooses to rent, return or list the bikes available in the shop. 

If it choses to rent bikes, the user is asked to define how many bikes and to choose between an hourly/daily/weekly plan, each with different fares (\$5, \$10, \$40). Users that rent 3 or more bikes are eligible for family discount of 30% of the total price.

*** This app was developed with the purpose to practice OOP and software development skills. ***

*This app was inspired by https://github.com/Xiangs18/Bike_Rental_System*

___
## How to run

This app is containerized with Docker to avoid conflicts between software versions and Operational systems. 

To run this app, ideally you should have docker. If you don't please visit: https://docs.docker.com/engine/install for instructions.

Then simply open a terminal and run: 

```bash
docker run -i bike_shop_py
```

Alternatively just open the terminal and start the application with regular python:

```bash 
python3 app.py
```