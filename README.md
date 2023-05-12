# Sun-Spot-Analyser-API

Prerequisites

Python 3.x

Docker (if you want to use a containerized application)

Installation

Clone the repository to your local machine.


Install the required Python packages using pip. Open a terminal window, navigate to the root directory of the project, and run:


Copy code

pip install -r requirements.txt

(Optional) If you want to use a containerized application, build the Docker image by running:

Copy code

docker build -t sun-spot-analyser .

Running the Application

To start the application, run:

Copy code

python app.py

(Optional) If you're using a containerized application, start the container by running:

arduino

Copy code

docker run -p 5000:5000 sun-spot-analyser

The API is now available at http://localhost:5000. You can use a tool like Postman to test the endpoints.

Endpoints

POST /sun-spot-analyser-api/grid

Create a new grid.


Request Body

json

Copy code

{

"size": 3,

"values": "1,2,3,4,5,6,7,8,9"

}

size: The size of the grid (integer).

values: A comma-separated list of integers representing the values of the cells in the grid. The length of the list should be size^2.

Response Body

json

Copy code

{

"id": 1

}

id: The ID of the newly created grid.

GET /sun-spot-analyser-api/scores?id={id}

Get the scores for a grid.

Request Parameters

id: The ID of the grid (integer).

Response Body

json

Copy code

{

"scores": [

{

"x": 2,

"y": 3,

"score": 21

},

{

"x": 2,

"y": 2,

"score": 20

},

{

"x": 1,

"y": 3,

"score": 18

},

{

"x": 3,

"y": 3,

"score": 18

},

{

"x": 1,

"y": 2,

"score": 17

},

{

"x": 3,

"y": 2,

"score": 17

},

{

"x": 2,

"y": 1,

"score": 14

},

{

"x": 1,

"y": 1,

"score": 13

},

{

"x": 3,

"y": 1,

"score": 13

}

]

}

scores: A list of dictionaries representing the scores for each cell in the grid. Each dictionary has the following keys:

x: The x-coordinate of the cell (integer).

y: The y-coordinate of the cell (integer).

score: The score for the cell (integer).
