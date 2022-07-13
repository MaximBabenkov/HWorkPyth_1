# Напишите программу, которая по заданному номеру четверти, показывает
# диапазон возможных координат точек в этой четверти (x и y)

numb = int(input('Enter your number of a quater: '))

if numb == 1:
    print('The range of possible coordinates: X (0; +∞), Y (0; +∞)')
elif numb == 2:
    print('The range of possible coordinates: X (0; -∞), Y (0; +∞)')
elif numb == 3:
    print('The range of possible coordinates: X (0; -∞), Y (0; -∞)')  
elif numb == 4:
    print('The range of possible coordinates: X (0; +∞), Y (0; -∞)')  
else:
    print('Your number of a quater is incorrect!')
