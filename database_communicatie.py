def lees_data_uit(bestandspad):
    bestand = open(bestandspad,"r")
    info = []
    for dingen in bestand:
        info.append(dingen)
    return info
bestandspad = "playerinfo.txt"
def zet_data_om_naar_dict(data):
    db = []
    for info in data:
        info = info.split(" - ")
        data_dict = {
            "username":info[0],
            "wachtwoord":info[1],
            "level":info[2],
            "exp":int(info[3]),
            "extra_bommen":int(info[4]),
            "extra_pogingen":int(info[5]),
        }
        db.append(data_dict)
    return db
def verander_level_en_exp(bestandspad,exp,gebruikers_index):
    level_up = False
    data = lees_data_uit(bestandspad)
    bestand = open(bestandspad,"w")
    for info in data:
        if info == data[gebruikers_index] :
            info = info.split(" - ")
            nieuw_exp = exp + int(info[3])
            if nieuw_exp < 100:
                info[3] = nieuw_exp
                bestand.write(info[0] + " - " + info[1] + " - " + info[2] + " - " + str(info[3])+" - "+ str(info[4]) + " - "+info[5])
            else:
                level = 1 + int(info[2])
                nieuw_exp -= 100
                info[2] = level
                info[3] = nieuw_exp
                bestand.write(info[0] + " - " + info[1] + " - " + str(info[2]) + " - " + str(info[3]) + " - " + str(info[4]) + " - " + info[5])
                level_up = True
        else:
            bestand.write(info)
        if level_up:
            bestand.close()
            return 1
    bestand.close()
    return 0


def inloggen(data_dict):
    gebruikersnaam = input("wat is je gebruikersnaam ")
    wachtwoord = input("wat is je wachtwoord ")
    for index,data in enumerate(data_dict):
        if gebruikersnaam == data["username"] and wachtwoord == data["wachtwoord"]:
            return index
    return False

def registreer(bestandspad,data_dict):
    gebruikersnaam = False
    while not gebruikersnaam:
        gebruikersnaam = input("wat is je gebruikersnaam ")
        for info in data_dict:
            if info["username"] == gebruikersnaam:
                print("sorry die is al bezet")
                gebruikersnaam = False

    wachtwoord = input("welk wachtwoord wil je kiezen ")
    bestand = open(bestandspad,"a")
    bestand.write("\n" + gebruikersnaam + " - "+wachtwoord+" - "+  "1" + " - " + "0" + " - " + "0" + " - " + "0")
    print("gebruiker geregistreerd")
def level_up_rewards_geven(bestandspad,gebruikers_index,bom_of_kanon):
    data = lees_data_uit(bestandspad)
    bestand = open(bestandspad,"w")
    for info in data:
        if info == data[gebruikers_index]:
            info = info.split(" - ")
            if bom_of_kanon == "bom":
                info[4] = 1 + int(info[4])
                bestand.write(info[0] + " - " + info[1] + " - " + str(info[2]) + " - " + str(info[3]) + " - " + str(info[4]) + " - " + info[5])
            else:
                info[5] = 3 + int(info[5])
                bestand.write(info[0] + " - " + info[1] + " - " + str(info[2]) + " - " + str(info[3]) + " - " + str(info[4]) + " - " + info[5])
        else:
            bestand.write(info)






