import os
import keyboard
import time
import threading
from colorama import Fore

choices = 0

def kybord():
    global choices

    while True:
        if keyboard.is_pressed("down"):
            choices += 1
            while keyboard.is_pressed("down"):
                pass

        if keyboard.is_pressed("up"):
            choices -= 1
            while keyboard.is_pressed("up"):
                pass

def choice(one, to, three):
    last_choice = -1

    while True:
        if choices != last_choice:
            os.system("cls")

            if choices == 0:
                print(f"{Fore.BLUE}{one}")
                print(f"{Fore.WHITE}{to}")
                print(f"{Fore.WHITE}{three}")

            elif choices == 1:
                print(f"{Fore.WHITE}{one}")
                print(f"{Fore.BLUE}{to}")
                print(f"{Fore.WHITE}{three}")

            elif choices == 2:
                print(f"{Fore.WHITE}{one}")
                print(f"{Fore.WHITE}{to}")
                print(f"{Fore.BLUE}{three}")

            last_choice = choices

        time.sleep(0.01)

thread1 = threading.Thread(
    target=choice,
    args=("Twitter", "Youtube", "Github")
)

thread2 = threading.Thread(
    target=kybord
)

thread1.start()
thread2.start()
