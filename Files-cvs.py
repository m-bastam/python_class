import csv
#comma-separated values (CSV) files
# Open CSV file with UTF-8 encoding, don't read in newline characters.
with open('cars.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    # reader = f.readlines()
    # print(f.read())
    
    # Loop through one row at a time, i is counter, row is entire row.
    for row in reader:
        print(row[2])

# print(reader[3][2])
print('Done')
    