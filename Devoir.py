from abc import ABC, abstractmethod
import json
class Animal(ABC):
    def __init__(self, code, nom_scientifique, espece, nombre_de_pieds, pays_d_origine):
        self.code = code
        self.nom_scientifique = nom_scientifique
        self.espece = espece
        self.nombre_de_pieds = nombre_de_pieds
        self.pays_d_origine = pays_d_origine

    def get_info(self):
        return self.code, self.nom_scientifique, self.espece, self.nombre_de_pieds, self.pays_d_origine

    def set_info(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key) and value is not None:
                setattr(self, key, value)

    def afficher_info(self):
        print(f"Code: {self.code}, Nom Scientifique: {self.nom_scientifique}, Espèce: {self.espece}, "
              f"Nombre de Pieds: {self.nombre_de_pieds}, Pays d'Origine: {self.pays_d_origine}")

    @abstractmethod
    def se_deplacer(self):
        pass


class Chien(Animal):
    def se_deplacer(self):
        print("Le chien marche avec 4 pieds.")

    def afficher_info(self):
        print("Chien")
        super().afficher_info()


class Chat(Animal):
    def se_deplacer(self):
        print("Le chat marche avec 4 pieds.")

    def afficher_info(self):
        print("Chat")
        super().afficher_info()


class Poulet(Animal):
    def se_deplacer(self):
        print("Le poulet marche avec 2 pieds.")

    def afficher_info(self):
        print("Poulet")
        super().afficher_info()


class Vache(Animal):
    def se_deplacer(self):
        print("La vache marche avec 4 pieds.")

    def afficher_info(self):
        print("Vache")
        super().afficher_info()


class Zoo:
    def __init__(self, nom, superficie):
        self.nom = nom
        self.superficie = superficie
        self.animals = []

    def ajouter_animal(self, animal):
        self.animals.append(animal)

    def supprimer_animal(self, code):
        self.animals = [a for a in self.animals if a.code != code]

    def update_animal(self, code, **kwargs):
        for animal in self.animals:
            if animal.code == code:
                animal.set_info(**kwargs)

    def chercher_animal(self, espece):
        return [a for a in self.animals if a.espece == espece]

    def nombre_animal(self, nom_scientifique):
        return sum(1 for a in self.animals if a.nom_scientifique == nom_scientifique)

    def tri_animal(self, key='code'):
        self.animals.sort(key=lambda x: getattr(x, key))

    def afficher_animal(self):
        for animal in self.animals:
            animal.afficher_info()

    def enregistrer_animal(self, filename="animals.txt"):
        with open(filename, "w") as f:
            for animal in self.animals:
                f.write(f"{animal.code}, {animal.nom_scientifique}, {animal.espece}, "
                        f"{animal.nombre_de_pieds}, {animal.pays_d_origine}\n")

    def load_json(self, filename="dev.json"):
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        for item in data:
            if item["espece"] == "Chien":
                new_animal = Chien(item["code"], item["nom_scientifique"], item["espece"], item["nombre_de_pieds"],
                                   item["pays_d_origine"])
            elif item["espece"] == "Chat":
                new_animal = Chat(item["code"], item["nom_scientifique"], item["espece"], item["nombre_de_pieds"],
                                  item["pays_d_origine"])
            elif item["espece"] == "Poulet":
                new_animal = Poulet(item["code"], item["nom_scientifique"], item["espece"], item["nombre_de_pieds"],
                                    item["pays_d_origine"])
            elif item["espece"] == "Vache":
                new_animal = Vache(item["code"], item["nom_scientifique"], item["espece"], item["nombre_de_pieds"],
                                   item["pays_d_origine"])
            else:
                continue
            self.ajouter_animal(new_animal)  # Use new_animal here


chien = Chien(1, "Canis lupus familiaris", "Chien", 4, "France")
chat = Chat(2, "Felis catus", "Chat", 4, "Egypt")
poulet = Poulet(3, "Gallus gallus domesticus", "Poulet", 2, "India")
vache = Vache(4, "Bos taurus", "Vache", 4, "Switzerland")

zoo = Zoo("Zoo de Tamesna", 1000)
zoo.ajouter_animal(chien)
zoo.ajouter_animal(chat)
zoo.ajouter_animal(poulet)
zoo.ajouter_animal(vache)

print("Animaux après ajout :")
zoo.afficher_animal()

zoo.supprimer_animal(2)
print("\nAnimaux après suppression du Chat :")
zoo.afficher_animal()

zoo.update_animal(1, nom_scientifique="Canis lupus familiaris mis à jour")
print("\nAnimaux après mise à jour du Chien :")
zoo.afficher_animal()

print("\nRecherche du Poulet :")
found_animals = zoo.chercher_animal("Poulet")
for animal in found_animals:
    animal.afficher_info()

print("\nNombre d'animaux avec le nom scientifique 'Bos taurus' :")
print(zoo.nombre_animal("Bos taurus"))

print("\nAnimaux après tri par code :")
zoo.tri_animal()
zoo.afficher_animal()

print("\nSauvegarde des animaux dans le fichier 'animals.txt'")
zoo.enregistrer_animal("animals.txt")

