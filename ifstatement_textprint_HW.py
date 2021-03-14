'''
 4) take input from user and if input is 'a' then print 'apple' like wise create a to g
'''

str=input("Enter any letter from 'a' to 'g' in lower case:")
if str not in ('a','b','c','d','e','f','g'):
    print('Enter letter between a to g only in lower case')
if str=='a':
    print('Apple')
elif str=='b':
    print('Ball')
elif str=='c':
    print('Cat')
elif str=='d':
    print('Duck')
elif str=='e':
    print('Elephant')
elif str=='f':
    print('Fish')
elif str=='g':
    print('Goat')
