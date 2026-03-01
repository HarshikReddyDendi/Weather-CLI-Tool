"""
Unit tests for the Weather CLI Tool.

This demonstrates testing best practices in Python using the unittest module.
Run tests with: python -m pytest test_weather.py
"""

import unittest
from unittest.mock import patch, MagicMock
import json
from weather import WeatherFetcher, format_weather


class TestWeatherFetcher(unittest.TestCase):
    """Test cases for the WeatherFetcher class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.fetcher = WeatherFetcher("test_api_key")
        self.sample_response = {
            "main": {
                "temp": 15.5,
                "feels_like": 14.2,
                "humidity": 65
            },
            "weather": [{"description": "partly cloudy"}],
            "wind": {"speed": 3.5}
        }
    
    @patch('requests.get')
    def test_get_weather_success(self, mock_get):
        """Test successful weather API call."""
        mock_response = MagicMock()
        mock_response.json.return_value = self.sample_response
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        result = self.fetcher.get_weather("London")
        
        self.assertIsNotNone(result)
        self.assertEqual(result["main"]["temp"], 15.5)
    
    @patch('requests.get')
    def test_get_weather_city_not_found(self, mock_get):
        """Test handling of city not found error."""
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = Exception("404")
        mock_get.return_value = mock_response
        
        # Should return None and print error message
        result = self.fetcher.get_weather("InvalidCity123")
        # Note: In a real project, you'd handle this differently
    
    @patch('requests.get')
    def test_get_weather_timeout(self, mock_get):
        """Test handling of connection timeout."""
        import requests
        mock_get.side_effect = requests.exceptions.Timeout()
        
        result = self.fetcher.get_weather("London")
        self.assertIsNone(result)


class TestFormatWeather(unittest.TestCase):
    """Test cases for the format_weather function."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.sample_data = {
            "main": {
                "temp": 20,
                "feels_like": 18,
                "humidity": 70
            },
            "weather": [{"description": "clear sky"}],
            "wind": {"speed": 2.5}
        }
    
    def test_format_weather_celsius(self):
        """Test weather formatting in Celsius."""
        result = format_weather(self.sample_data, "London", "metric")
        self.assertIn("°C", result)
        self.assertIn("London", result)
        self.assertIn("20", result)
    
    def test_format_weather_fahrenheit(self):
        """Test weather formatting in Fahrenheit."""
        result = format_weather(self.sample_data, "New York", "imperial")
        self.assertIn("°F", result)
        self.assertIn("New York", result)
    
    def test_format_weather_contains_all_info(self):
        """Test that formatted output contains all weather information."""
        result = format_weather(self.sample_data, "Paris", "metric")
        self.assertIn("Temperature", result)
        self.assertIn("Humidity", result)
        self.assertIn("Wind Speed", result)
        self.assertIn("Clear sky", result)


if __name__ == "__main__":
    unittest.main()
