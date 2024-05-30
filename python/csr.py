import os
import rich_click as click
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import ipaddress
from data import certificates
from subprocess import run


# TODO add password support for the private key
def generate_csr(private_key='work/key.pem', csr_file='work/csr.pem', template = certificates[0]):
    """Generate a private key and CSR for the SCEP server.
    Pass in the path and name for where you want to store the private key and CSR file.
    function returns the csr and key objects
    """
    # Generate our key
    key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=4096,)
    
    # Write our key to disk for safe keeping
    with open(private_key, "wb") as f:
        f.write(key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            # encryption_algorithm=serialization.BestAvailableEncryption(b""),
            encryption_algorithm=serialization.NoEncryption(),
        ))
    
    #process san entries and create a list of x509 objects
    san = []
    for item in template['san']:
        if item['type'] == 'DNS':
            san.append(x509.DNSName(item['value']))
        elif item['type'] == 'ipv4':
            san.append(x509.IPAddress(ipaddress.IPv4Address(item['value'])))  
    
    # Generate a CSR
    csr = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([
        # Provide various details about who we are.
        x509.NameAttribute(NameOID.COUNTRY_NAME, template['country']),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, template['state']),
        x509.NameAttribute(NameOID.LOCALITY_NAME, template['city']),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, template['org']),
        x509.NameAttribute(NameOID.COMMON_NAME, template['common_name']),
    ])).add_extension(
        x509.SubjectAlternativeName(san),
        critical=False,
    ).sign(key, hashes.SHA256())

    click.secho('\nCertificate information:', fg='white')
    click.secho(f"Country: {template['country']}")
    click.secho(f"State: {template['state']}")
    click.secho(f"City: {template['city']}")
    click.secho(f"Organization: {template['org']}")
    click.secho(f"Common Name: {template['common_name']}")
    click.secho(f"\nSubject Alternative Names:", fg="white")
    for item in template['san']:
        click.secho(f"Type: {item['type']}, Value: {item['value']}")
    click.secho(f"\n")

    # Write our CSR out to disk.
    with open(csr_file, "wb") as f:
        f.write(csr.public_bytes(serialization.Encoding.PEM))
        click.secho(f"Certificate Signing Request generated at {csr_file}", fg="green")
        click.secho(f"Private key is: {private_key}\n", fg="yellow")
    
    return csr, key




