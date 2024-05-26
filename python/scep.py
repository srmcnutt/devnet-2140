
from subprocess import run 

def enroll_scep():
    # Define the URL of the SCEP server
    scep_challenge_url = 'http://pki1.pod1.abl.ninja/certsrv/mscep_admin'
    scep_enroll_url = 'http://pki1.pod1.abl.ninja/certsrv/mscep/mscep.dll'

    # # Get the challenge password from the SCEP server
    # # use this once the pyscep library is patched
    # resp = requests.get(scep_challenge_url, auth=(scep_admin, scep_password))
    # htmldata = resp.content
    # parsedData = BeautifulSoup(htmldata, "html.parser")
    # tag=parsedData.find_all('b')
    # otp=tag[1].contents[0]
    # print(f"the one time password from the scep server is: {otp}")
    
    # Run the SCEP client
    res = run(['sscep', 'enroll', '-f', 'scep/sscep.conf'], capture_output=True, check=True)
    # print(res.stdout)
    return