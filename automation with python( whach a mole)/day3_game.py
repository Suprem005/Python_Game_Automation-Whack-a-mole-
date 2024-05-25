import pyautogui as gui
from time import sleep

moles = ['assets/mole1.png','assets/mole2.png']
continue_bot = 'assets/start_button.png'
#while(1): checking sursor position live
#   print(gui.position(20,96))
#   print(gui.click(20,96))
def continue_botton():
        try:
            # find coordinate
            locationn = gui.locateOnScreen(continue_bot, confidence=0.8, grayscale=True)
            gui.click(locationn)
        
        except Exception as e:
            print("No Mole Found!!")
    
def whack_mole():
    for mole in moles:
        try:
            # find coordinate
            location = gui.locateOnScreen(mole, confidence=0.8, grayscale=True)
            gui.click(location)
        
        except Exception as e:
            print("No Mole Found!!")

sleep(3)
while True:
    whack_mole()

    
