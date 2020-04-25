total = 100
sales_tax_rate = 0.065
taxable = True
if taxable:
    print(f"Subtotal : ${total:.2f}")
    sales_tax = total * sales_tax_rate
    print(f"Sales Tax: ${sales_tax:.3f}")
    total = total + sales_tax
    print(f"Total    : ${total:.0f}")
    
print('\t----------------------------\n')

import datetime as dt  
# Get the current date and time 
now = dt.datetime.now()
# Make a dicision based on hour
# print(now)
print(f"hour is: {now.hour}")
if now.hour < 12 :
    print('Good Morning')
elif now.hour == 12:
    print('Its time Lunch')
else:
    print('Good Afternoon')
print('I hope you understant it')


print('\t----------------------------\n')

light_color = "blue"

if light_color == "green":
    print("Go")
elif light_color == "red":
    print("Stop")
elif light_color=='blue':
    print('Hi farhad')
else:
    print("Proceed with caution")
    
print("This code executes no matter what")

print('\t----------------------------\n')