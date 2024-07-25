import wx

import Variables

class Calculadora(wx.Panel):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

    #////////////////////////////////////////////////////////////////////////////////////
    def estandar(self):
        identificador = wx.StaticText(self, label='ESTANDAR')
    
    #////////////////////////////////////////////////////////////////////////////////////
    def cientifica(self):
        identificador = wx.StaticText(self, label='CIENTIFICA')
    
