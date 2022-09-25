# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
day_week = int(input('Enter a number - '))
if day_week >= 1 and day_week <= 5:
    print('Working day')
elif day_week == 6 or day_week == 7:
    print('Weekend!')
else:
    print(None)