import wx

import Variables

class Window(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.main()

    def main(self):
        self.CenterOnScreen()
        
        
        self.Layout()
        self.Show(True)
    
if __name__ == "__main__":
    app = wx.App(False)

    window = Window(None, title="The Calculator", size=Variables.l_and_w)

    app.MainLoop()