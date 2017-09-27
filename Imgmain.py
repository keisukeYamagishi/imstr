from ImageConversion import ImageConversion
from Progress import Indicator
from ImgThread import ImgThread

class Imgmain:

    def __init__(self, argv,option):
        self.argv = argv
        self.option = option

    def imgmain(self):
        Img = ImgThread()
        Img.start()
        im = ImageConversion(self.argv,self.option)
        im.CreateHtml()
        Img.stop()
