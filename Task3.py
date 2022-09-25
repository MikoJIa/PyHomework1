# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

qur = int(input('Enter the quarter number - '))
if qur == 1:
    print('x > 0 and y > 0')
elif qur == 2:
    print('x < 0 and y > 0')
elif qur == 3:
    print('x < 0 and y < 0')
elif qur == 4:
    print('x > 0 and y < 0')
else:
    print(f'{None}: There is no such quarter')                 