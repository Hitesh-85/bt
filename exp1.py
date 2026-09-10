# nano generate_keys.py

import subprocess

def generate_rsa_keys(private_key_file="private.pem", public_key_file="public.pem", bits=2048):
    subprocess.run([
        "openssl", "genpkey",
        "-algorithm", "RSA",
        "-pkeyopt", f"rsa_keygen_bits:{bits}",
        "-out", private_key_file
    ], check=True)

    subprocess.run([
        "openssl", "pkey",
        "-in", private_key_file,
        "-pubout",
        "-out", public_key_file
    ], check=True)

    with open(public_key_file, "r") as f:
        public_key_content = f.read()

    print("Keys generated successfully")
    print(f"Private key saved in: {private_key_file}")
    print(f"Public key saved in: {public_key_file}\n")
    print("Public Key (PEM format):\n")
    print(public_key_content)

generate_rsa_keys()

# python3 generate_keys.py

# ls -> cat public.pem -> cat private.pem
# openssl pkey -in private.pem -text -noout
# openssl pkey -pubout -in public.pem -text -noout
