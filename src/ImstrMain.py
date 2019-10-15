from ImageString import ImageString

class ImstrMain:

    def __init__(self, argv,option):
        self.argv = argv
        self.option = option

    def imgmain(self):
        imageString = ImageString(self.argv,self.option)
        imageString.createHtml()
