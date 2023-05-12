# Sun-Spot-Analyser-API

Requirements
Python 3.6 or higher
Flask
SQLite3
Installation
Clone the repository to your local machine
Install the dependencies using pip: pip install -r requirements.txt
Usage
Start the application by running python app.py. This will start a development server on http://localhost:5000.
Use a tool such as Postman or cURL to send POST requests to http://localhost:5000/sun-spot-analyser-api/grid to create a new grid. The request body should be a JSON object with the following structure:
{
  "size": <integer>,
  "values": "<comma-separated list of integers>"
}
  
Example request body:
{
  "size": 3,
  "values": "1,2,3,4,5,6,7,8,9"
}
  
Example response:
{
  "id": 1
}
  
Use a tool such as Postman or cURL to send GET requests to http://localhost:5000/sun-spot-analyser-api/scores?id=<grid_id> to get the scores for a grid. Replace <grid_id> with the ID of the grid you want to get the scores for. Example request URL:

http://localhost:5000/sun-spot-analyser-api/scores?id=1
Example response:
{
  "scores": [
    {"x": 2, "y": 2, "score": 25},
    {"x": 3, "y": 2, "score": 24},
    {"x": 2, "y": 1, "score": 20},
    {"x": 3, "y": 1, "score": 19},
    {"x": 1, "y": 2, "score": 18},
    {"x": 1, "y": 3, "score": 15},
    {"x": 2, "y": 3, "score": 14},
    {"x": 3, "y": 3, "score": 13},
    {"x": 1, "y": 1, "score": 11}
  ]
}
  
Dockerization
Build the Docker image using the Dockerfile provided: docker build -t sun-spot-analyser-app .
Run the Docker container: docker run -p 5000:5000 sun-spot-analyser-app
Note: It's recommended to use environment variables to set configuration variables like DB URI, password, etc. instead of hardcoding them into the code or Dockerfile.
