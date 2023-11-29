#String step:
message = "MXeXeXtX XmXeX XaXtX XtXhXeX XpXaXrXkX"
decoded = message[0:38:2]
# decoded = message[:38:2]
print(decoded)


first_name = "Reiko"
last_name = "Matsuki"


# Find the 3rd item in both list and combine
def password_generator(first_name, last_name):
 return first_name[len(first_name)-3:] + last_name[len(last_name)-3:]
print(password_generator(first_name, last_name))
print(last_name[-3:])

#Splitting delimeters:
item = " bill:boe:bagans "
new_list = item.split(":")
print(new_list)

#Joining on Delimeters:
delimiter = ":"
original_str = delimiter.join(new_list)
print("*" + original_str.strip()+"*")

#formatting:
song = "Order my steps"
artist = "Brinson"
greeting = "My favorite song is {song} by {artist}.".format(song=song, artist=artist)
print(greeting)
