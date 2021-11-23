from PIL import Image
import pytesseract
import time
import keyboard
import random
 
IMAGE_INPUT_NAME = 'input.jpg'
FILE_OUTPUT_NAME = 'result.txt'
ACCEPTED_ASCII_LIST = []
for x in range(32, 127):
    ACCEPTED_ASCII_LIST.append(x)
 


def extract_text_from_image():
	PIPE_ASCII = 124
	
	time_start = time.perf_counter()
	text = pytesseract.image_to_string(Image.open(IMAGE_INPUT_NAME))