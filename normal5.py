from easy5 import mk_dir, rm_dir, list_dir
import os

def change_dir(folder):
    try:
        os.chdir(folder)
        print('Have changed the folder successfully')
    except FileNotFoundError:
        print('The move to this folder is imposseble. It does not exist!')


do = {
    1: change_dir,
     2: list_dir,
    3: rm_dir,
    4: mk_dir
}
while True:
    choice = input('Make your choice:\n'
                   '==================================\n'
                   '1. Go to the folder\n'
                   '2. Look through the content of current folder\n'
                   '3. Remove the folder\n'
                   '4.  Make a folder\n'
                   '5.  Exit\n\n')
    try:
        if len(choice.split()) == 2:      # Если нам передали более 1 аргумента
            choice, folder_name = choice.split()
            choice = int(choice)
            if do.get(choice):
                do[choice](folder_name)
        else:           # Если передали 1 аргумент
            choice = int(choice)
            if choice == 5:
                break
            elif do.get(choice):
                do[choice]()
    except ValueError:
        print('Mistake! You passed wrong data!\n')
    except TypeError:
        print('Mistake! You did not pass the name of the folder!')