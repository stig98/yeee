
#The user must be able to
#1. Locate all possible charging stations and supplier information.
#2. Get information about relevant specifications of a charger.
#3. Get information about the charging fee for each charging station.
#4. Get status updates while charging. The user wants to know how long the charging
#time is and when the car is fully charged.
#5. See the personal consumption.


import time
import mysql.connector
import pandas as pd # så man kan læse csv og håndtere dens data
import csv # man skal downloade csv for at kunne åbne csv filer
from beautifultable import BeautifulTable

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Kbq5nwo#",
    database="Greenstop"
)
cursor = conn.cursor()


def bruger():
    text1 = "Tak for at oprette dig som bruger"
    fornavn= input("Indtast fornavn ")
    efternavn = input("Indtast efternavn ")
    brugerpassword = input("Indtast dit password ")
    adresse= input("Indtast Adresse ")
    postnummer = input("Indtast din Postnummer ")
    telefonnummer = input("Indtast dit Telefonummer ")
    email = input("Indtast din email ")
    sql = "INSERT INTO Bruger (Fornavn,Efternavn,BrugerPassword,Adresse,Postnummer,Telefonnummer,Email) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    val = (fornavn,efternavn,brugerpassword,adresse,postnummer,telefonnummer,email)
    ### Her bliver dataen indsat i databasen.###
    cursor.execute(sql,val)
    conn.commit()
    print(text1)



### Her kommer funktionen der indsætter brugerdataen, fra tidligere funktion, ind i databasen. Da alle user_inputsne blev defineret som global variabels, kan de hentes i denne funktion.###
### Helt konkret sker det ved at der bliver oprettet variabler, som henter informationen med .get(), dernæst bliver de variabler indast i databasen med SQL connectoren.
#def opret_bruger():
    #fornavn = a1.get()
    #efternavn = b1.get()
    #password = f1.get()
    #telefon = w1.get()
    #adresse = c1.get()
    #postnummer = e1.get()
    #email = d1.get()

### Her gør vi brug af %s metoden til at indsætte data, dette gør vi af to årsager, ét så vi kan bruge user inputs som variabler, men også så der ikke kan søges i databasen ved hjælp af SQL injections.###
    #sql = "INSERT INTO Bruger (Fornavn,Efternavn, BrugerPassword, TelefonNummer, Adresse, PostNummer, Email) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    #val = (fornavn,efternavn,password,telefon,adresse, postnummer,email)
### Her bliver dataen indsat i databasen.###
    #cursor.execute(sql,val)
    #conn.commit()





def vis_ladestationer():
    text2 = " PlugID 1 = Type1 \n PlugID 2 = Type2 \n PlugID3 = Type3"
    th = ["Laengdegrad", "Breddegrad", "AntalLadere", "Udbyder", "PlugID"]
    cursor.execute("select Laengdegrad, Breddegrad, AntalLadere, Udbyder, PlugID from Ladestation where Ledighed = 'Ledig' limit 10")
    myresult = cursor.fetchall()
    table = BeautifulTable()
    table.columns.header = th
    table.set_style(BeautifulTable.STYLE_RST)
    for row in myresult:
        table.rows.append(row)
    print(table)
    print(text2)


def forbrug():
    th = ["LeverandoerNavn","Pris_Pr_KW"]
    cursor.execute("SELECT LeverandoerNavn, Pris_Pr_KW from leverandoer")
    myresult = cursor.fetchall()
    table = BeautifulTable()
    table.columns.header = th
    table.set_style(BeautifulTable.STYLE_RST)
    for row in myresult:
        table.rows.append(row)
    print(table)

#def forbrug():
    #mycursor.execute("select AntalKW from AkkumuleretForbrug")
    #mycursor.execute("select TotalBeloeb from AkkumuleretForbrug")

    #myresult2 = mycursor.fetchone()
    #antalKW = mycursor.execute("select AntalKW from AkkumuleretForbrug")

    for y in myresult2:
        outstring = "Du har i maj måned brugt: " + str(y) + "KW \n betalt " + str(f) + "Kr."
        print(y)

#class Bruger:

    #def __init__(self, fornavn, efternavn, adresse, postnummer, telefonnummer, nummerplade, email):
    #    self.fornavn = fornavn
    #    self.efternavn = efternavn
    #    self.adresse = adresse
    #    self. postnummer = postnummer
    #    self.telefonnummer = telefonnummer
    #    self.nummerplade = nummerplade
    #    self.email = email

    #def profil(self):
    #    return (f"""
    #    Navn: {self.fornavn} {self.efternavn}
    #    Adresse: {self.adresse} {self.postnummer}
    #    Kontakt: {self.telefonnummer} eller {self.email}
    #    Bils nummerplade: {self.nummerplade}""")

# så skal man på en måde kunne hente dataen om brugerne fra sql filen?? hvordan?


#class Ladestation:

    #def __init__(self, laengdegrad, breddegrad, antal_ladere, ledighed, leverandoer):
        #self.laengdegrad = laengdegrad
        #self.breddegrad = breddegrad
        #self.antal_ladere = antal_ladere
        #self.ledighed = ledighed
        #self. leverandoer = leverandoer

    #def ladeplads(self):
        #return (f"""
        #Lokation for ladestation: {self.laengdegrad}, {self.breddegrad}.
        #Der er {self.antal_ladere} til rådighed og de er {self.ledighed}.
        #Laderene er leveret af {self.leverandoer}.""")


#class Leverandoer:

    #def __init__(self, leverandoernavn, pris):
    #    self.leverandoernavn = leverandoernavn
    #    self.pris = pris_pr_kw

    #def leverandoer_info(self):
    #    return (f"""
    #    Leverandøren for denne ladestation er {self.leverandoernavn} og pris pr. Kw er {self.pris_pr_kw}.
    #    """)




function_dictionary = {'1':'Opret bruger', '2': 'Vis ledige ladestationer i nærheden.', '3':'Vis typer af ladere.', '4':'Se pris pr. Kw', '5':'Se status for min opladning.', '6':'Vis mit forbrug.','Q':'Tryk Q for at afslutte program.'}


# while loop
GreenStop_running = True
while GreenStop_running == True:
    time.sleep(2)#KAN FJERNES HVIS DET GÅR FOR LANGSOMT - DET ER I SEKUNDER.
    print("\n Velkommen til GreenStop.")
    for key,value in function_dictionary.items():
        print(str(key) + ". " + str(value))

    Choice = input('Vælge et nummer for at bruge menuen eller tryk Q for at afslutte.') # bed om brugerinput for at vælge funktion

    if Choice == "1":
        bruger()
    elif Choice == "2": # elif-statements kører kun igennem programmet hvis condition er opfyldt. Derfor sparer elif-statements på handligner i programmet frem for if-statemetns
        vis_ladestationer()
    elif Choice == "3":
        forbrug()
    elif Choice == "4":
        Opladning()
    elif Choice == "5":
        print()
    elif Choice == "6":
        forbrug()
    elif Choice == "Q":
        print("GreenStop lukker ned.")
        GreenStop_running = False
    else:
        print('Vælg en mulighed fra menuen.')


curP = cursor[8][10] #Henter nuværende procent for en person
remainingpower = 100-curP #udregner hvor meget strøm de mangler i procent
ladertid = 2 #hvor lang tid laderen er om at lade 1 procent i minutter
tidtilbage = ladertid * remainingpower # hvor lang tid der går før den er helt ladt op i minutter
kwpris = 10 #pris pr minut
samletpris = tidtilbage * kwpris #hvor meget man i alt skal betale

samletpris = (100-cursor[8][10])*2*10


#vi ændrer person nr 10 samlede forbrug ved at tilføje pris for at lade op
forbrug[3][10] = forbrug[3][10] + samletpris
#placering
