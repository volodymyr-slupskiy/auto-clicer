import keyboard, pyautogui, os

files = os.listdir('Button')

while keyboard.is_pressed("esc") == False:

    for f in files:

        picture = "Button/" + f

        button = pyautogui.locateOnScreen(picture, confidence = 0.95)

        if button:

            pyautogui.doubleClick(button)
            pyautogui.sleep(2)