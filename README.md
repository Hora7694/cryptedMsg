# 🔐 Script de Cryptage / Décryptage

Ce script Python permet de **chiffrer** et **déchiffrer** des messages à l’aide d’une **clé personnelle**.  
Il utilise une méthode basée sur l’algorithme **XOR**, puis encode le résultat en **Base64** afin que le message soit lisible et facilement partageable.

---

## ⚙️ Fonctionnement

### 1. Choix du mode
Au lancement, le programme propose 3 options :

- `C` → **Chiffrer un message**  
- `D` → **Déchiffrer un message**  
- `Q` → **Quitter le programme**

---

### 2. Mode Chiffrement (`C`)
1. L’utilisateur saisit le message à chiffrer.  
2. Il choisit ensuite une clé de cryptage :
   - Soit une **nouvelle clé**, par exemple :
     ```
     crypteIt
     ```
   - Soit une **clé enregistrée** dans le fichier de mots de passe, en indiquant son numéro de ligne précédé d’un **espace** et **tiret**.  
     Exemple :
     ```
      -3
     ```
     (Cela utilisera la clé enregistrée à la 3ᵉ ligne du fichier.)

3. Le script applique l’algorithme **XOR** entre chaque caractère du message et la clé choisie.  
4. Le résultat est encodé en **Base64** et affiché, prêt à être transmis.

---

### 3. Mode Déchiffrement (`D`)
1. L’utilisateur colle le **message chiffré** (exemple) :
   ```
   Jx8zGBMSBxQ=
   ```

2. Il fournit ensuite la **clé de cryptage associée** :
   ```
   crypteIt
   ```

3. Alternativement, il peut coller le message suivi du numéro de ligne d’une clé enregistrée. Exemple :
   ```
   Jx8zGBMSBxQ= -3
   ```

→ Le script ira lire la clé stockée à la ligne correspondante du fichier `passwords.txt`.

4. Si la ligne indiquée est **vide**, le programme propose d’enregistrer une nouvelle clé.  
5. Le message est alors **déchiffré** grâce à l’algorithme XOR.

---

### 4. Gestion et stockage des mots de passe
- Les mots de passe sont enregistrés dans :
   ```
   C:\Users\VOTRE_UTILISATEUR\cryptedMsg\passwords.txt
   ```

- Chaque ligne correspond à une clé.  
- Jusqu’à **50 lignes** sont créées par défaut.  
- Le numéro utilisé (`-3`, `-5`, etc.) correspond à la **position de la clé** dans ce fichier.

---

### 5. Quitter le programme (`Q`)
À tout moment, tapez : `Q` pour fermer le programme.

---
