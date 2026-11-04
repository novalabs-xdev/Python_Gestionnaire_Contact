def get_clean_input(msg : str, msg_error = "Saisie invalide, Recommencez") -> str:
    while True:
        entree = input(msg).strip() 
        if entree == "":
                print(msg_error)
                continue
        return entree

def get_numero_telephone() -> str:
    while True:
        telephone = get_clean_input("Entrez le numero du contact : ")
        telephone = telephone.replace(' ','')
        if not telephone.isdigit():
            print("Vous devez saisir uniquement des nombres, Recommencez !")
            continue
        if len(telephone) != 9:
            print("Le nombre de caractere ne doit pas depasser 9")
            continue
        return telephone


from tabulate import tabulate

def display_data(data, columns, format="rounded_grid") -> None:
    print(tabulate(data, headers=columns, tablefmt=format))


# TODO : Implementer La fonction qui permet d'afficher le menu
def display_menu(title:str, items:list[str], symb:str='*') -> None:
    pass
# TODO : Implementer la fonction qui permet de chercher un contact par son ou son telephone
def display_menu():
    pass


if __name__ == '__main__':
     pass