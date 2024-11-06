import tkinter as tk  # Importation du module tkinter pour créer des interfaces graphiques
from contact_gui import ContactGui  # Importation de la classe ContactGui depuis le fichier contact_gui.py

# Lancer l'interface graphique
root = tk.Tk()  # Création de la fenêtre principale
app = ContactGui(root)  # Création d'une instance de l'application ContactGui
root.mainloop()  # Lancement de la boucle principale de l'interface graphique