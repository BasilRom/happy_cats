import random
import time

list_of_cats = ['Мэри Шелли', 'Фламбуша', 'Петра', 'Родезия', 'Цукерка', 'Арракис', 'Комбат', 'Акапулько',
                'Конфуций', 'Така', 'Белёк']

mist = 0


def happy_cat():
    happy_cat_today = random.choice(list_of_cats)
    mes = f'Сегодня лучшее угощение получает {happy_cat_today}'
    print(mes)


def choice_action():
    global mist
    feed_cat = input('Хотите угостить кота? --> (да/нет)  ')


    if feed_cat == 'да' or feed_cat =='Да':
        happy_cat()
        choice_action()

    elif feed_cat == 'нет' or feed_cat =='Нет':
        print('Ах вы жадина!!!')
        choice_action()
    else:
        if mist != 2:
            print('Кажется, мы вас не понимаем. Отвечайте "Да" или "Нет".')
            mist += 1
            choice_action()
        if mist == 2:
            print('Какой-то вы неадекватный')
            print('До свидания')
            time.sleep(1)
            mist = 0


choice_action()