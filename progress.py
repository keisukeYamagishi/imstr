import sys, time

class Progress:

    _instance = None

    def __init__(self):
        self.isStop = False

    # @classmethod
    # def shared(cls):
    #     if cls._instance is None:
    #         cls._instance = cls()
    #     return cls._instance

    def ProgresBar(self):
        for num in range(0,5):
            sys.stdout.write('Waiting' + '.' *num + '\r')
            sys.stdout.flush()
            time.sleep(0.4)
            print '\b                    \r',
            time.sleep(0.4)

    def start(self):
        while self.isStop == False:
            self.ProgresBar()

    def stop(self):
        self.isStop = True
