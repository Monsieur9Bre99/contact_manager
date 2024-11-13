# BRE SANCTIFIE - B3 DEVIA FullStack

# Diagramme de Classe : Système de Gestion de Restaurant

## Classes et Relations

### Classe Personne
- **Attributs :**
  - `id_personne` : INT
  - `nom` : VARCHAR(50)
  - `adresse` : VARCHAR(100)
  
- **Méthodes :**
  - Aucun spécifique (classe de base)

### Classe Employe (hérite de Personne)
- **Attributs :**
  - `id_employe` : INT (hérité de `Personne`)
  - `role` : ENUM ('Serveur', 'Cuisinier', 'Caissier')
  
- **Méthodes :**
  - `prendreCommande()` (Serveur)
  - `servirVin()` (Serveur)
  - `preparerPlat()` (Cuisinier)
  - `encaisser()` (Caissier)

### Classe Client (hérite de Personne)
- **Attributs :**
  - `id_client` : INT (hérité de `Personne`)
  
- **Méthodes :**
  - `commanderPlat()`
  - `payerFacture()`

### Classe Commande
- **Attributs :**
  - `id_commande` : INT
  - `date_commande` : DATETIME
  - `statut` : VARCHAR(20)
  
- **Méthodes :**
  - `ajouterPlat()`
  - `ajouterBoisson()`
  - `validerCommande()`

- **Associations :**
  - Un `Client` passe une ou plusieurs `Commandes`
  - Un `Serveur` prend une `Commande`

### Classe Plat
- **Attributs :**
  - `id_plat` : INT
  - `nom` : VARCHAR(50)
  - `prix` : DECIMAL(5,2)
  
- **Méthodes :**
  - Aucun spécifique

- **Associations :**
  - Une `Commande` contient un ou plusieurs `Plats` (composition)

### Classe Boisson
- **Attributs :**
  - `id_boisson` : INT
  - `nom` : VARCHAR(50)
  - `prix` : DECIMAL(5,2)
  
- **Méthodes :**
  - Aucun spécifique

- **Associations :**
  - Une `Commande` contient une ou plusieurs `Boissons` (composition)

### Classe Facture
- **Attributs :**
  - `id_facture` : INT
  - `date_facture` : DATETIME
  - `montant_total` : DECIMAL(7,2)
  
- **Méthodes :**
  - `calculerTotal()`
  - `imprimerFacture()`

- **Associations :**
  - Une `Facture` est liée à une `Commande`
  - Un `Client` reçoit une `Facture`

---

## Notes sur les Relations

- **Héritage :** La classe `Employe` et la classe `Client` héritent de la classe `Personne`.
- **Composition :** Une `Commande` est composée de plusieurs `Plats` et `Boissons`.
- **Navigabilité des Associations :**
  - Un `Serveur` peut accéder à une `Commande`.
  - Un `Client` peut accéder à sa `Commande` et à sa `Facture`.

---

## Illustration
![Capture d'écran](https://imgur.com/KyLV8fx.png)



Ce diagramme textuel représente les classes principales et leurs relations pour un système de gestion de restaurant. Il inclut les attributs, les méthodes clés et les associations entre les classes.
