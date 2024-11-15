import base64

# Decode the Base64 key
base64_key = """MIIBTwKBgQC/lu9OM9TQ4VhbtJMgm2RiAwe0XHENOqQLx5sCv83ab4mM/uUVKI7v
YDDjgb5LYoT7SB51bUqFRITdMxKheJRLTC5f3o+7XaZ+J+HFCBYU5a3LUDJiwsto
b1oFEOr2TKXe+/G3vfKxyVCcLqCK21hPo24GZMm5cOVg9sCrwA+CyQIDAQABAoGA
dCSao4y2OX4yIz2/ZyfsXaI6nHLhscRXyDBT3wHJV97/wrKOyxnQNHraiECRzH9H
4FDi7gq3/zv/U1zvsWU4d7H2l2oMb+68iIqtmkAgKLY95s4hwRDLrYCv+VhzTIUW
4BfjLZ23eK8Xwg1t+mSt+2MTlUByknBdmw/pRjmKVoECQQD+eD3EsN37iUsCSzY0
Nu59nHtB4K479vDYuSPs5c6I3Wb4MF8Eb7G1f3ZRrsSnBiygiGK8SZ2a4e9Fw5bg
1B3Z"""

# Decode Base64 into DER
der_key = base64.b64decode(base64_key)

with open("decoded_key.der", "wb") as f:
    f.write(der_key)
