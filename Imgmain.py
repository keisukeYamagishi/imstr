from ImageConversion import ImageConversion
from Progress import Indicator
from ImgThread import ImgThread

class Imgmain:

    def __init__(self, argv):
        self.argv = argv

    def imgmain(self):
        Img = ImgThread()
        Img.start()
        im = ImageConversion(self.argv)
        im.CreateHtml()
        Img._Thread__stop()
