from game import game
from database_communicatie import inloggen
from database_communicatie import lees_data_uit
from database_communicatie import zet_data_om_naar_dict
from database_communicatie import registreer
from database_communicatie import verander_level_en_exp
from database_communicatie import level_up_rewards_geven
def main():
    bestandspad = "playerinfo.txt"
    data = lees_data_uit(bestandspad)
    data_dict = zet_data_om_naar_dict(data)
    gebruiker_index = False
    inloggen_of_registreren = input("welkom tot mijn zeeslag 1 voor inloggen 2 voor registreeren ")
    if inloggen_of_registreren == "1":
        while not gebruiker_index:
            gebruiker_index = inloggen(data_dict)
            if not gebruiker_index:
                print("fout sukkeltje")
    else:
        registreer(bestandspad,data_dict)
        data = lees_data_uit(bestandspad)
        data_dict = zet_data_om_naar_dict(data)
        while not gebruiker_index:
            gebruiker_index = inloggen(data_dict)
    print("welkom",data_dict[gebruiker_index]["username"])
    while True:
        keuze_stoppen_of_doorgaan = input("welkom wat wil je doen typ stoppen om te stoppen en alles anders om door te gaan")
        if keuze_stoppen_of_doorgaan.lower() != "stoppen":

            kanon_shoten = 5 + data_dict[gebruiker_index]["extra_pogingen"]
            bommen = 2 + data_dict[gebruiker_index]["extra_bommen"]
            exp = game(kanon_shoten, bommen)
            level_up = verander_level_en_exp(bestandspad,exp,gebruiker_index)
            if level_up == 1:
                print("gefeliciteerd je bent level up!")
                bom_of_kanon = input("wil je een extra bom: (1) of 3 extra kanon shoten: (2)")
                if bom_of_kanon.lower() == "bom" or bom_of_kanon == "1":
                    bom_of_kanon = "bom"
                    level_up_rewards_geven(bestandspad,gebruiker_index,bom_of_kanon)
                else:
                    bom_of_kanon = "kanon"
                    level_up_rewards_geven(bestandspad,gebruiker_index,bom_of_kanon)
            data = lees_data_uit(bestandspad)
            data_dict = zet_data_om_naar_dict(data)
            print("je hebt", exp, "exp er bij nog", 100 - data_dict[gebruiker_index]["exp"], "tot het volgende level")
        else:
            exit("bye for now ........")
        input()
if __name__ == '__main__':
    main()