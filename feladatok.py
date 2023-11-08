def feladat1():
    print("1. Feladat")
    '''1. Kérj be egy [200, 920] intervallumban lévő egész számot (ha nem ebben az intervallumban van, jelezz hibát!), majd írasd ki az első számjegyét!'''
    a: int=int(input("Adjon meg egy 200-920 közötti egész számot: "))
    if 200 <= a <= 920:
        szam: str= int(str(a)[0])
        print(szam)
    else:
        print("HIBA!")


def feladat2(szam:int):
    print("2. Feladat")
    print("Szám: ", szam)
    '''Hogy kapjuk meg az utolsó számjegyét?'''
    while (szam>9):
        print("Következő számjegy", szam % 10)
        szam= szam // 10
        print("Az aktuális szám ", szam)

    print("Az utolsó számjegy ", szam)


def feladat2_2(szam:int):
    szoveg_szam: str= str(szam)
    i=0
    while i<len(szoveg_szam):
        print(szoveg_szam[i])
        i += 1
    

def feladat3(a):
    print("3. Feladat")
    '''3. Írj eljárást, mely paraméterében kap egy számot, majd összeadja a számjegyeket és kiírja a számjegyek összegét a képernyőre. 
    PL. 324 -> „324 számjegyeinek összege: 9”'''
    osszeg = 0
    while a > 0:
        maradek = a % 10
        osszeg += maradek
        a //= 10
    print(f'A számjegyek összege: {osszeg}')


def feladat4(a:int):
    print("4. Feladat")
    '''4. Egy hétfői napon az 1-es csoportnak 9 órája van. Az első órában a teljesítményük 90%-át képesek nyújtani. A 2-3. órában már kissé éhesek, és csupán 60%-os a munkabírásuk. A 4-7. órában szerencsére programozást tanulnak, így némiképp javul a hatékonyságuk (70%), a 8-9. órában azonban már újra lecsökken (50%). Írj metódust, mely paraméterében kap egy egész számot 1 és 9 között (melyik órán vannak; jelezz hibát, ha nem ebben az intervallumban lévő számot kapsz, pl. “Ez már tényleg túlzás.”). Példa egy esetre: Be: 3, Ki: “Még bírjuk (60%).”    -  nem kell tesztfüggvényeket írni, de az alábbi táblázat alapján ellenőrizzétek a munkátokat!'''
    if a == 1:
        print("Kiválóan vagyunk (90%).")
    elif a == 2 or a == 3:
        print("Éhség nagy úr (60%).")
    elif a == 4 or a == 5 or a == 6 or a == 7:
        print("Kezdek jól lenni (70%).")
    elif a == 8 or a == 9:
        print("Nem túl jó (50%).")
    elif a == 0:
        print("Be se jövök!")
    else:
        print("Túl lő a célon!")


def feladat6():
    print("6. Feladat")
    '''6. A program számítsa ki egy beolvasott valós szám négyzetgyökét! A program adjon hibaüzenetet, ha a felhasználó negatív számból akar gyököt vonni!'''
    a: int= int(input("Adjon meg egy egész számot: "))
    if a > 0:
        gyok: int= a ** 0.5
        print(gyok)
    else:
        print("HIBA!")


'''8. Írj programot, ami kiírja a 10x10-es alapú szorzótáblát! 10-esével egymás alá! használj hozzá formázott kiiratást!'''
def feladat8():
    print("8. Feladat")
    a: int= 1
    b: int= 10
    while a <= 10:
        vege: int= a * b
        print(f"{a} * {b} = {vege}")
        a += 1


def ermedobas():
    # 1. kel egy olyan ciklus, ami pontosan 10-szer fut le
    i:int = 0
    f_szam:int = 0
    fhossz:int = 0
    max_hossz: int = 0
    elozo_string_f=False
    while i<10:
        jel:str = input("F/I: ")
        while not ((jel == "F") or (jel == "f") or (jel == "I") or (jel == "i")):
            jel:str = input("Nem jó, F/I -t adj meg!: ")

        if (jel == 'f' or jel == 'F'):
            f_szam += 1
            fhossz += 1
            elozo_string_f=True
        else:
            print("Aktuális hossz ", fhossz)
            elozo_string_f=False
            """itt összehasonlítjuk az eddigi max hosszt az aktuális hosszal"""
            if (max_hossz<fhossz):
                max_hossz=fhossz
            fhossz = 0

        i += 1

    print("aktuális hossz ", fhossz)
    if (max_hossz<fhossz):
        max_hossz=fhossz
    print("F-ek száma: ", f_szam)
    print("Maximális F hossz: ", max_hossz)