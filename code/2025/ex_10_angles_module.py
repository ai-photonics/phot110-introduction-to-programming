from numpy import sin, asin, deg2rad, rad2deg


def calc_reflection_angle(angle_inc):
    """Calculate the reflected angle of light incident at an interface

    :param angle_inc: Incident angle in degrees
    :return: reflected angle
    """
    angle_reflection = -angle_inc

    return angle_reflection


def calc_refraction_angle(angle_inc, n1, n2):
    """Calculate the refracted angle of light incident at an interface

    :param angle_inc: Incident angle in degrees
    :return: refracted angle
    """

    angle_inc_rad = deg2rad(angle_inc)
    angle_refraction = rad2deg(asin(n1/n2 * sin(angle_inc_rad)))

    return angle_refraction
