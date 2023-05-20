# Sun Spot Analyser API

The Sun Spot Analyser API is a RESTful API that allows users to analyze areas of the Sun for thermal activity. It provides endpoints to create a grid of raw heat measurements and calculate the solar activity scores for each location on the grid.

Getting Started
These instructions will guide you on setting up and running the Sun Spot Analyser API on your local machine.

Prerequisites
Python 3.x
Flask (Python web framework)
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/raal-jr/sun-spot-analyser-api.git
Navigate to the project directory:
bash
Copy code
cd sun-spot-analyser-api
Install the dependencies:
Copy code
pip install -r requirements.txt
Usage
Start the Flask development server:
Copy code
python app.py
The API will now be accessible at http://localhost:5000/.
Endpoints
The API provides the following endpoints:

POST /sun-spot-analyser-api/grid: Create a new grid of raw heat measurements.
GET /sun-spot-analyser-api/scores: Get the solar activity scores for a specific grid.
Refer to the API documentation or the code comments for detailed information about the request and response payloads of each endpoint.

Example Usage
To create a new grid:

css
Copy code
$uri = "http://127.0.0.1:5000/sun-spot-analyser-api/grid"
$headers = @{
    "Content-Type" = "application/json"
}
$body = @{
    "size" = 3
    "values" = "4,2,3,2,2,1,3,2,1"
} | ConvertTo-Json

$response = Invoke-RestMethod -Uri $uri -Method POST -Headers $headers -Body $body
$response

To get the solar activity scores for the grid:

bash
Copy code
GET /sun-spot-analyser-api/scores?id=1

Running Tests
You can run the unit tests for the API using the following command:

Copy code
python -m unittest discover tests

Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

License
This project is licensed under the MIT License.
