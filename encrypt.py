from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes


def generate_private_key():
    """
    Generates a private key
    :return: The private key
    """
    return rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )


def generate_public_key(private_key):
    """
    Generate a public key linked to the given private key
    :param private_key: The original private key
    :return: The public key generated from the private key
    """
    return private_key.public_key()


def save_private_key(file, key):
    """
    Writes the given private key to the given file
    :param file: The destination file
    :param key: The private key to save
    :return: True if the key has been saved, False otherwise
    """
    try:
        with open(file, 'wb') as f:
            f.truncate()
            f.write(key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            ))
        return True
    except:
        return False


def save_public_key(file, key):
    """
    Writes the given public key to the given file
    :param file: The destination file
    :param key: The public key to save
    :return: True if the key has been saved, False otherwise
    """
    try:
        with open(file, 'wb') as f:
            f.truncate()
            f.write(key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ))
        return True
    except:
        return False


def read_private_key(file):
    """
    Read the private key stored in the given file
    :param file: The source file
    :return: The private key read from the file
    """
    with open(file, "rb") as key_file:
        return serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )


def read_public_key(file):
    """
    Read the public key stored in the given file
    :param file: The source file
    :return: The public key read from the file
    """
    with open(file, "rb") as key_file:
        return serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )


def encrypt(data, public_key):
    """
    Encrypts the given string using the given public key and returns the encrypted data
    :param data: The data to encrypt
    :param public_key: The public key to use
    :return: The encrypted data
    """
    return public_key.encrypt(
        data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )


def decrypt(encrypted, private_key):
    """
    Decrypts the given encrypted data using the given private key and returns the decrypted data
    :param encrypted: The encrypted data to decrypt
    :param private_key: The private key to use
    :return: The decrypted data
    """
    return private_key.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
