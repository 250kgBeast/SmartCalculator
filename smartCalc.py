calc_loop = True
while calc_loop:
    user_input = input()
    if user_input == '/exit':
        print('Bye!')
        calc_loop = False
    elif user_input == '/help':
        print('The program calculates the sum of numbers')
    elif user_input == '' or user_input == ' ':
        continue
    else:
        print(sum([int(i) for i in user_input.split(' ')]))

