import os

class String:

    NotFound = -1

    def __init__(self, filePath):
        if filePath == '':
            self.filePath = 'index.html'
        else:
            self.filePath = filePath

    def replace(self):
        strList = os.path.splitext(os.path.basename(self.filePath))
        return '{}.html'.format(strList[0])

    def formatStr(self):
        return '{}/{}'.format(os.getcwd(), self.replace())
