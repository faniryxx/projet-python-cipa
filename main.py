##############################################
#   Python - Projet : prix de l'immobilier   #
#                                            #
#   Nathan RANAIVO RAVOAJA                   #
#   Alexandre TIGNAC                         #
#                                    CIPA4   #
##############################################

# 1. Affichage des ventes de maisons pour une commune et une année données

def mean(liste):
    """Prend en entrée une liste de nombres et retourne la moyenne de ces nombres 
    
    Paramètres: 
    liste (int[]): tableau contenant une suite de nombres

    Retourne:
    float: moyenne des valeurs dans liste
    """
    sum = 0
    for i in range(0, len(liste)):
        sum = sum + liste[i]
    if len(liste) != 0:
        moy = sum/len(liste)
    else:
        moy = 0
    return moy

def splitLineTable(data):
    """Prend en entrée une chaîne de caractères et retourne une liste des 
    portions de la chaîne d'entrée situées entre le caractère | 

    Paramètres:
    data (string): chaîne de caractères à séparer

    Retourne:
    list: portions de la chaîne data après séparation
    """
    return data.split('|')

def splitLineDictionary(entree1, entree2):
    """Prend en entrée deux chaînes de caractères et permet de créer un 
    dictionnaire à partir de ces chaînes

    Paramètres:
    entree1 (string): clés du dictionnaire à créer
    entree2 (string): valeurs du dictionnaire à créer

    Retourne:
    dict: dictionnaire avec les clés de entree1 et les valeurs de entree2
    """
    table = {}
    entree1 = splitLineTable(entree1)
    entree2 = splitLineTable(entree2)
    for index in range(0, len(entree1)):
        table[entree1[index]] = entree2[index]
    return table

def displayFunction(annee, insee):
    """Affiche un tableau avec les données correspondant à l'année et au code INSEE en paramètres

    Paramètres:
    annee (int): année correspondant au tableau qu'on veut obtenir
    insee (string): code INSEE à requêter
    """
    commune = ''
    sum = []
    sum_m2 = []
    table = []
    table.append(['Date mutation', 'Nature mutation', 'Parcelle cadastrale',
                      'Adresse', 'Valeur fonciere', 'Surface reelle bati'])
    file = open("valeursfoncieres-" + str(annee) + ".txt", "r")
    categories = file.readline()

    while True:
        line = file.readline()
        if not line:
            break
        currentDict = splitLineDictionary(categories, line)
        if len(currentDict['Code commune']) == 2:
            currentDict['Code commune'] = '0'+currentDict['Code commune']
        if len(currentDict['Code departement']) == 1:
            currentDict['Code departement'] = '0'+currentDict['Code departement']
        if (currentDict['Code departement'] + currentDict['Code commune']) == insee and (currentDict['Type local'] == 'Maison') and (currentDict['Nature mutation'] == 'Vente'):
            commune = currentDict['Commune']
            if currentDict['Valeur fonciere'] == '':
                currentDict['Valeur fonciere'] = '0,0'
            valeur = float(currentDict['Valeur fonciere'].replace(',','.'))
            sum.append(valeur)
            prix_m2 = valeur/float(currentDict['Surface reelle bati'])
            sum_m2.append(prix_m2)
            table.append([currentDict['Date mutation'], currentDict['Nature mutation'],
                currentDict['Section'] + currentDict['No plan'], 
                currentDict['No voie'] + ' ' + currentDict['Type de voie'] + ' ' + currentDict['Voie'],
                currentDict['Valeur fonciere'], currentDict['Surface reelle bati']])
                
    file.close()
    print('COMMUNE DE '+commune)
    print('Nombre de mutations concernant des maisons : '+str(len(table)-1))
    print('Valeur moyenne des mutations : '+str(round(mean(sum),2))+' E')
    print('Valeur moyenne des mutations par m2 : '+str(round(mean(sum_m2),2))+' E')
    table = sortDates(table)
    formatting = "| {:<15} | {:<15} | {:<20} | {:<35} | {:<20} | {:<20} |"
    header = formatting.format('Date mutation', 'Nature mutation', 'Parcelle cadastrale', 'Adresse', 'Valeur fonciere', 'Surface reelle bati')
    print('-'*len(header))
    print(header)
    print('-'*len(header))
    for i in range(1, len(table)):
        print (formatting.format(table[i][0], table[i][1], table[i][2], table[i][3], table[i][4] + ' E', table[i][5] + ' m2'))
    print('-'*len(header))

def sortDates(table):
    """Trie un tableau selon l'ordre chronologique du champ date mutation

    Paramètres:
    table (list): tableau à arranger selon l'ordre chronologique avec le champ date mutation à l'index 0

    Retourne:
    list: tableau trié chronologiquement
    """
    newTable = table
    newTable[0].append(0)
    for i in range(1, len(table)):
        date = table[i][0].split('/')
        days = int(date[0])+int(date[1])*30
        newTable[i].append(days)
    newTable.sort(key = lambda x:x[6])
    return newTable 
    
# 2. Affichage des communes les plus chères

def displayTown(annee, code, nbr):
    """Affiche les N villes les plus cher d'un département et d'une année 
    
    Paramètres:
    annee (int): année correspondant à la requête
    code (string): code du département à afficher
    nbr (int): nombre de villes à afficher
    """

    commune_list = {}
    commune_list_clean = {}
    moy_list = {}
    file = open("valeursfoncieres-" + str(annee) + ".txt", "r")
    categories = file.readline()

    # Récupération des données
    while True:
        commune = ''
        line = file.readline()
        if not line:
            break
        currentDict = splitLineDictionary(categories, line)
        if ((currentDict['Code departement'] == code) and (currentDict['Type local'] == 'Maison') and (currentDict['Nature mutation'] == 'Vente')):
            cadastrale = currentDict['Section'] + currentDict['No plan']
            commune = currentDict['Commune']
            if currentDict['Valeur fonciere'] == '':
                currentDict['Valeur fonciere'] = '0,0'
            valeur = float(currentDict['Valeur fonciere'].replace(',','.'))
            if(commune in commune_list):
                if(cadastrale in commune_list[commune]):
                    commune_list[commune][cadastrale][1] = float(commune_list[commune][cadastrale][1]) + float(currentDict['Surface reelle bati'])
                else:
                    commune_list[commune][cadastrale] = []
                    commune_list[commune].setdefault(cadastrale, []).append(valeur)
                    commune_list[commune].setdefault(cadastrale, []).append(currentDict['Surface reelle bati'])
            else:
                commune_list[commune] = {}
                commune_list[commune][cadastrale] = []
                commune_list[commune].setdefault(cadastrale, []).append(valeur)
                commune_list[commune].setdefault(cadastrale, []).append(currentDict['Surface reelle bati'])
    
    # Calcul du prix au m² de chaque parcelles triées par commune
    for key in commune_list:
        if(not key in commune_list_clean):
            commune_list_clean[key] = []
        for key2 in commune_list[key]:
            if (float(commune_list[key][key2][1]) != 0):
                prix_m2 = float(commune_list[key][key2][0])/float(commune_list[key][key2][1])
                commune_list_clean.setdefault(key, []).append(prix_m2)
    
    # Calcul de la moyenne du prix par m² de chaque communes
    for key in commune_list_clean:
        moy_list[key] = round(mean(commune_list_clean[key]),2)
    
    # Tri par le prix au m² (décroissant)
    sorted_dict = dict(sorted(moy_list.items(),
                           key=lambda item: item[1],
                           reverse=True))
    
    # Controle sur le nombre de villes à afficher
    if(nbr>len(sorted_dict)):
        nbr = len(sorted_dict)
    
    # Affichage de la liste des villes
    for i in range(0, nbr):
        print(str(i+1) + '.\t' + str(list(sorted_dict.keys())[i]) + ' : ' + str(sorted_dict[list(sorted_dict.keys())[i]]) + '€/m2')
    file.close()
    

def launcher():
    """Gère le déroulement du programme"""
    print("Quelle fonction voulez vous lancer ?")
    print("1 : Afficher toute les ventes de maisons pour un insee donné et une année")
    print("2 : Afficher les villes les plus cher pour un département donnné")
    retry = True
    while(retry == True):
        choix = input('Votre choix: ')
        if choix == '1' :
            retry = False
            annee = input("Quelle année : ")
            insee = input("INSEEE de la ville : ")
            displayFunction(int(annee), insee)
        elif choix == '2':
            retry = False
            annee = input("Quelle année : ")
            departement = input("Code du departement : ")
            nbr = input("Nombre de ville à afficher : ")
            displayTown(int(annee), departement, int(nbr))
        else:
            print("Mauvaise entrée")

if __name__ == "__main__":
    launcher()