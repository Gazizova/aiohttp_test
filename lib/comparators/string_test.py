import logging
import os
from os import listdir, makedirs
# from lib.logger import LoggingHandler
from os.path import abspath, isdir, expanduser, join
# __author__ = ''


class StringTest():
    # def test_log(self):
    # super().__init__()
    a = "string1-string2 strig3"
    print(a)
    b = a.capitalize()
    print(b)

    logging.basicConfig(level=logging.DEBUG)
    for i in range(0, 1):
        if i%2==0:
            logging.info('this number is:  {}'.format(i))
        else:
            logging.debug('Not even {}'.format(i))


def scan_directory(directory, ext):
    for file in listdir(directory):
        if file.endswith(ext):
            if file.endswith(ext):
                print(join(directory, file))
                logging.info("files in directory: {}".format(file))

c = os.getcwd()
a = scan_directory('./test_dir', 'png')
# a.test_log