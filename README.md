# SQLAlchemy - A small project - Surfs Up!

![surfs-up.png](Images/surfs-up.png)

In this small project some climate analysis was done on Honolulu, Hawaii weather data.

## Step 1 - Climate Analysis and Exploration

Python and SQLAlchemy were used to do basic climate analysis and data exploration of climate database. All of the following analysis were completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

Following steps were followed:

* SQLAlchemy `create_engine` was used to connect to sqlite database.

* SQLAlchemy `automap_base()` was used to reflect tables into classes.Two classes are there ,`Station` and `Measurement`.

* Python was linked to the database by SQLAlchemy session.


### Precipitation Analysis

  ![precipitation](Images/precipitation.png)


### Station Analysis

  ![station-histogram](Images/station-histogram.png)


- - -

## Step 2 - Climate App

A Flask API was cvreated with following routes:

### Routes

* `/`

  * Home page.
  * List all routes that are available.

* `/api/v1.0/precipitation`
* `/api/v1.0/stations`
* `/api/v1.0/tobs`
* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

- - -

## Other Analyses

### Temperature Analysis I

* Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?

* Pandas was used to perform this portion.

* The average temperatures were identified in June  and December  at all stations across all available years in the dataset. 

* Independent T-test was used to determine whether the difference in the means, if any, is statistically significant. 

### Temperature Analysis II

  ![temperature](Images/temperature.png)

### Daily Rainfall Average

* Rainfall was calculated and sorted per weather station using the previous year's matching dates.

### Daily Temperature Normals

* Calculate the daily normals for the duration of your trip. Normals are the averages for the min, avg, and max temperatures. You are provided with a function called `daily_normals` that will calculate the daily normals for a specific date. This date string will be in the format `%m-%d`. Be sure to use all historic TOBS that match that date string.

  * Set the start and end date of the trip.

  * Use the date to create a range of dates.

  * Strip off the year and save a list of strings in the format `%m-%d`.

  * Use the `daily_normals` function to calculate the normals for each date string and append the results to a list called `normals`.

* Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.

* Use Pandas to plot an area plot (`stacked=False`) for the daily normals.

  ![daily-normals](Images/daily-normals.png)

* Close out your session.

## Rubric

[Unit 10 Rubric - SQLAlchemy Homework - Surfs Up!](https://docs.google.com/document/d/1gT29iMF3avSvJruKpcHY4qovP5QitgXePqtjC6XESI0/edit?usp=sharing)

- - -

## References

Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, [https://doi.org/10.1175/JTECH-D-11-00103.1](https://doi.org/10.1175/JTECH-D-11-00103.1)

- - -

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
