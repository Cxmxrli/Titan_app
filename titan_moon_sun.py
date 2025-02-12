import requests
import asyncio
import winsdk.windows.devices.geolocation as wdg
from astropy.coordinates import EarthLocation, AltAz, get_sun, get_moon
from astropy.time import Time
import astropy.units as u
from astropy.coordinates import solar_system_ephemeris, get_body
from datetime import datetime
import ephem 
import datetime
from suntime import Sun

api_key = "4fdf1d2b85fa6d3fb20f7de7e966ce55"
      
#based on code by The_Redburn 
#(https://stackoverflow.com/questions/44400560/using-windows-gps-location-service-in-a-python-script)
#function to get the coridnates of the user using windows geolocator ator
async def get_coords():
    locator = wdg.Geolocator()
    pos = await locator.get_geoposition_async()
    gen_lat = pos.coordinate.latitude 
    gen_lon = pos.coordinate.longitude
    return [gen_lat, gen_lon]

#returns the location of the user relative to their long and lat
#using windows geolocator
def get_loc():
    try:
        #uses asyncio to get coorids with wdg.geolocator
        return asyncio.run(get_coords())
    except PermissionError:
        #returns error in terminal if location settings are disabled on windows
        print("ERROR: You need to allow applications to access you location in Windows settings")


print (get_loc())



#using the users location to tell if planets are visible
user_latitude, user_longitude = get_loc()#gets location from the function

#location on earth using the lat and lon
observe_loc = EarthLocation(lat=user_latitude * u.deg, lon=user_longitude * u.deg)

#current date and current location
date_time = datetime.datetime.now()
observer = ephem.Observer()
observer.lon, observer.lat = get_loc()

observer_date = date_time     
moon = ephem.Moon()

#returns the horizon location
moon.compute(observer)
print("%s" % (moon.alt))
if moon.alt < 0:
    print(f"moon is not visible at {observer_date}")
else:
    print(f"moon is visible at {observer_date}")

#checks the file path, its length and if folder is empty

#calculate the phase of the moon using eyphem, returned in float, 
#floats will show the associated moon phase

def get_moon_phase(date=None):
    if date is None:
        date = datetime.datetime.now()#sets date to now, if date not found

    #using eyhpem to define the moons data
    moon = ephem.Moon(date)
    moon_phase = round(moon.moon_phase,2)
    
    #dictionary containg moon phases
    phases = {
        0.00: ("image_files\\moon_phases\\1.png", "New moon"),
        0.25: ("image_files\\moon_phases\\3.png", "First quarter"),
        0.50: ("image_files\\moon_phases\\5.png", "Full moon"),
        0.75: ("image_files\\moon_phases\\7.png", "Last quarter"),
    }
      
    #phases in between main four with names and images being returned
    if moon_phase in phases:
        return phases[moon_phase]
    elif 0.00 < moon_phase < 0.25:
        return "image_files\\moon_phases\\2.png", "Waxing crescent"
    elif 0.25 < moon_phase< 0.50:
        return "image_files\\moon_phases\\4.png", "Waxing gibbous"
    elif 0.50 < moon_phase < 0.75:
        return "image_files\\moon_phases\\6.png", "Waning gibbous"
    elif 0.75 < moon_phase < 1.00:
        return "image_files\\moon_phases\\8.png", "Waning crescent"
    else:
        return "image_files\\moon_phases\\9.png", "Error no data"

m_img,m_txt = get_moon_phase()
print(m_txt)

def get_sunset(user_latitude,user_longitude):
    sun = Sun(user_latitude, user_longitude)
    sunrise = sun.get_sunset_time()
    sun_return = sunrise.strftime("%H:%M")
    return sun_return




