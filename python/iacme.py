from subprocess import run

def enroll_acme(csr='work/csr.pem', dns='dns_cf'):
    """Run the ACME client (must be installed and configured first)
    Pass in the path to the CSR and the DNS provider you want to use.
    For supported dns providers and how to condigure them check out
    https://github.com/acmesh-official/acme.sh/wiki/dnsapi
    """

    res = run(['/usr/bin/bash', '~/.acme.sh/acme.sh', '--signcsr', '--csr', csr, '--dns', dns], capture_output=True, check=True)
    print(res.stdout)
    return