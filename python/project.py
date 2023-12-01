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
    print("1) placeholder\n" +
          "2) placeholder 2\n" +
          "3) Exit\n" +
          "Please Enter What You Want to do: ", end='')
    return int(input())

def inputGeo():
    print("Please Enter the Latitude's Degrees, Minutes, and Seconds: ")
    lat = inputAngle()
    print("Please Enter the Longitude's Degrees, Minutes, and Seconds: ")
    lon = inputAngle()
    return GeoCoord(lat, lon)

def inputAngle():
    isNegative = False
    degs = int(input("Degrees: "))
    if degs < 0:
        degs = -degs
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
    geoCoord = inputGeo()
    degCoord = geoToDeg(geoCoord)
    print(f'{geoToString(geoCoord)} is {degCoord.latitude:.4f}°N\
 {degCoord.longitude:.4f}°W')

def convertGeoToDistance():
    geoCoord = inputGeo()
    degCoord1 = geoToDeg(geoCoord)

    geoCoord = inputGeo()
    degCoord2 = geoToDeg(geoCoord)

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
    theta = math.atan2(y, x)

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
