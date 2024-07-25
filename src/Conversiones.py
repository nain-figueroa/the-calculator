import wx

import Variables

class Conversiones(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.main()
    
    #////////////////////////////////////////////////////////////////////////////////////
    def main(self):
        self.SetSize(Variables.ventan_ext)
        self.CenterOnScreen()


