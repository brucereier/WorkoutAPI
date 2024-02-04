# Overview

I decided to make this project using Django mainly because Django uses Python, which is a language I feel very comfortable using. Additionally, Django having a prebuilt ORM and a lot of helpful admin functions for the creation of the API was extremely helpful given the time constraint of this project. 

Some design decisions I made were to split the main three functionalities of the API, which were querying, aggregating data, and deleting into three separate endpoints. The main reason for this was for data security, as I initially had all of them under the same endpoint, but was concerned that, in a production environment, users could find ways to exploit the system and delete data from the database. I figured that it would be better to migrate the delete functionality to its own endpoint on which more restrictive access could be applied. Additionally, I also decided to make the parameters of API requests consistent across all endpoints to make it easier for developers to understand. All of the parameters are also optional, which makes it so that there are many possible filters you can apply to the data.

To run and test this API, simply clone the repo, install all dependencies, and start the API with python3 manage.py runserver. From there, access the API with some sort of testing software like Postman.

# Documentation

## Endpoints

### /api/workouts/

This endpoint is used for querying and adding entries
#### POST
- Used to add workout entries to the data set.
##### Parameters
- duration - Represents how long the workout was in time. String In format HH:MM:SS.
- distance - How far the workout was in terms of distance. Double amount that represents miles.
- route_name - The name the user has for the route they ran. Any String
- heart_rate - Heart rate in beats per minute. Integer Value
- date_time - Date and time of the Workout. String In Format YYYY-MM-DDTHH:MM:SSZ
- image - Can store an image for the workout. Uses Django's field for the formatting and storage of the image.

#### GET
- Used to query the database
##### Expected Output 
- A list of JSON objects representing all workouts that fall under the queries.
##### Parameters
- min_id - set a minimum id value to search for, integer value.
- max_id - set a maximum id value to search for, integer value
- start_date -set a start date for workouts to search for, format: YYYY-MM-DDTHH:MM:SSZ
- end_date = set an end date for workouts to search for, format: YYYY-MM-DDTHH:MM:SSZ
- route_name = route name to search for, any string
- min_distance = set a minimum distance to search for, double value
- max_distance = set a maximum distance to search for, double value
- min_duration = set a minimum duration to search for, double value
- max_duration = set a maximum duration to search for, double value

### /api/workouts/aggregated/
#### GET
- Will query the database and take aggregated stats over all of the workouts
##### Expected Output
- A JSON object containing:
	- The total duration of all of the workouts in seconds
	- The average duration of all of the workouts in seconds
	- The total distance of all of the workouts in miles
	- The average duration of all of the workouts in miles
	- The average heart rate of all of the workouts in bpm
	- The average pace of all of the workouts in minutes per mile

##### Parameters
- Exactly the same as GET in /api/workouts/(see above)

### api/workouts/delete
#### DELETE
- Will query the database and delete all of the workouts that match the query.
##### Expected Output
- None except a status 204 in the terminal on a successful deletion

##### Parameters
- Exactly the same as GET in /api/workouts/(see above)
