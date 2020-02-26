from pathlib import Path
from zipfile import ZipFile
from urllib.request import urlopen
from os.path import abspath, dirname, join
from configparser import ConfigParser

CWD = dirname(abspath(__file__))


def hello(upper=False):
    config = ConfigParser()
    config.read(join(CWD, 'example.cfg'))
    msg = config['DEFAULT']['msg']
    if upper:
        msg = msg.upper()
    return msg


def load():
    resdir = join(CWD, 'resources')
    myzip = join(resdir, 'res.zip')
    Path(resdir).mkdir(parents=True, exist_ok=True)
    URL = 'https://github.com/mittelholcz/hellopypa/archive/0.0.10.zip'
    response = urlopen(URL)
    with open(myzip, 'wb') as myzipfh:
        myzipfh.write(response.read())
    with ZipFile(myzip, 'r') as myzipfh:
        myzipfh.extractall(resdir)
