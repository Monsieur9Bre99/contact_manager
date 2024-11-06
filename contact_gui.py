import tkinter as tk
from tkinter import messagebox, simpledialog
import webbrowser
import contact_manager
import requests
from PIL import Image, ImageTk
import io

class ContactGui(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Gestion des contacts')
        self.master.geometry('600x600')
        self.master.configure(bg="#BDE3F0")
        self.master.resizable(False, False)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Canvas pour le fond d'écran
        self.canvas = tk.Canvas(self, width=600, height=600)
        self.canvas.pack(fill="both", expand=True)
        try:
            # Télécharger l'image de fond depuis une URL
            image_url = "https://themarketive.com/wp-content/uploads/2017/04/contact-background-1.jpg"  # URL de l'image
            # image_url = "./images/background.png"  # URL de l'image
            response = requests.get(image_url)
            response.raise_for_status()  # Vérifie si la requête est réussie

            # Charger l'image
            image_data = response.content
            image = Image.open(io.BytesIO(image_data))
            self.background_image = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, anchor="nw", image=self.background_image)
            
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors du téléchargement de l'image : {e}")
            messagebox.showerror("Erreur", "Impossible de télécharger l'image de fond.")
            self.canvas.config(bg="white")
        except (IOError, Image.UnidentifiedImageError) as e:
            print(f"Erreur lors de l'ouverture de l'image : {e}")
            messagebox.showerror("Erreur", "Le fichier téléchargé n'est pas une image valide.")
            self.canvas.config(bg="white")

        # Titre du projet
        self.title_label = tk.Label(self.canvas, text="Gestion des contacts", font=("Helvetica", 16), bg="white")
        self.title_label.pack(pady=10)

        # Barre de recherche
        self.search_entry = tk.Entry(self.canvas, width=30)
        self.search_entry.pack(pady=5)
        self.search_button = tk.Button(self.canvas, text='Rechercher un contact', command=self.search_contact)
        self.search_button.pack(pady=5)

        # Champs de saisie pour le nom et le téléphone
        self.name_label = tk.Label(self.canvas, text="Nom:", bg="white")
        self.name_label.pack(pady=5)
        self.entry_name = tk.Entry(self.canvas, width=30)
        self.entry_name.pack(pady=5)

        self.phone_label = tk.Label(self.canvas, text="Téléphone:", bg="white")
        self.phone_label.pack(pady=5)
        self.entry_phone = tk.Entry(self.canvas, width=30)
        self.entry_phone.pack(pady=5)

        # Bouton pour ajouter un contact
        self.add_button = tk.Button(self.canvas, text='Ajouter un contact', command=self.add_contact)
        self.add_button.pack(pady=5)

        # Boutons pour modifier et supprimer un contact
        self.update_button = tk.Button(self.canvas, text='Modifier un contact', command=self.update_contact)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(self.canvas, text='Supprimer un contact', command=self.delete_contact)
        self.delete_button.pack(pady=5)

        # Bouton pour lister les contacts
        self.list_button = tk.Button(self.canvas, text='Mes contacts', command=self.list_contacts)
        self.list_button.pack(pady=5)

        # Liste des contacts
        self.listbox = tk.Listbox(self.canvas, width=50)
        self.listbox.pack(pady=10)

        # Footer avec des liens vers les réseaux sociaux
        self.footer_frame = tk.Frame(self.canvas, bg="white")
        self.footer_frame.pack(side="bottom", fill="x", pady=10)

        self.github_button = tk.Button(self.footer_frame, text="GitHub", command=lambda: self.open_link("https://github.com/Monsieur9Bre99/"))
        self.github_button.pack(side="left", padx=40)

        self.codepen_button = tk.Button(self.footer_frame, text="CodePen", command=lambda: self.open_link("https://codepen.io/Monsieur9Bre99/"))
        self.codepen_button.pack(side="left", padx=10)

        self.linkedin_button = tk.Button(self.footer_frame, text="LinkedIn", command=lambda: self.open_link("https://linkedin.com/in/Monsieur9Bre99/"))
        self.linkedin_button.pack(side="right", padx=40)

    def open_link(self, url):
        webbrowser.open_new(url)

    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        if contact_manager.validate_contact(name, phone):
            contact_manager.add_contact(name, phone)
            self.list_contacts()
            self.entry_name.delete(0, tk.END)
            self.entry_phone.delete(0, tk.END)
            messagebox.showinfo('Success', f"Le contact '{name}' a été ajouté avec succès")
        else:
            messagebox.showerror('Error', 'Veuillez entrer un nom et un numéro de téléphone valides')

    def search_contact(self):
        name = self.search_entry.get()
        if name:
            contact = contact_manager.search_contact(name)
            if contact:
                messagebox.showinfo('Contact trouvé', f"Nom: {contact['name']}\nTéléphone: {contact['phone']}")
            else:
                messagebox.showerror('Erreur', 'Contact non trouvé')
        else:
            messagebox.showerror('Erreur', 'Veuillez entrer un nom pour la recherche')

    def update_contact(self):
        name = simpledialog.askstring('Modifier un contact', 'Nom:')
        if name:
            contact = contact_manager.search_contact(name)
            if contact:
                phone = simpledialog.askstring('Modifier un contact', 'Nouveau téléphone:')
                if contact_manager.validate_contact(name, phone):
                    contact_manager.update_contact(name, phone)
                    self.list_contacts()
                    messagebox.showinfo('Success', f"Le contact '{name}' a été mis à jour avec succès")
                else:
                    messagebox.showerror('Erreur', 'Veuillez entrer un nom et un numéro de téléphone valides')
            else:
                messagebox.showerror('Erreur', 'Contact non trouvé')
    def delete_contact(self):
        name = simpledialog.askstring('Supprimer un contact', 'Nom:')
        if name:
            contact_manager.delete_contact(name)
            self.list_contacts()
            messagebox.showinfo('Success', f"Le contact '{name}' a été supprimé avec succès")

    def list_contacts(self):
        self.listbox.delete(0, tk.END)
        contacts = contact_manager.load_contacts()
        for contact in contacts:
            self.listbox.insert(tk.END, f"{contact['name']}: {contact['phone']}")
