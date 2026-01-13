from datetime import date

now = date.today()
current_month = now.month # Number of month will be displayed eg. december = 12

name = input('Please enter your name: ')

print(f'Hello {name}!')

print(f'There are {len(name)} letters in yor name!')

month = input('Please enter the month you were born: ')

if month == current_month:
    print('Happy Birthday Month!')
else:
    print('Not your bday month yet')