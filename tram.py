def rechercheArret(_lignes, _nomLignes, _arret):
    reponse = []
    numeroLigne = 0
    while numeroLigne < len(_lignes):
        numeroArret = 0
        while numeroArret<len(_lignes[numeroLigne]):
            if _lignes[numeroLigne][numeroArret] == _arret : 
                # print("Nom de la ligne : ",_nomLignes[numeroLigne])
                reponse.append(numeroLigne)
                reponse.append(_nomLignes[numeroLigne])
            numeroArret+=1
        numeroLigne+=1
    return reponse

def rechercheLigneEnCommun(_liste1, _liste2):
    i=0
    while i < len(_liste1):
        j=0
        while j < len(_liste2):
            if _liste1[i] == _liste2[j]:
                print("Tram sur la même ligne : ",_liste1[i])
            j+=1
        i+=1

# Affiche le terminus et la direction des lignes utilisé
def rechercheTerminusTrajet(_depart, _arrivee):
    listArret = ListeLigne[rechercheArret(ListeLigne, NomLigne, depart)[0]]

    if _depart > _arrivee in listArret:
        print("Le tramway ce dirige vers le début de la ligne, Terminus : ", listArret[0])
    else :
        print("Le tramway ce dirige vers la fin de la ligne, Terminus : ", listArret[-1])

# Toutes les correspondances entre le point de départ et l'arrivee
def correspondance(_depart, _arrivee):
    tousarret = []
    tousarret += (ListeLigne[rechercheArret(ListeLigne, NomLigne, _depart)[0]])
    tousarret += (ListeLigne[rechercheArret(ListeLigne, NomLigne, _arrivee)[0]])
    duplicates = []

    for i in range(len(tousarret)):
        for j in range(i+1, len(tousarret)):
            if tousarret[i] == tousarret[j]:
                if tousarret[i] not in duplicates:
                    duplicates.append(tousarret[i])

    if len(duplicates)>0:
        print("Correspondance :",duplicates)
    else:
        print("Aucune correspondance trouvé")

# Nombres d'arrets entre le depart et l'arrivee sur la même ligne
def nombreArrets(_depart, _arrivee):
    tousarret = []
    tousarret += (ListeLigne[rechercheArret(ListeLigne, NomLigne, _depart)[0]])
    tousarret += (ListeLigne[rechercheArret(ListeLigne, NomLigne, _arrivee)[0]])

    # print('tout les arrets : ', tousarret)

    count = 0

    for i in range(tousarret.index(_depart), tousarret.index(_arrivee)):
        count += 1
    print('nombre d\'arret : ', count)


if __name__ == "__main__":

    TronconPrincipalTramA = ["Le Haillan Rostand", "Les Pins","Frères Robinson", "Hôtel de Ville Mérignac", "Pin Galant","Mérignac Centre", "Lycées de Mérignac", "Quatre Chemins", "PierreMendès-France", "Alfred de Vigny", "Fontaine d'Arlac", "Peychotte","François Mitterrand", "Saint-Augustin", "Hôpital Pellegrin", "StadeChaban-Delmas", "Gaviniès", "Hôtel de Police", "Saint-Bruno - Hôtelde Région", "Mériadeck", "Palais de Justice", "Hôtel de Ville","Sainte-Catherine", "Place du Palais", "Porte de Bourgogne","Stalingrad", "Jardin botanique", "Thiers - Benauge", "Galin", "JeanJaurès", "Cenon Gare", "Carnot - Mairie de Cenon", "Buttinière"]
    TronconPrincipalTramB = ["Berges de la Garonne", "Claveau","Brandenburg", "New-York", "Rue Achard", "Bassins à Flot", "LesHangars", "Cours du Médoc", "Chartrons", "CAPC (Musée d'ArtContemporain)", "Quinconces", "Grand Théâtre", "Gambetta", "Hôtel deVille", "Musée d'Aquitaine", "Victoire", "Saint-Nicolas","Bergonié", "Barrière Saint-Genès", "Roustaing", "Forum","Peixotto", "Béthanie", "Arts et Métiers", "François Bordes", "DoyenBrus", "Montaigne-Montesquieu", "UNITEC", "Saige", "Bougnard"]
    TronconPrincipalTramC = ["Parc des Expositions", "Palais desCongrès", "Quarante Journaux", "Berges du lac", "Les Aubiers","Place Ravezies-Le Bouscat", "Grand Parc", "Émile Counord", "CamilleGodard", "Place Paul Doumer", "Jardin Public", "Quinconces", "Placede la Bourse", "Porte de Bourgogne", "Saint-Michel", "Sainte-Croix","Tauzia", "Gare Saint-Jean", "Belcier", "Carle Vernet", "BèglesTerres Neuves", "La Belle Rose", "Stade Musard", "Calais –Centujean", "Gare de Bègles", "Parc de Mussonville", "Lycée VaclavHavel"]
    TronconPrincipalTramD = ["Quinconces", "Charles Gruet", "MarieBrizard", "Barrière du Médoc", "Courbet", "Calypso", "Mairie duBouscat", "Les Ecus", "Sainte-Germaine", "Hippodrome","Le Sulky","Toulouse Lautrec", "Picot", "Eysines Centre", "Les Sources","Cantinolle"]

    NomLigne = ["TramA","TramB","TramC","TramD"]
    ListeLigne = [TronconPrincipalTramA,TronconPrincipalTramB,TronconPrincipalTramC,TronconPrincipalTramD]

    # Recherche départ dans une ligne
    depart = input('Saisir le nom de l\'arret de départ : ')
    ListeLignesDepartTrouvees = rechercheArret(ListeLigne, NomLigne, depart)
    print("Ligne départ : ",ListeLignesDepartTrouvees[1])

    # Recherche départ dans une ligne
    arrivee = input('Saisir le nom de l\'arret de arrivé : ')
    ListeLignesArriveeTrouvees = rechercheArret(ListeLigne, NomLigne, arrivee)
    print("Ligne arrivé",ListeLignesArriveeTrouvees)

    # Recherche départ et arrivée sur une même ligne
    rechercheLigneEnCommun(ListeLignesDepartTrouvees, ListeLignesArriveeTrouvees)

    rechercheTerminusTrajet(depart, arrivee)

    correspondance(depart, arrivee)

    nombreArrets(depart, arrivee)


     

