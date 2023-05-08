# pgp-afterburn
Python 3 script that generates a random password and a PGP keypair with the RSA algorithm and a bit size of 4096.





---

# PGP Keypair and Password Generator

This is a Python script that generates a random password and a PGP keypair with the RSA algorithm and a bit size of 4096.

The `generate_password()` function generates a random password with a length of 16 characters, using a combination of uppercase and lowercase letters, digits, and punctuation marks.

The `generate_keypair()` function generates a PGP keypair with the specified name, email, and passphrase, using the RSA algorithm with a bit size of 4096. The private and public keys are exported and saved to files in the current directory.

To use the script, simply run it in a Python environment, and follow the prompts to enter your name, email address, and a passphrase for the PGP key. The script will generate a random password and a PGP keypair, print the fingerprint of the keypair to the console, and save the private and public keys to files.

This script requires the `gnupg` package to be installed. You can install it using `pip` and in some cases `apt`:

```
pip3 install gnupg
sudo apt install gnupg
```
