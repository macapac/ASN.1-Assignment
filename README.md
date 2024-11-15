# ASN.1-Assignment

# What is Given in the Assignment
A Base64-Encoded Private Key

A Base64-Encoded Ciphertext, This is a message encrypted using RSA that you need to decrypt.


# Summary of Steps
Decode the private key from Base64 and extract its ASN.1 structure.
Reformat the key into a standard RSA PEM format.
Use the PEM key with OpenSSL to decrypt the ciphertext.
Display the decrypted plaintext.



openssl asn1parse -in decoded_key.der -inform DER


