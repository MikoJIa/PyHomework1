# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

import math

x_a = float(input('Enter cootdinates X_a - '))
y_a = float(input('Enter cootdinates Y_a - '))
x_b = float(input('Enter cootdinates X_b - '))
y_b = float(input('Enter cootdinates Y_b - '))
distance = math.sqrt((x_a - x_b)**2 + (y_a - y_b)**2)
print(f'Расстояние между точками {distance}')