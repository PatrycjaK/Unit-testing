def f1(a, b=0):
    return a * a + b

def f2(a):
    if not a:
        return 'BUUUM'
    else:
        return a[0]

def f3(a):
    if a == 1:
        return 'jeden'
    elif a == 2:
        return 'dwa'
    elif a == 3:
        return 'trzy'
    else:
        return 'other'

def f4(a, b = ''):
    if b == '':
        return f'{a} ma kota'
    else:
        return f'{a} ma kota i {b}'

def f5(a, b = 1):
    return [num for num in range(0, a, b)]

def f6(s):
  return s * '*'

def f7(a):
    if type(a) == type('ala') and len(a.split()) == 1:
        return 'slowo'
    elif type(a) == type('ala') and len(a.split()) > 1:
        return 'zdanie'
    if type(a) == type(1) and 0 <= a <= 9:
        return 'cyfra'
    elif type(a) == type(1) and  a >= 10:
        return 'liczba'
    # if a in </:
    #     return 'tag koncowy'
    # elif a in <:
    #     return 'tag poczatkowy'

def f8(a, b):
    return a in b

def f9(a, b):
    if a >= 1 and b >= 1:
        return 'dodatnie'
    elif a < 0 and b < 0:
        return 'ujemne'
    elif (a >= 1 and b < 0) or (a < 0 and b >= 1):
        return 'roznych znakow'
    elif a == 0 or b == 0:
        return 'jest zero'

def f10(a, b):
    if a == b:
        return 'rowne'
    else:
        return 'rozne'
