# importing the Fernet class from the fernet module of the cryptography package  
from cryptography.fernet import Fernet  
  
# generating the key  
theKey = Fernet.generate_key()  
  
# variable holding the value of key  
first = Fernet(theKey)  
  
# the plain text is converted into cipher text using the encrypt() method  
theToken = first.encrypt(b"This example demonstrates the implementation of the decode() method.")  
  
# printing the encrypted message  
print("Encrypted Message: ", theToken)  
  
# the cipher text is converted back into plain text using the decrpyt() method  
decryptMsg = first.decrypt(theToken)  
  
# printing the plain text using the decode() method  
# this method converts the message from byte to string  
print("\nDecrypted Message: ", decryptMsg.decode())  