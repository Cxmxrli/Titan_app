import requests
import asyncio
import winsdk.windows.devices.geolocation as wdg
from astropy.coordinates import EarthLocation, AltAz, get_sun, get_moon
from astropy.time import Time
import astropy.units as u
from astropy.coordinates import solar_system_ephemeris, get_body
import titan_gui as tgui
import astropy 
import datetime
import ephem 
import datetime
from suntime import Sun

#based on code by The_Redburn (https://stackoverflow.com/questions/44400560/using-windows-gps-location-service-in-a-python-script)


api_key = "4fdf1d2b85fa6d3fb20f7de7e966ce55"
      
#function to get the coridnates of the user using windows geolocator
async def get_coords():
    locator = wdg.Geolocator()
    pos = await locator.get_geoposition_async()
    gen_lat = pos.coordinate.latitude 
    gen_lon = pos.coordinate.longitude
    return [gen_lat, gen_lon]

#returns the location
def get_loc():
    try:
        return asyncio.run(get_coords())
    except PermissionError:
        return("ERROR: You need to allow applications to access you location in Windows settings")

#print (get_loc())


#using the users location to tell if planets are visible
latitude, longitude = get_loc()
#print (latitude)
#print (longitude)
#location iof the observer
observe_loc = EarthLocation(lat=latitude * u.deg, lon=longitude * u.deg)
'''

if latitude and longitude is not None:

    
    time = Time.now()
    altazframe = AltAz(obstime=time, location=observe_loc, pressure=0)
    
    with solar_system_ephemeris.set("builtin"):
        mur_planet = get_body('mercury', time, observe_loc)
    
        mercury_az=mur_planet.transform_to(altazframe)

        if mercury_az < 0 * u.deg:
            print("mercury not visible ")
        else:
            print("mecrury is visible ")
'''

#calculate the phase of the moon using eyphem, returned in float, 
#floats will show the associated moon phase

def get_moon_phase(date=None,):
    if date is None:
        date = datetime.datetime.now()

    moon = ephem.Moon(date)
    phase = moon.moon_phase
    phase = round(phase,2)
    moon_img = ("image_files\\moon_phases\\")
    if phase == 0:
        moon_img = ("image_files\\moon_phases\\1.png") # new moon
        moon_text = "New moon"
    elif 0 < phase < 0.25:
        moon_img = ("image_files\\moon_phases\\2.png") # waxing cresent
        moon_text = "Waxing cresent"
    elif phase == 0.25:
        moon_img = ("image_files\\moon_phases\\3.png") # first quarter
        moon_text = "First quarter"
    elif 0.25 < phase < 0.5:
        moon_img = ("image_files\\moon_phases\\4.png") # waxing gibbous
        moon_text = "Waxing gibbous"
    elif phase == 0.5:
        moon_img = ("image_files\\moon_phases\\5.png") # full moon 
        moon_text = "Full moon"
    elif 0.5 < phase < 0.75:
        moon_img = ("image_files\\moon_phases\\6.png") # waning gibbous
        moon_text = "Waning gibbous"
    elif phase == 0.75:
        moon_img = ("image_files\\moon_phases\\7.png") # last quarter
        moon_text = "Last quarter"
    elif 0.5 < phase < 0.75:
        moon_img = ("image_files\\moon_phases\\8.png") # warning cresent
        moon_text = "Warning cresent"
    else:
        moon_img = ("image_files\\moon_phases\\9.png") # error icon
        moon_text = "Error no data"
    return moon_img
    

def get_sunset(latitude,longitude):
    sun = Sun(latitude, longitude)
    sunrise = sun.get_sunset_time()
    sun_return = sunrise.strftime("%H:%M:%S")
    return (sun_return)

sen = get_sunset(longitude,latitude)
print (sen)
