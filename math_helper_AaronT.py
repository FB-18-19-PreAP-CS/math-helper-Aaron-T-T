from math import *

def slope(y1,y2,x1,x2):
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
def slopez():
    y1 = int(input('Input Y1: '))
    y2 = int(input('Input Y2: '))
    x1 = int(input('Input X1: '))
    x2 = int(input('Input X2: '))
    slope(y1,y2,x1,x2)
    

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
    
    
    
def distancez():
    y1 = int(input('Input Y1: '))
    y2 = int(input('Input Y2: '))
    x1 = int(input('Input X1: '))
    x2 = int(input('Input X2: '))
    distance(x1,x2,y1,y2)
    
    
    
def midpoint(x1,x2,y1,y2):
    '''
        It gets x coordinates and adds them and divides them by 2
        then gets the y coordinates and adds them and divides it by 2 and prints the midpoint
        
        
        >>> midpoint(7,15,22,2)
        11.0,12.0
        
        >>> midpoint(0,0,0,0)
        0.0,0.0
        
        >>> midpoint(-3,-42,-9,23)
        -22.5,7.0
        
    '''
    a = (x1 + x2)/2
    b = (y1 + y2)/2
    print(f'{a},{b}')

def midpointz():
    y1 = int(input('Input Y1: '))
    y2 = int(input('Input Y2: '))
    x1 = int(input('Input X1: '))
    x2 = int(input('Input X2: '))
    midpoint(x1,x2,y1,y2)
    
def sphere(r):
    '''
        gives the volume and surface area of a sphere
    >>> sphere(2)
    33.51
    50.27
    >>> sphere(3)
    113.1
    113.1
    >>> sphere(0)
    0.0
    0.0
    '''
    if r+1 == r: #catches a value like 1e100
        raise OverflowError("n is too large")
    a = 4/3*pi
    v = a*(r**3)
    v = round(v,2)
    
    sa = 4*pi*r**2
    sa = round(sa,2)
    print(f'{v}')
    print(f'{sa}')
    
def spherez():
    r = int(input('Input radius: '))
    
    sphere(r)
    


def main():
    print('Please pick the formula you would like to use')
    print(' ')
    print('Slope    formula: 1')
    print('Distance formula: 2')
    print('Midpoint formula: 3')
    print('Sphere   formula: 4')
    print('Quit: 0')
    a = str(input('pick which formula you want to use: '))
    if a == '1':
        slopez()
    elif a == '2':
        distancez()
    elif a == '3':
        midpointz()
    elif a == '4':
        spherez()
    elif a == '0':
        print(a)
        
    
    while a != '1' or a != '2' or a != '3' or a != '4':
        print('That is not a formula option')
        print(' ')
        print(' ')
        main()
    
          
    
    




if __name__ == "__main__":
    #import doctest
    #doctest.testmod()
    main()
    
    
    