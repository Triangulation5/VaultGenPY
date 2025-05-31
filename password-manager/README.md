# Python Password Manager

A simple and secure command-line password manager written in Python. Store, retrieve, and manage your passwords with encryption, all from your terminal.

## Features

- Securely store passwords for multiple sites and accounts
- All data is encrypted using a master password
- Easy-to-use command-line interface
- Quickly add, retrieve, and list your stored accounts

## Getting Started

### Requirements

- Python 3.7 or higher

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/password-manager.git
   cd password-manager
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
python password_manager.py
```

You will be prompted to set or enter your master password on first use.

## Project Structure

```
password-manager/
├── password_manager.py      # Main CLI logic
├── storage.py              # Encrypted storage management
├── crypto_utils.py         # Encryption/decryption helpers
├── requirements.txt        # Project dependencies
├── .gitignore              # Ignored files and folders
└── README.md               # This file
```

## Security Notice

- All passwords are encrypted locally using your master password.
- **Do not lose your master password!** There is no way to recover your vault without it.
- Be careful not to upload your encrypted vault or master password to any public repository.

## License

MIT License

---

**Enjoy your simple and secure password manager!**
