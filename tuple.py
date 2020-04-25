''' A tuple is just an immutable list. 
a tuple is a list, but after it’s defined you can’t change it.
 '''

prices = (29.95, 9.98, 4.95, 79.98, 2.95 ,9 , 9, 98, 2, 29.95)
print(prices)
print(f"length of tuple: {len(prices)}")
print(prices[2])

look_for = 9.98
print(prices.count(look_for))

if look_for in prices:
    position = prices.index(look_for)
else:
    position=-1
print(position)

#Loop through and display each item in the tuple.
for price in prices:
    print(f"${price:.2f}", end= ", ")

print()  

'''
To define a set, use curly braces where you would have used square brackets for
a list and parentheses for a tuple. The difference between a set and a list is 
that the items in set have no specific order. Even though you may define the set
 with the items in a certain order, none of the items get index numbers to identify
  their positions.
'''
# Define a set named sample_set.
sample_set = {1.98, 98.9, 74.95, 2.5, 1, 16.3, 1}
# Show the whole set
print(f" sample_set = {sample_set} , len= {len(sample_set)}")
# Make a copy and show the copy.
ss2 = sample_set.copy()
ss3 = sample_set
print(f"id sample_set= {id(sample_set)} , id ss2 = {id(ss2)}, id ss3= {id(ss3)} ")
print(ss2)
sample_set.add(11.98)
print(f" new sample_set  = {sample_set} , len= {len(sample_set)}")
sample_set.update([14.4, 123.45, 2.98])
print(f" New sample_set  = {sample_set} , len= {len(sample_set)}")

sample_set.remove(1)
print(f" after remove sample_set  = {sample_set} , len= {len(sample_set)}")

sample_set.clear()
print(f" after clear sample_set  = {sample_set} , len= {len(sample_set)}")