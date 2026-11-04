from helpers import get_clean_input, get_numero_telephone
from contacts import creer_contact, ajouter_contact, lister_contacts
from db import contacts

if __name__ == "__main__":
    while True:
        print("#=======CARNET DE CONTACTS=======#")
        print("1. Creer contact")
        print("2. Lister contacts")
        print("0. Quitter")
        choix = get_clean_input("==> ")
        match(choix):
            case '1':
                nom = get_clean_input("Entrez le nom du contact : ")
                telephone = get_numero_telephone()
                contact = creer_contact(nom, telephone)
                ajouter_contact(contacts, contact)
                print(f"{contact["nom"]} enregistre(e) avec succes")
            case '2':
                lister_contacts(contacts)
            case '0':
                print("Au revoir")
                break
    