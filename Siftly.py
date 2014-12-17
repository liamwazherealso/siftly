import os
import glob
import shutil
import logging
import json
import sys

from datetime import datetime


class Siftly():

    def __init__(self):
        # load stored configuration from the config.json file
        if not os.path.exists('./config.json'):
            logging.info('Config.json not found using example_config.json.')
            shutil.copy('./example_config.json', './config.json')

        self.config = json.load(open('config.json'))
        self.extensions = self.config['extensions']
        self.dwnld = os.path.normpath(self.config['download_path'])
        self.test = False

        # logs are stored by the date then the time in the log folder
        current_date = datetime.today().strftime('%d_%m_%y_%H_%M')

        # create log folder if it is not there.
        if not os.path.exists('log'):
            os.makedirs('log')

        # touch file
        fname = 'log/' + current_date + '.log'
        file = open(fname, 'w')
        file.close()


        logging.basicConfig(filename=fname, level=logging.INFO)

    def run(self):
        if os.path.exists(self.dwnld):
            for key in self.extensions:
                if not os.path.exists(key):
                    if self.test or raw_input('Folder ' + key + ' does not exist, would you like to create one? (yes or'
                                                                ' no) ') == 'y':
                        os.makedirs(key)
                    else:
                        print "Directory not made."

            # checks through the files in the dwnld dir to see if they match any of the extensions and moves them.
            for key in self.extensions:
                for extension in self.extensions[key]:
                    for file_name in glob.glob(self.dwnld + '/*' + extension):
                        # not a great solution if there are many duplicates but fuck it
                        if os.path.isfile(os.path.join(key, file_name)):
                            file_name = '_' + file_name

                        if len(sys.argv) > 1 and 'v' in sys.argv[1]: # verbose
                            print 'Moving ' + file_name + ' to' + key

                        logging.info('Moving ' + file_name + ' to ' + key)
                        print '1' + file_name
                        shutil.move(file_name, key)

            # checking remaining files to determine if they are a folder, I assume folder are applications
            for file_name in os.listdir(self.dwnld):
                if os.path.isdir(os.path.join(self.dwnld, file_name)) and 'Applications' in self.extensions:
                    logging.info('Moving ' + file_name + ' to' + self.extensions['Applications'])

        else:
            print 'Failed to open: ' + self.dwnld + '\n'
            dnwld = os.path.normpath(raw_input('Enter a new directory'))

if __name__ == '__main__':
    siftly = Siftly()
    siftly.run()