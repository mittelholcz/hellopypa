from os.path import abspath, dirname, join
from configparser import ConfigParser


def hello():
    here = dirname(abspath(__file__))
    config = ConfigParser()
    config.read(join(here, 'example.cfg'))
    msg = config['DEFAULT']['msg']
    return msg
