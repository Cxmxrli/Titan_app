import requests
import asyncio
import winsdk.windows.devices.geolocation as wdg

#function to get the coridnates of the user using windows geolocator
async def getCoords(gen_lat, gen_lon):
    locator = wdg.Geolocator()
    pos = await locator.get_geoposition_async()
    gen_lat = pos.coordinate.latitude 
    gen_lon = pos.coordinate.longitude
    return gen_lat,gen_lon

#returns the location
def getLoc():
    try:
        return asyncio.run(getCoords())
    except PermissionError:
        print("ERROR: You need to allow applications to access you location in Windows settings")


def get_weather_conditions(lat, lon, api_key):
    # OpenWeatherMap API endpoint
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    # Parameters for the API request
    params = {
        'lat': lat,
        'lon': lon,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    
        
        
latitude = getCoords(gen_lat)   
longitude = getCoords(gen_lon)  
api_key = "4fdf1d2b85fa6d3fb20f7de7e966ce55"

get_weather_conditions(latitude, longitude, api_key)
    



