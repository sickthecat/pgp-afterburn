import os
import string
import gnupg

def generate_password(length=16):
    """Generate a random password with the specified length."""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join([alphabet[ord(os.urandom(1)) % len(alphabet)] for i in range(length)])
    return password

def generate_keypair(name, email, passphrase, private_key_file='private.key', public_key_file='public.key'):
    """Generate an RSA PGP keypair with the specified name, email, and passphrase and save it to files."""
    gpg = gnupg.GPG()
    input_data = gpg.gen_key_input(
        key_type='RSA',
        key_length=4096,
        name_real=name,
        name_email=email,
        passphrase=passphrase
    )
    key = gpg.gen_key(input_data)
    private_key = gpg.export_keys(key.fingerprint, True, passphrase=passphrase)
    public_key = gpg.export_keys(key.fingerprint)
    with open(private_key_file, 'w') as f:
        f.write(private_key)
    with open(public_key_file, 'w') as f:
        f.write(public_key)
    return key

if __name__ == '__main__':
    password = generate_password()
    print('Generated Password:', password)

    name = input('Enter your name: ')
    email = input('Enter your email address: ')
    passphrase = input('Enter a passphrase for your PGP key: ')

    key = generate_keypair(name, email, passphrase)
    fingerprint = key.fingerprint
    print('Generated PGP key with fingerprint:', fingerprint)
    print('Private key saved to private.key')
    print('Public key saved to public.key')
