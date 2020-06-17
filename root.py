import math

def raiz(a, b, c):

    print(f'para a = {a}, b = {b} e c = {c}' )

    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print('não há uma solução real')

    elif delta == 0:
        print('há um solução que é x =', (-b + (delta) ** 0.5) / (2 * a))

    else:
        x1 = (-b + (delta) ** 0.5) / (2 * a)
        x2 = (-b - (delta) ** 0.5) / (2 * a)
        print(f'há duas raízes, x1 = {x1:_^40} e x2 = {x2:_^40}')

print('seja {} uma equação do segundo grau'.format('ax^2 + bx + c = 0'))
a,b,c = input('informe os coeficientes do polinômio: ').split(" ")
raiz(float(a), float(b), float(c))