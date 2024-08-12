# House pricing prediction

## Goals

There are four high-level goals for this case study:

- Create a linear regression model that can predict the sale price of a house
- Create plots and tables that illustrate interesting relationships the sale price of the houses and other features
- Clean the data and do feature engineering
- Execute a hypothesis test
- Communicate your results to a non-technical audience
- Create a WebUI where user can play around with the model

## Housing Price Dataset Description

- [Find the source of the dataset here.](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/overview)

This data set includes 79 explanatory variables describing (almost) every aspect of residential homes in Ames, Iowa.

## Deliverables

### WebUI

Be able to deploy the test WebUI so user can access them from the internet

### API server

Implement an API server.

- Implement a fastAPI server
- Add endpoints to get a prediction

## Run the application

### Source code

The to runt he application run:

```sh
make setup # to install the application
make run # to runt the application

```

### Docker

To run the application in a docker container, use the provided docker compose file, and run:

```sh
Docker compose up -d # use -d flag to run detached form the current terminal.
```

By the default the application will be running on port 5010.
