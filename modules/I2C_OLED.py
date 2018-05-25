import Adafruit_SSD1306 as displib
import Adafruit_GPIO.SPI 
import os, sys
import time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

par_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
font_path = par_dir + '/cache/Roboto-Regular.ttf'
data_path = par_dir + '/data/Block'
runFlag_path = par_dir + '/cache/runFlag'

runFlag_file = open(runFlag_path, 'r')
runFlag = int(runFlag_file.read())
if not runFlag: 
	sys.exit()

RST = 24
disp = displib.SSD1306_128_64(rst = RST)

def disp_setup(): 
	disp.begin()
	disp.clear()
	disp.display()

def disp_block(): 
	width   = disp.width
	height  = disp.height
	image = Image.new('1', (width, height))

	draw = ImageDraw.Draw(image)
	font_small = ImageFont.truetype(font_path, 15)
	font_large  = ImageFont.truetype(font_path, 49)

	block_file = open(data_path, 'r')
	block = block_file.read()
	block_file.close()

	draw.text((0, 0), 'Next block is: ', font = font_small, fill = 255)
	draw.text((0, 15), block, font = font_large, fill = 255)

	disp.image(image)
	disp.display()

disp_setup()

while True: 
	disp_block()
	time.sleep(60)

