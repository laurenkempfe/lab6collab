def encode(password):
    global epass
    epass = ''
    password = str(password)
    for i in range(len(password)):
        epass += str(int(password[i])+3)
    return int(epass)

if __name__ == '__main__':
    print('Menu\n-------------\n1. Encode\n2. Deocde \n3. Quit ')
    option = int(input('Please enter an option: '))
    if option == 1:
        encode(input('Please enter your password to encode:'))
        print('Your password has been encoded and stored!')


