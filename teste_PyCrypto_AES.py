from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

chave = get_random_bytes(16)  # Gera uma chave de 128 bits
bloco = 16  # Tamanho do bloco AES

dados = 'Mensagem secreta'.encode('utf-8')  # Conversão para bytes
dados = pad(dados, bloco)  # Preenchimento para garantir que os dados correspondam ao tamanho do bloco

# Generate a random IV
iv = get_random_bytes(bloco)

# Create the cipher object for encryption
cipher_encrypt = AES.new(chave, AES.MODE_CBC, iv)
mensagem_cifrada = cipher_encrypt.encrypt(dados)

print('-----------------------------------------------------------------')
print(chave.hex())
print('-----------------------------------------------------------------')
print(iv.hex())  # Print the IV
print('-----------------------------------------------------------------')
print(mensagem_cifrada.hex())
print('-----------------------------------------------------------------')

# Create the cipher object for decryption using the same IV
cipher_decrypt = AES.new(chave, AES.MODE_CBC, iv)
dados_decifrados = cipher_decrypt.decrypt(mensagem_cifrada)
dados_decifrados = unpad(dados_decifrados, bloco)  # Remove o preenchimento

print(dados_decifrados.decode('utf-8'))  # Converte de volta para string
print('-----------------------------------------------------------------')
