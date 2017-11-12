#Przeszukiwanie randomowej tablicy
import random

def search():
    tab = []
    for i in range(10):
        tab.append(random.randint(0,100))
    number = int(input("number: "))
    if number in tab:
        return number
    else:
        return None

print(search())
##########################################
#Binarcy search

