#!/usr/bin/python

import os
import glob
import shutil
import logging
import json
import sys

from datetime import datetime


class sifter(object):
    def __init__(self):
        if not os.path.exists('./config.json'):
            # use the basic log file instead
            shutil.copy('./example_config.json', './config.json')

        self.config = json.load(open('config.json'))
        self.extensions = self.config['extensions']
        self.downloadDir = os.path.normpath(self.config['download_path'])

        current_date = datetime.today().strftime('%y_%m_%d_%H_%M')

        # setup logging
        if not os.path.exists('log'):
            os.makedirs('log')

        fname = 'log/' + current_date + '.log'
        file = open(fname, 'w')
        file.close()

        # set the log to write to the file
        logging.basicConfig(filename=fname, level=logging.INFO)

        if not os.path.exists(self.downloadDir):
            print('Failed to open: ' + self.downloadDir + '\n')   
            dnwld = os.path.normpath(input('Enter a new directory'))

        # iterate through the paths that the files should be going to and check that they exists
        for key in self.extensions:
            if not os.path.exists(key):
                if raw_input('Folder ' + key + ' does not exist, would you like to create one? (yes or no) ') == 'y':
                    os.makedirs(key)
                else:
                    self.extensions.remove(key)
                    print("Directory not made.")

    def sift(self):
        # checks through the files in the downloadDir dir to see if they match any of the self.extensions and moves them.
        for key in self.extensions:
            # iterate through the lists of extensions
            for extension in self.extensions[key]:
                for file_name in glob.glob(self.downloadDir + '/*' + extension):

                    if len(sys.argv) > 1 and 'v' in sys.argv[1]: # verbose
                        print('Moving ' + file_name + ' to' + key)
                    try:
                        logging.info('Moving ' + file_name + ' to ' + key)
                        shutil.move(file_name, key)
                    except:
                        logging.error("Failed to move " + str(file_name))

        # checking remaining files to determine if they are a folder, I assume folder are applications
        for file_name in os.listdir(self.downloadDir):
            if os.path.isdir(os.path.join(self.downloadDir, file_name)) and 'Applications' in self.extensions:
                logging.info('Moving ' + file_name + ' to' + self.extensions['Applications'])

mySifter = sifter()
mySifter.sift()