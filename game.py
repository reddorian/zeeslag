from random import randint
from wapens import check_voor_bom
from wapens import kanon
def game(kanon_shoten, bommen):
    array = [
        ["~", "~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~", "~"],
    ]
    for x in array:
        print(x)
    randint1 = randint(0, 5)
    randint2 = randint(0, 5)
    while kanon_shoten > 0 or bommen > 0:
        try:
            print("je hebt nog", bommen, "bommen")
            if bommen < 1:
                wat_doen = 1
            elif kanon_shoten < 1:
                wat_doen = 2
            else:
                wat_doen = int(input("wat will je doen 1 voor kanon 2 voor bom"))
            if wat_doen == 1:
                rij = int(input("Kies een rij (1-6):")) - 1
                kolom = int(input("Kies een kolom (1-6): ")) - 1
                getal = kanon(randint1, randint2, array, rij, kolom)
                if getal == "raak":
                    break
                else:
                    kanon_shoten += getal
            elif wat_doen == 2:
                print("waar wil je de bom gooien")
                rij = int(input("Kies een rij (1-6):")) - 1
                kolom = int(input("Kies een kolom (1-6): ")) - 1
                iets = check_voor_bom(randint1, randint2, rij, kolom, array)
                if iets == "raak":
                    break
                else:
                    bommen -= 1
                print()
            print("je hebt nog", kanon_shoten, "kanon shoten")
            for x in array:
                print(x)
        except ValueError:
            print("alleen getallen sukkel 3 kanon shoten minder voor jouw")
            kanon_shoten -= 3
        except IndexError:
            print("maat 0 tot 4 kan je niet lezen ofzo min 3 pogingen voor jouw")
            kanon_shoten -= 3
        except UnboundLocalError:
            print("maatje wtf heb jij ingevuld geen pogingen meer voor jouw")
            kanon_shoten -= 100
    if kanon_shoten < 0 and bommen < 0:
        print("het antwoord was", randint1, randint2)
        array[randint1][randint2] = "S"
        for x in array:
            print(x)
        return 5
    else:
        for x in array:
            print(x)
        print("Gefeliciteerd")
        return 25
