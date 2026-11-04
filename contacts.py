#=================== Imports  ===================#
from helpers import display_data 
from db import operateurs

#=================== Imports  ===================#

def creer_contact(nom: str, telephone: str) -> dict[str, str]:
    return {
        "nom" : nom,
        "telephone" : telephone,
        "operateur": detecter_operateur(telephone)
        }

def afficher_contact(contact: dict[str]) -> None:
    print(f"{contact.get("nom")} : {contact.get('telephone')} : {contact.get('operateur')}")


def ajouter_contact(contacts: list[dict[str, str]], contact: dict[str, str]) -> None:
    contacts.append(contact)

def lister_contacts(contacts: list[dict[str, str]]) -> None:
    # print(contacts)
    display_data(contacts, "keys")

def detecter_operateur(telephone: str) -> str:
    for nom_operateur, indicatifs in operateurs.items():
        if telephone[:2] in indicatifs:
            return nom_operateur
    return "Inconnu"


# =====Programme principale ======#


if __name__ == '__main__':
   pass
