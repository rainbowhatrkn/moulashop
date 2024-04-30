import os
import shutil

def replace_in_file(file_name, old_expression, new_expression):
    try:
        # Vérifier si le fichier existe
        if not os.path.exists(file_name):
            print(f"File '{file_name}' not found.")
            return

        # Lire le contenu du fichier
        with open(file_name, 'r') as file:
            file_content = file.read()

        # Créer une sauvegarde du fichier
        backup_file_name = f"{file_name}.bak"
        shutil.copyfile(file_name, backup_file_name)

        # Remplacer l'ancienne expression par la nouvelle
        new_content = file_content.replace(old_expression, new_expression)

        # Écrire le nouveau contenu dans le fichier
        with open(file_name, 'w') as file:
            file.write(new_content)

        print(f"Expression '{old_expression}' replaced with '{new_expression}' in '{file_name}' successfully.")
        print(f"Backup created: '{backup_file_name}'")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    file_name = input("Enter the file name: ")
    old_expression = input("Enter the expression to replace: ")
    new_expression = input("Enter the new expression: ")
    replace_in_file(file_name, old_expression, new_expression)

if __name__ == "__main__":
    main()