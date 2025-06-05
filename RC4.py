def keyScheduling(key):
    s = list(range(256))  
    key_array = [ord(key[i % len(key)]) for i in range(256)] 
    j = 0

    for i in range(256):
        j = (j + s[i] + key_array[i]) % 256
        s[i], s[j] = s[j], s[i]  

    return s 

def pseudo_random_generation_algorithm(s, n):
    i = j = 0
    keyStream = []

    for _ in range(n): 
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i] 
        t = (s[i] + s[j]) % 256
        keyStream.append(s[t]) 

    return keyStream

def rc4_encryption(key_stream, pt):
    ct = ""
    for i in range(len(pt)):
        ct += (chr)(ord(pt[i]) ^ key_stream[i])
    return ct

def rc4_decryption(key_stream, ct):
    pt = ""
    for i in range(len(ct)):
        pt += (chr)(ord(ct[i]) ^ key_stream[i])
    return pt

def main():
    key = input("Enter Key (only text):")
    s_array = keyScheduling(key)
    pt = input("Enter Plain Text :")
    key_stream = pseudo_random_generation_algorithm(s_array, len(pt))
    ct = rc4_encryption(key_stream, pt)
    print("Cipher Text :", ct)
    pt = rc4_decryption(key_stream, ct)
    print("Plain Text :", pt)

main()