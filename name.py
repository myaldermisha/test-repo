
while True:
    get_name = input('Введите ваше имя: ')
    print('Привет, ' + get_name)

    with open('GET_NAME.txt', 'a') as f:
        f.write(get_name + '\n')

