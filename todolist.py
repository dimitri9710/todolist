from pymongo import MongoClient


client = MongoClient('localhost', 27017)


db = client['todolist_db']


collection = db['tasks']

def afficher_taches(taches):
    if not taches:
        print("La liste des tâches est vide.")
    else:
        print("Liste des tâches :")
        for index, tache in enumerate(taches, start=1):
            print(f"{index}. {tache}")


def ajouter_tache(taches, nouvelle_tache):
    taches.append(nouvelle_tache)
    print(f"Tâche '{nouvelle_tache}' ajoutée.")


def supprimer_tache(taches, numero_tache):
    if numero_tache > 0 and numero_tache <= len(taches):
        tache_supprimee = taches.pop(numero_tache - 1)
        print(f"Tâche '{tache_supprimee}' supprimée.")
    else:
        print("Numéro de tâche invalide.")


def main():
    taches = []  

    while True:
        print("\nQue souhaitez-vous faire ?")
        print("1. Afficher les tâches")
        print("2. Ajouter une nouvelle tâche")
        print("3. Supprimer une tâche")
        print("4. Quitter")

        choix = input("Entrez votre choix : ")

        if choix == '1':
            afficher_taches(taches)
        elif choix == '2':
            nouvelle_tache = input("Entrez la nouvelle tâche : ")
            ajouter_tache(taches, nouvelle_tache)
        elif choix == '3':
            afficher_taches(taches)
            numero_tache = int(input("Entrez le numéro de la tâche à supprimer : "))
            supprimer_tache(taches, numero_tache)
        elif choix == '4':
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 4.")

if __name__ == "__main__":
    main()
