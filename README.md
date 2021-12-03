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

A Flask API was created with following routes:

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

  ![daily-normals](Images/daily-normals.png)

#### Contact Info
* [Linkedin Link](https://www.linkedin.com/in/tamasree-sinha/)
* email id :tamasree.g@gmail.com