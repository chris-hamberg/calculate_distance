from math import radians, sin, cos, asin
from haversine import haversine, Unit
import numpy as np
from geopy import distance as vin


#RADIUS = 6372.8 # km
RADIUS = 6.371e6 # meters
#RADIUS = 6372.8e3 # wtf
#RADIUS = 3963 # miles

my_lat = 39.1114
my_lon = -84.4712

re_lat = 39.08961
re_lon = -84.4922799

vectors = [my_lat, my_lon, re_lat, re_lon]

expectation = '436.9641404452979' # in meters


def my_haversine(vectors):

    dlat   = np.radians(vectors[2] - vectors[0])
    dlon   = np.radians(vectors[3] - vectors[1])
    my_lat = np.radians(vectors[0])
    re_lat = np.radians(vectors[2])

    a = np.sin(dlat/2)**2 + np.cos(my_lat) * np.cos(re_lat) * np.sin(dlon/2)**2

    c = 2 * np.arcsin(np.sqrt(a))

    return c * RADIUS


def euclidean(vectors):

    c1 = convert(vectors[0], vectors[1])
    c2 = convert(vectors[2], vectors[3])

    return np.sqrt(
            (c2[0] - c1[0])**2 + (c2[1] - c2[1])**2 + (c2[2] - c1[2])**2
            )


def convert(lat, lon):

    lat, lon = np.deg2rad(lat), np.deg2rad(lon)
    R = RADIUS

    x = R * np.cos(lat) * np.cos(lon)
    y = R * np.cos(lat) * np.sin(lon)
    z = R * np.sin(lat)

    return x, y, z


def great_circle(vectors):
    my_lat, my_lon, re_lat, re_lon = map(np.radians, vectors)
    c = np.arccos(np.sin(my_lat) * np.sin(re_lat) + np.cos(my_lat) * \
            np.cos(re_lat) * np.cos(my_lon - re_lon))
    return c * RADIUS


def vincenty(vectors):
    org = tuple(vectors[:2])
    des = tuple(vectors[2:])
    return vin.distance(org, des)


print(f'Expected: {expectation}')
print(f'My Haversine Result: {my_haversine(vectors)}')
print(f'Euclidean Result: {euclidean(vectors)}')
print(f'Haversine Result: {haversine((vectors[0], vectors[1]), (vectors[2], vectors[3])) * 1000}')
print(f'Great Circle Result: {great_circle(vectors)}')
print(f'Vincenty Result: {vincenty(vectors) * 1000}')
