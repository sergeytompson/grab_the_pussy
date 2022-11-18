# -*- coding: UTF-8  -*-

import requests
import threading
import datetime
import os


class Grasper:

    def __init__(self, url: str, path: str):
        self.path = path
        self.url = url

    def grab_the_pussy(self) -> None:
        pussy = requests.get(self.url)
        with open(self.path, 'wb') as p:
            p.write(pussy.content)


class PussyThread(threading.Thread):

    NORMAL_URL = 'https://cataas.com/cat'

    def __init__(self, path: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grasper = Grasper(self.NORMAL_URL, path)

    def run(self) -> None:
        self.grasper.grab_the_pussy()


class PussyTalk:

    BASE_PATH = 'cookie jar'

    def run(self):
        print('Добро пожаловать в Хвататель Киски. Здесь ты сможешь получить столько кисок, сколько сможешь унести')
        num = input('Сколько кисок ты хочешь получить? ')
        while not num.isdigit():
            num = input('Неверно, введи целое число: ')
        num = int(num)
        now_dir = datetime.datetime.now().strftime('%d %b %Y %H-%M-%S')
        pussy_dir = os.path.join(os.getcwd(), self.BASE_PATH, now_dir)
        os.makedirs(pussy_dir)
        for i in range(1, num + 1):
            pussy_path = pussy_dir + '/' + str(i)
            pussy_thread = PussyThread(pussy_path)
            pussy_thread.start()
        print(f'Все ваши киски скачаны. Вы можете увидеть их в папке {pussy_dir}')
