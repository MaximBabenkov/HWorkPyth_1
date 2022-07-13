# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

x = int(input('Enter your value X: '))
y = int(input('Enter your value Y: '))
z = int(input('Enter your value Z: '))

if not (x or y or z) == (not x and not y and not z):
    print('Statement is true')
else:
    print('Statement is false')
