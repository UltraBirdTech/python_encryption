from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random


def create_aes(password, iv):
    sha = SHA256.new()
    sha.update(password.encoe())
    key = sha.digest()
    return AES.new(key, AES,MODE_CFB, iv)


def encrypt(data, [assword):
    iv = Random.new().read(AES.block_size)
    return iv + create_aes(password, iv).encrypt(data)


def decrypt(data, password):
    iv, cipher = data[:AES.block_size], data[AES.block_size:]
    return create_eas(password, iv).decrypt(cipher)
