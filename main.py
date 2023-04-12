import random
import time
from adding_cats import list_of_cats, wright_cat

# list_of_cats = ['Мэри Шелли', 'Фламбуша', 'Петра', 'Родезия', 'Цукерка', 'Арракис', 'Комбат', 'Акапулько',
#                 'Конфуций', 'Така', 'Белёк']

mist = 0


def happy_cat():
    happy_cat_today = random.choice(list_of_cats)
    mes = f'\nСегодня лучшее угощение получает {happy_cat_today}\n'
    print(mes)


def choice_action():
    global mist

    feed_cat = input('Выберите действие:\n 1 - посмотреть список котов\n2 - записать нового кота\n3 - покормить кота -->   ')


    if feed_cat =='3':
        happy_cat()
        choice_action()

    elif feed_cat == '1':
        # print('Ах вы жадина!!!')
        print('Вот список котов:')
        for cat in list_of_cats:
            print(cat)
        choice_action()

        # finish_choice = input('Точно не хотите угостить кота?  ')
        # if finish_choice == 'Нет' or finish_choice == 'нет':
        #     choice_action()
        # else:
        #     print('До свидания')
    elif feed_cat == '2':
        wright_cat()
        choice_action()

    else:
        if mist != 2:
            print('Кажется, мы вас не понимаем. Напишите цифру 1, 2 или 3.')
            mist += 1
            choice_action()
        if mist == 2:
            print('Какой-то вы неадекватный')
            print('До свидания')
            time.sleep(1)
            mist = 0


choice_action()