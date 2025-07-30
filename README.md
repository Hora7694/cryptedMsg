# 🔐 Script de Cryptage/Décryptage

Ce script Python permet de **chiffrer** et **déchiffrer** des messages à l’aide d’une clé personnelle.  
Il utilise une méthode simple basée sur l’algorithme **XOR** et encode les messages chiffrés en **Base64** pour être lisibles et transmissibles facilement.  

## ⚙️ Fonctionnement

1. **Choix du mode**
   - Au démarrage, le programme propose trois options :  
     - `C` → Mode Cryptage  
     - `D` → Mode Décryptage  
     - `Q` → Quitter le programme  

2. **Mode Cryptage (C)**
   - L’utilisateur saisit un message et une clé de cryptage.
   - Le script applique l’algorithme XOR entre chaque caractère du message et la clé.
   - Le résultat est ensuite encodé en **Base64** pour être affiché sous une forme lisible et partageable.

3. **Mode Décryptage (D)**
   - L’utilisateur colle un message chiffré suivi d’un numéro de ligne, par ex. :
     ```
     Jx8zGBMSBxQ= -3
     ```
   - Le script lit le mot de passe stocké à la ligne correspondante du fichier `passwords.txt`.  
   - Si la ligne est vide, il propose d’en enregistrer un nouveau.
   - Le message est alors déchiffré avec ce mot de passe grâce à l’algorithme XOR.

4. **Stockage des mots de passe**
   - Les mots de passe sont enregistrés dans le fichier :
     ```
     C:\Users\VOTRE_UTILISATEUR\cryptedMsg\passwords.txt
     ```
   - Chaque ligne correspond à un mot de passe (jusqu’à 50 lignes créées par défaut).  
   - Le numéro de ligne indiqué (`-3`, `-5`, etc.) détermine quel mot de passe utiliser.

5. **Quitter (Q)**
   - Tapez `Q` pour fermer le programme à tout moment.

---
