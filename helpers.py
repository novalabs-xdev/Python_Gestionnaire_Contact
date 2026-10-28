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



        


if __name__ == '__main__':
     pass