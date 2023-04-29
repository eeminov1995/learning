import random

answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен(а) в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

yes_answer = ['LF', 'ДА', 'lf', 'да', 'Lf', 'Да', 'lF', 'дА',]

no_answer = ['YTN', 'НЕТ', 'ytn', 'нет', 'Ytn', 'Нет', 'yTN', 'нЕТ', 'yTn', 'нЕт', 'ytN', 'неТ',]

print()
print('***' + 'Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос'.upper() + '***')
print()
name = input('Введите Ваше имя: ')
print()
print(f'Привет, {name}!')

game = True

while game:
    print()
    question = input(f'{name}, задай свой вопрос: ')
    if question != '':
        print()
        print(f'~~~{random.choice(answers).upper()}~~~')
    else:
        continue

    print()
    the_answer_to_yes_or_no = input(f'{name}, хочешь задать ещё один вопрос? "да" или "нет": ')

    check = 'on'

    while check == 'on':
        if the_answer_to_yes_or_no in yes_answer:
            check = 'off'
        elif the_answer_to_yes_or_no in no_answer:
            print()
            print('Возвращайся если возникнут вопросы!')
            check = 'off'
            game = False
        else:
            print()
            the_answer_to_yes_or_no = input('Введите "да" или "нет": ')
            check = 'on'
            continue

   

    



        

