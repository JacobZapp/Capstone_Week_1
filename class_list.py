classes = [] # Empty list to add onto with while loop



class_name = input('Enter class name or Enter to Quit:')

while class_name:
    classes.append(class_name)
    class_name = input('Enter class name or Enter to Quit: ')

   
print(classes)

# This is the simpler for loop that prints each class name on a new line
# for c in classes:
#     print(c)

# This for loop uses index, which numbers each class, adding +1 is so the number starts at 1 instead of 0
for index, c in enumerate(classes):
    print(index + 1, c)
