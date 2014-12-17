import unittest
import Siftly
import os


class TestSiftly(unittest.TestCase):

    # add file types to test here.
    file_list = ['ant.jpeg', 'koala.jpg']
    def setUp(self):
        os.makedirs('from')
        os.makedirs('to')

        # creates test files
        for name in self.file_list:
            open('from' + name, 'a').close()

    def test_sort(self):
        siftly = Siftly()
        siftly.test = True
        siftly.run()

if __name__ == '__main__':
    unittest.main()