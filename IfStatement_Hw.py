'''
 3) find the maximum number from 5 variables
'''

num1 = input('Enter 1st number:')
num2 = input('Enter 2nd number:')
num3 = input('Enter 3rd number:')
num4 = input('Enter 4th number:')
num5 = input('Enter 5th number:')
if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
    print(f'num1 :{num1} is biggest number')
elif num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
    print(f'num2 :{num2} is biggest number')
elif num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5:
    print(f'num3 :{num3} is biggest number')
elif num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5:
    print(f'num4 :{num4} is biggest number')
elif num5 > num1 and num5 > num2 and num5 > num3 and num5 > num4:
    print(f'num5 :{num5} is biggest number')
else:
    print('no output')



'''
num1=input('Enter 1st number:')
num2=input('Enter 2nd number:')

# n2=5
# n1=10
if num1 > num2:
    print(f'num1 {num1} is bigger number')
elif num1==num2:
    print(f'num1 {num1} and num2 {num2} are same numbers')
else:
    print(f'num2 {num2} is bigger number')
'''