import random
import math

"""Véletlen számok generálása"""

def veletlen():
    """[10,30] közötti véletlen számokat"""
    i: int= 0 
    while i<10:
        szam: int= math.floor(random.random()*21+10)
        print(szam, end=" ")
        i+=1

    
"""
1. Generálj 5 véletlen lottószámot
        [1,90]

2. Generálj 1 véletlen kétjegyű egész számot
        Döntsd el róla, hogy páros, vagy páratlan!

3. Generálj 15 db egész számot [0,1] között
        Hány 1-est generáltál?

4. Generálj egy véletlen számot 1 és 10 között!
        Szorozd meg 3-mal
        Vonj ki belőle  15-öt
        Oszd el 6-tal
        szorozd be 2-vel
        Vond ki belőle az eredeti számot!
        A program írja ki, hogy az eredmény egyenlő-e 5-tel?

5. Írj metódust, mely a paraméterben kapott szövegnek kiírja a hosszát!
        Az 5. karakterét nagybetűvel!
"""

def lottoszamok():
    '''1. Generálj 5 véletlen lottószámot
        [1,90]'''
    print("1. Feladat: lottószámok")
    i: int= 0
    while i<5:
        szam: int= math.floor(random.random()*91)
        print(szam, end=" ")
        i += 1


def ketjegyu_szam():
    '''2. Generálj 1 véletlen kétjegyű egész számot
        Döntsd el róla, hogy páros, vagy páratlan!'''
    print("2. Feladat: kétjegyűszám")
    i: int= 0
    while i<1:
        szam: int= math.floor(random.random()*90+10)
        if szam % 2 == 0:
            print(f"A {szam} szám páros!")
        else:
            print(f"A {szam} szám páratlan!")
        i += 1


def intervallum():
    '''3. Generálj 15 db egész számot [0,1] között
        Hány 1-est generáltál?'''
    print("3. Feladat: 15 db egész szám")
    i: int= 0
    egyesek: int= 0
    while i < 15:
        szam: int= math.floor(random.random()*2+0)
        print(szam, end=" ")
        i += 1
        if szam == 1:
            egyesek += 1

    print(" ")    
    print("1-esek száma:", egyesek)


def veletlen_szam_muveletek():
    '''4. Generálj egy véletlen számot 1 és 10 között!
        Szorozd meg 3-mal
        Vonj ki belőle  15-öt
        Oszd el 6-tal
        szorozd be 2-vel
        Vond ki belőle az eredeti számot!
        A program írja ki, hogy az eredmény egyenlő-e 5-tel?'''
    print("4. Feladat: véletlen szám műveletek")
    i: int= 0
    while i<1:
        szam: int= math.floor(random.random()*10)
        osszeg: int= szam * 3 - 15 / 6 * 2 - szam
        if osszeg == 5:
             print(f"A(z) {osszeg} egyenlő 5-tel!")
        else:
            print(f"A(z) {osszeg} nem egyenlő 5-tel!")  
        i += 1
   
def szoveg_kiiras(szoveg):
    '''5. Írj metódust, mely a paraméterben kapott szövegnek kiírja a hosszát!
        Az 5. karakterét nagybetűvel!'''
    print("5. Feladat: szöveg kiírás")
    print(szoveg)
    hossz = len(szoveg)
    print("A szöveg hossza:", hossz)
    nagybetu = szoveg[:4] + szoveg[4].upper() + szoveg[5:]
    print(nagybetu)
    
    