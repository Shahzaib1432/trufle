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
        # self.sidebarFrame = t.Frame(self, corner_radius=0, border_width=0,
        #                             border_color='#000000', frame_color=interGrad,
        #                             width=170, height=self.winH, x=0,y=0)

        self.sg = t.SizeGripFrame(self,self, x=0,y=0)

window = MainWindow()
