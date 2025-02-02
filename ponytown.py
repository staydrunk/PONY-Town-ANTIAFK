import random
import pyautogui
import time

keys = ["u", "x", "v", "k"]

class term_color:
    
    FAIL = r'\033[91m'  
    ENDC = r'\033[0m'  

def mode_selection():
    available_selection = ["BLANK", "Start"]
    while True:
        try:
            selection = input(
                "No ban risk! Close the tab to make the app stop.\n" +
                "--> Type 'Start' to begin, MADE BY STAYDRUNK ON GITHUB. Thanks for the inspirations and making me do this!.\n"
                ">>> ").strip()
            if selection in available_selection:
                return selection
            else:
                raise ValueError
        except ValueError:
            print(f"{term_color.FAIL}Please choose a valid option from the list{term_color.ENDC}")


def seconds_interval():
    while True:
        try:
            second_selection = int(input("Select every how many seconds it will repeat >>> "))
            if isinstance(second_selection, int):
                return second_selection
            else:
                raise ValueError
        except ValueError:
            print(f"{term_color.FAIL}Value must be a number{term_color.ENDC}")


def move_mouse():
    current_mouse_x, current_mouse_y = pyautogui.position()
    pyautogui.moveTo(current_mouse_x - 1, current_mouse_y - 1)


def main():
    try:
        mode = mode_selection()
        seconds_to_repeat = seconds_interval()
        while True:
            if mode == "Start":
                move_mouse()
                rand = random.randint(0, len(keys) - 1)
                press_and_depress_with_delay(keys[rand], 0.5)
            time.sleep(seconds_to_repeat)
    except KeyboardInterrupt:
        pass


def press_and_depress_with_delay(key, sleep):
    pyautogui.keyDown(key)
    time.sleep(sleep)
    pyautogui.keyUp(key)


if __name__ == "__main__":
    main()
