from sympy import mod_inverse

def calculate_missing_rsa_components(n, e, d, p):
    # Calculate q
    q = n // p

    # Calculate d mod (p-1) and d mod (q-1)
    d_mod_p = d % (p - 1)
    d_mod_q = d % (q - 1)

    # Calculate (inverse of q) mod p
    coefficient = mod_inverse(q, p)

    return q, d_mod_p, d_mod_q, coefficient

def main():
    # Example modulus, private exponent, and prime1 from your decoded output
    n = 129543377622660260548144449617272364146326409820810052258259005291495741627137646329071560485751168077623925063321435760621025933051931679081253541714867621828251997547738832474176843887236095727701985630478122716315524310520484805990961614613892687979529486586379917318990122755945607631698811430511392939407
    e = 65537
    d = 4352572097061169930375422708656693865300681362061487939220384357719664053327999408221547769803684515722841799127726346108114486543179479642597621173629223994672205297428623761356018343824158473260073449918215907824061149083047765091030179849191638417065744829474323317231024263871675181211858423927877150353
    p = 12450191150313284813043384719119744487448892591927191624238458752965275403080500440454110929720642448244722789042403242871007074837314848634594404655820947

    q, d_mod_p, d_mod_q, coefficient = calculate_missing_rsa_components(n, e, d, p)
    print("Calculated q:", q)
    print("d mod (p-1):", d_mod_p)
    print("d mod (q-1):", d_mod_q)
    print("Coefficient (inverse of q mod p):", coefficient)

        # Verify the multiplicative inverse
    if (coefficient * q) % p == 1:
        print("Coefficient is correctly calculated.")
    else:
        print("Error in coefficient calculation.")

    

if __name__ == "__main__":
    main()