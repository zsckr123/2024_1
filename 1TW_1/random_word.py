import random, string

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

def szyfruj(word):
    lista_zaszyfrowana = []

    for znak in word:
        z = ord(znak)
        lista_zaszyfrowana.append(z)
    return lista_zaszyfrowana


# print(randomword(5))
print(szyfruj(randomword(5)))
