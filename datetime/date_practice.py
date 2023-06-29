from datetime import datetime

def get_day_of_week(key):
    switch = {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday"
    }

    return switch.get(key, "Invalid key. Please provide a key between 0 and 6.")

# Example usage:
key = 3  # Assuming key = 3
day_of_week = get_day_of_week(key)
print(day_of_week)  # Output: "Wednesday"

birthday = datetime(1978, 4, 5, 23, 12)

print(birthday)
print(birthday.year)
print(birthday.month)
print(birthday.weekday())
print(get_day_of_week(birthday.weekday()))
print(datetime.now())

#subtract datetime ( you cant add or multiply dates)
# https://docs.python.org/3/library/datetime.html
datetime_dif = datetime(2018, 1, 1) - datetime(2017, 1, 1)
print(datetime_dif)
print(datetime.now() - datetime(2018, 1, 1))
parsed_date = datetime.strptime("Jan 15, 2018",  "%b %d, %Y")
print("Month:",parsed_date.month)

# Create a string from a datetime
date_string = datetime.strftime(datetime.now(), "%b %d, %Y")
print("String:", date_string)

#https://www.programiz.com/python-programming/datetime/strftime
