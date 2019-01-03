# ceasar cypher
# https://nostarch.com/crackingcodes (BSD licensed)

import pyperclip

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
mode = input('Choose encrypt or decrypt: ') ##can be set to encrypt or decrypt
message = input('Enter the message to be translated: ') ##default to 'This is my secret message.'
translated = ''
key = int(input('Enter key: '))

for character in message:
    if character in SYMBOLS:
        charIndex = SYMBOLS.find(character)
        if mode == 'encrypt':
            translatedIndex = charIndex + key
        elif mode == 'decrypt':
            translatedIndex = charIndex - key
        elif mode != 'encrypt' and mode != 'decrypt':
            print('Error - check spelling')
            break
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)
        translated += SYMBOLS[translatedIndex]
    else:
        translated += character

print(translated)
pyperclip.copy(translated)
