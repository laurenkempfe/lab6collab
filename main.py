# laurenkempfe
def encode(password):
    global epass
    epass = ''
    password = str(password)
    for i in range(len(password)):
        epass += str(int(password[i])+3) if int(password[i]) <= 6 else str(int(password[i]) - 7)
    return int(epass)


def decode(password):  # decodes password by subtracting 3 from each number in password (Made by: Zachary Bradley)
    epass = ''
    password = str(password)
    for digit in password:
        epass += str(int(digit) - 3) if int(digit) >= 3 else str(int(digit) + 7)
    return int(epass)


def main():
    while True:
        print('Menu\n-------------\n1. Encode\n2. Decode \n3. Quit \n')
        option = int(input('Please enter an option: '))
        if option == 1:
            encode(input('Please enter your password to encode:'))
            print('Your password has been encoded and stored!\n')
        if option == 2:
            print(f"The encoded password is {epass}, and the original password is {decode(epass)}.\n")
        if option == 3:
            quit()


if __name__ == '__main__':
    main()
