#!/usr/bin/python3

import hashlib
def ntlm(pw):
    print(hashlib.new('md4', pw.encode('utf-16le')).hexdigest())
    
pfile=input('Enter Filename: ')
ofile=open(pfile)
for line in ofile:
    if len(line)>0:
        line=line.rstrip('\n')
        print(line)
        ntlm(line)
