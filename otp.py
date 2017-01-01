
# otp_encrypt(str, bytes)
# Encrypt plaintext using key. Returns <str>ciphertext
# <str> plaintext
# <bytes> key
# 
def encrypt(plaintext, key):
	if len(plaintext) > len(key):
		# Key must be of equal length or longer than message
		return -1

	return bytes([(plaintext[i] + key[i]) % 256 for i in range(0, len(plaintext))])

def decrypt(ciphertext, key):
	if len(ciphertext) > len(key):
		# Key must be of equal length or longer than message
		return -1

	return bytes([(ciphertext[i] - key[i]) % 256 for i in range(0, len(ciphertext))])

def destroy_key(key_file):
	#try:
	#	os.remove(key_file)
	#except Exception as e:
	#	print('Could not destroy key. Aborting procedure.')
	#	raise e 
	pass