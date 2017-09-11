import os.path

class Extentions:

    __VERSION__ = '1.0.1'

    def __init__(self, argv):
        self.argv = argv
        self.val = argv[0]
        self.isConver = 1
        if len(argv) == 1:
            self.isConver = 0
        else:
            self.fullpath = argv[1]

    def CanConversion(self):
        isCon = 0
        if self.isConver == 0:
            isCon = 0
            self.val = self.shaping(self.val)
            print 'Use it this\n\t' + self.val + ' image path [ /home/shichimi/conversion.png ]\n\t' + self.val + ' -v [ Disply this version ]\nSupported image format\n\tpng, jpeg, kpg, jpe'
        else:

            if self.argv[1] == '-v':
                print self.shaping(self.val) +  ' version: ' + Extentions.__VERSION__
            else:
                path, ext = os.path.splitext(self.fullpath)
                print ext
                if ext == '.png' or ext == '.jpeg' or ext == '.jpg' or ext == '.jpe':
                    print 'isImage'
                    isCon = 1
                else:
                    print 'should set the image, the image format is png or jpeg or jpg, jpe'
                    isCon = 0

        return isCon

    def shaping(self, path):
        if path.find('./') != -1:
            string = path.split('./')
            self.val = string[1]
        return self.val
