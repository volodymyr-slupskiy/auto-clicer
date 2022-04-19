import keyboard, time, mouse

Click = False

def clicker():
    global Click
    if Click:
        Click = False
        print('Clicker off')
    else:
        Click = True
        print("Clicker on")


keyboard.add_hotkey('capslock', clicker)

while True:
    if Click:
        mouse.double_click(button = 'left')
        time.sleep(0.01)
# while True:
#     if Click:
#         keyboard.press('f')
#         time.sleep(0.01)
