'''
Funkcje zaczynamy od słówka "def"
'''

def arytmetyka(a,b):
    print('suma liczb',a + b)
    print('odejmowanie liczb',a - b)
    print('mnożenie liczb',a * b)
    if b==0:
        print("dzielenie niewykonalne")
    else:
        print('Iloraz liczb a i b =', a / b)
# Wywołanie/uruchomienie funkcji
arytmetyka(2,0)