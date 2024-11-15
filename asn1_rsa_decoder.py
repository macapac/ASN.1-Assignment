from pyasn1.type.univ import Sequence, Integer
from pyasn1.type.namedtype import NamedType, NamedTypes, OptionalNamedType
from pyasn1.codec.ber import decoder
from pyasn1.codec.der import encoder
import base64
import subprocess

# Define the ASN.1 structure

class RSAPrivateKey(Sequence):
    componentType = NamedTypes(
        NamedType('modulus', Integer()),               # n
        NamedType('publicExponent', Integer()),        # e
        NamedType('privateExponent', Integer()),       # d
        OptionalNamedType('prime1', Integer()),        # p
        OptionalNamedType('prime2', Integer()),        # q
        OptionalNamedType('exponent1', Integer()),     # d mod (p-1)
        OptionalNamedType('exponent2', Integer()),     # d mod (q-1)
        OptionalNamedType('coefficient', Integer())    # q^-1 mod p
    )


def decode_key(base64_key):
    ber_key = base64.b64decode(base64_key)
    key, _ = decoder.decode(ber_key, asn1Spec=RSAPrivateKey())
    print(key.prettyPrint())  # Debugging output
    return key

def encode_to_pem(key):
    der_encoded = encoder.encode(key)  # ASN.1 to DER
    pem = (
        "-----BEGIN RSA PRIVATE KEY-----\n"
        + base64.encodebytes(der_encoded).decode().strip()
        + "\n-----END RSA PRIVATE KEY-----"
    )
    return pem


def save_pem_file(pem, filename="key.pem"):
    # Save PEM key to a file
    with open(filename, 'w') as pem_file:
        pem_file.write(pem)

def decrypt_ciphertext(ciphertext_base64, pem_file="key.pem", output_file="plaintext.txt"):
    ciphertext_bin = base64.b64decode(ciphertext_base64)
    
    with open("ciphertext.bin", 'wb') as f:
        f.write(ciphertext_bin)
    
    subprocess.run(
        [
            "openssl", "rsautl", "-decrypt",
            "-inkey", pem_file,
            "-in", "ciphertext.bin",
            "-out", output_file
        ],
        check=True
    )
    
    with open(output_file, 'r') as plaintext_file:
        return plaintext_file.read()

if __name__ == "__main__":
    # Input: Base64-encoded RSA private key and ciphertext
    base64_key = """MIIBTwKBgQC/lu9OM9TQ4VhbtJMgm2RiAwe0XHENOqQLx5sCv83ab4mM/uUVKI7v
YDDjgb5LYoT7SB51bUqFRITdMxKheJRLTC5f3o+7XaZ+J+HFCBYU5a3LUDJiwsto
b1oFEOr2TKXe+/G3vfKxyVCcLqCK21hPo24GZMm5cOVg9sCrwA+CyQIDAQABAoGA
dCSao4y2OX4yIz2/ZyfsXaI6nHLhscRXyDBT3wHJV97/wrKOyxnQNHraiECRzH9H
4FDi7gq3/zv/U1zvsWU4d7H2l2oMb+68iIqtmkAgKLY95s4hwRDLrYCv+VhzTIUW
4BfjLZ23eK8Xwg1t+mSt+2MTlUByknBdmw/pRjmKVoECQQD+eD3EsN37iUsCSzY0
Nu59nHtB4K479vDYuSPs5c6I3Wb4MF8Eb7G1f3ZRrsSnBiygiGK8SZ2a4e9Fw5bg
1B3Z"""
    ciphertext_base64 = """ScWRo782jdGfgRjBRfuwwbLQhsJznYXJqhVCzn7SNbWXl5MccngVWOWu8Rwd6WRALUe+LcFt47Ly
p1CO6H1rXwRcfCPB9iZfTB1x1Ddx4bKEFUqZIUIdGa25fEYx8Qeuz1zX34BpCqzHvDqqVC1kIfn5
GuRgphYOq3suVR4ejCQ="""

    # Decode the RSA private key
    private_key = decode_key(base64_key)
    print(private_key.prettyPrint())


    # Convert to PEM format
    pem_key = encode_to_pem(private_key)
    save_pem_file(pem_key)


    # Decrypt the ciphertext
    print("Decrypting ciphertext...")
    plaintext = decrypt_ciphertext(ciphertext_base64)
    print("Decrypted plaintext:")
    print(plaintext)
