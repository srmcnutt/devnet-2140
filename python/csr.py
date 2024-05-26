import os
import rich_click as click
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import ipaddress
from subprocess import run

# TODO add password support for the private key
def generate_csr(private_key='work/key.pem', csr_file='work/csr.pem'):
    """Generate a private key and CSR for the SCEP server.
    Pass in the path and name for where you want to store the private key and CSR file."""
    # generate a key if we don't already have one
    if not os.path.exists(private_key):
        # Generate our key
        key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,)
        print(key)
        
        # Write our key to disk for safe keeping
        with open(private_key, "wb") as f:
            f.write(key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                # encryption_algorithm=serialization.BestAvailableEncryption(b""),
                encryption_algorithm=serialization.NoEncryption(),
            ))
    else:
        with open(private_key, 'r') as f:
            data = f.read()
        key = serialization.load_pem_private_key(data.encode(), password=None)  

    # Generate a CSR
    csr = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([
        # Provide various details about who we are.
        x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "North Carolina"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, "Charlotte"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Always Be Labbing"),
        x509.NameAttribute(NameOID.COMMON_NAME, "ise1.pod1.abl.ninja"),
    ])).add_extension(
        x509.SubjectAlternativeName([
            # Describe what sites we want this certificate for.
            x509.DNSName("ise1.pod1.abl.ninja"),
            x509.DNSName("ise1"),
            x509.DNSName("ise"),
            x509.IPAddress(ipaddress.IPv4Address('10.253.68.202')),
            x509.IPAddress(ipaddress.IPv4Address('10.253.68.203')),
        ]),
        critical=False,
    ).sign(key, hashes.SHA256())

    # Write our CSR out to disk.
    with open(csr_file, "wb") as f:
        f.write(csr.public_bytes(serialization.Encoding.PEM))
        click.secho(f"Certificate Signing Request generated at {csr_file}", fg="green")
        click.secho(f"Private key is: {private_key}", fg="yellow")

    return



