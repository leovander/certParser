#!/usr/bin/python
from subprocess import Popen, PIPE

# input file
# need to add command line options
inputFile = open('certificates.pem', 'r')

# certificate tags
beginningTag = '-----BEGIN CERTIFICATE-----'
endingTag = '-----END CERTIFICATE-----'

# certificates
certificates = []

# new certificate in file
publicCert = ''

# read file line by line
for line in inputFile:
    # top of cert
    if (str.strip(line) == beginningTag):
        publicCert += beginningTag + '\n'
    # end of cert, append to certs array and clear contents if we find a new
    # cert
    elif (str.strip(line) == endingTag):
        publicCert += endingTag
        certificates.append(str(publicCert))
        publicCert = ''
    # hopefully just an encoded line
    else:
        publicCert += line

for certficate in certificates:
    # Currently printing everything, need to add more filters/options, and
    # identify chains
    cmdCall = Popen(
        ['openssl', 'x509', '-noout', '-text'],
        stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdout, stderr = cmdCall.communicate(certficate)

    print stdout
