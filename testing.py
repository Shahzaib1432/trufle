# This file is used to test bugs

import trufle as t
class MainWindow(t.Window):
    def __init__(self):
        super().__init__('Game Store')
        self.THEMECOL = '#EF5D17'
        self.winH = self.info_height()
        self.winW = self.info_width()

        self.defineUI()
        self.run()

    def defineUI(self):
        self.sg = t.SizeGripFrame(self,self, x=0,y=0)

window = MainWindow()
