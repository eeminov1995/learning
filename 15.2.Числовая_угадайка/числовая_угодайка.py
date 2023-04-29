from random import randint

def rand_num(down_num: int, up_num: int) -> int:
    return randint(down_num, up_num + 1)

def play_game():
    flag = True
    while flag:
        name = input('Введите Ваше имя: ')
        attempt = 1
        
        x = input('Введите начало диапазона: ')
        if x.isdigit():
            pass
        else:
            flag_x = 'not ok'
            while flag_x:
                x = input('Введите целое число: ')
                if x.isdigit():
                    flag_x = 'ok'
                    break
 
        y = input('Введите конец диапазона: ')
        if y.isdigit():
            pass
        else:
            flag_y = 'not ok'
            while flag_y:
                y = input('Введите целое число: ')
                if y.isdigit():
                    flag_y = 'ok'
                    break

        tmp_num = rand_num(int(x), int(y))
        user_num = input(f'Введите число от {x} до {y}: ')

        while True:
            if not user_num.isdigit():
                user_num = input(f'А может быть все-таки введем целое число от {x} до {y}?: ')
                continue
            if int(user_num) < int(x) or int(user_num) > int(y):
                user_num = input(f'А может быть все-таки введем целое число от {x} до {y}?: ')
                continue
            if int(user_num) == tmp_num:
                vin_text = input(f'{name}, вы угадали с {attempt} попытки, поздравляем!\nХотете продолжить игру?\nОтветьте "да" или "нет": ')
                if vin_text == 'lf' or vin_text == 'LF' or vin_text == 'да' or vin_text == 'ДА':
                    break
                elif vin_text == 'ytn' or vin_text == 'YTN' or vin_text == 'нет' or vin_text == 'НЕТ':
                    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                    flag = False
                    break
            elif int(user_num) < tmp_num:
                user_num = input('Ваше число меньше загаданного, попробуйте еще разок: ')
                attempt += 1
            elif int(user_num) > tmp_num:
                user_num = input('Ваше число больше загаданного, попробуйте еще разок: ')
                attempt += 1
            else:
                user_num = input(f'А может быть все-таки введем целое число от {x} до {y}?: ')
                

print('Добро пожаловать в числовую угадайку!')

play_game()
