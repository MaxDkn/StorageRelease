""" programme commencé par Max le 15/02/2022 : Ce programme est fait pour supprimer les répertoires vides


>>> Aide module :
os. rmdir(path) --> pas vidé : OSError
os.path.isdir(path) --> True : si répertoire | False : si fichier

"""
import os


def sorting(chemin):
    """La fonction va lister tout les fichiers du répertoire et vérifier si ce dossier est vide, et retourner tout les
        dossier vide"""

    fichier_dossier = os.listdir(chemin)
    dossier = []
    for name in fichier_dossier:
        if os.path.isdir(f'{chemin}/{name}'):
            dossier.append(name)
    return dossier


def vacuum(path, directory):
    new_directory = []
    for name in directory:
        try:
            os.rmdir(f'{path}/{name}')
        except OSError:
            print(f"\nThe following directory was not emptied: [{name}]\n")
        else:
            print(f"The following directory is empty so it has been deleted: [{name}]\n")


def void(root):
    dossier = sorting(chemin=root)
    vacuum(path=root, directory=dossier)

if __name__ == '__main__':
    #path = 'C:/Users/max/Documents/Test'
    while True:
        path = input("Enter the root you want to check : ")
        if os.path.exists(path):
            void(root=path)
        else:
            print("\nThe root does not exist")


