import datetime as dt
"""
-> Class: A piece of code from which you can generate a unique object, where
    each object is a single instance of the class.It’s customary to start a class
    name with an uppercase letter to help distinguish classes from variables. 
-> Object (Instance): One unit of data plus code generated from a class as an instance
    of that class. Each instance of a class is also called an object just like all the
    different cars are objects, all created by same car factory (class).
-> Attribute: A characteristic of an object that contains information about the
    object. Also called a property of the object.
-> Method: A Python function that’s associated with the class. It defines an
    action that object can perform. 
"""
# Define a class named Member for making member objects.
class Member:
    """ Create a member from uname and fname """
    
    #Set a default for free days.
    free_days = 90
    def __init__(self, uname, fname, uactive = True):
        """ The def is short for define, and __init__ is the name of a built-in Python method
        that’s capable of creating objects from within a class. The self part is just a variable name,
        and it is used to refer to the object being created at the moment. You can use the name 
        of your own choosing instead of self ."""
        # Define attributes and give them values.
        self.username = uname
        self.fullname = fname
        # Default date_joined to today's date.
        self.date_joined = dt.date.today()
        # Set is active to True initially
        self.is_active = uactive
        # Set an expiration date
        self.free_expires = dt.date.today() + dt.timedelta(days = Member.free_days)
        print('a new object is initiated!' , self)
        
    
    # Define methods as functions, use self for "this" object.
    def show_datejoined(self):
        """ A method to return a formatted string to show the date of joined """
        return f"{self.fullname} joined on {self.date_joined:%d/%m/%Y}"    
    # Method to activate (True) or deactivate (False) account.
    def activate(self, yesno):
        """ True for active, False to make inactive """
        self.is_active = yesno
            
        
    # Class methods follow @classmethods and use cls rather then self.
    @classmethod
    def setـfreedays(cls,days):
        """A class method is a method that is associated with the class as a whole, not specific
        instances of the class. In other words, class methods are similar in scope to 
        class variables in that they apply to the whole class and not just individual instances
        of the class."""
        cls.free_days = days
        
        
    @staticmethod
    def currenttime():
        """Static method is the same as any other method, but you don’t use self and 
        you don’t use cls . Becausea static method isn’t strictly tied to a class or object,
        except to the extent you want to keep it there for organizing your code."""
        now = dt.datetime.now()
        return f"{now:%I:%M %p}"

# Create an object from Member
new_person = Member('Mostafa' , 'Bastam')
new_person2 = Member('Mostafa' , 'Bastam')
new_person3 = new_person
print(new_person2 is new_person)
print(new_person3 is new_person)
print(new_person)
print(type(new_person))
print(new_person.username)
print(new_person.fullname)
print(new_person.date_joined)
print(new_person.free_expires)
print(new_person.is_active)
print('\t------------------------------\n')
new_person.username = "Ardavan"
# new_person.is_active = False
new_person.activate(False)
# new_person.activate(True)
# Member.activate(new_person, False) # ‌an alternative syntax
print(new_person.username)
print(new_person.is_active)
print(new_person.show_datejoined())
print(new_person.is_active)
print(new_person.free_days)
# new_person.free_days = 150
# print(new_person.free_days)

print(new_person.free_expires)

print('\t------------------------------\n')
# np = Member("Farhad", "Abasi", False)
# print (np.username)
# print(np.free_days)
Member.setـfreedays(120)

second_person = Member('Mary' , 'Anderson')
print(second_person.show_datejoined())
print(second_person.is_active)
print(second_person.free_days)
print(second_person.free_expires)

print('\t------------------------------\n')
third_person = Member('John' , 'Pit')
print(third_person.show_datejoined())
third_person.activate(False)
print(third_person.is_active)
print(third_person.free_days)
print(third_person.free_expires)
print('\t------------------------------\n')

# return a dictionary of object's attributes
print(second_person.__dict__)
   
print(Member.currenttime())
print(third_person.currenttime())
