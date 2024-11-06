import json
import os

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    # Charge les contacts depuis le fichier contacts.json
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, 'r') as f:
        return json.load(f)

def save_contacts(contacts):
    # Sauvegarde les contacts dans le fichier contacts.json
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)

def add_contact(name, phone):
    # Ajoute un contact après validation
    if validate_contact(name, phone):
        contacts = load_contacts()
        contacts.append({'name': name, 'phone': phone})
        save_contacts(contacts)
    else:
        raise ValueError("Nom ou téléphone invalide")

def search_contact(name):
    # Recherche un contact par son nom
    contacts = load_contacts()
    contacts_dict = {contact['name']: contact for contact in contacts}
    return contacts_dict.get(name)

def update_contact(name, phone):
    # Met à jour le numéro de téléphone d'un contact après validation
    if validate_contact(name, phone):
        contacts = load_contacts()
        for contact in contacts:
            if contact['name'] == name:
                contact['phone'] = phone
                break
        save_contacts(contacts)
    else:
        raise ValueError("Nom ou téléphone invalide")

def delete_contact(name):
    # Supprime un contact par son nom
    contacts = load_contacts()
    contacts = [contact for contact in contacts if contact['name'] != name]
    save_contacts(contacts)

def list_contacts():
    # Liste tous les contacts
    contacts = load_contacts()
    for contact in contacts:
        print(f"{contact['name']}: {contact['phone']}")

def validate_contact(name, phone):
    # Valide le nom et le téléphone du contact
    if not name or not phone:
        return False
    if not phone.isdigit() or len(phone) < 4:  # Accepte les numéros de téléphone de 4 chiffres ou plus
        return False
    return True