import base64
import os
import re  # pour vérifier la fin de chaîne avec regex

# Définir le chemin du dossier
USER_FOLDER = os.path.expanduser(r"~\\cryptedMsg")
PASSWORD_FILE = os.path.join(USER_FOLDER, "passwords.txt")

def init_password_file():
    """Créer le dossier et le fichier s'ils n'existent pas."""
    if not os.path.exists(USER_FOLDER):
        os.makedirs(USER_FOLDER)
        print(f"\033[93mDossier créé : {USER_FOLDER}\033[0m")
    if not os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "w", encoding="utf-8") as f:
            f.write("\n" * 50)  # 50 lignes vides
        print(f"\033[93mFichier créé : {PASSWORD_FILE}\033[0m")

def read_password(line_number: int) -> str:
    """Lire un mot de passe à une ligne donnée."""
    with open(PASSWORD_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return lines[line_number - 1].strip() if 0 < line_number <= len(lines) else ""

def write_password(line_number: int, password: str):
    """Écrire un mot de passe à une ligne donnée."""
    with open(PASSWORD_FILE, "r+", encoding="utf-8") as f:
        lines = f.readlines()
        while len(lines) < line_number:
            lines.append("\n")
        if lines[line_number - 1].strip() == "":
            lines[line_number - 1] = password + "\n"
            f.seek(0)
            f.writelines(lines)
            print(f"\033[93mNouveau mot de passe enregistré à la ligne {line_number}.\033[0m")
        else:
            print("\033[91mErreur : ligne déjà occupée !\033[0m")

def xor_cipher(message: str, key: str) -> bytes:
    return bytes([ord(c) ^ ord(key[i % len(key)]) for i, c in enumerate(message)])

def programStart():
    return input("\nCryptage (C) | Decryptage (D) | Quitter (Q) ? ")

# Init fichier/dossier
init_password_file()

# Flag pour saluer uniquement la première fois
first_run = True

while True:
    if first_run:
        print("\033[96mBonjour 👋\033[0m")
        first_run = False

    userInputChoice = programStart()
    while userInputChoice not in ["C", "c", "D", "d", "Q", "q"]:
        print("\033[91mErreur entrée incorrecte !\033[0m")
        userInputChoice = programStart()

    if userInputChoice in ["Q", "q"]:
        print("\033[93mProgramme quitté.\033[0m")
        break

    if userInputChoice in ["C", "c"]:
        print("\033[93mMode cryptage choisi\033[0m\n")
        message = input("Entrez le message à chiffrer : ")
        key_input = input("Entrez la clé de cryptage (ou ' -numéro' pour utiliser un mot de passe enregistré) : ")

        # Vérification avec regex si format " -nombre"
        if re.fullmatch(r" -\d+", key_input):
            line_number = int(key_input.strip()[1:])  # enlève l'espace et le tiret
            password = read_password(line_number)
            if password == "":
                print(f"\033[93mAucun mot de passe trouvé à la ligne {line_number}.\033[0m")
                new_pass = input("Entrez un mot de passe pour cette ligne : ")
                write_password(line_number, new_pass)
                password = new_pass
        else:
            password = key_input

        message_crypte = xor_cipher(message, password)
        message_crypte_b64 = base64.b64encode(message_crypte).decode()

        print(f"\n\033[92mMessage crypté : {message_crypte_b64}\033[0m")

    elif userInputChoice in ["D", "d"]:
        print("\033[93mMode décryptage choisi\033[0m\n")
        message_full = input("Entrez le message à déchiffrer (format : msg -numéro ou msg) : ")

        # Vérifier si fin correspond à " -nombre"
        match = re.search(r" -(\d+)$", message_full)
        if match:
            message_b64 = message_full[:match.start()]
            line_number = int(match.group(1))
            password = read_password(line_number)
            if password == "":
                print(f"\033[93mAucun mot de passe trouvé à la ligne {line_number}.\033[0m\n")
                new_pass = input("Entrez un mot de passe pour cette ligne : ")
                write_password(line_number, new_pass)
                password = new_pass
        else:
            # Si pas de -numéro, demander une clé
            message_b64 = message_full
            password = input("Aucune référence de mot de passe trouvée. Entrez une clé de décryptage : ")

        try:
            message_bytes = base64.b64decode(message_b64)
            message_decrypte = ''.join(
                chr(b ^ ord(password[i % len(password)])) for i, b in enumerate(message_bytes)
            )
            print(f"\n\033[92mMessage décrypté : {message_decrypte}\033[0m")
        except Exception as e:
            print(f"\033[91mErreur de décryptage : {e}\033[0m")
