def citire_lista():
    """
    Functia citeste o lista de nr intregi
    :return: lista
    """
    lista = []
    lungime_lista = int(input("Dati lungimea listei :"))
    nr_elemente = 1
    while lungime_lista:
        element = int(input(f" Elementul {nr_elemente} este :"))
        lista.append(element)
        lungime_lista -= 1
        nr_elemente += 1
    return lista

def numar_pozitie(lista,nr,poz):
    """
    cauta un numar pe o pozitite citita de la tastatura
    :param lista: lista de nr intregi
    :return: true daca numarul citit este pe pozitita citita sau false in caz contrar
    """
    pozitie=0
    for x in lista:
        if nr==x and pozitie >= poz:
            return True
        else:
            pozitie += 1
    return False

def test_numar_pozitie():
    assert numar_pozitie([2,32,122,12,1456],12,3) == True
    assert numar_pozitie([2,32,122,12,1456],12,4) == False
    assert numar_pozitie([1,2,3,4],1,0) == True
    assert numar_pozitie([1,3,5,6,7],6,2) == True

def suma(lista):
    """
    calculeaza suma nr pare din lista
    :param lista: lista de nr intregi
    :return: suma
    """
    s = 0
    for x in lista:
        if x % 2 == 0:
            s = s + x
    return s

def test_suma():
    assert suma([2,3,4,5,6]) == 12
    assert suma([2,3,12,5,9]) == 14

def nr_pare_unicate(lista):
    """
    functia identifica numerele pare din lista ce apar o singura data
    :param lista: lista de nr intregi
    :return: lista doar cu numerele pare ce apar o singura data
    """
    rezultat = []
    nr_aparitii=0
    for x in lista:
        nr_aparitii=lista.count(x)
        if nr_aparitii == 1 and x % 2 == 0:
            rezultat.append(x)

    return rezultat

def test_nr_pare_unicate():
    assert nr_pare_unicate([23,12,3,52,13]) == [12,52]
    assert nr_pare_unicate([2,4,5,4,6,12]) == [2,6,12]

def inlocuire_nr(lista):
    """
    inlocuieste numerele din lista care se pot scrie ca suma de alte 2  numere distincte din lista
    :param lista: lista de nr intregi
    :return: tuplu
    """
    rezultat = lista[:]
    for i in range(0, len(lista) - 1):
        for j in lista:
            now = lista[i] - j
            if now in lista and now != j:
                rezultat[i] = (j, now)

    return rezultat



def main():

    lista=[]

    test_numar_pozitie()
    test_suma()
    test_nr_pare_unicate()

    while True:
        print("1.Citeste lista")
        print("2.Det data un numar citit se afla pe o pozitie citita")
        print("3.Afiseaza suma elementelor pare din lista")
        print("4.Afișeaza toate numere din lista care sunt pare si apar o singura data")
        print("5.Afișați lista obținută prin înlocuirea fiecărui număr cu un tuplu format din două numere de pe"
                "poziții distincte")
        print("x.Iesire")
        optiune = input("Alegeti optiunea :")

        if optiune == "1":
            lista =citire_lista()
            print()
        if optiune == "2":
            nr = int(input("dati un nr:"))
            poz = int(input("dati o pozitie:"))
            if numar_pozitie(lista,nr,poz):
                print("DA")
            else:
                print("NU")
        if optiune == "3":
            print(suma(lista))
        if optiune == "4":
            print(nr_pare_unicate(lista))
        if optiune == "5":
            print(inlocuire_nr(lista))
        if optiune == "x":
            break



main()
