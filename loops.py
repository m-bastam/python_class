# for num in range(10):
#     print(num)
# print("All done")

# print("\t-----------------------------\n")

# count = 0
# str1 = "Mostafa"
# for char in str1:
#     print(char, end="; ")
#     print(count)
#     count +=1
# print(f"length of text is = {len(str1)}")
# print("Done")

# print("\t-----------------------------\n")

# for element in ["The", "rain", "in", "Spain", 1, 13.24, [100, 200, 300, 400]]:
#     print(element)
#     # print(element , type(element))
# print("Done!")

# print("\t-----------------------------\n")

# answers = ["A", "C", "", "B", "D", "", "E"]
# for answer in answers:
#     if answer == "":
#         # break
#         continue
        
#     print(answer)
# print("Loop is done")

# print("\t-----------------------------\n")

# ascii_code = 0
# while ascii_code < 2048:
#     print(str(ascii_code), ' = ' , chr(ascii_code))
#     ascii_code +=1
# print('all done!')
  
# print("\t-----------------------------\n")
  
import random
print("Numbers that aren't evenly divisible by 5")
counter = 1
while counter <= 10:
    # Get a random number
    number = random.randint(1,999)
    # if int(number / 5) == number / 5:
    if int(number % 5) == 0:
        # If it's evenly divisible by 5,
        # break
        continue
    # Otherwise, print it and keep going for a while.
    print('counter =', counter , ', number = ',number)
    # Increment the loop counter.
    counter += 1
print("Loop is done")

print("\t-----------------------------\n")