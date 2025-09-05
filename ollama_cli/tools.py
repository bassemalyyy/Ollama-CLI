import geocoder
import os
from dotenv import load_dotenv
import requests
import json , datetime
import pytz

def location():
    """Get location based on public IP."""
    g = geocoder.ip('me')
    return g.address if g.ok and g.address else "Address not found."

def search(query: str) -> str:
    """Perform a web search using Serper.dev."""
    # Load environment variables
    load_dotenv()
    SERPER_API_KEY = os.getenv("SERPER_API_KEY")
    
    if not SERPER_API_KEY:
        return "Search API key not configured. Please set SERPER_API_KEY environment variable."
        
    try:
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {
                'X-API-KEY': SERPER_API_KEY,
                'Content-Type': 'application/json'
            }
            
        response = requests.post(url, headers=headers, data=payload)
            
        if response.status_code == 200:
            results = response.json()
                
            if "organic" not in results or not results["organic"]:
                return f"No search results found for '{query}'."
                
            formatted_results = []
                # Get search time
            search_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # Show more results (5 instead of 3)
            for idx, result in enumerate(results["organic"][:5], 1):
                title = result.get("title", "No title")
                link = result.get("link", "No link")
                snippet = result.get("snippet", "No description")
                formatted_results.append(f"{idx}. {title}\nURL: {link}\nDescription: {snippet}\n")
                
            return f"Search results as of {search_time}:\n\n" + "\n".join(formatted_results)
        else:
            return f"Error searching for '{query}'. Status code: {response.status_code}"
    except Exception as e:
        return f"Error performing search for '{query}'. Please try again later."
    
def Time(location: str = None):
    """Get the current date and time in Egypt, which all share a single timezone."""
    display_location = location if location else "Egypt"
    tz = pytz.timezone('Africa/Cairo')
    current_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
    return f"The current time in {display_location} is {current_time}"

def get_weather(location: str = 'egypt', query: str = None) -> str:
    """Get weather for a location using OpenWeatherMap API."""
    # Use 'query' if 'location' is not provided
    if not location and query:
        location = query
    elif not location and not query:
        location = 'egypt'

    # Load environment variables
    load_dotenv()
    OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")

    if not OPENWEATHERMAP_API_KEY:
        return "Weather API key not configured. Please set OPENWEATHERMAP_API_KEY environment variable."
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPENWEATHERMAP_API_KEY}&units=metric"
        response = requests.get(url)
            
        if response.status_code == 200:
            data = response.json()
            temp = data["main"]["temp"]
            condition = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            return f"Weather in {location}: {condition.capitalize()}, {temp}°C, Humidity: {humidity}%"
        else:
            return f"Weather data for {location} not available. Error: {response.status_code}"
    except Exception as e:
        return f"Error getting weather for {location}. Please check the location name and try again."
