# Sun Spot Analyser API

Welcome to the Sun Spot Analyser API. This API allows you to create grids, calculate scores, retrieve cell values, and get top values from the sun spot data.

## Installation

1. Clone the repository:
   ```shell
   git clone https://github.com/your/repo.git
Install the dependencies:
shell
Copy code
pip install -r requirements.txt
Usage
Start the Flask server:

shell
Copy code
python app.py
Access the API endpoints:

POST /sun-spot-analyser-api/grid: Create a new grid.

Request Body:
json
Copy code
{
  "size": 3,
  "values": "4,2,3,2,2,1,3,2,1"
}
Example Request:
shell
Copy code
curl -X POST -H "Content-Type: application/json" -d '{"size": 3, "values": "4,2,3,2,2,1,3,2,1"}' http://localhost:5000/sun-spot-analyser-api/grid
Example Response:
json
Copy code
{
  "id": 1
}
GET /sun-spot-analyser-api/scores: Get scores for a grid.

Parameters:
id: The ID of the grid.
Example Request:
shell
Copy code
curl -X GET http://localhost:5000/sun-spot-analyser-api/scores?id=1
Example Response:
json
Copy code
{
  "scores": [
    {"x": 1, "y": 1, "score": 10},
    {"x": 1, "y": 2, "score": 14},
    {"x": 1, "y": 3, "score": 8},
    ...
  ]
}
GET /sun-spot-analyser-api/cell: Get the value of a cell in a grid.

Parameters:
id: The ID of the grid.
x: The X-coordinate of the cell.
y: The Y-coordinate of the cell.
Example Request:
shell
Copy code
curl -X GET http://localhost:5000/sun-spot-analyser-api/cell?id=1&x=2&y=2
Example Response:
json
Copy code
{
  "x": 2,
  "y": 2,
  "value": 2
}
GET /sun-spot-analyser-api/top: Get the top values from a grid.

Parameters:
id: The ID of the grid.
limit (optional): The maximum number of top values to retrieve (default: 5).
Example Request:
shell
Copy code
curl -X GET http://localhost:5000/sun-spot-analyser-api/top?id=1&limit=3
Example Response:
json
Copy code
{
  "top_values": [4, 3, 2]
}
Contributing
Fork the repository.
Create a new branch.
Make your changes and commit them.
Push your changes to your forked repository.
Create a pull request.
License
This project is licensed under the MIT License.
