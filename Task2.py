# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).
 
x = int(input('Enter exis X - '))
y = int(input('Enter exis Y - '))
if x > 0 and y > 0:
    print('1 quarter')
if x < 0 and y > 0:
    print('2 quarter')
if x < 0 and y < 0:
    print('3 quarter')
if x > 0 and y < 0:
    print('4 quarter')