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

#def pointslope(y1,x1,m):
    
    
    




if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    
    