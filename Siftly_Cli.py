#!/usr/bin/python

import os
import glob
import shutil
import logging
import json
import sys

from datetime import datetime

"""
logging - used to make a log file for what happened
json - Javascript Object Format is used to save what folders extentions should go in
glob - for string pattern matching with *
"""
# load stored configuration from the config.json file
# Check that the path exists
if not os.path.exists('./config.json'):
    # use the basic log file instead
    shutil.copy('./example_config.json', './config.json')

# JSON is like a dictionary
config = json.load(open('config.json'))
# load a list of
extensions = config['extensions']
# load the path to download from
dwnld = os.path.normpath(config['download_path'])

# logs are stored by the date then the time in the log folder
current_date = datetime.today().strftime('%y_%m_%d_%H_%M')

# create log folder if it is not there.
if not os.path.exists('log'):
    os.makedirs('log')

# touch file
fname = 'log/' + current_date + '.log'
file = open(fname, 'w')
file.close()

# set the log to write to the file
logging.basicConfig(filename=fname, level=logging.INFO)

# logs are stored by the date then the time in the log folder
current_date = datetime.today().strftime('%y_%m_%d_%H_%M')

# touch file
fname = 'log/' + current_date + '.log'
file = open(fname, 'w')
file.close()

logging.basicConfig(filename=fname, level=logging.INFO)

if os.path.exists(dwnld):
    # iterate through the paths that the files should be going to and check that they exists
    for key in extensions:
        if not os.path.exists(key):
            if input('Folder ' + key + ' does not exist, would you like to create one? (yes or'
                                                        ' no) ') == 'y':
                os.makedirs(key)
            else:
                extensions.remove(key)
                print("Directory not made.")

    # checks through the files in the dwnld dir to see if they match any of the extensions and moves them.
    for key in extensions:
        # iterate through the lists of extentions
        for extension in extensions[key]:
            for file_name in glob.glob(dwnld + '/*' + extension):

                if len(sys.argv) > 1 and 'v' in sys.argv[1]: # verbose
                    print('Moving ' + file_name + ' to' + key)
                try:
                    logging.info('Moving ' + file_name + ' to ' + key)
                    shutil.move(file_name, key)
                except:
                    logging.error("Failed to move " + str(file_name))

    # checking remaining files to determine if they are a folder, I assume folder are applications
    for file_name in os.listdir(dwnld):
        if os.path.isdir(os.path.join(dwnld, file_name)) and 'Applications' in extensions:
            logging.info('Moving ' + file_name + ' to' + extensions['Applications'])

else:
    print('Failed to open: ' + dwnld + '\n')
    dnwld = os.path.normpath(input('Enter a new directory'))
