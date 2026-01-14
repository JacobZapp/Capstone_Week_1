from datetime import date # Datetime library to get real time date and time, when printing it uses ISO Format

now = date.today()
current_month = now.month # Tthis stores the current month in the variable for reference later

name = input('Please enter your name: ')

print(f'Hello {name}!')

print(f'There are {len(name)} letters in your name') #f is format strings, easier to read but make sure I can talk it out and understand it

birth_month = int(input('Please enter the number of the month you were born: ')) # correlate number with month and make sure that is the current month or not

if birth_month == current_month:
    print('Happy Bday Month!')
else:
    print('Not your bday month yet')