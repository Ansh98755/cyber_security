#rc4
# def ksa(key):
#     key_length=len(key)
#     S=list(range(256))
#     j=0
#     for i in range(256):
#         j=(j+S[i]+key[i%key_length])%256
#         S[i],S[j]=S[j],S[i]
#     return S
# def prga(S,n):
#     i=0
#     j=0
#     keyStream=[]
#     while True:
#         i=(i+1)%256
#         j=(S[i]+j)%256
#         S[i],S[j]=S[j],S[i]
#         k=(S[i]+S[j])%256
#         keyStream.append(k)
#     return keyStream
# def encrypt_rc4(keyStream,pt):
#     ct=""
#     for i in range(len(pt)):
#         ct+=(chr)(ord(pt[i])^keyStream[i])
#     return ct
# def decrypt_rc4(keyStream,ct):
#     pt=""
#     for i in range(len(ct)):
#         pt+=(chr)(ord(ct[i])^keyStream[i])
#     return pt
# def main():
#     key=input("Enter the key")
#     s_array=ksa(key)
#     pt=input("Enter the plaintext")
#     keyStream=prga(s_array,len(pt))
#     ct=encrypt_rc4(keyStream,pt)
#     print("Cipher text: ", ct)
#     pt=decrypt_rc4(keyStream,ct)
#     print("Plain Text: ", pt)

# main()


### RSA####
# def gcd(a,b):
#     while b:
#         a,b=b,a%b
#     return a

# def mod_inv(e,phi):
#     for d in range(3,phi):
#         if d*e%phi==1:
#             return d
#     return None
# def generate_keypair():
#     p=sympy.random(100,500)
#     q=sympy.random(100,500)
#     n=p*q
#     phi=(p-1)*(q-1)
#     e=random.randrange(2,phi)
#     while gcd(e,phi)!=1:
#         e=random.randrange(2,phi)
#     d=mod_inv(e,phi)
#     return ((e,n), (d,n))
# def rsa_encrypt(public_key,pt):
#     e,n=public_key
#     cipher=[pow(ord(char),e,n) for char in pt]
#     return cipher
# def rsa_decrypt(private_key,ct):
#     d,n=private_key
#     pt=[pow(ord(char),d,n) for char in ct]
#     return pt
# def main():
#     public_key,private_key=generate_keypair()
#     if choice==1:
#         print("Public key:", public_key)
#         print("Private key:", private_key)
#     elif choice==2:
#         msg=print("Enter the plain text: ")
#         ct=rsa_encrypt(msg,public_key)
#         print("Cipher text: ", ct)
#     elif choice==3:
#         cipher=input("Enter decrypted text")
#         cipher=list(map(int,cipher.split()))
#         pt=rsa_decrypt("Plain Text: ", pt)
#         print("Plain Text: ", pt)
#     elif choice==4:
#         print("Exiting...")
#     else:
#         print("Invalid Choice")
# main()

#### RSADS########
# def hash_function(pt):
#     pt=hashlib.sha256(pt.encode('Utf-8')).hexdigest()
#     return pt
# def gcd(a,b):
#     while b:
#         a,b=b,a%b
#     return a
# def checkPrime(n):
#     if n<2:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True
# def generate_keypair(p,q):
#     if not (checkPrime(p))and(checkPrime(q)):
#         raise ValueError("Invalid prime number")
#     n=p*q
#     phi=(p-1)*(q-1)
#     e=random.choice([i for i in range(2,phi) if gcd(i,phi)==1])

#     def mod_inv(e,phi):
#         for d in range(2,phi):
#             if d*e%phi==1:
#                 return d
#         return None
#     d=mod_inv(e,phi)
#     return ((e,n),(d,n))
# def generate_signature(msg,private_key):
#     d,n=private_key
#     digest=hash_function(msg)
#     digest_int=int(digest,16)%n
#     print("Sender's message digest:", digest_int)
#     signature=pow(digest_int,d,n)
#     print("Sender's signature: ", signature)
#     return signature
# def verify_signature(msg,signature,public_key):
#     e,n=public_key
#     digest=hash_function(msg)
#     digest_int=int(digest,16)%n
#     print("Reciever's message digest: ", digest_int)
#     decrypted_hash=pow(signature,e,n)
#     print("Reciever's unpacked hash:" ,decrypted_hash)

##### hill cipher #####
# def generate_key_matrix(key,size):
#     key_matrix=[]
#     k=0
#     for i in range(size):
#         row=ord([key[k+j] ]for j in range(size))
#         key_matrix.append(row)
#         k+=size
#     return key_matrix
# def mod_inv_matrix(key_matrix,mod):
#     det=int(round(np.linalg.det(key_matrix)))
#     try:
#         det_inv=pow(det,-1,mod)
#     except ValueError:
#         raise ValueError("Key matrix is not invertible with 26")
#     adjugate=np.round(det*np.linalg(key_matrix)).astype(int)%mod
#     return det_inv*adjugate
# def encrypt(pt, key ,size):
#     key_matrix=generate_key_matrix(key,size)
#     message_vector=np.array([[ord(char)%65]for char in pt])
#     cipher_matrix=np.dot(key_matrix,message_vector)%26
#     ciphertext=''.join(chr(int(num)+65)for num in cipher_matrix.flatten())
#     return ciphertext
# def decrypt(ct,key,size):
#     key_matrix=get_key_matrix(key,size)
#     key_matrix_inv=mod_inv_matrix(key_matrix,26)
#     cipher_vector=np.array([[ord(char)%65]for char in ct])
#     plain_matrix=np.dot(key_matrix_inv,cipher_vector)%26
#     plaintext=''.join(chr(int(num)+65) for num in plain_matrix.flatten())
#     return plaintext
# def main():
#     if choice==1:
#         pt=input("Enter the plain text").upper()
#         key=input("Enter the key (lenght must be a perfect square)").upper()
#         size=int(len(key)**0.5)
#         if(size*size!=len(key)):
#             print("Invalid key")
#         else:
#             ct=encrypt(pt,key,size)
#     elif choice==2:
#         ct=input("Enter the cipher text")
#         key=input("Enter the key (length must be perfect square)")
#         size=int(len(key)**0.5)
#         decrypt_text=decrypt(ct,key,size)
#     elif choice ==3:
#         print("Exiting////")
#     else:
#         print("Invalid choice!!!!!!!")
# main()

#### RSADS ####
# def hash_function(msg):
#     msg=hashlib.sha256(msg.encode('Utf-8')).hexdigest()
#     return msg
# def gcd(a,b):
#     while b:
#         a,b=b,a%b
#     return a
# def checkPrime(n):
#     if n<2:
#         return False
#     for i in range(n):
#         if n%i==0:
#             return False
#     return True


# def generate_keyPair(p,q):
#     if not checkPrime(p)and checkPrime(q):
#         raise ValueError ("p and q are not prime numbers")
#     n=p*q
#     phi=(p-1)*(q-1)
#     e=random.choice([i for i in range(2,phi)])
#     def mod_inv(e,phi):
#         for d in range(2,phi):
#             if (d*e)%phi==1:
#                 return d
#         return None
#     d=mod_inv(e,phi)
#     if d is None:
#         raise ValueError("d is none")
#     return ((e,n),(d,n))
# def generate_signature(private_key,msg):
#     d,n=private_key
#     digest=hash_function(msg)
#     digest_int=int(digest,16)%n
#     print("Sender's signature: ", digest_int)
#     signature=pow(digest_int,d,n)
#     return signature
# def verify_signature(public_key,msg,signature):
#     e,n=public_key
#     digest=hash_function(msg)
#     digest_int=int(digest,16)%n
#     print("Reciever's hash: ", digest_int)
#     decrypted_hash=pow(signature,e,n)
#     print("Reciver's signature: ", decrypted_hash)
#     return digest_int==decrypted_hash
# def main():
#     msg=input("Enter the plain text")
#     print("Enter two prime numbers")
#     p=int(input("Enter the value of p"))
#     q=int(input("Enter the value of q"))
#     public_key,private_key=generate_keyPair(p,q)
#     print("Public key: ", public_key)
#     print("Private key: ",private_key)
#     signature=generate_signature(private_key,msg)
#     if verify_signature(public_key,msg):
#         print("Verified Successfully")
#     else:
#         print("Signature not verified")

# main()

#### RSA##########
# def gcd(a,b):
#     while b:
#         a,b=b,a%b
#     return a
# def mod_inv(e,phi):
#     for d in range(3,phi):
#         if d*e==1:
#             return d
#     return None
# def generate_keyPair():
#     p=sympy.random(100,500)
#     q=sympy.random(100,500)
#     n=p*q
#     phi=(p-1)*(q-1)
#     e=random.randrange(2,phi)
#     while gcd(e,26)!=1:
#         e=random.randrange(2,phi)
#     d=mod_inv(e,phi)
#     return ((e,n), (d,n))
# def encrypt_rsa(public_key,pt):
#     e,n=public_key
#     cipher=[pow(ord(char),e,n) for char in pt]
#     return cipher
# def decrypt_rsa(private_key,ct):
#     d,n=private_key
#     pt=[pow(ord(char),d,n) for char in ct]
#     return ct
# def main():
#     private_key,public_key=generate_keyPair()
#     pt=input("Enter the plain text: ")
#     if choice==1:
#         print("Public key: ", public_key)
#         print("Private key: ", private_key)
#     elif choice==2:
#         ct=encrypt_rsa(public_key,pt)
#         print("ct:",ct)
#     elif choice==3:
#         cipher=input("Enter the space seperated values")
#         cipher=list(map(int,cipher.split()))
#         decrypted_message=decrypt_rsa(private_key,cipher)
#         print("Cipher text:", decrypted_message)
#     else:
#         print("Exiting the prog")

# main()

######## RC4####### 
# def ksa(key):
#     key_length=len(key)
#     S=list(range(256))
#     j=0
#     for i in range(256):
#         j=(j+S[i]+key[i%key_length])%256
#         S[i],S[j]=S[j],S[i]
#     return S
# def prga(S,n):
#     i=0
#     j=0
#     keyStream=[]
#     while True:
#         i=(i+1)%256
#         j=(j+S[i])%256
#         S[i],S[j]=S[j],S[i]
#         k=(S[i]+S[j])%256
#         keyStream.append(k)
#     return keyStream
# def rc4_encrypt(keyStream,pt):
#     ct=""
#     for i in range(len(pt)):
#         ct+=(chr)(ord(pt[i])^keyStream[i])
#     return ct
# def rc4_decrypt(keyStream,ct):
#     pt=""
#     for i in range(len(ct)):
#         pt+=(chr)(ord(ct[i])^keyStream[i])
#     return pt
# def main():
#     key=input("Enter the key: ")
#     s_array=ksa(key)
#     pt=input("Enter the plain text")
#     keyStream=prga(s_array,len(pt))
#     ct=rc4_encrypt(keyStream,pt)
#     pt=rc4_decrypt(keyStream,ct)


# main()

# def encrypt_row(pt,key):
#     pt=''.join(filter(str.isalpha(),pt.upper()))
#     key_length=len(key)
#     padding_length=(key_length-(len(pt)%key_length))%key_length
#     pt='X'*padding_length
#     rows=[pt[i:i + key_length]for i in range(0,len(pt),key_length)]
#     ct=''
#     for k in sorted((val,idx) for idx, val in enumerate(key)):
#         col_idx=k[1]
#         ct+=rows[col_idx]
#     return ct
# def decrypt_row(ct,key):
#     ct=''.join(filter(str.isalpha().upper()))
#     key_length=len(key)
#     num_rows=len(ct)
#     grid=[['' for _ in range(key_length) ] for _ in range(num_rows)]
#     sorted_key=sorted((val,idx)for idx,val in enumerate(key))
#     index=0
#     for _, col_idx in sorted_key:
#         for row in range(num_rows):
#             grid[row][col_idx]=ct[index]
#             index+=1
#     pt+=''.join(''.join for row in grid)
#     return pt

#### hill cipher### 
def generate_key_matrix(key,size):
    key_matrix=[]
    k=0
    for i in range (size):
        row=[ord(key [k+j])%65 for j in range(size)]
        k+=size
        key_matrix.append(row)
    return key_matrix
def mod_inv_matrix(key_matrix,mod):
    det=int(round(np.linalg.det(key_matrix)))
    try:
        det_inv=pow(det,-1,mod)
    except ValueError:
        raise ValueError("Not invertible")
    adjugate=np.round(det*np.linalg.inv(key_matrix).astype()%mod)
    return adjugate*det_inv
def hill_encrypt(pt,key,size):
    key_matrix=generate_key_matrix(key,size)
    message_vector=np.array((ord(char))%65 for char in pt)
    cipher_matrix=np.dot(key_matrix,message_vector)
    ct+=''.join(chr(int (num)+65)for num in cipher_matrix.flatten())
    return ct
def hill_decrypt(ct,key,size):
    key_matrix=generate_key_matrix(key,size)
    try:
        key_matrix_inv=mod_inv_matrix(key_matrix,size)
    except ValueError:
        raise 
    cipher_vector=np.array([[ord(char)%65]for char in ct])
    plain_matrix=np.dot(key_matrix_inv,cipher_vector)
    pt+=''.join(chr(int(num)+65)for num in cipher_matrix.flatten())
    return pt

