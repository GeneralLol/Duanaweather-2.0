from datetime import datetime
import os

datetime = str(datetime.now())			#Fetching date & time in a long big string
date = datetime[:10]					#Separates date and time
time = datetime[11:]
time =     time[:8 ]					#Gets rid of the milliseconds

finalString = date + '\n' + time		#Produces a final string that looks like 2018-03-06\n16:12:21

#Fetches the directory that the data files are in
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = dir + '/data/Time'

os.remove(data_dir)							#Removes the previous time file and makes a new one
f = open(data_dir, 'w+')
f.write(finalString)					#Writes the final string into the cache file
quit()
