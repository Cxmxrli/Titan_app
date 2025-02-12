import ephem
from titan_moon_sun import get_loc, get_sunset #importing location function from titan_moon_sun
import datetime
import math


#list of all planets in out solarsystem (barring earth for obvios reasons)
#ephem."planet" allows the visibiity to be checked for each one
planets = [
    ephem.Mercury(),#mercury
    ephem.Venus(),#venus
    ephem.Mars(),#mars
    ephem.Jupiter(),#jupiter
    ephem.Saturn(),#saturn
    ephem.Uranus(),#uranus
    ephem.Neptune()#neptune
    ]

def get_planets():
    #assigns data from get_loc to user_logitude/user_latitude
    user_latitude, user_longitude = get_loc()

    #observer fucntion in ephem, to calculate planet positon
    #based on calculated user location
    user_observer = ephem.Observer()
    user_observer.name = "username"#will replace with users username
    user_observer.lon = user_longitude
    user_observer.lat = user_latitude
    #set to sea level as i cannot calulatw user elevation
    user_observer.elevation = 2000

    user_observer.date = datetime.datetime.now()#current user date
    sunset = get_sunset(user_longitude, user_latitude)

    sun = ephem.Sun()
    sun.compute(user_observer)
    sun_alt = sun.alt
    sunset_tf = False
    if sun_alt < 0:
        sunset_tf = True
        print ("sun is set")
        min_altitude = 10. *math.pi / 180
        for planet in planets:
            planet.compute(user_observer),
            if planet.alt > min_altitude:
                print (f"{planet}, is currently visible")
            else:
                print (f"{planet}, is not visible")
    else:
        sunset_tf = False
        print("sun has not set")
        for planet in planets:
            print (f"{planet}, is not visible")


