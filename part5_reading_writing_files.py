# Open a file for reading with  with open

with open('E:/Tutorials/codeacademy/python/python_practice/text/real_cool_document.txt') as cool_doc:
	cool_contents = cool_doc.read()
	print(cool_contents)

# How to read text files line by line using readLines():
with open('E:/Tutorials/codeacademy/python/python_practice/text/keats_sonnet.txt') as keats_sonnet:
  for line in keats_sonnet.readlines():
    print(line)

#How to read text files line by line using readLines():
with open('E:/Tutorials/codeacademy/python/python_practice/text/Keats_sonnet.txt') as keats_sonnet:
  for line in keats_sonnet.readlines():
    print("Keats:", line)

# Read text files with readline():
with open('E:/Tutorials/codeacademy/python/python_practice/text/just_the_first.txt') as first_line_doc:
  count = 0;
  first_line = first_line_doc.readline()
  print(first_line)

#Read text files with readline():
with open('E:/Tutorials/codeacademy/python/python_practice/text/Keats_sonnet.txt') as first_line_doc:
  count = 0;
  first_line = first_line_doc.readline()
  print("ReadLine:", first_line)

#How to write files: Use “w”
with open('E:/Tutorials/codeacademy/python/python_practice/text/generated_file.txt', 'w') as gen_file:
  gen_file.write("What an incredible file!")

#Appending Text to Files: use “a”
with open('E:/Tutorials/codeacademy/python/python_practice/text/generated_file.txt', 'a') as gen_file:
  gen_file.write("n/… and it still is")

#Old Method to Append to Files:
fun_cities_file = open('E:/Tutorials/codeacademy/python/python_practice/text/fun_cities.txt', 'a')
 
# We can now append a line to "fun_cities".
fun_cities_file.write(" Montreal")
 
# But we need to remember to close the file
fun_cities_file.close()

#Convert csv into a dictionary with csv library:
import csv
 
list_of_email_addresses = []
with open('E:/Tutorials/codeacademy/python/python_practice/text/users.csv', newline='') as users_csv:
  user_reader = csv.DictReader(users_csv)
  for row in user_reader:
    list_of_email_addresses.append(row['Email'])
  print("List:", list_of_email_addresses)

  #Get A Specific Feild from Delimited files:
import csv
 
with open('E:/Tutorials/codeacademy/python/python_practice/text/addresses.csv', newline='') as addresses_csv:
  address_reader = csv.DictReader(addresses_csv, delimiter=';')
  for row in address_reader:
    print(row['Address'])

#Create A CSV File:
big_list = [{'name': 'Fredrick Stein', 'userid': 6712359021, 'is_admin': False}, {'name': 'Wiltmore Denis', 'userid': 2525942, 'is_admin': False}, {'name': 'Greely Plonk', 'userid': 15890235, 'is_admin': False}, {'name': 'Dendris Stulo', 'userid': 572189563, 'is_admin': True}] 
 
import csv
 
with open('E:/Tutorials/codeacademy/python/python_practice/text/output.csv', 'w') as output_csv:
  fields = ['name', 'userid', 'is_admin']
  output_writer = csv.DictWriter(output_csv, fieldnames=fields)
 
  output_writer.writeheader()
  for item in big_list:
    output_writer.writerow(item)

#Create JSON Reader:
# Purchase_14781239.json: {
#   'user': 'ellen_greg',
#   'action': 'purchase',
#   'item_id': '14781239',
# }

import json
 
with open('E:/Tutorials/codeacademy/python/python_practice/text/purchase_14781239.json') as purchase_json:
  purchase_data = json.load(purchase_json)
 
print(purchase_data['user'])
# Prints 'ellen_greg'

#Create a JSON File:
turn_to_json = {
  'eventId': 674189,
  'dateTime': '2015-02-12T09:23:17.511Z',
  'chocolate': 'Semi-sweet Dark',
  'isTomatoAFruit': True
}

import json
 
with open('E:/Tutorials/codeacademy/python/python_practice/text/output.json', 'w') as json_file:
  json.dump(turn_to_json, json_file)
