#https://www.nostarch.com/crackingcodes/ (BSD License)

import pyperclip

def main():
    myMessage = input('Message to encrypt: ')
    myKey = input('Key: ')
    ciphertext = encryptMessage(myKey, myMessage)
    print(ciphertext + '|') #in case there are blank spaces at the end of the ciphertext
    pyperclip.copy(ciphertext)

def encryptMessage(key,message):
    ciphertext = [''] * int(key)
    for column in range(int(key)):
        currentIndex = column
        while currentIndex < len(message):
            ciphertext[column] += message[currentIndex]
            currentIndex += int(key)
    return ''.join(ciphertext)

if __name__ == '__main__':
    main()
