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

#subtract datetime
newDate = datetime(2018, 1, 1) - datetime(2017, 1, 1)
print(newDate)