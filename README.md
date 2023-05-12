# Sun-Spot-Analyser-API
Overview

This is a Flask API for analysing sun spot data.

Setup
Prerequisites
Make sure you have the following installed on your machine:

Docker
Instructions
Clone the repository:

git clone https://github.com/raal-jr/sun-spot-analyser-api.git

Build the Docker image:

docker build -t sun-spot-analyser-api .

Run the Docker container:

docker run -p 5000:5000 sun-spot-analyser-api

This will start the Flask server inside the container, and map port 5000 of the container to port 5000 of your machine.

The API is now ready to use. You can make requests to it using your favorite HTTP client. For example, to create a new grid:


curl -X POST -H "Content-Type: application/json" -d '{"size": 3, "values": "1,2,3,4,5,6,7,8,9"}' http://localhost:5000/sun-spot-analyser-api/grid

This will return the ID of the newly created grid. To get the scores for the grid:

curl -X GET http://localhost:5000/sun-spot-analyser-api/scores?id=<grid_id>

Replace <grid_id> with the ID of the grid you want to get the scores for.

Notes
The Docker container exposes port 5000 by default. If you want to use a different port, you'll need to modify the docker run command accordingly.

The API is running in debug mode (debug=True). This is not recommended for production use. If you're deploying this API to production, make sure to turn off debug mode.
