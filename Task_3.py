# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

#  Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Enter your X coordinate: '))
y = int(input('Enter your Y coordinate: '))

if (x > 0 and y > 0):
    print('The point locates in quarter 1')
elif (x < 0 and y > 0):
    print('The point locates in quarter 2')
elif (x < 0 and y < 0):
    print('The point locates in quarter 3')
elif (x > 0 and y < 0):
    print('The point locates in quarter 4')
else:
    print('Your coordinates are incorrect!')
