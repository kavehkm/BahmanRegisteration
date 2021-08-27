# standard
import sys
# internal
from src import settings
from src import license
from src.robot import Robot


# create settings object
s = settings.Settings()


class Index(object):
    """Index"""
    def __init__(self):
        self.data = s.as_dict()
        self.robot = Robot(s.browser, settings.DRIVERS_PATH, float(s.delay))

    @staticmethod
    def print_menu():
        menu = [
            '[1] get to url',
            '[2] set the form up',
            '[x] exit'
        ]
        print('\n'.join(menu))

    def dispatcher(self, answer):
        if answer == '1':
            self.robot.get(s.url)
        elif answer == '2':
            self.robot.setupForm(self.data)
        elif answer == 'x':
            sys.exit()
        else:
            print('Hmm?')

    def loop(self):
        while True:
            # print menu to user
            self.print_menu()
            # get answer from user
            answer = input()
            # dispatch the answer
            self.dispatcher(answer)


def main():
    index = Index()
    index.loop()


if __name__ == '__main__':
    # check license before main
    if license.check(settings.LICENSE_PATH, settings.SETTINGS_FILE_PATH, settings.SALT):
        main()
    else:
        print('EEK, invalid license')
