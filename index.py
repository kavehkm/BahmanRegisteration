# standard
import sys
import os
# internal
from src.settings import Settings
from src.robot import Robot

# create settings object
s = Settings()

# create robot
robot = Robot(s.browser, float(s.delay))


def print_menu():
    menu = [
        '[1] get to url',
        '[2] set the form up',
        '[x] exit'
    ]
    print('\n'.join(menu))


def dispatcher(answer):
    if answer == '1':
        robot.get(s.url)
    elif answer == '2':
        data = s.as_dict()
        robot.setupForm(data)
    elif answer == 'x':
        sys.exit()
    else:
        print('Hmm?')


def main():
    while True:
        # print menu to user
        print_menu()
        # get answer from user
        answer = input()
        # dispatch the answer
        dispatcher(answer)


if __name__ == '__main__':
    main()
