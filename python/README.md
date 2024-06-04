
***********************************************************************
!                                                                     !
!                       Disclaimer:                                   !
!     This is protoyping code - use at your own risk!                 !
!     Remember: a certificate is only as safe as the private key      !
!                                                                     !
***********************************************************************

# Setup
1. create an virtual environment<br>
        ex: ```python3 -m venv venv ```
2. load the virtual environment<br>
        ex: ```source venv/bin/activate```
3. (one-time) install dependencies<br>
        ex: ```pip install -r requirements.txt```
4. (one-time) install external dependencies<br>
        see the [External Dependencies](#external-dependenies) section of README
5. Optional: create environment shell script<br>
6. Optional: run environmnt shell script<br>

In this example I'm going to create a shell script called ise_env.sh
in my home folder with the follwing information:

```
export ISE_PAN="ise_hostname_or_ip"
export ISE_USER="api_username"
export ISE_PASSWORD="password"
```

You can load the varibles with the source command like this:
```source ~/ise_env.sh```

(~/ is a shortcut for home directory)

# Running the code
The main script in this package is ise-c.py.  you can pass in the ISE 
API gateway node and creds either through environment variables, or
interactively at the start of the program is they're not found

On startup ise-c does a liveness check, then looks for a command argument.
If none is specified, it will go into interactive mode using a simple menu system.
the commands are read from the main_commands dictionary loacated in data.py.  This
makes it easy to add and remove funcionality to the program.


# External Dependenies
External (non-python dependencies) for this project:
* acme.sh (https://github.com/acmesh-official/acme.sh) - needed for acme enrollment
* socat (ex: sudo apt install socat -y) - used by acme.sh
* Cloudflare API keys for the DNS challenge exported to  CF_Token and CF_Zone_ID environment variables<br>
        ```export CF_Token="<token>"```
        ```export CF_Zone_ID="<zone id>"```
* Active directory certificate services and an NDES server
* sscep (https://github.com/certnanny/sscep) - needed for scep enrollment
* A certificate provider. I used zerossl
In the demo I set up a zerossl.com account and initialized acme with the following:
acme.sh  --register-account  --server zerossl \
        --eab-kid  xxxxxxxxxxxxx \
        --eab-hmac-key  xxxxxxxxxxx


