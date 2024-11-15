from pyasn1.type.univ import Sequence, Integer
from pyasn1.type.namedtype import NamedType, NamedTypes
from pyasn1.codec.ber import decoder
from pyasn1.codec.der import encoder
import base64
import subprocess

# Define the ASN.1 structure
class RSAPrivateKey(Sequence):
    componentType = NamedTypes(
        NamedType('modulus', Integer()),
        NamedType('publicExponent', Integer()),
        NamedType('privateExponent', Integer()),
        NamedType('prime1', Integer())
    )

def decode_key(base64_key):
    # Decode base64 to BER
    ber_key = base64.b64decode(base64_key)
    
    # Parse the BER key to extract ASN.1 structure
    key, _ = decoder.decode(ber_key, asn1Spec=RSAPrivateKey())
    return key

def encode_to_pem(key):
    # Encode the ASN.1 structure to DER
    der_encoded = encoder.encode(key)
    
    # Convert DER to PEM format
    pem = f"-----BEGIN RSA PRIVATE KEY-----\n{base64.encodebytes(der_encoded).decode().strip()}\n-----END RSA PRIVATE KEY-----"
    return pem

def save_pem_file(pem, filename="key.pem"):
    # Save PEM key to a file
    with open(filename, 'w') as pem_file:
        pem_file.write(pem)

def decrypt_ciphertext(ciphertext_base64, pem_file="key.pem", output_file="plaintext.txt"):
    # Decode the ciphertext from base64
    ciphertext_bin = base64.b64decode(ciphertext_base64)
    
    # Save the binary ciphertext to a temporary file
    with open("ciphertext.bin", 'wb') as f:
        f.write(ciphertext_bin)
    
    # Use OpenSSL to decrypt
    subprocess.run(
        [
            "openssl", "rsautl", "-decrypt",
            "-inkey", pem_file,
            "-in", "ciphertext.bin",
            "-out", output_file
        ],
        check=True
    )
    
    # Read and return the plaintext
    with open(output_file, 'r') as plaintext_file:
        return plaintext_file.read()

if __name__ == "__main__":
    # Input: Base64-encoded RSA private key and ciphertext
    base64_key = """<replace_with_base64_encoded_private_key>"""
    ciphertext_base64 = """<replace_with_base64_encoded_ciphertext>"""

    # Decode the RSA private key
    print("Decoding RSA private key...")
    private_key = decode_key(base64_key)

    # Convert to PEM format
    print("Converting key to PEM format...")
    pem_key = encode_to_pem(private_key)
    save_pem_file(pem_key)

    # Decrypt the ciphertext
    print("Decrypting ciphertext...")
    plaintext = decrypt_ciphertext(ciphertext_base64)
    print("Decrypted plaintext:")
    print(plaintext)
