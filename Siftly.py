#!/usr/bin/python
import sys
import os
import glob
import shutil
import logging
import json
import sys

from PyQt4 import QtGui
from window import Ui_Siftly
from datetime import datetime


class Siftly(QtGui.QMainWindow):
    def sift(self):
        # logs are stored by the date then the time in the log folder
        current_date = datetime.today().strftime('%y_%m_%d_%H_%M')

        # create log folder if it is not there.
        if not os.path.exists('log'):
            os.makedirs('log')

        # touch file
        fname = 'log/' + current_date + '.log'
        file = open(fname, 'w')
        file.close()


        logging.basicConfig(filename=fname, level=logging.INFO)

        # load stored configuration from the config.json file
        config = json.load(open('config.json'))
        extensions = config['extensions']
        dwnld = str(self.ui.sift_folder.text())


        # logs are stored by the date then the time in the log folder
        current_date = datetime.today().strftime('%y_%m_%d_%H_%M')


        # touch file
        fname = 'log/' + current_date + '.log'
        file = open(fname, 'w')
        file.close()


        logging.basicConfig(filename=fname, level=logging.INFO)

        while not os.path.exists(self.dwnld):
            print('Failed to open: ' + self.dwnld + '\n')
            self.dnwld = os.path.normpath(input('Enter a new directory'))

        for key in self.extensions:
            if not os.path.exists(key):
                if self.test or input('Folder ' + key + ' does not exist, would you like to create one? (yes or'
                                                            ' no) ') == 'y':
                    os.makedirs(key)
                else:
                    self.extensions.remove(key)
                    print("Directory not made.")

        # checks through the files in the dwnld dir to see if they match any of the extensions and moves them.
        for key in self.extensions:
            for extension in self.extensions[key]:
                for file_name in glob.glob(self.dwnld + '/*' + extension):

                    if len(sys.argv) > 1 and 'v' in sys.argv[1]: # verbose
                        print('Moving ' + file_name + ' to' + key)
                    try:
                        logging.info('Moving ' + file_name + ' to ' + key)
                        shutil.move(file_name, key)
                    except:
                         logging.error("Failed to move " + str(file_name))

        # checking remaining files to determine if they are a folder, I assume folder are applications
        for file_name in os.listdir(self.dwnld):
            if os.path.isdir(os.path.join(self.dwnld, file_name)) and 'Applications' in self.extensions:
                logging.info('Moving ' + file_name + ' to' + self.extensions['Applications'])

        current_log = glob.glob("log/*")
        current_log.reverse()
        current_log = open(current_log[0], 'r').read()
        self.ui.sift_latest_log.setText(current_log)

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_Siftly()
        self.ui.setupUi(self)

        #Connect to handler methods
        self.ui.sift_btn_select_folder.clicked.connect(self.folder_chooser)
        self.ui.logs_dump.clicked.connect(self.dump_logs)
        self.ui.sift_btn.clicked.connect(self.sift)

        current_log = glob.glob("log/*")
        current_log.sort()
        if len(current_log) > 0:
            current_log = open(current_log[len(current_log) - 1], 'r').read()
        else:
            current_log = "No log"

        self.ui.sift_latest_log.setText(current_log)

        # load stored configuration from the config.json file
        if not os.path.exists('./config.json'):
            logging.info('Config.json not found using example_config.json.')
            shutil.copy('./example_config.json', './config.json')


        self.config = json.load(open('config.json'))
        self.extensions = self.config['extensions']
        self.dwnld = os.path.normpath(self.config['download_path'])

        self.ui.sift_folder.setText(self.dwnld)

    def folder_chooser(self):
        """
        Called when user wants to select a folder to sort.

        """
        openfile = QtGui.QFileDialog.getExistingDirectory(self.ui.sift_folder)
        if len(openfile) > 0:
            self.ui.sift_folder.setText(openfile)

    def dump_logs(self):
        """
        To destroy log files.
        """
        shutil.rmtree('log')
        os.makedirs('log')
        self.ui.sift_latest_log.setText('No log')


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Siftly()
    window.show()
    sys.exit(app.exec_())