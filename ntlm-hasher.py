#!/usr/bin/python2.7

import hashlib,binascii
def ntlm(pw):
    hash = hashlib.new('md4', pw.encode('utf-16le')).digest()
    print binascii.hexlify(hash)

pfile=raw_input('Enter filename: ')
ofile=open(pfile)
for line in ofile:
    if len(line)>0:
        line=line.rstrip('\n')
#        print(line)
        ntlm(line)
