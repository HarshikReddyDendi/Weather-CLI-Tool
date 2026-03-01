Weather CLI Tool 🌤️
A beginner-friendly Python project that fetches and displays weather information from the command line.
Learning Objectives
This project teaches you:

Making HTTP requests with the requests library
Working with JSON data
Building command-line interfaces (CLI)
Error handling and exception management
Writing unit tests with unittest
Using environment variables
Project structure and organization
Using APIs

Features

Fetch real-time weather data for any city
Display temperature, humidity, wind speed, and conditions
Support for both Celsius and Fahrenheit
Error handling for network issues and invalid cities
Fully tested with unit tests
Clean, documented code

Project Structure
weather_cli_tutorial/
├── weather.py           # Main weather tool
├── test_weather.py      # Unit tests
├── requirements.txt     # Project dependencies
├── .gitignore          # Git ignore rules
├── LICENSE             # MIT License
└── README.md           # This file
Getting Started
Prerequisites

Python 3.7 or higher
pip (Python package manager)
Free OpenWeatherMap API key (see Setup section)

Setup

Clone the repository

bash   git clone https://github.com/yourusername/weather_cli_tutorial.git
   cd weather_cli_tutorial

Create a virtual environment (recommended)

bash   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate

Install dependencies

bash   pip install -r requirements.txt

Get an API key

Visit OpenWeatherMap
Sign up for a free account
Generate an API key from your account dashboard


Set the API key as an environment variable

bash   # On Windows (Command Prompt):
   set OPENWEATHER_API_KEY=your_api_key_here
   
   # On Windows (PowerShell):
   $env:OPENWEATHER_API_KEY='your_api_key_here'
   
   # On macOS/Linux:
   export OPENWEATHER_API_KEY=your_api_key_here
Usage
Basic Usage
Get weather for a city in Celsius (default):
bashpython weather.py London
Output:
Weather in London
========================================
Temperature: 15.5°C
Feels Like: 14.2°C
Condition: Partly Cloudy
Humidity: 65%
Wind Speed: 3.5 m/s
Using Fahrenheit
bashpython weather.py "New York" --fahrenheit
Examples
bash# Get weather for Tokyo
python weather.py Tokyo

# Get weather for Paris in Fahrenheit
python weather.py Paris --fahrenheit

# City names with spaces should be quoted
python weather.py "San Francisco"
Running Tests
Run all unit tests:
bashpython -m pytest test_weather.py -v
Run a specific test:
bashpython -m pytest test_weather.py::TestWeatherFetcher::test_get_weather_success -v
See test coverage:
bashpip install pytest-cov
pytest test_weather.py --cov=weather
Code Explanation
Main Components
WeatherFetcher Class

Handles all API communication
Uses the requests library to make HTTP requests
Implements error handling for various failure scenarios
Returns JSON data or None on failure

pythonfetcher = WeatherFetcher(api_key)
weather_data = fetcher.get_weather("London", units="metric")
format_weather Function

Takes raw API response and formats it for display
Handles both metric and imperial units
Returns nicely formatted string

main Function

Entry point for the CLI application
Parses command-line arguments
Orchestrates the fetching and display of weather data

Error Handling
The tool handles several error scenarios:

Connection Error: No internet or API server is down
Timeout: Request takes too long
HTTP 404: City not found
HTTP 401: Invalid API key
Invalid Input: Wrong command-line arguments

Learning Path

Start here: Run the tool with different cities
Explore the code: Read through weather.py and understand each function
Check the tests: Look at test_weather.py to see how testing works
Modify it: Try adding features like:

Multiple cities forecast
Save favorite cities to a file
Convert temperature between units
Display weather icons
Add caching to reduce API calls



Common Issues
"OPENWEATHER_API_KEY not set"
Make sure you've set the environment variable correctly. Test it with:
bash# On Windows:
echo %OPENWEATHER_API_KEY%

# On macOS/Linux:
echo $OPENWEATHER_API_KEY
"City not found"

Check spelling of the city name
Use official English city names
Some small cities might not be in the database

"Invalid API key"

Verify the API key is correct
Make sure you copied the entire key
Check that the key is for the free tier API

Contributing
Have ideas for improvements? Great! You can:

Fork the repository
Create a feature branch (git checkout -b feature/amazing-feature)
Make your changes
Run tests to ensure everything works
Commit your changes (git commit -m 'Add amazing feature')
Push to the branch (git push origin feature/amazing-feature)
Open a Pull Request

License
This project is licensed under the MIT License - see the LICENSE file for details.
Resources

OpenWeatherMap API Documentation
Python Requests Library
Python unittest Documentation
Real Python - Making HTTP Requests
