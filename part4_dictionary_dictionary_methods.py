# Combine two lists in the Dict Comprehension:
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]
# Zip an iterator of pairs between two lists:
zipped_students = zip(names, heights)
students_comprehension = {key:value for key, value in zipped_students}
print(students_comprehension)

#Check if a key exists in a dictionary:

key_to_check = 'Landmark 81'
buildings = ['Landmark 81', 'Empire State', 'Twin Towers', 'Dodger Stadium']
heights = [61, 70, 67, 64]
# Zip an iterator of pairs between two lists:
zipped_buildings = zip(buildings, heights)

building_heights = {key:value for key, value in zipped_buildings}

print(building_heights)

if key_to_check in building_heights:
  print("true", building_heights[key_to_check])


#Use get to determine if a key is in the Dictionary
  print(f"Get {key_to_check}:", building_heights.get(key_to_check, 0))  

# Remove a key value with .pop():
raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}
raffle.pop(320291, "No Prize")

# Pop an item off a dictionary and print the results
print("Pop:", raffle)

# Get an array of keys from a dictionary
print("List:", list(raffle))

# Get an array of keys from a dictionary
print("Keys:", raffle.keys())

# Sum all the values within a Dictionary with values():
num_exercises = {"squats": 34, "push-ups": 55}

total_exercises = 0;

for exercise in num_exercises.values():   
    total_exercises += exercise
print("Dictionary Sum", total_exercises)

# Get a single key/value pari with .item():
pct_women_in_occupation = {
    "CEO": 28,
    "Engineering Manager": 9,
    "Pharmacist": 58,
    "Physician": 40,
    "Lawyer": 37,
    "Aerospace Engineer": 9
}

for occupation, percentage in pct_women_in_occupation.items():
    print(f"Women make up {percentage} percent of {occupation}s")

# Looping through multiple dictionary items:
tarot = { 
1: "The Magician", 
2: "The High Priestess", 
3: "The Empress", 
4: "The Emperor", 
5: "The Hierophant", 
6: "The Lovers", 
7: "The Chariot", 
8: "Strength", 
9: "The Hermit", 
10: "Wheel of Fortune", 
11: "Justice", 
12: "The Hanged Man", 
13: "Death", 
14: "Temperance", 
15: "The Devil", 
16: "The Tower", 
17: "The Star", 
18: "The Moon", 
19: "The Sun", 
20: "Judgement", 
21: "The World", 
22: "The Fool"
} 

spread = {} 
spread["past"] = tarot.pop(13) 
spread["present"] = tarot.pop(22) 
spread["future"] = tarot.pop(10) 
for key, object in spread.items(): print(f"Your {key} is the {object} card.")
