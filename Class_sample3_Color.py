class Color():
    '''An RGB color, with red, green and blue components.'''
    def __init__(self,r=0, g=0, b=0):
        '''A new color with red value r, green value g, and 
        blue value b.All components are integers in the range 0-255.'''
        self.red=r
        self.green=g
        self.blue=b
    
    def __str__(self):
        '''Return a string representation of this Color in the
        form of an RGBtuple.'''
        
        return '({0}, {1}, {2})'.format(self.red, self.green, self.blue)
    
    def __add__(self, other_color): #operator overloading
        '''Return a new Color made from adding the red, green, and blue
        components of this Color to Color other_color's components. If the
        sum is greater than 255, then the color is set to 255.'''
        
        return Color(min(self.red + other_color.red, 255),
                    min(self.green + other_color.green, 255),
                    min(self.blue + other_color.blue, 255))
        
    # def __add__(self, other_color):
    #     '''This is a bad way to define this method.'''
    #     self.red += other_color.red
    #     self.green += other_color.green
    #     self.blue += other_color.blue
    #     return self
        
        
    def __sub__(self, other_color):
        '''Return a new Color made from subtracting the red, green, and blue
        components of this Color from Color other_color's components. If
        the difference is less than 0, then the color is set to 0.'''
        return Color(max(self.red - other_color.red, 0),
                    max(self.green - other_color.green, 0),
                    max(self.blue - other_color.blue, 0))
       
       
    def __eq__(self, other_color):
        '''Return True if this Color' s components are equal to Color
        other_color's components.'''
        return self.red == other_color.red and \
            self.green == other_color.green and \
                self.blue == other_color.blue
        

# new_point=Color(100,30,22);
# print ('value of red={0}\nvalue of green={1}\nvalue of blue={2}'.format(new_point.red, new_point.green, new_point.blue) )     
# print(new_point)
purple = Color(128, 0, 128)
white = Color(255, 255, 255)
dark_grey = Color(50, 50, 50)
print (purple + dark_grey) #operator overloading
print (purple.__add__(dark_grey))
print (white == Color(255, 255, 255))
print (white - dark_grey)
print(dark_grey.__dict__)
# print(dir(white))
# help(Color)