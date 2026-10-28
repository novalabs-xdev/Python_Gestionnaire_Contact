#=================== Imports  ===================#
from helpers import get_clean_input, get_numero_telephone
#=================== Imports  ===================#



contacts = []

def creer_contact(nom: str, telephone: str) -> dict:
    return {
        "nom" : nom,
        "telephone" : telephone,
        "operateur": "Inconnu"
        }

def afficher_contact(contact: dict[str]) -> None:
    print(f"{contact.get("nom")} : {contact.get('telephone')} : {contact.get('operateur')}")


def ajouter_contact(contacts: list[dict], contact: dict) -> None:
    contacts.append(contact)


def lister_contacts(contacts: list[dict]) -> None:
    for contact in contacts:
        afficher_contact(contact)


# =====Programme principale ======#



if __name__ == '__main__':
    nom = get_clean_input("Entrez le nom du contact : ", msg_error="Nom invalide, Veuillez recommencer !")
    telephone = get_numero_telephone()       
       
    contact1 = creer_contact(nom, telephone)
    ajouter_contact(contacts, contact1)
    lister_contacts(contacts)