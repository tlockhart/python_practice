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


