import datetime as dt

# Base class is used for all kinds of Members.
class Member:
    """ The Member class attributes and methods are for everyone """
    # By default, a new account expires in one year (365 days)
    expiry_days = 365
    # Initialize a member object.
    def __init__(self, firstname, lastname):
        ''' init in supper class'''
        # Attributes (instance variables) for everybody.
        self.firstname = firstname
        self.lastname = lastname
        # Calculate expiry date from today's date.
        self.expiry_date = dt.date.today() + dt.timedelta(days = self.expiry_days)

    # Method in the base class
    def show_expiry(self):
        return f"{self.firstname} {self.lastname} expires on {self.expiry_date}"
    
    def get_status(self):
        return f"{self.firstname} is a Member."

user = Member('Sara', 'Brown')
print(user.firstname, user.lastname, user.expiry_date)
print(user.get_status())
print(user.show_expiry())

print('\t--------------1-----------------\n\n')

# Subclass for Admins.
class Admin(Member):
    # Admin accounts don't expire for 100 years.
    expiry_days = 365.2422 * 100
    # Subclass parameters
    def __init__(self, firstname, lastname, secret_code):
        """ init in subclass"""
        # Pass Member parameters on up to Member class
        super().__init__(firstname, lastname)
        # Assign the remaining parameters to this object
        self.secret_code = secret_code
    
    def get_status(self):
        return f"{self.firstname} is an Admin."
        

# Subclass for Users.
class User(Member):
    # pass
    def get_status(self):
        return f"{self.firstname} is a regular User."


user_A = Admin('Hamid', 'Ahmadi', '123!@#asd')
print(user_A.firstname, user_A.lastname, user_A.expiry_date)
print(user_A.secret_code)
print(user_A.show_expiry())
print(user_A.get_status())

print('\t--------------2-----------------\n\n')

user_C = User('sara', 'naghavi')
print(user_C.firstname, user_C.lastname, user_C.expiry_date)
print(user_C.show_expiry())
print(user_C.get_status())
#  __class__ is an atribute for an object that it returns the name of class
print(user_C.__class__)
#  __bases__ is an atribute for a class that returns the parent(base) calss
print(User.__bases__)
print(Member.__bases__)
x = 10
print(x.__class__)
print(int.__base__)
print(__name__)

# help(Admin)
# print(Admin.__dict__)