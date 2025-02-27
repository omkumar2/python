
#or
import math

pi = 22/7

def area_Rectangle(l,b):
    return l*b

def areaCricle(r):
    return pi*r*r

def perimeterRectangle(l,b):
    return 2*(l+b)

def perimeterCricle(r):
    return 2*pi*r

polygon = ''
while (polygon != 'exit') :
    print('\nPOLYGONS\ncircle\nrectangle\nexit')
    polygon = input ('\nChoose the polygon type or exit: ')
    property =''
    if(polygon == 'circle') :
        r = float (input ('\nEnter the radius of the circle: ') )
        while (property == '') :
            print('\nCIRCLE PROPERTIES\narea\nperimeter\nback')
            property = input ('\nChoose the circle property or go back: ')
            if (property == 'area') :
                cArea = circlearea (r)
                print (f'Area of circle with radius {r} = {cArea} sq. units')
                property = ''   
            elif (property == 'perimeter') :
                cPerimeter = circle_perimeter (r)
                print (f'Perimeter of circle with radius {r} = {cPerimeter} unit')
                property = ''
            elif (property == 'back') :
                break
            else:
                print ('Please select the correct polygon property')
                property = ''
    elif (polygon == 'rectangle') :
                1 = float(input ('\nEnter the length of the rectangle: ') )
                b = float(input ('\nEnter the breadth of the rectangle: ') )
                while(property == ''):  
                    print('\nRECTANGLE PROPERTIES\narea\nperimeter\nback')
                    property = input ('\nChoose the rectangle property or go back: ')
                    if (property == 'area') :
                        rArea = rectangle_area (1, b)
                        print (f'Area of rectangle with length {1} and breadth {b} = {rArea} sq. units')
                        property = ''
                    elif (property == 'perimeter') :
                        rPerimeter = rectangle_perimeter (1, b)
                        print (f'Perimeter of rectangle with length {1} and breadth {b} = {rPerimeter} units')
                        property = ''
                    elif (property == 'back') :
                        break
                    else:
                        print ('Please select the correct polygon property')
                        property = ''
                
