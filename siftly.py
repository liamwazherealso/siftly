import os
import glob
import shutil
import logging
import json
import sys

from datetime import datetime


# load stored configuration from the config.json file
config = json.load(open('config.json'))
extensions =  config['extensions']
dwnld = os.path.normpath(config['download_path'])
host_path  = os.path.normpath(config['host_path'])

# logs are stored by the date then the time in the log folder
current_date = datetime.today().strftime('%d_%m_%y_%H_%M')

# touch file
fname = 'log/' + current_date + '.log'
file = open(fname, 'w')
file.close()

logging.basicConfig(filename=fname, level=logging.INFO)

if (os.path.exists(dwnld)):
	for key in extensions:
		for extension in extensions[key]:
			for file_name in glob.glob(dwnld + '/*' + extension): 	
				if sys.argv > 1 and '-' == sys.argv[1][0] and 'v' in sys.argv[1]:
					print 'Moving ' + file_name  + ' to' + host_path + '/' + key

				logging.info('Moving ' + file_name  + ' to' + host_path + '/' + key)
				shutil.move(file_name,  os.path.join(host_path + '/' + key))	

else:
	print 'Failed to open: ' + dwnld + '\n'
	dnwld = os.path.normpath(raw_input('Enter a new directory'))
