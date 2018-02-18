# coding:utf-8
import sys, time

class Indicator:

    _instance = None
    INDIGICATOR = 1
    STRINGPROGRESS = 2
    BEERPROGRESS = 3
    LOADINGINGICATOR = 4
    BEERWAITING = 5
    CREATING = 6

    def __init__(self,indis,dur):
        self.isStop = False
        self.indis = indis
        self.dur = dur

    @staticmethod
    def Ind(indiType):
        if indiType == Indicator.INDIGICATOR:
            indis = ('|','/','ー','\\','|','/','ー','\\')
            speed = 0.03
            pro = Indicator(indis,speed)
            pro.start()
        elif indiType == Indicator.STRINGPROGRESS:
            indis = ('Waiting','Waiting.','Waiting..','Waiting...')
            speed = 0.3
            pro = Indicator(indis,speed)
            pro.start()
        elif indiType == Indicator.BEERPROGRESS:
            indis = ('🍺 '*1,'🍺 '*2,'🍺 '*3,'🍺 '*4,'🍺 '*5,'🍺 '*6)
            speed = 0.1
            pro = Indicator(indis,speed)
            pro.start()
        elif indiType == Indicator.LOADINGINGICATOR:
            indis = ('Loading','Loading.','Loading..','Loading...','Loading....')
            speed = 0.3
            pro = Indicator(indis,speed)
            pro.start()
        elif indiType == Indicator.BEERWAITING:
            indis = ('Waiting' + '🍺 '*1 ,'Waiting' + '🍺 '*2 ,'Waiting' + '🍺 '*3,'Waiting' + '🍺 '*4, 'Waiting' + '🍺 '*4 + '🍻 ')
            speed = 0.3
            pro = Indicator(indis,speed)
            pro.start()
        elif indiType == Indicator.CREATING:
            indis = ('Creating','Creating.','Creating..','Creating...','Creating....')
            speed = 0.3
            pro = Indicator(indis,speed)
            pro.start()

    def Indicator(self):
        for num in range(0,len(self.indis)):
            if self.isStop == True:
                break
            self.bufferOut(self.indis[num],self.dur)

    def bufferOut(self,buf,t):
        space = ' '
        sys.stdout.write(buf + '\r')
        sys.stdout.flush()
        time.sleep(t)
        print '\b' + space * len(buf) + '\r',
        time.sleep(t)

    def start(self):
        while self.isStop == False:
            self.Indicator()
    def stop(self):
        self.isStop = True
