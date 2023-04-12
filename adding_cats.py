import os
import pickle
import shutil
import sys

if os.path.isfile('save_cats') == True:

    with open('save_cats', 'rb') as old_file:
        list_of_cats = []
        old_list = pickle.load(old_file)
        for obj in old_list:
            list_of_cats.append(obj)


else:
    list_of_cats = []
    with open('save_cats', 'wb') as new_wr:
        pickle.dump(list_of_cats, new_wr)


def wright_cat():
    print('Вот список котов на данный момент')
    choice_wr_cat = input('Хотите записать нового кота? (Да/Нет) --> ')
    if choice_wr_cat == 'Да' or choice_wr_cat == 'да':
        new_cat = input('Имя нового кота --> ')
        print(new_cat)
    if choice_wr_cat == 'Нет' or choice_wr_cat == 'нет':
        print('Программа закрывается')


wright_cat()

