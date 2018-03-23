# ntlm-hasher.py & hasher2.py
Script to hash a wordlist into the Windows NTLM format line by line and print it to stdout.

<del>Still having issues. I am able to add a word to the code and it will print out the correct hash but when running through the file the hashes are incorrect. I already stripped out the newline characters.</del>

All is working. Issue was the file format was in dos creating a '\r' I didn't account for. In VIM ":set ff=unix" fixed the issue. 

# hash3r.py
Tool that can create hashes of words in a file, line by line, from various algorithms and write them to a new file or print to the terminal. 

I'm aware that my proficiency is laughable no need to remind me. :)
