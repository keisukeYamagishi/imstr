import os.path

class Option:

    __VERSION__ = '2.0.1'

    def __init__(self, argv):
        self.argv = argv
        self.val = self.shaping(argv[0])
        self.isConver = False
        self.VERSION = False
        self.SELECTED = False
        self.OUTPUT_PATH = False
        self.htmlName = ''

        if len(argv) == 1:
            self.isConver = True

    def setup(self):

        if self.isConver == True:
            self.output = 'Use it this\n\t' + self.val + ' path option \noptions\n\t-n html_name\n\t-v [ Disply this version ]\n\t-o Not Display output path\nSupported image format\n\tpng, jpeg, jpg, jpe'
        else:
            for op in range(len(self.argv)):
                if self.argv[op] == '-v':
                    self.VERSION = True
                    self.versionDisplay = self.val +  ' version: ' + Option.__VERSION__
                elif self.argv[op] == '-n':
                    self.SELECTED = True
                    if self.argv[op+1] is None:
                        self.htmlName = ''
                    else:
                        self.htmlName = self.argv[op+1]
                elif self.argv[op] == '-o':
                    self.OUTPUT_PATH = True

    def shaping(self, path):
        val = ''
        if path.find('./') != -1:
            string = path.split('./')
            val = string[1]
        return val