from ImageConversion import ImageConversion
from Progress import Indicator
from ImgThread import ImgThread

class Imgmain:

    def __init__(self, argv,htmlName):
        self.argv = argv
        self.htmlName = htmlName

    def imgmain(self):
        Img = ImgThread()
        Img.start()
        im = ImageConversion(self.argv,self.htmlName)
        im.CreateHtml()
        Img._Thread__stop()
