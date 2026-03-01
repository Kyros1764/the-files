import pyscreenshot as ImageGrab
import pytesseract
from PIL import Image
import pyautogui
import time
import keyboard
import random

def select_region():
    print("Move your mouse to the top-left corner of the region and click.")
    time.sleep(2)  # Give the user time to move the mouse
    x1, y1 = pyautogui.position()
    print(f"Top-left corner selected at ({x1}, {y1})")

    print("Move your mouse to the bottom-right corner of the region and click.")
    time.sleep(2)  # Give the user time to move the mouse
    x2, y2 = pyautogui.position()
    print(f"Bottom-right corner selected at ({x2}, {y2})")

    return (x1, y1, x2, y2)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Capture the screen

region = select_region()

while True:
    image = ImageGrab.grab(bbox=region)

    # Convert the image to RGB mode if it's not already
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # Now you can use the size attribute
    print(image.size)

    # ... rest of your code ...

    text = pytesseract.image_to_string(image)
    
    keyboard.write(text=text, delay=(random.randint(1, 4)/100))
    
    time.sleep(2.5)
    
    