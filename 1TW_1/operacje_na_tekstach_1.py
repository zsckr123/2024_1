
text = 'napis 2'
#       0123456
print(text)

print(text[0]) # pierwszy element
print(text[-1]) # ostatni element
# '''
# Drukowanie od początku do elementu o indeksie 2 ale
# bez tego elementu
# '''
print(text[1:4]) # drukowanie od elementu drugiego do piątego ale bez piątego
'''
# drukowanie od elementu drugiego 
do piątego ale bez piątego - co drugi element
'''
print(text[1:4:2])
#
print('--------------')
for t in text:
    print(t)