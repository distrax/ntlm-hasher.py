#!/usr/bin/env python3
import hashlib
#Comprehensive python tool to hash wordlists and phrases
#Function Section:
def ntlm(pw):
    print(hashlib.new('md4', pw.encode('utf-16le')).hexdigest())
def md5(pw):
    print(hashlib.md5(pw.encode('utf-8')).hexdigest())
def sha256(pw):
    print(hashlib.sha256(pw.encode()).hexdigest())
def sha512(pw):
    print(hashlib.sha512(pw.encode()).hexdigest())
algo={1:ntlm,
      2:md5,
      3:sha256,
      4:sha512,
      }
dos=[('1', 'ntlm'), ('2', 'md5'), ('3', 'sha256'), ('4', 'sha512')]
#for k, v in algo.items():
#    print(v)
for a, b in dos:
    print(a, '=', b)
try:
    hash3r=input('Enter number corresponding to desired algorithm: ')
    hash3r=int(hash3r)
except:
    print('Not a valid hash choice.')
pfile=input('Enter filename: ')
try:
    pw=open(pfile)
except:
    print('File not found.')
for line in pw:
    if len(line)>0:
        line=line.rstrip('\n')
        print(line)
        algo[hash3r](line)
