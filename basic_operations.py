import numpy

def add(numbers):
    return sum(numbers)

def subtraction(numbers):
    for i in range(len(numbers) - 1):
        numbers[i + 1] = -1*numbers[i + 1]
    return sum(numbers)

def multiplication(numbers):
    return numpy.prod(numbers)

def division(numbers):
    fractional = numbers[0] / numbers[1]
    integer = numbers[0] // numbers[1]
    rest = numbers[0] % numbers[1]

    return (fractional, integer, rest)

print('{:=^50}'.format('  calculator  '))
print('\n\n select the desired operation number\n\n')
print("1 - add \n2 - subtraction \n3 - \
multiplication \n4 - devision \n")

option = int(input('type your option: '))
print('\n')

numbers = []

if option == 1:
    numbers.append(float(input("type the first numbers: ")))
    while True:
        n = input('type another number, if you dont want to put more, type "no": ')
        if n == 'no':
             break
        else:
            numbers.append(float(n))

    print(f'the sum of these terms is : {add(numbers)}')

elif option == 2:
    numbers.append(float(input("type the first numbers: ")))
    while True:
        n = input('type another number, if you dont want to put more, type "no": ')
        if n == 'no':
             break
        else:
            numbers.append(float(n))

    print(f'the subtraction of terms by the first is : {subtraction(numbers)}')

elif option == 3:
    numbers.append(float(input("type the first numbers: ")))
    while True:
        n = input('type another number, if you dont want to put more, type "no": ')
        if n == 'no':
             break
        else:
            numbers.append(float(n))

    print(f'the multiplication between these terms is : {multiplication(numbers)}')

elif option == 4:
    numbers.append(float(input("type the first numbers: ")))
    numbers.append(float(input("type the second numbers: ")))
    result = division(numbers)
    print(f'the division between the first and the second term is : ')
    print(f'fractional : {division(numbers)[0]}\ninteger: {division(numbers)[1]}\nrest: {division(numbers)[2]}')

else:
    print('try again')