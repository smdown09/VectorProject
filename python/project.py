# Team #9
# Names: Seth Bohannon, Sam Downs, Kristina Nguyen, Gia Patel
# Date: 2023-12-01
# Section: 03

from dataclasses import dataclass
import math

@dataclass
class Angle:
    degrees: int
    minutes: int
    seconds: float
    isNegative: bool

@dataclass
class GeoCoord:
    latitude: Angle
    longitude: Angle

def mainMenu():
    print("1) dms to Decimal\n" +
          "2) Coordinates to Vector\n" +
          "3) Exit\n",
          end="")
    return int(input("Please Enter What You Want to do: "))

def inputGeo():
    lat = float(input("Please input the latitude: "))
    long = float(input("Please input the longitude: "))
    return GeoCoord(lat, long)

def inputAngle():
    isNegative = False
    degs = int(input("Degrees: "))
    if degs < 0:
        isNegative = True
    mins = int(input("Minutes: "))
    secs = float(input("Seconds: "))
    return Angle(degs, mins, secs, isNegative)

def angleToDecimal(angle):
    decimal = angle.degrees
    fraction = angle.minutes / 60 + angle.seconds / 3600
    if angle.isNegative:
        decimal -= fraction
    else:
        decimal += fraction
    return decimal

def geoToDeg(coord):
    return GeoCoord(
        angleToDecimal(coord.latitude),
        angleToDecimal(coord.longitude))

def angleToString(angle):
    return f'{angle.degrees}°{angle.minutes:02d}′{angle.seconds:02.3f}″'

def geoToString(geo):
    lat = f'{angleToString(geo.latitude)}{"S" if geo.latitude.isNegative else "N"}'
    lon = f'{angleToString(geo.longitude)}{"E" if geo.longitude.isNegative else"W"}'

    return f'{lat} {lon}'

def convertGeoToDeg():
    angle = inputAngle()
    decimal = angleToDecimal(angle) 
    print(f'{angleToString(angle)} is {decimal:.4f}°')

def convertGeoToDistance():
    latitude = float(input("Please input Latitude 1: "))
    longitude = float(input("Please input Longitude 1: "))
    degCoord1 = GeoCoord(latitude, longitude)

    latitude = float(input("Please input Latitude 2: "))
    longitude = float(input("Please input Longitude 2: "))
    degCoord2 = GeoCoord(latitude, longitude)
    

    angle = math.acos(math.sin(math.radians(degCoord1.latitude)) *
                      math.sin(math.radians(degCoord2.latitude))
                      +
                      math.cos(math.radians(degCoord1.latitude)) *
                      math.cos(math.radians(degCoord2.latitude)) *
                      math.cos(math.radians(math.fabs(
                          degCoord1.longitude -
                          degCoord2.longitude))))
    distance = 6371009 * angle

    diffCoord = GeoCoord(degCoord2.latitude - degCoord1.latitude,
                         degCoord2.longitude - degCoord1.longitude)
    x = diffCoord.longitude * (40000000 / 360)
    y = diffCoord.latitude * (40000000 / 360)
    R = (y ** 2 + x ** 2) ** .5
    theta = math.degrees(math.atan2(y, x))

    print("Resultant Vector:")
    print(f'  Components: ({x:.2f}î, {y:.2f}ĵ) m')
    print(f'  R:           {R:.2f} m')
    print(f'  θ:           {theta:.2f}°')

state = 0
while state != 3:
    state = mainMenu()
    match state:
        case 1:
            convertGeoToDeg()
        case 2:
            convertGeoToDistance()
