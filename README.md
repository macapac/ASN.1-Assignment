# ASN.1-Assignment


Web Security 2024 assignment, understanding and applying ASN.1 encoding principles to RSA private keys. Using OpenSSL and programming tools to decrypt Base64-encoded ciphertext using a non-standard RSA private key format.


Private key: "MIIBTwKBgQC4edQipK1/cAl05q2M5DLt/41IcG1yr1S72snlmoiGSTKeQFNsrp78
AJ2PYZJXz5aelUPebIV/9h9NSh/638W6dMvBRPTcmwvj7aQfUBNuiw/ItfrZwsNq
d+wKGyAsuQUfkxvPjOI0hBP3x0UPIaURnmxLcT8fFGx4nbwSSYVdjwIDAQABAoGA
BjLBt/BEjBWdm7nsduFr/KcrfhWY99OAS1eMlRReJfTrqHmM1AgB+4GhyaGDo0Os
UeO+BgkrayM/5f7pmCpQoGaGq1qplrT9dsAvPU3bJTwQWJXsn+s/eFuQeUD+v+uJ
eXIh9NgXZas/9fMyLri0xePwFbB0oJjKWGBZTaFcJpECQQDtt0RFahsT+bJAjmMU
0Gc+OdE7LyWpLUAjWFh7iQUdh5PQayBp7CNtKzISJAzRdf7imzFy2MumOsbvR6Vy
dfCT"



Ciphertext: "E9k1i26GAJkOqTAd7GZmqWD8nCyePYG7P+G8TeJI4OJGXDxKObKlS4qmso7NCK77nVclKpuu/pKC
kuGUpPEPZHHDBwOX0vUWXMfmH8WdgQnIRO1fXFzuA8r0pOHHOs0b9VwoYxYStmsayLzm+kiDMNnp
0s1HNXaT5YAjYqqIpNI="



//1: 
python dump.py --pem private_key.pem 


//2: 
python rsa_key_completion.py 


//3:
python finalize_rsa_key.py 


//4: 
openssl base64 -d -in encrypted_data.txt -out encrypted.bin


//5: 
openssl pkeyutl -decrypt -inkey complete_private_key.pem -in encrypted.bin -out decrypted.txt



// View Key Structure
openssl rsa -in complete_private_key.pem -text -noout


