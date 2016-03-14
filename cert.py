from subprocess import Popen, PIPE
import array

# input file
#inputFile = open('wiki_wild_card.pem', 'r')
inputFile = open('certificates.pem', 'r')

# certificate tags
beginningTag = '-----BEGIN CERTIFICATE-----'
endingTag = '-----END CERTIFICATE-----'

# certificates
certificates = []

publicCert = ''

for line in inputFile:
	if (str.strip(line) == beginningTag):
		publicCert += beginningTag + '\n'
	elif (str.strip(line) == endingTag):
		publicCert += endingTag
		certificates.append(str(publicCert))
		publicCert = ''
	else:
		publicCert += line


for certficate in certificates:
	#tempCertFile = open('tempCertFile.pem', 'w')
	#tempCertFile.write(str(certficate))
	#tempCertFile.close()

	#tempCertFile = open('tempCertFile.pem', 'r')

	cmdCall = Popen(['openssl', 'x509', '-noout', '-text'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
	stdout, stderr = cmdCall.communicate(certficate)

	print stdout

	# tempCertFile.close()

	# print stdout
	# print stderr


# Print contents
# date = subprocess.check_output(['date'])

# Write to file
# derFile = file('wiki_wikd_card.cer', 'w')
# derFile.write(derContents)