# coding:utf-8
import threading
import time
from Progress import Indicator

class ImgThread(threading.Thread):

    def __init__(self):
        super(ImgThread, self).__init__()

    def run (self):
        Indicator.Ind(Indicator.BEERWAITING)
