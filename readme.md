Flight Booking API
Introduction

This Flask application provides a RESTful API for managing flight bookings. Users can interact with the API through HTTP requests to:

Retrieve information about all available flights
View existing bookings
Add new bookings
Filter flights based on price
Dependencies

The application relies on the following libraries:

Flask: Web framework for creating web applications (https://flask.palletsprojects.com/)
Flask-MySQLdb: Extension for interacting with MySQL databases ([invalid URL removed])
Config: Custom configuration file (location to be specified)
utils.py: Contains utility functions for interacting with the database and handling logic (location to be specified)
Configuration

Create a config.py file in your project directory and define the following configuration variables:

Python
MYSQL_HOST = "localhost"  # Replace with your MySQL host address
MYSQL_USER = "your_username"  # Replace with your MySQL username
MYSQL_PASSWORD = "your_password"  # Replace with your MySQL password
MYSQL_DB = "your_database_name"  # Replace with your MySQL database name
Use code with caution.

API Endpoints

/all-flights (GET):

Retrieves a list of all available flights from the database.
This endpoint utilizes the allFlights function from utils.py.
/all-bookings (GET):

Fetches a list of all existing bookings from the database.
The allBookings function in utils.py handles this operation.
/add-bookings (POST):

Allows users to add new booking entries.
Requires a JSON request body containing booking details.
This is processed by the addBooking function in utils.py.
/price (POST):

Enables users to search for flights within a specific price range.
Requires a JSON request body with price criteria.
The getByPriceUtil function from utils.py filters flights based on price.
Deployment

Install required dependencies:

Bash
pip install Flask Flask-MySQLdb
Use code with caution.

Configure the application (replace placeholders in config.py).

Run the API:

Bash
python app.py  # Replace with your main application file name
Use code with caution.

This starts the API server on http://localhost:5000/ in debug mode.

Further Enhancements

Authentication: Implement user authentication to restrict access to sensitive data or actions.
Error Handling: Employ more robust error handling to provide informative feedback to users when requests fail.
Documentation: Provide detailed API documentation outlining request parameters, response structures, and error codes.
Validation: Validate user inputs to ensure data integrity.
Testing: Write comprehensive unit and integration tests to ensure code quality and reliability.
By following these recommendations, you can create a well-structured, documented, and secure Flask application for flight booking management.