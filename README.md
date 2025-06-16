# VaultGen

A simple and secure command-line password manager and password generator written in Python. Store, retrieve, and generate strong passwords with encryption, all from your terminal.

## Features

- Securely store passwords for multiple sites and accounts
- All data is encrypted using a master password
- Built-in strong password generator with customizable options
- Easy-to-use command-line interface
- Quickly add, retrieve, and list your stored accounts

## Getting Started

### Requirements

- Python 3.7 or higher

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/VaultGen.git
   cd VaultGen
   ```

2. **(Recommended) Create a virtual environment**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install required packages**

   ```bash
   pip install -r requirements.txt
   ```

### Usage

Run the password manager from the command line:

```bash
python -m vaultgen.password_manager
```

You will be prompted to set or enter your master password on first use.

## Project Structure

```
vaultgen/
├── __init__.py
├── password_manager.py
├── storage.py
├── crypto_utils.py
├── password_generator.py
requirements.txt
README.md
LICENSE
.gitignore
```

## Security Notice

- All passwords are encrypted locally using your master password.
- **Do not lose your master password!** There is no way to recover your vault without it.
- Be careful not to upload your encrypted vault or master password.

## License

MIT License

---

**Enjoy your secure and flexible password management with VaultGen!**
