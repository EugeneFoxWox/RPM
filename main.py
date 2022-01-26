from math import sqrt
if __name__ == '__main__':
    a = float(input('введите а: '))
    b = float(input('введите b: '))
    c = float(input('введите c: '))
    D = b ** 2 - 4 * a * c
    if D == 0:
        x = -b / (2 * a)
        print(x)
    elif D < 0:
        print('корней нет')
    else:
        x1 = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)
        print(x1, x2)
        
