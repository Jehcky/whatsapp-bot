from turtle import position
import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller, Button
from time import sleep
from whatsAppResponses import response

# Mouse click workaround for MAC OS
mouse = Controller()

class WhatsAppBot:
    # Starting Values
    def __init__(self, speed=.5, click_speed=.3):
        self.speed = speed
        self.click_speed = click_speed
        self.message = ''
        self.last_message = ''

    # Navigate to the green dots on main windows for new messages
    def nav_green_dot(self):
        try:
            position = pt.locateOnScreen('green_dot.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-100, 0, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exception (nav_green_dot): ', e)

    def nav_input_box(self):
        try:
            position = pt.locateOnScreen('paperclip.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(100, 10, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exception (nav_input_box): ', e)

    def nav_message(self):
        try:
            position = pt.locateOnScreen('paperclip.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(10, -50, duration=self.speed)
        except Exception as e:
            print('Exception (nav_message): ', e)

    def get_message(self):
        try:
            mouse.click(Button.left, 3)
            sleep(self.speed)
            mouse.click(Button.right, 1)
            sleep(self.speed)
            pt.moveRel(13, -180, duration=self.speed)
            mouse.click(Button.left, 1)
            sleep(1)

            self.message = pc.paste()
            print('Usuário: ', self.message)
        except Exception as e:
            print('Exception (get_message): ', e)

    def send_message(self):
        try:
            #Checar se a última mensagem enviada é a mesma
            if (self.message != self.last_message):
                bot_response = response(self.message)
                print('You say :', bot_response)
                pt.typewrite(bot_response, interval=.1)
                pt.typewrite('\n')
                self.last_message = self.message
            else:
                print('Não há novas mensagens.')
        except Exception as e:
            print('Exception (send_message): ', e)

whatsAppBot = WhatsAppBot(speed=.5, click_speed=.4)

sleep(5)

while True:
    whatsAppBot.nav_green_dot()
    whatsAppBot.nav_message()
    whatsAppBot.get_message()
    whatsAppBot.nav_input_box()
    whatsAppBot.send_message()
    sleep(10)