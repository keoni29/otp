#!/usr/bin/env python3

import sys
import os
import argparse
from otp import *

def to_decimal(fooBytes):
	fooStr = ''
	for byte in fooBytes:
		fooStr += str(byte).zfill(5) + ' '

	return fooStr

def list2oct(ls):
	return ''.join(oct(d)[2:].zfill(3)+(' ') for d in ls)

parser = argparse.ArgumentParser()
parser.add_argument('-k', '--key', type=str, required=True)
parser.add_argument('-o', '--output', type=str)
parser.add_argument('-i', '--input', type=str)
parser.add_argument('-d', '--decrypt', action='store_true')
parser.add_argument('-e', '--encrypt', action='store_true')

args = parser.parse_args()

with open(args.input, 'rb') as infile:
	intext = infile.read()

	with open(args.key, 'rb') as keyfile:
		key = keyfile.read()

		with open(args.output, 'wb') as outfile:
			if args.encrypt:
				print("Encrypting file:",args.input, "with key:", args.key,"!")
				destroy_key(args.key)
				print("Writing ciphertext to file:", args.output, "!")
				outfile.write(encrypt(intext, key))
			elif args.decrypt:
				print("Decrypting file:",args.input, "with key:", args.key,"!")
				destroy_key(args.key)
				print("Writing plaintext to file:", args.output, "!")
				outfile.write(decrypt(intext, key))

try:
	infile.close()
except Exception as e:
	raise e
	#pass
