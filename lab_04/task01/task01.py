import random as rd
import math

def random_points(radius, x_center, y_center):
    x_point=rd.uniform(x_center-radius, x_center+radius)
    y_point=rd.uniform(y_center-radius, y_center+radius)
    check=math.sqrt( (x_point-x_center)**2 + (y_point-y_center)**2 )
    while check >= radius:
        x_point=rd.uniform(x_center-radius, x_center+radius)
        y_point=rd.uniform(y_center-radius, y_center+radius)
        check=math.sqrt( (x_point-x_center)**2 + (y_point-y_center)**2 )
    return (x_point,y_point)