'''
Funkcje zaczynamy od słówka "def"
'''

def arytmetyka(x,y):
    print('Suma liczb a i b =', x + y)
    print('Rożnica liczb a i b =', x - y)
    print('Iloczyn liczb a i b =', x * y)
    if y == 0:
        print('Dzielenie przez zero niewykoanlne')
    else:
        print('Iloraz liczb a i b =', x / y)

# Funkcje trzeba uruchomić czyli wywołać
arytmetyka(2,0)


