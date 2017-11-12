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
##########################################

#Binary search
def binarySearch():
    tab = []
    for i in range(10):
        tab.append(random.randint(0,100))
    tab.sort()
    print("tab: ", tab)
    l = 0
    p = len(tab)-1
    print(p)
    liczba = int(input("Number: "))
    if l > p:
        return None
    else:
        s = (l+p)//2
        if liczba == tab[s]:
            print("znaleziono")
        elif liczba < tab[s]:
            p = s -1
            print("w pierwszych:", p)
            return p
        elif liczba > tab[s]:
            l = s + 1
            print("od wartosci tbalicy; ", l)
##############################################################






