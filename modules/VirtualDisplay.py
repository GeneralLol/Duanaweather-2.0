import pygame, os, sys
from pygame.locals import *
import time

#Actual program
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = dir + '/data'
icon_dir = dir + '/icon.jpg'
pygame.init()
font = pygame.font.SysFont('roboto', 40)
#x and y are dimensions of the window.
x = 500
y = 309
icon   = pygame.image.load(icon_dir)
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((x,y))	#Sets the size

#Sets the window. Working.
def set_window():
	window_caption = 'Duanaweather'
	pygame.display.set_caption(window_caption)	#Sets the title
	#Sets the background
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((150, 150, 150))

	screen.blit(background, (0, 0))				#Applies the background
	pygame.display.flip()				#Refreshes the window

#Adds the time.
def display_time():

	time_dir = data_dir + '/Time'
	try:
		date_time_file = open(time_dir   , 'r')
	except FileNotFoundError:
		return

	date_time      = date_time_file.readlines()
	#If clause: If time file is empty(created by 'open'), skip this function.
	try:
		if os.stat(time_dir).st_size == 0:
			return
	except FileNotFoundError:
		return

	#Try to load the date and time in, if it doesn't work skip this round.
	try:
		date = date_time[0]
		time = date_time[1]
		date = date[:10]			#Gets rid of the \n at the end of the line
	except:
		return

	font = pygame.font.SysFont('roboto', 70)
	time_label = font.render(time, 1, (255, 255, 255))

	font = pygame.font.SysFont('roboto', 30)
	date_label = font.render(date, 1, (255, 255, 255))

	screen.blit(time_label, (5  , 80))
	screen.blit(date_label, (5, 5))

	pygame.display.flip()

def display_weather():

	weather_dir = data_dir + '/Weather'
	try:
		city_weather_file = open(weather_dir, 'r')
	except FileNotFoundError:
		return

	city_weather      = city_weather_file.readlines()
	#If clause: If weather file is empty, skip this function.
	if os.stat(weather_dir).st_size == 0:
		return

	city        = city_weather[0]
	city		= city   [:len(city)-1]
	weather     = city_weather[1]
	weather 	= weather[:len(weather)-1]
	temperature = city_weather[2]

	font = pygame.font.SysFont('roboto', 50)
	weather_label     = font.render(weather    , 1, (255, 255, 255))
	font = pygame.font.SysFont('roboto', 30)
	loc_label         = font.render(city       , 1, (255, 255, 255))
	font = pygame.font.SysFont('roboto', 30)
	temperature_label = font.render(temperature, 1, (255, 255, 255))

	screen.blit(weather_label    , (5  , 35 ))
	screen.blit(loc_label        , (5  , 280))
	screen.blit(temperature_label, (250, 45 ))

	pygame.display.flip()

def display_block():
	block_dir = data_dir + '/Block'
	try:
		block_file = open(block_dir, 'r')
	except:
		return

	block = block_file.read()
	block_file.close()

	font = pygame.font.SysFont('roboto', 40)
	block_label1 = font.render('Next Block is: ', 1, (255, 255, 255))
	font = pygame.font.SysFont('roboto', 160)
	block_label2 = font.render(block            , 1, (255, 255, 255))
	screen.blit(block_label1, (5  , 150))
	screen.blit(block_label2, (200, 150))
	pygame.display.flip()

def reset_window():
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((150, 150, 150))

	screen.blit(background, (0, 0))				#Applies the background
	pygame.display.flip()						#Refreshes the window

#Initial check to see if to run the module or not.
runFlag_dir = dir+'/cache/runFlag'
flag_raw = open(runFlag_dir)
flag = flag_raw.readlines()
flag_raw.close()
if flag[0] == '0':
	quit()

set_window()
reset_window()
display_time()
display_weather()
display_block()
#Try-except used to detect keystrokes and to quit the program.
refresh_interval = 1
past_time    = time.clock()
current_time = time.clock()
interval = current_time - past_time
while True:
	current_time = time.clock()
	interval = current_time - past_time
	if interval >= refresh_interval:
		reset_window()
		display_time()
		display_weather()
		display_block()
		past_time = current_time
	#Check whether the flag is still up. If flag down, end display.
	flag_raw = open(runFlag_dir)
	flag = flag_raw.readlines()
	flag_raw.close()
	for event in pygame.event.get():
		if event.type == QUIT:
			os.remove (runFlag_dir)
			f = open(runFlag_dir, 'w')
			f.write('0')
			f.close()
			sys.exit()
	if flag[0] == '0':
		sys.exit()

	time.sleep(0.1)
