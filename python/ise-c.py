#!/usr/bin/env python
import os
import rich
import rich_click as click
from art import banner
from functions import\
    get_nodes,\
    print_cert_list,\
    export_cert_list,\
    get_ise_creds,\
    expiration_check

# get ISE environment variables
# prompt for any missing information
if not "ISE_PAN" in os.environ and "ISE_USER" not in os.environ\
    and "ISE_PASSWORD" not in os.environ:

    print("""
    Error: missing one or more environment variables.

    Please ensure you've defined the following:
    ISE_PAN
    ISE_USER
    ISE_PASSWORD
    """)
    exit(1)

ise_pan, ise_user, ise_password = get_ise_creds()

@click.command()
@click.option('-c', '--command',\
    type = click.Choice(['ls', 'export','cert-list', 'expire']))
@click.version_option(version="0.1")
def cli(command):
    """
    ls - list nodes in the ISE deployment.
    export - export all certificates to cert_backup folder using --password.
    expire - check for certificates expiring in --days.
    """
    if command == None:
        click.echo("No command selected. use --help for available commands.")
   
    # get list of nodes in the deployment
    if command == "ls":
        click.echo("Retrieving list of nodes in the deployment:\n")
        ise_nodes = get_nodes(ise_pan, ise_user, ise_password)
        for node in ise_nodes:
            print(f"Found node: {node['name']}")
            print(f"node id: {node['id']}\n")

    elif command == "export":
        # retrieve certificates and populate cert list under the node object
        ise_nodes = get_nodes(ise_pan, ise_user, ise_password)
        export_cert_list(ise_nodes)
    
    elif command == "cert-list":
        ise_nodes = get_nodes(ise_pan, ise_user, ise_password)
        print_cert_list(ise_nodes)
        
    elif command == "expire":
        click.echo("Checking for Expiring Certs")
        ise_nodes = get_nodes(ise_pan, ise_user, ise_password)
        expiration_check(ise_nodes)



if __name__ == "__main__":
    print(banner)
    cli()