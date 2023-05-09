import os
import gnupg
import getpass

def generate_keypair(name, email, passphrase, key_type='RSA', key_length=4096, subkey_type='RSA', subkey_length=4096):
    """Generate a PGP keypair with the specified parameters and save it to disk."""
    gpg = gnupg.GPG()
    input_data = gpg.gen_key_input(
        key_type=key_type,
        key_length=key_length,
        subkey_type=subkey_type,
        subkey_length=subkey_length,
        name_real=name,
        name_email=email,
        passphrase=passphrase,
    )
    key = gpg.gen_key(input_data)
    private_key = gpg.export_keys(key.fingerprint, True, passphrase=passphrase)
    public_key = gpg.export_keys(key.fingerprint)
    with open('private.key', 'w') as f:
        f.write(private_key)
    with open('public.key', 'w') as f:
        f.write(public_key)
    print('Generated PGP key with fingerprint:', key.fingerprint)
    print('Private key saved to private.key')
    print('Public key saved to public.key')

def get_password():
    """Prompt the user to enter a password."""
    password = getpass.getpass('Enter your password: ')
    return password.strip()

if __name__ == '__main__':
    name = input('Enter your name: ')
    email = input('Enter your email address: ')
    password = get_password()

    generate_keypair(name, email, password)
