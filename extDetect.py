import os.path

class Extentions:

    NOT_DO = 0
    VERSION_DISPALY = 1
    HTML_NAME = 2
    NOT_SELECTED = 3

    __VERSION__ = '2.0.1'

    def __init__(self, argv):
        self.argv = argv
        self.val = self.shaping(argv[0])
        self.isConver = 1
        self.VERSION = -1
        self.SELECTED = -1
        self.OUTPUT_PATH = 0
        self.htmlName = ''

        if len(argv) == 1:
            self.isConver = 0

    def CanConversion(self):

        if self.isConver == 0:
            self.output = 'Use it this\n\t' + self.val + ' [ /home/shichimi/conversion.png ]\noptions\n\t-n html_name\n\t-v [ Disply this version ]\n\t-o Not Display output path\nSupported image format\n\tpng, jpeg, jpg, jpe'
        else:

            for op in range(len(self.argv)):
                if self.argv[op] == '-v':
                    self.VERSION =  Extentions.VERSION_DISPALY
                    self.versionDisplay = self.val +  ' version: ' + Extentions.__VERSION__
                elif self.argv[op] == '-n':
                    self.SELECTED = Extentions.HTML_NAME
                    if self.argv[op+1] is None:
                        self.htmlName = ''
                    else:
                        self.htmlName = self.argv[op+1]
                elif self.argv[op] == '-o':
                    self.OUTPUT_PATH = 1
                    
    def shaping(self, path):
        if path.find('./') != -1:
            string = path.split('./')
            self.val = string[1]
        return self.val
