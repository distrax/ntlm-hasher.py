#!/usr/bin/env python3
import hashlib
#Comprehensive python tool to hash wordlists and phrases
#Function Section:
def ntlm(pw):
    return(hashlib.new('md4', pw.encode('utf-16le')).hexdigest())
def md5(pw):
    return(hashlib.md5(pw.encode('utf-8')).hexdigest())
def sha256(pw):
    return(hashlib.sha256(pw.encode()).hexdigest())
def sha512(pw):
    return(hashlib.sha512(pw.encode()).hexdigest())
#Dictionary of functions
algo={1:ntlm,
      2:md5,
      3:sha256,
      4:sha512,
      }
print('Welcome to hash3r.py. This tool can be used to hash either a passphrase or a wordlist line by line. The wordlist must be formatted to have a desired phrase to hash per line.')
#Hack to print options that will update with added functions
hash3r=0
while hash3r>len(algo) or hash3r<1:
    for key, value in algo.items():
        print(key, ('='), str(value).split(' ')[1])
    try:
        hash3r=input('Enter a number corresponding to desired algorithm: ')
        hash3r=int(hash3r)
    except:
        print('Not a valid hash choice.')
        hash3r=0
        continue
    if hash3r>len(algo) or hash3r<1:
        print('Not in range of choices.')
pfile=input('Enter a phrase to hash or the filename: ')
try:
    pw=open(pfile)
except:#Hash the input phrase if it's not a file
    print(algo[hash3r](pfile))
    quit()
create=input('Would you like the hashed passwords to be saved to a new file? Y or n: ').lower()
#Hash the file line by line and write it to a file
if create[0] == 'y' or len(create)==0:
    x=str(algo[hash3r]).split(' ')
    fn=input("Warning! Any file that has the same name will be replaced. Enter name for new file: ") or pfile+x[1]+'hash.txt'
    output=open(fn, "w")
    for line in pw:
        if len(line)>0:
            output.write(algo[hash3r](line.rstrip('\r\n'))+('\n'))
    output.close()
else:#Hash a file line by line and print it to stdout
    for line in pw:
        if len(line)>0:
            line=line.rstrip('\r\n')
            print(line)
            print(algo[hash3r](line))
