dict_with_variables = {}


def assign_variable(user_input):
    global dict_with_variables
    list_of_symbols = []
    for i in user_input:
        if i == '=':
            break
        else:
            list_of_symbols.append(i)
    for i in [str(x) for x in range(0, 9)]:
        if i not in list_of_symbols:
            exec(user_input, dict_with_variables)
        else:
            print('Invalid identifier')
            break


calc_loop = True
while calc_loop:
    user_input = input()
    if user_input == '/exit':
        print('Bye!')
        calc_loop = False
    elif user_input == '/help':
        print('The program calculates the sum of numbers')
    elif user_input.startswith('/'):
        print('Unknown command')
    elif user_input == '' or user_input == ' ':
        continue
    elif '=' in user_input:
        try:
            assign_variable(user_input)
        except NameError:
            print('Unknown variable')
        except SyntaxError:
            print('Invalid identifier')
    else:
        try:
            print(eval(user_input, dict_with_variables))
        except NameError:
            print('Unknown variable')
        except SyntaxError:
            print('Invalid expression')
