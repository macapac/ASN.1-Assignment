# ASN.1-Assignment

//1 

cd C:UsersasusASN.1-Assigment

//2 
python dump.py --pem private_key.pem 

//3 
python rsa_key_completion.py 

//4
python finalize_rsa_key.py 

//5 
openssl base64 -d -in encrypted_data.txt -out encrypted.bin

//6 
openssl pkeyutl -decrypt -inkey complete_private_key.pem -in encrypted.bin -out decrypted.txt


// View Key Structure
openssl rsa -in complete_private_key.pem -text -noout

