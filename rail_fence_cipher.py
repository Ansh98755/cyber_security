def rail_fence_encryption(pt, n):
    colNumber = len(pt)
    matrix = [[""]*colNumber for _ in range(n)]
    row, inc = 0, -1
    for i in range(0, len(pt)):
        matrix[row][i] = pt[i]
        if row == 0 or row == n-1:
            inc = -inc
        row += inc
    ct = ""
    for i in range(n):
        ct += "".join(ch for ch in matrix[i])
    return ct

def rail_cipher_decryption(ct, n):
    colSize = len(ct)
    matrix = [['\n'] * colSize for _ in range(n)]
    row, inc = 0, -1
    for i in range(colSize):
        matrix[row][i] = '*'
        if row == 0 or row == n - 1:
            inc = -inc
        row += inc
    index = 0
    for i in range(n):
        for j in range(colSize):
            if matrix[i][j] == '*' and index < len(ct):
                matrix[i][j] = ct[index]
                index += 1

    result = ""
    row, inc = 0, -1
    for i in range(colSize):
        result += matrix[row][i]
        if row == 0 or row == n - 1:
            inc = -inc
        row += inc
    return result

def rail_fence_cipher():
    message = input("Enter message to encrypt :")
    n = int(input("Enter Rail Fence Value :"))
    cipher_text = rail_fence_encryption(message, n)
    print("Cipher Text :" + cipher_text)
    plain_text = rail_cipher_decryption(cipher_text, n)
    print("Plain Text :" + plain_text)

rail_fence_cipher()