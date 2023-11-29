#Write your function here
def max_num(nums):
 max = nums[0];
 for index in range(1, len(nums)):
   print("index:", index);
   if( max < nums[index]):
     max = nums[index]
 return max


#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))

# Print Learning Loops 0-5, 6 times, or 0- to (6-1), as the 6 is exclusive (not included)
for temp in range(6): print("Learning Loops!")

# iterate i, 2 times, from 0-2
def append_sum(my_list) :
  for i in range(3) :
    last = my_list[-1]
    second_to_last = my_list[-2]
    sum = last + second_to_last
    my_list.append(sum)
  return my_list
#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))

count = 0
while count <= 3: 
  print(count)
  count += 1

  # break:
  items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]


print("Checking the sale list!")


for item in items_on_sale:
  print(item)
  if item == "knit dress":
    break


print("End of search!")

#continue:
big_number_list = [90, 89, 45, -1, 0, 60]
for i in big_number_list:
  if i <= 0:
    continue
  print(i)

numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 for num in numbers]
print(doubled)

numbers = [2, -1, 79, 33, -45]
negative_doubled = [num * 2 for num in numbers if num < 0]
print(negative_doubled)

#Tuples: Immutable data structure
my_info = ("Tony", 55, "Programmer")
print(my_info, my_info[1])
# my_info[0] = "Tigger"
name, age, occupation = my_info
print(name, age, occupation)

one_element_tuple = (4,)
print(one_element_tuple)

#zipped:
names = ("Navin", "Kiran", "Harsh", "Navin")
comps = ("Dell", "Apple", "MS", "Dell")
zipped = zip(names, comps)
# print(zipped)

# list
zipped_list = list(zipped);
print(zipped_list)

for (a, b) in zipped_list:
  print(a, b);

#set: Does not maintain order
# zipped_set = set(zipped);
# print(zipped_set)

#dictionary:
# zipped_dictionary = dict(zipped)
# print(zipped_dictionary)


#multiple Return:
weather_data = ['Sunny', 'Sunny', 'Cloudy', 'Raining', 'Snowing']
def threeday_weather_report(weather):
  first_day = " Tomorrow the weather will be " + weather[0]
  second_day = " The following day it will be " + weather[1]
  third_day = " Two days from now it will be " + weather[2]
  return first_day, second_day, third_day
#destructuring:
monday, tuesday, wednesday = threeday_weather_report(weather_data)

print(monday);
print(tuesday)
print(wednesday)

#Formatting string literals with f".."
def dog_years(name, age):
 age = age * 7;
 return f"{name}, you are {age} years old in dog years"

# Uncomment these function calls to test your dog_years function:
print(dog_years("Lola", 16))