import math

# Continued Fraction Expansion
def continued_fraction_expansion(numerator, denominator):
    cf = []
    while denominator:
        a = numerator // denominator
        cf.append(a)
        numerator, denominator = denominator, numerator - a * denominator
    return cf

# Compute Convergents from Continued Fraction
def convergents_from_cf(cf):
    convergents = []
    for i in range(len(cf)):
        if i == 0:
            convergents.append((cf[0], 1))
        elif i == 1:
            h = cf[0] * cf[1] + 1
            k = cf[1]
            convergents.append((h, k))
        else:
            h1, k1 = convergents[i - 1]
            h2, k2 = convergents[i - 2]
            h = cf[i] * h1 + h2
            k = cf[i] * k1 + k2
            convergents.append((h, k))
    return convergents

# Check if a Number is a Perfect Square
def is_perfect_square(n):
    if n < 0:
        return None
    root = int(math.isqrt(n))
    return root if root * root == n else None

# Wiener's Attack Implementation
def wiener_attack(e, n):
    print("\nStep 1: Continued Fraction Expansion of e/n:")
    cf = continued_fraction_expansion(e, n)
    print("Continued Fraction:", cf)

    print("\nStep 2: Computing Convergents:")
    convs = convergents_from_cf(cf)
    for i, (k, d) in enumerate(convs):
        print(f"Convergent {i}: k = {k}, d = {d}")

    print("\nStep 3: Testing convergents to find private key d...")
    for (k, d_candidate) in convs:
        if k == 0:
            continue

        if (e * d_candidate - 1) % k != 0:
            continue

        phi_candidate = (e * d_candidate - 1) // k
        a, b, c = 1, -(n - phi_candidate + 1), n

        discriminant = b * b - 4 * a * c
        sqrt_discriminant = is_perfect_square(discriminant)
        if sqrt_discriminant is None:
            continue

        x1 = (-b + sqrt_discriminant) // 2
        x2 = (-b - sqrt_discriminant) // 2

        if x1 * x2 == n:
            return d_candidate
    return None

# Main function with user input
def main():
    print("Wiener's Attack Demonstration")
    print("-----------------------------")
    try:
        e = int(input("Enter the RSA public exponent (e): "))
        n = int(input("Enter the RSA modulus (n): "))
    except ValueError:
        print("Invalid input. Please enter valid integer values for e and n.")
        return

    d = wiener_attack(e, n)

    if d is not None:
        print("\nSuccess! The private exponent d is:")
        print(d)
    else:
        print("\nWiener's attack failed. The private exponent is likely not small enough.")

if __name__ == "__main__":
    main()
