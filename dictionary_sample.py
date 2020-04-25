
letter_counts = {}

for letter in "Missi123ss231ippi":
   letter_counts[letter] = letter_counts.get(letter,0) + 1
   # letter_counts[letter] += 1
    

print(letter_counts)

letter_items = list(letter_counts.items())
print(letter_items)

letter_items.sort()
print(letter_items)

