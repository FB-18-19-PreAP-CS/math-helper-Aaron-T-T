from math import *

def slope(y1,y2,x1,x2):
#    y1 = float(input("Give Y1: "))
#    y2 = float(input("Give Y2: "))
#    x1 = float(input("Give X1: "))
#    x2 = float(input("Give X2: "))
    ''' Gets the inputs for the y1,y2,x1,and x2
        
        >>> slope(7,2,2,9)
        -5/7
        >>> slope(7,-8,3,-5)
        15/8
        >>> slope(0,0,0,0)
        0/0
            
    
    '''
    a = y2-y1
    b = x2 -x1
    if a < 0 and b < 0:
        a = a * -1
        b = b * -1
    print(f"{a}/{b}")

def distance(x1,x2,y1,y2):
    '''
        gets the distance from two points
        
        >>> distance(2,9,3,7)
        8.06
        >>> distance(0,0,0,0)
        0.0
        >>> distance(-2,2,3,-5)
        8.94
        
    '''
        
    dist = sqrt((x2-x1)**2+(y2-y1)**2)
    dist = round(dist,2)
    print(dist)
    
    
    




if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    
    