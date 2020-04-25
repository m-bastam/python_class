# students = ["Mark", "Mary", "Todd", "Anita", "Sandy"]
# print(f"the initial length of List is: {len(students)}")
# student_name = "John"
# #Add student_name but only if not already in the list.
# if student_name in students:
#     print (student_name + " is already in the list")
# else:
#     students.append(student_name)   #add element to end of list
#     print (student_name + " is added to the list")
# print(f"the length of List is: {len(students)}")
# print(f"students are: {students}")

# student_name = "Sara"
# # Add student name to anywhere of the list that you want.
# students.insert(3, student_name) 
# #Show me the new list.
# print(f"students are: {students}")
# print(f"the length of List is: {len(students)}")

# #change a member of list
# students[0] = 'Ardavan'
# print(f"students are: {students}")

# print('\t-----------------------------------\n\n')
# ''' If you have two lists that you want to combine into a single list,
#     use the extend()'''
# # Create two lists of Names.
# list1 = ["Zara", "Lupe", "Hong", "Alberto", "Jake"]
# list2 = ["Huey", "Dewey", "Louie", "Nader", "Bubba"]
# print(f'Length of list1 = {len(list1)}, Length of list2 = {len(list2)} ')
# # Add list2 names to list1.
# list1.extend(list2)
# print(f"extended list: {list1}")
# print(f'Length of list1 = {len(list1)}, Length of list2 = {len(list2)} ')
# # to sort list
# list1.sort()
# print(f"Sorted list: {list1}")
# # or reverse sort 
# list1.sort(reverse = True)
# # attention! list1.reverse() is not equal list1.sort(reverse=True)
# print(f"Reverse Sort: {list1}")

print('\t-----------------------------------\n\n')
# Python offers a remove() method so you can remove any value from the list.
# If the item is in the list multiple times, 
# only the first occurrence is removed.

#Create a list of strings.
# letters = ["A", "B", "C", "D", "C", "E", "C"]
# print(f"Initial letters: {letters}")
# letters.reverse()
# print(f"Reverse list: {letters}")
# # delete by pass value
# char = letters.remove("C")
# print(char)
# #Show me the new list.
# print(f"Second letters:  {letters}")

# #delete by pass index
# char2 = letters.pop()
# print (char2)
# print(f"Third letters:  {letters}")
# char3 = letters.pop(1)
# print(char3)
# print(f"4th letters:   {letters}")
# # Remove item sub 2.
# del letters[2]
# print(f"5th letters:   {letters}")
# #remove the entire list
# del letters
# # print(letters)

# print('\t-----------------------------------\n\n')
# Create a list of strings.
letters = ["A", "B", "C", "D", "E", "F", "G"]
# Clear the list of all entries.
letters.clear()
# Show me the new list.
print(f"clear list: {letters}")

print('\t-----------------------------------\n\n')

# Create a list of strings.
grades = ["C", "B", "A", "D", "C", "B", "C"]
print(grades)
char = "C"
count_char = grades.count(char)
print(f"There are {count_char} {char}s in the list")
# Decide what to look for

# See if the item is in the list.
if char in grades:
# If it's in the list, get and show the index.
    print(str(char) + " is at index " + str(grades.index(char)))
else:
# If not in the list, don't even try for index number.
    print(str(char) + " isn't in the list.")

# remove all same item in list 
for grade in grades:
    if grade == char:
        grades.remove(char)
        
print(grades)
        
print('\t-----------------------------------\n\n')