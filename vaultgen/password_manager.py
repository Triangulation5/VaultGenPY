import getpass
from .storage import PasswordStorage
from .password_generator import generate_password

def main():
    print("Welcome to VaultGen!")
    master_password = getpass.getpass("Enter your master password: ")
    store = PasswordStorage(master_password)

    while True:
        print("\nOptions:")
        print("1. Add new password")
        print("2. Retrieve password")
        print("3. List accounts")
        print("4. Generate password")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            site = input("Site: ")
            username = input("Username: ")
            password = getpass.getpass("Password: ")
            store.add_password(site, username, password)
            print("Password added!")
        elif choice == "2":
            site = input("Site: ")
            creds = store.get_password(site)
            if creds:
                print(f"Username: {creds['username']}\nPassword: {creds['password']}")
            else:
                print("No entry found.")
        elif choice == "3":
            sites = store.list_sites()
            if sites:
                print("Stored accounts:")
                for site in sites:
                    print("-", site)
            else:
                print("No accounts stored yet.")
        elif choice == "4":
            try:
                min_length = int(input("Enter minimum password length: "))
            except ValueError:
                print("Invalid length.")
                continue
            has_number = input("Include numbers? (y/n): ").strip().lower() == "y"
            has_special = input("Include special characters? (y/n): ").strip().lower() == "y"
            pwd = generate_password(min_length, has_number, has_special)
            print("Generated password:", pwd)
            use_it = input("Use this password to create a new account entry? (y/n): ").strip().lower()
            if use_it == "y":
                site = input("Site: ")
                username = input("Username: ")
                store.add_password(site, username, pwd)
                print("Password added!")
        elif choice == "5":
            print("Bye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()