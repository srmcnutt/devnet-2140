import json
with open('local.crt', 'rt') as file:
    cert = file.read()
    newcert = json.dumps(cert)

with open('local1.crt', 'rt') as file:
    cert1 = file.read()
    