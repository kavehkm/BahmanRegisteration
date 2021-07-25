# standard
import sys
import os
# internal
from src.settings import Settings
from src.robot import Robot

# create settings object
s = Settings()

# create robot
robot = Robot(s.browser, s.driver_path)


def print_menu():
    menu = [
        '[1] get to url',
        '[2] set the form up',
        '[x] exit'
    ]
    print('\n'.join(menu))


def main():
    while True:
        print_menu()
        answer = input()
        if answer == '1':
            robot.get(s.url)
        elif answer == '2':
            robot.setupForm({})
        elif answer == 'x':
            sys.exit()
        else:
            print('Hmm?')


if __name__ == '__main__':
    main()
