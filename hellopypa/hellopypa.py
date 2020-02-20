from os.path import abspath, dirname, join
from configparser import ConfigParser


def hello(upper=False):
    mydir = dirname(abspath(__file__))
    config = ConfigParser()
    config.read(join(mydir, 'example.cfg'))
    msg = config['DEFAULT']['msg']
    if upper:
        msg = msg.upper()
    return msg
