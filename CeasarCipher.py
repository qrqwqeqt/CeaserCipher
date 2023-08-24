import string

alphabet_lowercase = string.ascii_lowercase
alphabet_uppercase = string.ascii_uppercase
commands = ['1', '2', '3']


def foundIndex(letter):
    index = alphabet_lowercase.find(letter.lower())
    return index


def changeIndex(index, step):
    new_index = (index + step) % len(alphabet_lowercase)
    return new_index


def swapUpperLetter(letter, step):
    index = foundIndex(letter)
    new_index = changeIndex(index, step)
    return alphabet_uppercase[new_index]

def swapLowerLetter(letter, step):
    index = foundIndex(letter)
    new_index = changeIndex(index, step)
    return alphabet_lowercase[new_index]


#*If the step is negative, decryption is in progress
def encryptCeaser(text, step):
    encrypted_text = ""
    for letter in text:
        if letter.isupper():
            encrypted_text += swapUpperLetter(letter, step)
            
        elif letter.islower():
            encrypted_text += swapLowerLetter(letter, step)
        #*If the character is not a letter
        else: 
            encrypted_text += letter
    return encrypted_text
    


while True:
    action = input('1. Encrytp text \n2. Decipher the text\n3. Exit \n')
    if action in commands:
        if action == '3':
            break
        step = input('Enter Shift: ')
        if step.isdigit():
            text = input('Enter Message: ')
            if action == '1':
                print (encryptCeaser(text, int(step)))
            if action == '2':
                print (encryptCeaser(text, -(int(step))))
        else:
            print('Incorrect input')
        
        
            