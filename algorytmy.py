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

#Suma cyfr liczby calkowitej
def sumaCyfry():
    x = int(input("Podaj liczbe: "))
    result = 0
    if x == result:
        return None
    while(x>0):
        result = result + (x%10) #np dla x = 112 -> 0=0+2
        x=x//10 #112=112/10->11 -> petla
    return result
################################################################
#Potegowanie
def potegowanie():
    a=int(input("a: "))
    b=int(input("b: "))
    wynik=1
    while(b>0):
        wynik = a * wynik
        b = b - 1
    while(b<0):
        wynik = wynik *a
        b = b + 1
    return wynik
#################################################################
#srednia arytmetyczna
def sredniaArytmetyczna():
    n = int(input("Podaj ilosc liczb: "))
    wynik = 0
    i = 0
    while(i<n):
        a = int(input("a:"))
        wynik = wynik + a
        i = i +1
    wynik = wynik / n
    return wynik

print(sredniaArytmetyczna())






