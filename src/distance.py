from math import acos, cos, radians, sin


# Earth Radius in Kilometers: https://en.wikipedia.org/wiki/Earth_radius
EARTH_RADIUS_KMS = 6371


def distance_between_points(lat1, long1, lat2, long2):
    """ Returns distance between point 1 with 'lat1','long1' and point 2 with
    'lat2','long2' https://en.wikipedia.org/wiki/Great-circle_distance#Formulae

    Parameters:
        lat1 (float): Latitude, in degrees, from the point 1
        long1 (float): Longitude, in degrees, from the point 1
        lat2 (float): Latitude, in degrees, from point 2
        long2 (float): Longitude, in degrees, from the point 2
    Returns:
        distance (float): Distance, between point 1 and point 2 in KMs
    """
    lat1 = float(lat1)
    lat2 = float(lat2)
    long1 = float(long1)
    long2 = float(long2)


    # Convert degrees to radians
    long1 = radians(long1)
    long2 = radians(long2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    # Delta between longitudes
    dlong = long2 - long1

    # Central angle between point 1 and point 2
    c = acos((sin(lat1)*sin(lat2) + cos(lat1) * cos(lat2) * cos(dlong)))

    # Distance, in KMs, is central angle * Earth radius
    return c * EARTH_RADIUS_KMS
