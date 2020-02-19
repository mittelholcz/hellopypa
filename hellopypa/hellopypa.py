from os.path import abspath, dirname, join
from configparser import ConfigParser


def hello(case=None):
    here = dirname(abspath(__file__))
    config = ConfigParser()
    config.read(join(here, 'example.cfg'))
    msg = config['DEFAULT']['msg']
    if case == 'l':
        msg = msg.lower()
    elif case == 'u':
        msg = msg.upper()
    return msg
