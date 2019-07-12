from math import pi


def degrees_to_radians(degrees):
    """ Converts Degrees to Radians: https://en.wikipedia.org/wiki/Radian#Conversion_between_radians_and_degrees
    Parameters:
        degrees (int): Degrees to be converted
    Returns:
        radians (float): Degrees 'degrees' converted to Radians
    """
    return degrees * pi / 180
