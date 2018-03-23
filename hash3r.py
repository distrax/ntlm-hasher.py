#!/usr/bin/env python3
import hashlib
#Comprehensive python tool to hash wordlists and phrases
#Function Section:
def ntlm(pw):
    h=hashlib.new('md4', pw.encode('utf-16le')).hexdigest()
    return(h)
def md5(pw):
    h=hashlib.md5(pw.encode('utf-8')).hexdigest()
    return(h)
def sha256(pw):
    h=hashlib.sha256(pw.encode()).hexdigest()
    return(h)
def sha512(pw):
    h=hashlib.sha512(pw.encode()).hexdigest()
    return(h)
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
    quit()
pfile=input('Enter filename: ')
try:
    pw=open(pfile)
except:
    print('File not found.')
    quit()
create=input('Would you like the hashed passwords to be saved to a new file? Y or n: ').lower()
if create[0] == 'y' or len(create)==0:
    x=str(algo[hash3r]).split(' ')
    output=open(pfile+x[1]+'hash.txt', "w")
    for p in pw:
        if len(p)>0:
            p=p.rstrip('\n')
            z=(algo[hash3r](p))
            output.write(z+'\n')
    output.close()
else:
    for line in pw:
        if len(line)>0:
            line=line.rstrip('\n')
            print(line)
            z=(algo[hash3r](line))
            print(z)
