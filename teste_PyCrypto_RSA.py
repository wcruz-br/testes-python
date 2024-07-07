from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)
private_key = key
public_key = key.publickey()
private_key_export = key.exportKey()
public_key_export = key.publickey().exportKey()

# print('Private Key:')
# print(private_key)
# print
# print('Public Key:')
# print(public_key)

encryptor = PKCS1_OAEP.new(public_key)
encrypted = encryptor.encrypt(b'Mensagem secreta')

print('-----------------------------------------------------------------')
print(encrypted.hex())
print('-----------------------------------------------------------------')

decryptor = PKCS1_OAEP.new(private_key)
decrypted = decryptor.decrypt(encrypted)

print(decrypted.decode('utf-8'))
print('-----------------------------------------------------------------')