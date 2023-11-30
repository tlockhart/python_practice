#Use keyword type to Check the type of a Python variable:
print(type("Cool String") )
# returns <class'‘str'>
print(type(12))
#returns <class ‘int’>

#Example 1: Class Pass By Reference: 
class CoolClass:
    # Pass by reference
    pass

class_reference = CoolClass()
# prints “<class ‘__main__.CoolClass’>”
print(type(class_reference)) 

#Example 2: Class Instance Variables: 
class Musician:
  title = "Rockstar"
 
drummer = Musician()
# prints "Rockstar"
print(drummer.title)

#Example 3: Class method: Passing self as first argument: Functions that are defined as a part of a class.

class Dog:
  dog_time_dilation = 7
 
  def time_explanation(self, num):
    print("Dogs experience {} years for every {} human year.".format(self.dog_time_dilation, num))
 
pipi_pitbull = Dog()
# Prints "Dogs experience 7 years for every 1 human year."
print(pipi_pitbull.time_explanation(1))


#Example 4: Class Instantiation
class Circle:
  pi = 3.14
  def area(self, radius):
    area = self.pi * radius ** 2
    return area
  
# Class instantiation:
circle = Circle()
pizza_area = circle.area(12/2)
teaching_table_area = circle.area(36/2)
round_room_area = circle.area(11460/2)

print("Pizza Area:", pizza_area)
print("Circle Area:", teaching_table_area)
print("Round Room Area:", round_room_area)

#Example 5: Class Constructor (Dunder)
class Shouter:
	def __init__(self, phrase):
		print(f"Hello? {phrase}!")

greeting = Shouter("Hushenholloer")
print(greeting)

#Example 6: Class Constructor
class Circle:
  pi = 3.14
  
  # Add constructor here:
  def __init__(self, diameter):
    print(f"New circle with diameter: {diameter}")

circle1 = Circle(10)
print("CircleDiameter", circle1)

#Example7: Joining two Instance variables: Dot Notation:
class FakeDict:
	pass

fake_dict1 = FakeDict()
fake_dict2 = FakeDict()
 
#Instance variables must have a value before assigning:
fake_dict1.fake_key = "This works!"
fake_dict2.fake_key = "This too!"
 
# Let's join the two strings together!
working_string = "{} {}".format(fake_dict1.fake_key, fake_dict2.fake_key)

# prints "This works! This too!"
print(working_string)

#Example8: Check object/class attributes, get attributes
can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"], {"test": "example"}]
for item in can_we_count_it:
  if hasattr(item, "count"):
    print("ItemCount:", getattr(item, "count"))
    print(str(type(item)) + " has the count attribute!")
else:
    print(str(type(item)) + " does not have the count attribute :(")

#Example9: Initializing Instance Variables
class SearchEngineEntry:
  secure_prefix = "https://"
  def __init__(self, url):
    self.url = url
 
  def secure(self):
    return "{prefix}{site}".format(prefix=self.secure_prefix, site=self.url)
 
codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")
 
# prints "https://www.codecademy.com"
print(codecademy.secure())

# prints "https://www.wikipedia.org" 
print(wikipedia.secure())

#Example 10:Class Instantiation and method calls
class Circle:
  
  pi = 3.14

  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    self.radius = diameter/2

  def circumference(self):
    circumference = 2 * self.pi * self.radius
    return circumference
  
medium_pizza = Circle(12)
print(medium_pizza.circumference())

teaching_table = Circle(36)
print(teaching_table.circumference())

round_room = Circle(11460)
print(round_room.circumference())

#Example 11: def__repr__(self):
class Employee():
  def __init__(self, name):
    self.name = name
 
  def __repr__(self):
    return self.name
 
argus = Employee("Argus Filch")

# prints "Argus Filch"
print("Print String representation of the class data", argus)

#JavaScript OOP Example: Passing class instances as arguments
class Grade:
    minimum_passing = 65

    def __init__(self, score):
        self.score = score

    #Print string representation of score

    def __repr__(self):
        return f"Grade(score={self.score})"

class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []  # Initialize grades list here

    #Like toString() method
    def __repr__(self):
        return f"Student(name={self.name}, year={self.year}, grades={self.grades})"

    def add_grade(self, grade):
        if isinstance(grade, Grade):
            self.grades.append(grade)


roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

newGrade = Grade(100)
pieter.add_grade(newGrade)

print("Pieter's Grades:", pieter.grades)
