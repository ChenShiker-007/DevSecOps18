pass = ''

print('Enter a password that contains at least 8 char and end with 16 and contains no spaces and also starts with _')
pass1 = input('enter a char for your password : ')
while loop:
    pass1 = input('type a password: ')
    if len(pass1) > 8 and pass1.islower() and pass1.isupper() and pass1.isdigit():
        print('password successful')
        break
    else:
        print('Password not valid, please retry')
