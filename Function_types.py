def f1(id:int , score:float) -> str:
    ''' to suggest programer input and output type '''
    
    print(f1.__annotations__)
    return str(id)

print('\t-------------------------------\n\n')

def f2( **args ):
    """ Pass in any number of arguments Inside the function,
     they treated as a dictionary named args """
    print(f3.__annotations__)
    for key,value in args.items():
        print(key , " = " ,value)
    print(type(args))
    args['grade'] = 20
    del args['name']
    print(args)
    print("in f2 *args" ,*args)
    print(f"in f2 args = {args}")
    

def f3(*args):
    """ Pass in any number of arguments separated by commas
    Inside the function, they treated as a tuple named args """
    print(args)
    print(type(args))
    print(len(args))
    print(args[2])
    # args[2]='Naser'
    new_list = list(args)
    print(new_list)
    

id_txt = f1(100 , 23.1)
print (id_txt , type(id_txt))
print('\t-------------------------------\n\n')
f2(name ='mostafa' ,family = "ahmadi", grade = 19 , birth_date = '1982/12/23')
print('\t-------------------------------\n\n')
f3(12,3,'ahmad','mashhad',200)
