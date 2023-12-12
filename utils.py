import numpy as np

def distance(pointA, pointB):
    '''
    Return euclidian dist between to points in a 2D space
    '''
    x = pointB[0] - pointA[0]
    y = pointB[1] - pointA[1]
    return np.sqrt(x**2 + y**2)

def vect(pointA, pointB):
    '''
    Return the vector AB
    '''
    x = pointA[0] - pointB[0]
    y = pointA[1] - pointB[1]
    return np.array([x,y])

def array_max_abs(array):
    ''' Works only for column vectors '''
    m=0
    for i in range(len(array)):
        x=abs(array[i])
        if x>m:
            m=x
    return m