filename = 'encrypt_file'
message = input('Eneter you Message: ')
key = int (input('Enter the Key value: '))

def encrypt(fname,msg, key): 
    with open(fname,'w') as f:
        for ch in msg:
            f.write(chr(ord(ch) + key ))
       

def decrypt(fname, key):
    org_msg = ''
    with open(fname,'r') as f:
        msg = f.read()
        for ch in msg:
            org_msg += chr(ord(ch) - key )
        with open(f.name + '_decrypt', 'w') as fw:
            fw.write(org_msg)
    
    
    
encrypt(filename,message, key)
decrypt(filename, key)
# print(org_message)