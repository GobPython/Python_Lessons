import math
def treugolnik():
    x = float(input('\nВведите длинну строны 1: '))
    y = float(input('Введите длинну строны 2: '))
    z = float(input('Введите длинну строны 3: '))
    p = (x + y + z)/2
    return(round(math.sqrt(p*(p-x)*(p-y)*(p-z)), 2))

