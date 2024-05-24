#!/usr/bin/env python
import os
import rich
import rich_click as click
from art import banner
from data import main_commands
from functions import\
    get_nodes,\
    print_cert_list,\
    export_cert_list,\
    get_ise_creds,\
    expiration_check,\
    commands,\
    clear

# get ISE environment variables
# prompt for any missing information
if "ISE_PAN"not in os.environ:
    os.environ["ISE_PAN"] = click.prompt("Enter ISE PAN hostname or IP address")
if "ISE_USER" not in os.environ:
    os.environ["ISE_USER"] = click.prompt("Enter ISE username")
if "ISE_PASSWORD" not in os.environ:
    os.environ["ISE_PASSWORD"] = click.prompt("Enter ISE password", hide_input=True)


  #  print("""
  #  Error: missing one or more environment variables.#

  ##  Please ensure you've defined the following:
  ##  ISE_PAN
  ##  ISE_USER
  ##  ISE_PASSWORD
  #  """)
  #  exit(1)

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
    click.secho("Connection successful! Lets do some ISE things\n", fg="green")

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

    # get list of nodes in the deployment
    if command == "ls" or "export" or "cert-list" or "expire":
        commands(command)
    
    # if no command line argument is passed, enter interactive mode
    if command == None:
        click.secho("No command line argument detected: entering interactive mode.\n", fg="yellow")
        menu()
    
            
def menu():
    while True:
        i = 0
        for item in main_commands:
            click.secho(f"{i}. {item['description']}", fg="white")
            i += 1
        choice = click.prompt("\nEnter a number to select a command", type=int)
        if choice == 0:
            exit(0)
        elif choice == 1:
            commands(main_commands[1]['command'], menu=True)
        elif choice == 2:
            commands(main_commands[2]['command'], menu=True)
        elif choice == 3:
            commands(main_commands[3]['command'], menu=True)
        elif choice == 4:
            commands(main_commands[4]['command'], menu=True)
        elif choice == 5:
            commands(main_commands[5]['command'], menu=True)
        elif choice == 6:
            commands(main_commands[6]['command'], menu=True)
        else:
            click.secho("Invalid selection", fg="red")
            menu()

if __name__ == "__main__":
    click.clear()
    print(banner)
    testLogin()
    cli()