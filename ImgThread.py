# coding:utf-8
import threading
import time
from Progress import Indicator

class ImgThread(threading.Thread):

    def __init__(self):
        super(ImgThread, self).__init__()
        indis = ('Creating','Creating.','Creating..','Creating...','Creating....')
        speed = 0.3
        self.pro = Indicator(indis,speed)

    def run (self):
        self.pro.start()
        
    def stop(self):
        self.pro.stop()
