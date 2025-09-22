def f(x):
    return x**2-5

def metoda_bisekcji():
    epsilon = abs(float(input('Podaj dokladność wartości funkcji')))
    delta = abs(float(input('Podaj dokladność na osi OX')))
    lewy = 0
    prawy = 0
    while lewy >= prawy:
        lewy = float(input('Podaj lewy koniec przedziału'))
        prawy = float(input('Podaj prawy koniec przedziału'))
    if f(lewy) * f(prawy) > 0:
        return "W tym  przedziale nie ma pierwiastka. Szukaj dalej!"
    if abs(f(lewy)) < epsilon:
        return lewy
    if abs(f(prawy)) < epsilon:
        return prawy


    while abs(prawy - lewy) > delta:
        x = (lewy + prawy) / 2
        if abs(f(x)) < epsilon:
            break
        if f(lewy) * f(x) <0:
            prawy = x
        else:
            lewy = x
    return x
while True:
    print(metoda_bisekcji())
    q=input("Nacisnij x żeby skończyć lub dowolny przycisk dalej")
    if q=='x':
        break