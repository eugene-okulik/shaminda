secret_number = 7
while True:
    user_input_number = int(input('input number: '))
    if secret_number == user_input_number:
        print('your right!!')
        break
    else:
        print('please try again')

print('you win!')
