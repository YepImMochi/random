#projects
#encryption program

import random
import string

chars = ' ' + string.ascii_letters + string.digits + string.punctuation
chars = list(chars)
keys = chars.copy()
random.shuffle(keys)

#print(f'chars : {chars}')
#print(f'keys : {keys}')

def encrypt():
    plain_text = input('Please enter the text to be encrypted: ')
    cipher_text = ''
    while True :
        for letter in plain_text:
            if letter in chars:
                index = chars.index(letter)
                cipher_text += keys[index]
            else:
                cipher_text += letter
        print(cipher_text)
        break

def main():
    print('******encryption******')
    while True:
        choice = input('Would you like to encrypt?: ')
        if choice == 'y':
            encrypt()
            break
        elif choice == 'n':
            print('I see , have a nice day!')
            break
        else :
            print('please enter a choice between y and n')

if __name__ == "__main__":
    main()