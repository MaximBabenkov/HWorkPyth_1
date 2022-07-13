# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным

numb = int(input('Enter your number of a day of week: '))

if numb == 6 or numb == 7:
    print('It is a day off work')
else:
    print('It is a working day')
