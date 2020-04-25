class Rectangle():
    '''Represent a rectangular section of an image.'''
    
    def __init__(self, x0, y0, width, height):
        '''Create a rectangle with non-zero area. (x0,y0) is the
        lower left corner, width and height the X and Y extent.'''
        self.x0 = x0
        self.y0 = y0
        self.width = width
        self.height = height
        
    def area(self):
        '''Return the area of the rectangle.'''
        return self.width * self.height
    
    def contains(self, x, y):
        '''Return True if (x,y) point is inside a rectangle,
            and False otherwise.'''
        return (self.x0 <= x) and (x <= self.x0 + self.width) and \
                (self.y0 <= y) and (y <= self.y0 + self.height)

    def get_min_x(self):
        '''Return the minimum X coordinate.'''
        return self.x0
    
    def get_min_y(self):
        '''Return the minimum Y coordinate.'''
        return self.y0
    
    
    def get_max_x(self):
        '''Return the maximum X coordinate.'''
        return self.x0 + self.width
    
    
    def get_max_y(self):
        '''Return the maximum Y coordinate.'''
        return self.y0 + height
   
    def str1(self):
        '''str'''
        msg="({0}, {1}, {2}, {3})".format(self.x0,self.y0, self.width, self.height)
        return msg
    
    def __str__(self):
        '''__str__'''
        msg="({0}, {1}, {2}, {3})".format(self.x0,self.y0, self.width, self.height)
        return msg
        
    
    
r1 = Rectangle(10, 20, 50, 50)
r2 = Rectangle(4, 5, 12, 30)

print(r1.area())
print(r1.contains(15,35))
print(r1)
print(r1.str1())
print( "\t--------------------------\t\n")

import copy
# shallow copying
new_rec1 = copy.copy(r1)
# deep copying
new_rec2 = copy.deepcopy(r1)
print (new_rec1 is r1)
print(new_rec2 is r1)

# print(dir(Rectangle)) 
# print(dir(list))


# help(r1)
# print(help(list))
