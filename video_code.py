print("Hello from real python")

# Variables - You do not need to declare String, int, float, python will infer, but for me Im going to be a precise as possible for understading
school = 'MCTC' # String 
gpa = 2.5 # Float - decimal numbers, not whole
students_in_class = 25 # Integer


# if-statements
if gpa == 4: # 4 is the condition to meet to print or do the action
    print('WOW!') # This is conditional code - this prints when the gpa = 4 
elif gpa > 3:
    print('Awesome!')
else:
    print('Cool!')



# lists - Use Square Brackets for lists
schools = ['MCTC', 'DCTC', 'North Hennepin Technical College']
if 'MCTC' in schools: # in operator is saying this if MCTC is in the schools lists, then run conditional code
    print('MCTC is one of the schools in the list')

# You can add, remove, alter lists as you please basically
schools.sort() # Sorts by alphabet
print(schools)
schools.append('Century College') # Append adds to the end of the list
print(schools)
schools.reverse() # This reverses the order of the list, but you have to print afterwards to see that change, otherwise it will return none
print(schools)


# strings - I know what a string is, variable like floats and integers, can do tons of things with them
class_name = "Software Development Capstone"
print(class_name.upper())
print(len(class_name))

if 'Capstone' in class_name:
    print('This must be the capstone class')

# Loops - for loops over range
for x in range(10):
    print(x)

# loops - for loops over sequence
for s in schools:
    print(s.upper()) # upper prints the desired output in all caps

for letter in school:
    print(letter * 10) # math with strings

data = [0] * 10 # this wouyld make a new list with ten 0's in it, basically placeholder so i can use list later
print(data)

more_data = [None] * 10
print(more_data)

# while Loops
#name = input('Enter your name')


# longer version of a while loop
#while len(name) == 0: # this is saying while the length of the name variable is 0, print.
    #print('please enter at least one character')
    #name = input('Enter your name: ')

# does the same as the above loop, just less typing for cleaner code - not required but should come with using code more
#while not name:
  #  print('please enter at least one character')
   # name = input('Enter your name: ')
# True and False and None

start_of_semester = True # Boolean, setting the variable to be true or false, and then acting upon what the value is
winter = False # Boolean as well,

if winter: # this line is saying IF winter = true. A little hard to catch imo, but cleaner coding and less typing
    print('brrr!')
else:
    print('it is not winter') 

# Dictionaries - Hashmats in c# and objects in Java - all the same thing
# key value pairs

class_codes = { 2905: 'Capstone', 2560: 'Web', 2545: 'Java'}

print(class_codes[2560])

for code in class_codes:
    print(code)
    print(class_codes[code])

for code, name in class_codes.items():
    print('The class code is ' + str(code) + ' and the name is ' + name) # str(code) is changing int to string because in python we cannot concatenate

for code, name in class_codes.items():
    print(f'The class code is {code} and the name is {name}') # f is the formatting tool to make it easier to read


# Slicing Strings, Lists
schools = ['MCTC', 'DCTC', 'North Hennepin Technical College']

first_two = schools[0:2] # [:2] is shorthand for it otherwise
print(first_two)

last_school = schools[-1]
print(last_school)
last_two_schools = schools[-2:]
print(last_two_schools)

school_name = 'Minneapolis Community and Technical College'
city = school_name[:11]
print(city)

# File Input and Output
with open('data.txt') as f:
    print(f.read())


# Functions

def get_name():
    print('Hello, please enter your name!')
    name = input('Your name is: ')
    return name

name = get_name()