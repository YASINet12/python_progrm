

import datetime

list = []
date = datetime.datetime.now().strftime("%x")

for i in range(3):
    nom = str(input('Saisir le nom du produit : '))
    type_pro = str(input('Saisir le type de produit : '))
    quantite = float(input('Saisir la quantité : '))
    prix_unitaire = float(input('Saisir le prix unitaire : '))
    date_ex = input("Saisir la date d'expiration au format (MM/DD/YY) : ").split("/")
    date_exp = [int(i) for i in date_ex]
    thisdic = {
        'nom': nom,
        'type_pro': type_pro,
        'prix_unitaire': prix_unitaire,
        'date_expt': date_exp,
        'quantite': quantite
    }
    list.append(thisdic)

def func(list):
    types = ['lait', 'yaourt', 'fromage', 'oeufs', 'huile']
    list_ver = []
    current_date = datetime.datetime.now().strftime("%x").split('/')
    current_date = [int(i) for i in current_date]

    for dic in list:
        if dic['type_pro'].lower() in types:

            if dic['date_expt'][-1] > current_date[-1] or \
                    (dic['date_expt'][-1] == current_date[-1] and dic['date_expt'][-3] > current_date[-3]) or \
                    (dic['date_expt'][-1] == current_date[-1] and dic['date_expt'][-3] == current_date[-3] and
                     dic['date_expt'][-2] > current_date[-2]):
                list_ver.append(dic)

    return list_ver

list_ver = func(list)

def panie(list):
    panier = []
    for _ in range(3):
        try:
            produit = input('Saisir le nom du produit que vous voulez acheter et la quantité (ex: lait,2) : ')
            nom_produit, quantite = produit.split(',')
            nom_produit = nom_produit.strip().lower()
            quantite = float(quantite)
        except ValueError:
            print("Erreur : veuillez entrer les données dans le format 'nom_produit,quantité' (ex : lait,2).")
            continue
            #pour garanti la continuite de code si unn ereur exist

        produit_trouve = False
        for dic in list:
            if dic['nom'].lower() == nom_produit:
                produit_trouve = True
                if quantite <= dic['quantite']:
                    panier.append({
                        'nom': dic['nom'],
                        'prix_unitaire': dic['prix_unitaire'],
                        'quantite': quantite
                    })
                else:
                    print(f"Quantité demandée  non disponible!")
                break

        if not produit_trouve:
            print(f"Le produit {nom_produit} n'existe pas!")

    return panier


panier = panie(list_ver)

def calcule_montant(panier):
    total = sum(item['quantite'] * item['prix_unitaire'] for item in panier)
    if total > 500:
        total *= 0.95
    return total

def generer_facture(panier):
    total = sum(item['quantite'] * item['prix_unitaire'] for item in panier)
    montant_a_payer = calcule_montant(panier)
    date = datetime.datetime.now().strftime("%m/%d/%Y")

    with open("facture.txt", "w") as file:
        file.write("Nom Produit\tPrix Unitaire\tQuantité\tPrix\n")
        for item in panier:
            file.write(
                f"{item['nom']}\t{item['prix_unitaire']}\t{item['quantite']}\t{item['quantite'] * item['prix_unitaire']}\n")
        file.write(f"Total: {total:.2f} Dh\n")
        file.write(f"Montant à payer: {montant_a_payer:.2f} Dh\n")
        file.write(f"Date: {date}\n")

if panier:
    generer_facture(panier)
    print("Facture ajoute avec succès dans 'facture.txt'.")
else:
    print("le panie rest vide donc Facture non générée.")




