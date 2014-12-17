import unittest
import Siftly
import os
import shutil

class TestSiftly(unittest.TestCase):

    # add file types to test here.
    file_list = ['ant.jpeg', 'ant.jpeg', 'koala.jpg']
    def setUp(self):
        os.makedirs('from')
        os.makedirs('to')

        # creates test files
        for name in self.file_list:
            open('from/' + name, 'a').close()

        open('to/ant.jpeg', 'a').close()

    def test_sort(self):
        siftly = Siftly.Siftly()
        siftly.dwnld = 'from'
        siftly.test = True

        # configure siftly so that it sorts files from the tests
        temp = siftly.extensions
        newtemp = {}
        for key in temp:
            # the key is the dir, we are replacing the first dir with 'from'
            temp_key = key.split('/')
            temp_key = temp_key[1:]
            temp_key[0] = 'to'

            newtemp['/'.join(temp_key)] = temp[key]

        siftly.extensions = newtemp
        siftly.run()

    def tearDown(self):
        shutil.rmtree('to')
        shutil.rmtree('from')

if __name__ == '__main__':
    unittest.main()