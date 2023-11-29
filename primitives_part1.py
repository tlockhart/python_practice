print("I'm running Python code on my own environment!")
# print("a"-3)

fruits = ["apple", "bananna", "pineapple", "mango"];
print(fruits[:-1])

number_collection = [[100, 200], [100, 200], [475, 29], [34, 34]]
num_pairs = number_collection.count([100, 200])
# print how many times [100, 200] appears
print(num_pairs)

#Write your function here
def append_size(my_list):
  length = len(my_list)
  my_list.append(length)
  return my_list

#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))

list1 = [1,2,3,4,5]
print("list1:", list1)
list1 = []
del list1[:]
print("list1:", list1)

from typing import List
str = ["Jiho", "Adam", "Sonny", "Alisha"]
garden_waitlist: List[str];
print(garden_waitlist)

