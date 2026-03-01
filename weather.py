#!/usr/bin/env python3
"""
Simple Weather CLI Tool

A beginner-friendly Python project that fetches weather data using OpenWeatherMap API.
This project teaches you about:
- Making HTTP requests
- Handling JSON responses
- Command-line arguments
- Error handling
- Environment variables
"""

import requests
import sys
import json
from pathlib import Path


class WeatherFetcher:
    """Fetches weather data from OpenWeatherMap API."""
    
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    
    def __init__(self, api_key):
        """
        Initialize the weather fetcher.
        
        Args:
            api_key (str): Your OpenWeatherMap API key
        """
        self.api_key = api_key
    
    def get_weather(self, city, units="metric"):
        """
        Fetch weather data for a city.
        
        Args:
            city (str): Name of the city
            units (str): Temperature units - 'metric' (Celsius) or 'imperial' (Fahrenheit)
            
        Returns:
            dict: Weather data or None if request fails
        """
        try:
            params = {
                "q": city,
                "appid": self.api_key,
                "units": units
            }
            
            response = requests.get(self.BASE_URL, params=params, timeout=5)
            response.raise_for_status()  # Raise an error for bad status codes
            
            return response.json()
        
        except requests.exceptions.ConnectionError:
            print("Error: Unable to connect to the weather service. Check your internet connection.")
            return None
        except requests.exceptions.Timeout:
            print("Error: Request timed out. The service is taking too long to respond.")
            return None
        except requests.exceptions.HTTPError as e:
            if response.status_code == 404:
                print(f"Error: City '{city}' not found.")
            elif response.status_code == 401:
                print("Error: Invalid API key.")
            else:
                print(f"Error: HTTP {response.status_code}")
            return None


def format_weather(weather_data, city, units="metric"):
    """
    Format weather data for display.
    
    Args:
        weather_data (dict): Weather data from API
        city (str): City name
        units (str): Temperature units
        
    Returns:
        str: Formatted weather information
    """
    temp_symbol = "°C" if units == "metric" else "°F"
    
    temp = weather_data["main"]["temp"]
    feels_like = weather_data["main"]["feels_like"]
    description = weather_data["weather"][0]["description"].capitalize()
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]
    
    output = f"""
Weather in {city}
{'=' * 40}
Temperature: {temp}{temp_symbol}
Feels Like: {feels_like}{temp_symbol}
Condition: {description}
Humidity: {humidity}%
Wind Speed: {wind_speed} m/s
"""
    return output


def main():
    """Main function - entry point for the CLI tool."""
    
    if len(sys.argv) < 2:
        print("Usage: python weather.py <city_name> [--fahrenheit]")
        print("\nExample:")
        print("  python weather.py London")
        print("  python weather.py 'New York' --fahrenheit")
        sys.exit(1)
    
    city = sys.argv[1]
    units = "imperial" if "--fahrenheit" in sys.argv else "metric"
    
    # Get API key from environment variable
    api_key = os.environ.get("OPENWEATHER_API_KEY")
    
    if not api_key:
        print("Error: OPENWEATHER_API_KEY environment variable not set.")
        print("Get a free API key at: https://openweathermap.org/api")
        sys.exit(1)
    
    # Fetch and display weather
    fetcher = WeatherFetcher(api_key)
    weather_data = fetcher.get_weather(city, units)
    
    if weather_data:
        print(format_weather(weather_data, city, units))
    else:
        sys.exit(1)


if __name__ == "__main__":
    import os
    main()
