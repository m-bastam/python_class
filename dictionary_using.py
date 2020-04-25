import datetime as dt

right_now = dt.datetime.now()

alno = {0: 0, 1: 1} 
def fib(n): 
    """ the first method using dictionary"""
    if n not in alno:
        alno[n] = fib(n-1) + fib(n-2)
        # print(alno)
    return alno[n]


# def fib(n):
#     '''The second way not using dictionary'''
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2)


duration = dt.datetime.now() - right_now

print(fib(40))
print(duration)

