import keyboard
import mouse
import time
import random
import pyautogui

import schedule
from PIL import Image

# from pynput import mouse
# import keyboard

# # Флаг для управления состоянием слушателя
# running = True


import cv2
import numpy as np


from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta

from pyrogram import Client

# # Ваши API ID и API Hash
# api_id = ''
# api_hash = ''
# phone_number = ''
# session_name = ''

# app = Client(session_name, api_id=api_id, api_hash=api_hash, phone_number=phone_number)


RED = "\033[91m"
RESET = "\033[0m"
GREEN = "\033[92m"
PURPLE = "\033[95m"



def find_piece(screenshot, rocket_template, accuracy, Import = True):
    if Import:
        screenshot_np = cv2.imread(screenshot, cv2.IMREAD_COLOR)
    
    else:
        screenshot_np = np.array(screenshot)
    
    rocket = cv2.imread(rocket_template, cv2.IMREAD_COLOR)


    result = cv2.matchTemplate(screenshot_np, rocket, cv2.TM_CCOEFF_NORMED)
    
    threshold = accuracy 
    loc = np.where(result >= threshold)
    rocket_coordinates = []
    
    for pt in zip(*loc[::-1]):
        rocket_coordinates.append([pt[0], pt[1]])
        print(rocket_template, [pt[0], pt[1]])
    
    return rocket_coordinates


def random_kor(start, end):
    return random.randint(start, end)
def random_sec(start, end):
    return random.uniform(start, end)

def move_and_click(x, y):
    pyautogui.moveTo(x, y)
    time.sleep(0.3)
    mouse.click(button='left')
def move_and_double_click(x, y):
    pyautogui.moveTo(x, y)
    time.sleep(0.3)
    mouse.click(button='left')
    time.sleep(0.1)
    mouse.click(button='left')
def move_to_coordinates(x, y):
    print(f'Перемещение к координатам: ({x}, {y})')
    time.sleep(0.5)
    pyautogui.moveTo(x, y)
    print(f'Курсор перемещен к: ({x}, {y})')
def move_and_fast_click(x, y):
    pyautogui.moveTo(x, y)
    mouse.click(button='left')
def move_and_right_click(x, y):
    pyautogui.moveTo(x, y)
    time.sleep(0.3)
    mouse.click(button='right')

def get_pixel_color(x, y):
    screenshot = pyautogui.screenshot() # Сделать скриншот всего экрана
    image = Image.frombytes('RGB', screenshot.size, screenshot.tobytes()) # Преобразовать скриншот в объект изображения
    
    r, g, b = image.getpixel((x, y))# Получить цвет пикселя
    return r, g, b



def on_telegr_to_Menu_BS():
    move_and_double_click(710, 890)  # телеграмм
    time.sleep(30)
    move_and_click(35, 105)  # Меню
    time.sleep(3)
def on_Chat_to_Tup_BS():
    move_and_click(305, 182)   # Чат бота
    time.sleep(2)
    move_and_click(570, 850)   # Play(х1)
    time.sleep(9)
    move_and_click(570, 850)   # Play(х2)
    time.sleep(9)
    move_and_click(790, 770)   # Прибыль
    time.sleep(2)
    # for i in range(1, 601):
    #     x = random_kor(1, 5)*10
    #     y = random_kor(2, 6)*10
    #     move_and_fast_click(787 + x, 660 + y)
    #     time.sleep(random_sec(0.001, 0.003))
    move_and_click(450, 100)   # Выход
    time.sleep(2)

    OKX_Bot()
    time.sleep(2)
    Dogs_Bot()

    move_and_click(35, 105)  # Меню
    time.sleep(2)


def on_Desktop_to_Menu_LD():
    move_and_double_click(806, 906)  # Эмулятор
    time.sleep(30)
    move_and_click(960, 350)  # Телеграмм
    time.sleep(5)
    move_and_click(200, 215)  # Меню
    time.sleep(3)
def on_Chat_to_Tup_LD():
    move_and_click(500, 320)   # Чат бота
    time.sleep(2)
    move_and_click(790, 1000)   # Play(х1)
    time.sleep(9)
    move_and_click(790, 1000)   # Play(х2)
    time.sleep(9)
    move_and_click(930, 900)   # Прибыль
    time.sleep(2)
    move_and_click(200, 215)   # Выход
    time.sleep(2)
    move_and_click(200, 215)  # Меню
    time.sleep(2)


first_start_bot = False


def OKX_Bot():
    global first_start_bot
    move_and_click(220, 270)  # OKX чат
    time.sleep(2)
    move_and_click(560, 850)  # Play
    time.sleep(2)
    move_and_click(560, 850)  # Play
    time.sleep(2)
    move_and_click(515, 810)  # Главное меню
    if first_start_bot == True:
        move_and_click(750, 810)  # Задания
        time.sleep(2)
        move_and_click(800, 645)  # Ежедневка
        time.sleep(2)
        move_and_click(770, 790)  # Собрать
        time.sleep(5)
        move_and_click(515, 810)  # Главное меню
        time.sleep(5)
    for i in range(0, 3):
        for j in range(1, 11):
            x = random_kor(2, 6)*5
            y = random_kor(1, 4)*2
            move_and_click(655 + x, 720 + y) # Long
            time.sleep(10)
        move_and_click(740, 820)  # Задания
        time.sleep(2)
        move_and_click(800, 400)  # Доп прокрутки
        time.sleep(2)
        move_and_click(750, 790)  # Потучить
        time.sleep(4)
        move_and_click(515, 810)  # Главное меню
        time.sleep(1)
    move_and_click(450, 105)  # Выход
    time.sleep(1)
    
def Dogs_Bot():
    global first_start_bot
    move_and_click(220, 350)  # Dogs чат
    time.sleep(2)
    move_and_click(560, 850)  # Play
    time.sleep(2)
    move_and_click(560, 850)  # Play
    time.sleep(2)
    # if first_start_bot == True:
    #     move_and_click(740, 820)  # Задания
    #     time.sleep(2)
    #     move_and_click(780, 640)  # Ежедневка
    #     time.sleep(2)
    #     move_and_click(750, 790)  # Собрать
    #     time.sleep(5)
    #     move_and_click(515, 810)  # Главное меню
    #     time.sleep(5)
    move_and_click(450, 105)  # Выход




def Start_Homiak_Bot():
    print("Бот начал заходить в эмуляторы")
    on_telegr_to_Menu_BS()

    move_and_click(130, 270)  # Хомяк 1
    time.sleep(2)
    on_Chat_to_Tup_BS()

    move_and_click(130, 330)  # Хомяк 2
    time.sleep(2)
    on_Chat_to_Tup_BS()

    move_and_click(130, 400)  # Хомяк 3
    time.sleep(2)
    on_Chat_to_Tup_BS()

    move_and_click(130, 270)  # Хомяк 1
    time.sleep(2)
    move_and_click(1470, 15)  # Закрыть эмулятор
    time.sleep(2)
    move_and_click(885, 500)  # Подтвердить
    time.sleep(2)
    move_and_click(860, 615)  # Подтвердить х2
    time.sleep(5)

    on_Desktop_to_Menu_LD()
    move_and_click(300, 430)  # Хомяк 1
    time.sleep(2)
    on_Chat_to_Tup_LD()

    move_and_click(300, 510)  # Хомяк 2
    time.sleep(2)
    on_Chat_to_Tup_LD()

    move_and_click(300, 580)  # Хомяк 3
    time.sleep(2)
    on_Chat_to_Tup_LD()

    move_and_click(300, 430)  # Хомяк 1
    time.sleep(2)
    move_and_click(1740, 115)  # Закрыть эмулятор
    time.sleep(2)
    print("Бот завершил работу на 2х эмуляторах")


#--------------------------------------------------------------

def Start_RP_GRAM():
    print("Бот начал фармить монетки в RP_GRAM")
    move_and_click(1230, 1170)  # телеграмм
    time.sleep(5)
    move_and_click(33, 62)  # Меню
    time.sleep(1)
    move_and_click(120, 270)  # Новый Хомяк
    time.sleep(1)
    move_and_click(318, 101)  # скрол проверка
    time.sleep(1)
    move_and_click(150, 350)  # чат
    time.sleep(1)
    move_and_click(470, 940)  # Заработать
    time.sleep(3)
    move_and_click(530, 670)  # Просмотр постов
    time.sleep(5)
    move_and_click(630, 290)  # Верхний
    time.sleep(5)
    for i in range(1, 11):
        move_and_click(555, 710)  # следующий
        time.sleep(10)

    count_iter = 0
    x, y = 670, 815
    time.sleep(2)
    color = get_pixel_color(x, y)
    print(f"Цвет пикселя на ({x}, {y}): RGB = {color}")
    while color == (14, 22, 33):
        count_iter+=1
        time.sleep(1+count_iter)
        move_and_click(470, 940)  # Заработать
        if count_iter >= 5:
            return 0

    move_and_click(525, 570)  # Подписаться на канал
    time.sleep(5)

    for i in range(1, 11):
        time.sleep(1)
        move_and_click(500, 250)  # Первый сверху подписаться
        time.sleep(3)
        move_and_click(318, 101)  # скрол проверка
        time.sleep(1)
        count_iter = 0
        x, y = 240, 350
        # print(f"Цвет пикселя на ({x}, {y}): RGB = {color}")
        while color == (43, 82, 120):
            count_iter+=1
            time.sleep(1+count_iter)
            move_and_click(500, 250)  # Первый сверху подписаться
            if count_iter >= 5:
                return 0
        move_and_click(630, 1110)  # Подписаться(в канале)
        time.sleep(1)
        move_and_click(630, 1110)  # Убрать звук
        time.sleep(1)
        move_and_click(350, 60)  # Стрелка назад
        time.sleep(1)

        move_and_click(750, 240)  # Проверить 1
        time.sleep(3)
        count_iter = 0
        x, y = 450, 800
        color = get_pixel_color(x, y)
        # print(f"Цвет пикселя на ({x}, {y}): RGB = {color}")
        while color != (24, 37, 51):
            color = get_pixel_color(x, y)
            count_iter+=1
            time.sleep(1+count_iter)
            if count_iter >= 5:
                return 0

        # Не менять координаты!!!
        move_and_right_click(604, 767)  # Правой кнопкой мыши по сообщению
        time.sleep(1)
        move_and_click(710, 957)  # Удалить
        time.sleep(1)
        move_and_click(604, 639)  # Подтвердить
        time.sleep(1)
        print("Подписался на:" + str(i) + " каналов")
    time.sleep(1)
    move_and_click(934, 12) # Закрыть
 

def Start_VZ_BOT():
    print("Бот начал фармить монетки в Взаим Боте")
    move_and_click(1230, 1170)  # телеграмм
    time.sleep(5)
    move_and_click(33, 62)  # Меню
    time.sleep(1)
    move_and_click(120, 270)  # Новый Хомяк
    
    move_and_click(313, 105)  # скрол проверка
    time.sleep(1)
    move_and_click(160, 440)  # чат
    time.sleep(2)
    for i in range(1, 11):
        move_and_click(500, 1000)  # Заработать
        time.sleep(3)
        x1, y1 = 370, 824
        color1 = get_pixel_color(x1, y1)
        print(f"Цвет пикселя на ({x1}, {y1}): RGB = {color1}")
        if color1 == (255, 231, 56):
            print(f"Задания закончились")
            break
        move_and_click(610, 820)  # Подписаться 
        time.sleep(3)
        move_and_click(630, 1110)  # Подписаться на канал
        time.sleep(2)
        move_and_click(630, 1110)  # Убрать звук
        time.sleep(2)
        move_and_click(350, 60)  # Стрелка назад
        time.sleep(2)
        move_and_click(620, 870)  # Проверить подписку
        time.sleep(2)
        print("Подписался на:" + str(i) + " каналов")
    time.sleep(1)
    move_and_click(934, 12) # Закрыть 



def Start_prog():

    try:
        move_and_click(1, 1)
        time.sleep(3)
        move_and_click(2, 1)

        now = datetime.now()
        print(f"{RED}Программа начала работать{RESET} {PURPLE}{now.strftime('%H:%M:%S')}{RESET}")

        # if not app.is_connected:
        #     app.start()
        # chat_id = '@Vanechka_101'
        # message = 'Бот заходит на аккаунты'
        # app.send_message(chat_id, message) 

        Start_Homiak_Bot()
        # Start_RP_GRAM()
        # Start_VZ_BOT()

        # # Условие для остановки слушателя
        # if not running:
        #     return False

    except Exception as e:
        print(f"Ошибка в Start_prog_1: {e}")



def main():
    
    scheduler = BackgroundScheduler()

    today = datetime.today()
    time_start_1 = today + timedelta(minutes=1)
    time_start_2 = today + timedelta(minutes=181)  
    time_start_3 = today + timedelta(minutes=361)  


    # Сон после первого выполнения
    sleep_begin_1 = time_start_1 + timedelta(minutes=1)
    sleep_end_1 = time_start_2 - timedelta(minutes=1)

    # Сон после Второго выполнения
    sleep_begin_2 = time_start_2 + timedelta(minutes=1)
    sleep_end_2 = time_start_3 - timedelta(minutes=1)
    
    # Время завершения программы
    time_end = time_start_3 + timedelta(minutes=1)


    if today > time_start_1:
        print("Заданное время уже прошло")
        return
    
    print(f"{RED}Первый запуск{RESET} {PURPLE}{time_start_1}{RESET}")
    print(f"{RED}Второй запуск{RESET} {PURPLE}{time_start_2}{RESET}")
    print(f"{RED}Третий запуск{RESET} {PURPLE}{time_start_3}{RESET}")


    

    scheduler.add_job(Start_prog, 'date', run_date=time_start_1)
    scheduler.add_job(Start_prog, 'date', run_date=time_start_2)
    scheduler.add_job(Start_prog, 'date', run_date=time_start_3)

    scheduler.start()




    
    while datetime.now() < time_end:
        now = datetime.now()
        if sleep_begin_1 <= datetime.now() <= sleep_end_1:
            time_sleep_begin = sleep_begin_1
            time_sleep_end = sleep_end_1
        else:
            time_sleep_begin = sleep_begin_2
            time_sleep_end = sleep_end_2   

        if time_sleep_begin <= now <= time_sleep_end:
            print(f"{GREEN}Время сна{RESET} {PURPLE}{now.strftime('%H:%M:%S')}{RESET}")
            time.sleep(3600)  
        else:
            print("Перерыв минута")
            time.sleep(59) 
    
    scheduler.shutdown()
    



# def stop_program():
#     global running
#     running = False
#     print("Программа завершена")
#     listener.stop()

# # Создаем слушатель событий мыши
# listener = mouse.Listener(on_click=main)
# listener.start()

# # Добавляем горячую клавишу для остановки программы
# keyboard.add_hotkey('esc', stop_program)

# # Ждем завершения работы слушателя
# listener.join()


if __name__ == '__main__':
    main()
    











