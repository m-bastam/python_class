def f1(id:int , score:float) -> str:
    ''' to suggest programer input and output type '''
    
    print(f1.__annotations__)
    return str(id)

def f2( **args ):
    """ Pass in any number of arguments Inside the function,
     they treated as a dictionary named args """
    for key,value in args.items():
        print(key , " = " ,value)
    print(args.get('family'))

def f3(*args):
    """ Pass in any number of arguments separated by commas
    Inside the function, they treated as a tuple named args """
    print(args)
    print(type(args))
    print(len(args))
    print(args[2])
    new_list = list(args)
    

print(f1(413, 17.5))
f2(name='mostafa' ,family="ahmadi", grade=19)
# f3(12,3,'ahmad','mashhad',200)
