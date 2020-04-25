def multi_return(x, y):
    """this is to return several values"""
    return x+y, x/y, x*y, x/y

print (multi_return(10, 4))

x = multi_return(10, 4)
print(type(x))
print(f"(sum = {x[0]}, div = {x[1]}, mul = {x[2]}, sub = {x[3]})")

add, div, mul, sub = multi_return(10, 4)
print(f"(A+B = {add}, A/B = {div}, A*B = {mul}, A-B = {sub})")