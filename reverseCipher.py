#Reverse Cipher
#https://www.nostarch.com/crackingcodes/ (BSD License)

message = input('Enter message to be encrypted: ')
translated = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    #print('i is ', str(i),', message[i] is ',message[i],', translated is ',translated)
    i = i - 1

print(translated)