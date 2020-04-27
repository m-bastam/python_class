class Cpoint:
    
    def __init__(self, a, b):
        self.x = a
        self.y = b
    
    def __str__(self):
        return f"({self.x},{self.y})"
       
    
    
class Rectangle():
    '''Represent a rectangular section of an image.'''
    
    def __init__(self, point, width, height):
        '''Create a rectangle with non-zero area. (x0,y0) is the
        lower left corner, width and height the X and Y extent.'''
        # self.x0 = point.x
        # self.y0 = point.y
        self.point = point
        self.width = width
        self.height = height
        
    def area(self):
        '''Return the area of the rectangle.'''
        return self.width * self.height
    
    def contains(self, new_point):
        '''Return True if (x,y) point is inside a rectangle,
            and False otherwise.'''
        return (self.point.x <= new_point.x) and (new_point.x <= self.point.x + self.width) and \
                (self.point.y <= new_point.y) and (new_point.y <= self.point.y + self.height)

    def get_min_x(self):
        '''Return the minimum X coordinate.'''
        return self.point.x
    
    def get_min_y(self):
        '''Return the minimum Y coordinate.'''
        return self.point.y
    
    
    def get_max_x(self):
        '''Return the maximum X coordinate.'''
        return self.point.x + self.width
    
    
    def get_max_y(self):
        '''Return the maximum Y coordinate.'''
        return self.point.y + height
   
    # def str1(self):
    #     '''str'''
    #     msg="({0}, {1}, {2}, {3})".format(self.x0,self.y0, self.width, self.height)
    #     return msg
    
    def __str__(self):
        '''__str__'''
        
        msg = f"({self.point}, {self.width}, {self.height})"
        return msg
        
    

point1 = Cpoint(10, 20)    
r1 = Rectangle(point1, 50, 50)
point2 = Cpoint(4, 5)
r2 = Rectangle(point2, 12, 30)

print(r1.area())
print(r1.contains(Cpoint(15,35)))
print(r1)

print(r2.area())
print(r2.contains(Cpoint(25,35)))
print(r2)
print(r2.get_max_x())
print( "\t--------------------------\t\n")

rec1 = r1
print (rec1 is r1)
rec1.point = Cpoint(50, 50)
print (rec1.point)
print(r1.point)

print("\t---------------------------\n")
import copy
# shallow copying
new_rec1 = copy.copy(r1)
print (new_rec1 is r1)
print(r1.point)
new_rec1.point = Cpoint(100, 100)
print(new_rec1.point)
print(r1.point)

print("\t---------------------------\n")
# deep copying
new_rec2 = copy.deepcopy(r1)
print(new_rec2 is r1)
print(r1.point)
new_rec2.point = Cpoint(200, 200)
print(new_rec2.point)
print(r1.point)
