def bom_maakt_x(randint3,randint4,array):
    print("boom je hebt de bom gegooid")
    index = 0
    for x in array:
        x[randint4] = "X"
    for _ in array[randint3]:
        array[randint3][index] = "X"
        index += 1
    return -1

def kanon(randint1,randint2,array,rij,kolom):
    if array[rij][kolom] == "X":
        print("daar heb je al geschoten sukkeltje 2 pogingen weg nu")
        return -2
    else:
        array[rij][kolom] = "X"
    if array[randint1][randint2] == "X":
        print("Raak! Je hebt het schip geraakt!")
        array[randint1][randint2] = "S"
        return "raak"
    else:
        print("Mis! Er ligt geen schip op deze plek.")
        array[rij][kolom] = "X"
        return -1
def check_voor_bom(randint1,randint2,rij,kolom,array):
        iets = bom_maakt_x(rij,kolom,array)
        if array[randint1][randint2] == "X":
            print("Raak! Je hebt het schip geraakt!")
            array[randint1][randint2] = "S"
            return "raak"
        else:
            return iets
