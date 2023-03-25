
def encrypt(text):
    Finaltext = ''
    for letter in text:
        ascii = ord(letter)
        ascii += 1
        Finaltext += chr(ascii)
    return Finaltext

def decrypt(text):
    print('The text to decrypt is: ' + text)
    Finaltext = ''
    for letter in text:
        ascii = ord(letter)
        ascii -= 1
        Finaltext += chr(ascii)
    return Finaltext


def encryptFile(filePath):
    file = open(filePath, 'r')
    text = file.read()
    file.close()
    encryptedText = encrypt(text)

    file = open(filePath, 'w')
    file.write(encryptedText)
    file.close()
    print('Information Encrypted Successfully')

def decryptFile(filePath):
    file = open(filePath, 'r')
    text = file.read()
    file.close()
    decryptedText = decrypt(text)

    file = open(filePath, 'w')
    file.write(decryptedText)
    file.close()
    print('Information Decrypted Successfully')

responseToEncrypt = input('Type letter "E" to encrypt, or letter "D" to decrypt')
filePath = input('Enter the file path')

if responseToEncrypt == 'E':
    encryptFile(filePath)
else:
    decryptFile(filePath)