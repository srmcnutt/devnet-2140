#!/usr/bin/env python
import os
import rich_click as click
from art import banner
from data import main_commands
from functions import\
    get_nodes,\
    get_ise_creds,\
    commands

# get ISE environment variables
# prompt for any missing information
if "ISE_PAN"not in os.environ:
    os.environ["ISE_PAN"] = click.prompt("Enter ISE PAN hostname or IP address")
if "ISE_USER" not in os.environ:
    os.environ["ISE_USER"] = click.prompt("Enter ISE username")
if "ISE_PASSWORD" not in os.environ:
    os.environ["ISE_PASSWORD"] = click.prompt("Enter ISE password", hide_input=True)

ise_pan, ise_user, ise_password = get_ise_creds()

def testLogin():
    """
    Test the connection to the ISE deployment
    """
    click.secho("Testing connection to ISE deployment...", fg="blue")
    try:
        ise_nodes = get_nodes(ise_pan, ise_user, ise_password)
    except Exception as e:
        click.echo(f"Error: {e}")
        click.echo("Exiting")
        exit(1)
    click.secho("Connection successful! Lets do some ISE things", fg="green")

#TODO refactor cli to use main_commands from data.py
@click.command()
@click.option('-c', '--command',\
    type = click.Choice(['ls', 'export','cert-list', 'expire']))
@click.version_option(version="0.3")
def cli(command):
    """
    ls - list nodes in the ISE deployment.
    export - export all certificates to cert_backup folder using --password.
    expire - check for certificates expiring in --days.
    """

    # get list of nodes in the deployment
    # TODO refactor to read commands from database (currently data.py)
    if command == "ls" or "export" or "cert-list" or "expire":
        commands(command)
    
    # if no command line argument is passed, enter interactive mode
    if command == None:
        click.secho("No command line argument detected: entering interactive mode.\n", fg="yellow")
        menu()
    
# read menu options from data.py            
def menu():
    while True:
        i = 0
        for item in main_commands:
            click.secho(f"{i}. {item['description']}", fg="white")
            i += 1
        choice = click.prompt("\nEnter a number to select a command", type=int)
        if choice == 0:
            exit(0)
        if choice < len(main_commands):
            commands(main_commands[choice]['command'], menu=True)
        else:
            click.secho("Invalid selection", fg="red")
            menu()

if __name__ == "__main__":
    click.clear()
    print(banner)
    testLogin()
    cli()