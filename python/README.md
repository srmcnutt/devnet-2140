External (non-python dependencies) for this project:
* acme.sh (https://github.com/acmesh-official/acme.sh) - needed for acme enrollment
* socat (ex: sudo apt install socat -y) - used by acme.sh
* sscep (https://github.com/certnanny/sscep) - needed for scep enrollment

In the demo I set up a zerossl.com account and innitialized acme with the following:
acme.sh  --register-account  --server zerossl \
        --eab-kid  xxxxxxxxxxxxx \
        --eab-hmac-key  xxxxxxxxxxx

