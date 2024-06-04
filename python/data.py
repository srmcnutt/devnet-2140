# This file contains the data for the program
main_commands = [
            {'command': 'exit', 'description': 'Quit program'},\
            {'command': 'ls', 'description': 'List Servers',},\
            {'command': 'cert-list', 'description': 'List Certificates'},\
            {'command': 'export', 'description': 'Back up certificates'},\
            {'command': 'expire', 'description': 'Show expiring certificates'},\
            {'command': 'external-csr', 'description': 'Create a certificate Signing Request'},\
            {'command': 'enroll-scep', 'description': 'Enroll a certificate with SCEP'},\
            {'command': 'enroll-acme', 'description': 'Enroll a certificate with ACME'},\
            {'command': 'import', 'description': 'Import a certificate into ISE with its private key'},\
            ]

certificates = [
            {'friendly name': 'test certificate 1', 'country': 'us', 'state': 'nc',\
             'city': 'Charlotte', 'org': 'Always Be Labbing, Inc.',\
             'common_name': 'ise99.pod1.abl.ninja',\
             'san': [
                {'type': 'DNS', 'value': 'ise99.pod1.abl.ninja'},
                {'type': 'DNS', 'value': '*.abl.ninja'},
                {'type': 'DNS', 'value': 'ise'},
                {'type': 'ipv4', 'value': '10.253.68.202'},
                {'type': 'ipv4', 'value': '10.253.68.203'}
                ]
            },

             {'friendly name': 'test certificate 2', 'country': 'us', 'state': 'nc',\
             'city': 'Charlotte', 'org': 'Always Be Labbing, Inc.',\
             'common_name': 'ise100.pod1.abl.ninja',\
             'san': [
                {'type': 'DNS', 'value': 'ise100.pod1.abl.ninja'},
                {'type': 'DNS', 'value': '*.abl.ninja'},
                ]
            }
        ]