# Wienersattack
Wiener's Attack on RSA This repository implements Wiener's attack—a cryptographic attack that exploits weak RSA keys with small private exponents (d). The code is written in Python with a Jupyter Notebook setup for testing and exploring RSA vulnerabilities.

# Wiener's Attack on RSA

## Introduction
Wiener's attack is a cryptographic attack that exploits weak **RSA keys** with **small private exponents (d)**. If *d* is too small, the security of RSA is compromised, allowing an attacker to recover the private key using **continued fractions**.

This repository contains:
- A **Jupyter Notebook** implementation of Wiener's Attack.
- Detailed **explanations** of how the attack works.
- A step-by-step **guide** to testing vulnerable RSA keys.

## Enhancements & Future Improvements
Automated weak RSA key generation for testing.
Web interface for interactive attack demonstrations.
Performance optimizations for handling larger RSA keys.

## Disclaimer
This project is intended solely for educational purposes to demonstrate cryptographic vulnerabilities.
Do not use this code for malicious, illegal, or unethical purposes.
The author takes no responsibility for misuse of this tool.
Always follow ethical hacking practices and obtain proper authorization.

## How Wiener's Attack Works
RSA encryption relies on the security of large prime factorization. However, when the **private exponent (d)** is too small, the fraction **e/n** (where *e* is the public exponent and *n* is the modulus) can be **well approximated** by its continued fraction expansion. This leads to a vulnerability where an attacker can recover *d*.

### Steps in the Attack:
1. Compute the **continued fraction expansion** of `e/n`.
2. Find **convergents** (best rational approximations).
3. Use the quadratic equation derived from `φ(n)` to recover **prime factors**.
4. If successful, retrieve **the private key d**.

## Installation & Setup
### **Install Dependencies**
Before running the attack, install **Jupyter Notebook** and required Python libraries:
```bash
pip install jupyter sympy

### Open Terminal or Command Prompt
Run the following command:
```bash
jupyter notebook
