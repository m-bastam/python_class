# Import the datetime module, nickname dt
import datetime as dt
# Store today's date in a variable named today.

this_day = dt.date.today()
print(this_day)
print("day is : {this_day.day}")
print(f"day is : {this_day.day}")
print(f"month is: {this_day.month}")
print(f"year is: {this_day.year}")
print("\t-------------------------\n")
# Store some other date in a variable called last_of_teens
last_of_teens = dt.date(2019,12,31)
print(last_of_teens)
print(f"{last_of_teens:%A, %B %d, %Y}")
print(f"{this_day:%m/%d/%Y}")

print("\t-------------------------\n")

midnight = dt.time()
print(midnight)
print(type(midnight))

almost_midnight = dt.time(23,59,59,999999)
print(almost_midnight)


right_now = dt.datetime.now()
print(f"{right_now:%A, %B %d, %Y at %I:%M%p}")
print(f"{right_now:%m/%d/%y at %H:%M}")
print(f"{right_now:%I:%M %p on %b %d}")
print(f"{right_now:%c}")
print(f"aa{right_now:%x}")

new_years_day = dt.datetime(2020,1,1,12,32,45,435)
days_between = right_now - new_years_day
print(days_between)
print(type(days_between))

duration = dt.timedelta(days=146, hours= 23 , weeks=3)
print(new_years_day + duration)

birth_date = dt.datetime(1982,12,23,8,30,50)
my_age = right_now - birth_date
print(my_age, my_age.days//365)

utc_now = dt.datetime.utcnow()
time_difference = (right_now - utc_now)
print(f"My time is: {right_now: %I:%M %p}")
print(f"UTC time is: {utc_now: %I:%M %p}")
print(f"difference is : {time_difference}")



'''
Sample Datetime Format Strings

    Format                      String Example
%A, %B %d at %I:%M%p     Tuesday, December 31 at 11:59PM
%m/%d/%y at %H:%M%p      12/31/19 at 23:59
%I:%M %p on %b %d        11:59 PM on Dec 31
%x                       12/31/19
%c                       Tue Dec 31 23:59:00 2019
%m/%d/%y at %I:%M %p     12/31/19 at 11:59 PM
%I:%M %p on %m/%d/%y     1:59 PM on 12/31/2019
'''