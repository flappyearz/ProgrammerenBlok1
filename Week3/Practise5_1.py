def convert(celsius):
    fahrenheit =  celsius * 1.8 + 32
    return fahrenheit

def table():
    for c1 in range(-30, 41, 10):
        f1 = convert(c1)
        print('{}, {}'.format(c1, f1))

print('C', ' F')
table()




