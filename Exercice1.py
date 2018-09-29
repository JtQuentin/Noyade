# Fonction qui vérifie si l'année saisie est bissextile ou non
def bissextile(year):
    biss = False
    if year % 400 == 0:
        biss = True
    elif year % 100 == 0:
        biss = False
    elif year % 4 == 0:
        biss = True
    return biss


# Fonction qui vérifie que le jour rentré est correct par rapport au mois et à l'année pour février
def verifJour(day, month, year):
    verif = True
    mois30 = ["avril", "juin", "septembre", "novembre"]
    if day < 1 or day > 31:
        verif = False
    elif month == "février":
        if bissextile(year):
            if day > 29:
                verif = False
        elif bissextile(year) is False:
            if day > 28:
                verif = False
    elif month in mois30:
        if day > 30:
            verif = False
    return verif


# On vérifie les valeurs rentrées par l'utilisateur
months = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
year = int(input("Saisir l'année : "))
while year < 1582:
    print("L'année doit être supérieure à 1581")
    year = int(input("Saisir l'année : "))
month = input("Saisir le mois : ").casefold()
while month not in months:
    print("Mois incorrect")
    month = input("Saisir le mois : ").casefold()
day = int(input("Saisir le jour : "))
while verifJour(day, month, year) is False:
    print("Le jour n'est pas correct")
    day = int(input("Saisir le jour : "))

# On garde les deux derniers chiffres de l'année
n = year % 100

# On ajoute 1/4 de ce chiffre en ignorant les restes
n += (n // 4)

# On ajoute la journée du mois
n += day

# On ajoute selon le mois
if month == "mai":
    n += 1
elif month == "août":
    n += 2
elif month == "février" or month == "mars" or month == "novembre":
    n += 3
elif month == "juin":
    n += 4
elif month == "septembre" or month == "décembre":
    n += 5
elif month == "avril" or month == "juillet":
    n += 6

# Si l'année est bissextile et le mois est janvier ou février, on ôte 1
if bissextile(year) and month == "janvier":
    n -= 1
elif bissextile(year) and month == "février":
    n -= 1

# On ajoute selon le siècle
if str(year).startswith("16") or str(year).startswith("20"):
    n += 6
elif str(year).startswith("17") or str(year).startswith("21"):
    n += 4
elif str(year).startswith("18"):
    n += 2

# On divise la somme par 7 et on garde le reste
n %= 7

# Le reste représente le jour de la semaine recherché
if n == 0:
    print("Le {} {} {} est un Dimanche".format(day, month, year))
elif n == 1:
    print("Le {} {} {} est un Lundi".format(day, month, year))
elif n == 2:
    print("Le {} {} {} est un Mardi".format(day, month, year))
elif n == 3:
    print("Le {} {} {} est un Mercredi".format(day, month, year))
elif n == 4:
    print("Le {} {} {} est un Jeudi".format(day, month, year))
elif n == 5:
    print("Le {} {} {} est un Vendredi".format(day, month, year))
elif n == 6:
    print("Le {} {} {} est un Samedi".format(day, month, year))
