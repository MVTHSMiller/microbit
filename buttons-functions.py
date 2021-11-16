# Add your Python code here. E.g.
from microbit import *

#function definitions
def happy():
    display.show(Image.HAPPY)
    
def angry():
    display.show(Image.ANGRY)
    
while True:
   
    if (button_a.is_pressed() and button_b.is_pressed()):
        break
    
    elif button_a.is_pressed():
        happy()
        
    elif button_b.is_pressed():
        angry()
        
display.scroll('Bye')
        
