class Cpoint:
    
    def __init__(self, a, b):
        self.x = a
        self.y = b
        print('I am in initializing')
    
    
    def __str__(self):
       return '({0}, {1})'.format(self.x, self.y)
        
    def test(self):
        print('this is test')
    
         
        
point1 = Cpoint(10, 20)
point2 = Cpoint(20, 30)
point3 = Cpoint(5, 8 )

print(point1)
print(point2)
print(point3)


point3.test()
Cpoint.test(point3)
point1.z = 100
print (point1 , point1.z)
# print (point2 , point2.z)
del point1
# point1.test()
