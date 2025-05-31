import getpass
from storage import PasswordStorage

def main():
    print("Welcome to Python Password Manager!")
    master_password = getpass.getpass("Enter your master password: ")
    store = PasswordStorage(master_password)

    while True:
        print("\nOptions:")
        print("1. Add new password")
        print("2. Retrieve password")
        print("3. List accounts")
        print("4. Exit")
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
            print("Bye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()