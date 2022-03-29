import pywhatkit as py
import keyboard
import time


def send_message():
    try:
        py.sendwhatmsg("Receiver Number", 'Your Message', 23, 30)
        time.sleep(60)
        keyboard.press('enter')
        keyboard.press('enter')
        print('Message sent!')

    except():
        print("Error occurred while sending message!")


if __name__ == '__main__':
    send_message()
