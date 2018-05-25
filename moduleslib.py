def time():
    from datetime import datetime
    import os

    datetime = str(datetime.now())			#Fetching date & time in a long big string
    date = datetime[:10]					#Separates date and time
    time = datetime[11:]
    time =     time[:8 ]					#Gets rid of the milliseconds

    finalList = [date]                      #Returns a list of strings, 0 is date, 1 is time.
    finalList.append(time)

    return finalList


def weather(city, state):
    import urllib.request
    import json

    import os, sys
    url = 'http://api.wunderground.com/api/386a8e8ab04d7748/conditions/q/'+state+'/'+city+'.json'

    response = urllib.request.urlopen(url)
    response_str = response.read().decode('utf-8')
    res = json.loads(response_str)			#This line is broken

    if 'error' in res['response'].keys():
    	return 'Error. Check input.'

    obs_rst = res['current_observation']			#Fetches the observation results as a large dictionary

    def location():
    	endString = city + ' ' + state				#Processes two strings into one for final output
    	return endString
    #location() works and returns a string that looks like "San Fran CA".

    weather	= obs_rst['weather']					#Fetches weather as a string
    temp 	= str(obs_rst['temp_c']) + ' degrees Celsius'			#Fetches temperature, outputs something like "20 degrees Celsius"
    loc		= location()							#Fetches location

    finalList = [weather] + [temp] + [loc]
    return finalList

def calendar():
    from apiclient.discovery import build
    from httplib2 import Http
    from oauth2client import file, client, tools
    import datetime, time
    import os

    dir = os.path.dirname(os.path.abspath(__file__))
    secret_dir = 'cache/secret.json'

    credentials_dir = 'modules/credentials.json'
    # Setup the Calendar API
    SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
    store = file.Storage(credentials_dir)
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(secret_dir, SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    now_ref = time.time()
    calendarid = 'i7vs7cuh27t4kvh0k517tnk3m8fjms11@import.calendar.google.com'
    events_result = service.events().list(calendarId=calendarid, timeMin=now,
                                          maxResults=60, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])
    blocks = [None]

    if not events:
        return ['No events', '']

    index = 0
    refresh_index = 0
    start = [None] * 60
    refresh_flag = False
    refresh_counter = True
    for event in events:
        start[index] = event['start'].get('dateTime', event['start'].get('date'))
        #If there are 20 chars in start, it's a class. Otherwise it's a homework.
        if len(start[index]) == 20:
            blocks.append(event['summary'])
            refresh_flag = True
        if refresh_flag and refresh_counter:
            current_event_index = index-1
            refresh_index = index
            refresh_counter = False
        index += 1
    blocks.pop(0)

    #Final process that isolates the block information from the entire string
    next_block = ''
    flag = False

    for i in blocks[1]:
        if i == '(':
            flag = True
        if i == ')':
            flag == False
        if flag:
            next_block += i
    length = len(next_block)
    next_block = next_block[1:]
    next_block = next_block[:length-2]

    utc_time = datetime.datetime.strptime(start[refresh_index+1], "%Y-%m-%dT%H:%M:%SZ")
    epoch = datetime.datetime.utcfromtimestamp(0)
    secs_ref = str((utc_time-epoch).total_seconds())
    finalList = [next_block] + [secs_ref]
    return finalList

class display:
    import pygame, os, sys
    from pygame.locals import QUIT
    import time as timelib
    dir = str(os.path.dirname(os.path.abspath(__file__)))
    date = None
    time = None
    city = None
    state = None
    weather = None
    temperature = None
    block = None

    def virtualDisplay():
        import pygame, os, sys
        from pygame.locals import QUIT
        import time as timelib

        icon_dir  = 'icon.jpg'
        pygame.init()
        font = pygame.font.SysFont('roboto', 40)
        #x and y are dimensions of the window.data
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

        def readCache():
            cache_dir = 'cache/cache'
            try:
                cache_file = open(cache_dir, 'r')
            except:
                pass
            cache_content_str = cache_file.readlines()
            cache_content_byt = [] * (len(cache_content_str)+1)
            cache_file.close()

            for i in range(len(cache_content_str)-1):
                cache_content_byt[i] = bytes(cache_content_str[i], 'utf-8')

            date = cache_content_byt[0]
            time = cache_content_byt[1]
            city = cache_content_byt[2]
            state = cache_content_byt[3]
            weather = cache_content_byt[4]
            temperature = cache_content_byt[5]
            block = cache_content_byt[6]

        #Adds the time.
        def display_time():

        	font = pygame.font.SysFont('roboto', 70)
        	time_label = font.render(time, 1, (255, 255, 255))

        	font = pygame.font.SysFont('roboto', 30)
        	date_label = font.render(date, 1, (255, 255, 255))

        	screen.blit(time_label, (5  , 80))
        	screen.blit(date_label, (5, 5))

        	pygame.display.flip()

        def display_weather():

        	city_weather      = city_weather_file.readlines()
        	#If clause: If weather file is empty, skip this function.
        	if os.stat(weather_dir).st_size == 0:
        		return

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

        set_window()
        reset_window()
        readCache()
        display_time()
        display_weather()
        display_block()
        #Try-except used to detect keystrokes and to quit the program.
        refresh_interval = 1
        past_time    = timelib.clock()
        current_time = timelib.clock()
        interval = current_time - past_time
        while True:
        	current_time = timelib.clock()
        	interval = current_time - past_time
        	if interval >= refresh_interval:
        		reset_window()
        		display_time()
        		display_weather()
        		display_block()
        		past_time = current_time

        	for event in pygame.event.get():
        		if event.type == QUIT:
        			return 'quit'

        	timelib.sleep(0.1)
