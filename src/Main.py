import wx

import Variables
from Calculadoras import *
from Conversiones import *

class Window(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.main()
    #////////////////////////////////////////////////////////////////////////////////////
    def main(self):
        self.extra_l = Variables.lenght_w
        self.extra_a = int(Variables.widht_w / 3)

        self.size_conver = (self.extra_l, self.extra_a)

        #ID´s============================================================================
        #==CONVERSIONES====================
        volumen_ID = self.NewControlId()

        #==IDIOMAS=========================
        espanol_ID = self.NewControlId()
        ingles_ID = self.NewControlId()

        #==TOOL BAR========================
        m_ID = self.NewControlId()

        self.CenterOnScreen()

    #BARRA DE MENU=======================================================================
        menu_bar = wx.MenuBar()

        #MENU DE CONVERSIONES============================================================
        conversor_menu = wx.Menu()
        volumen = conversor_menu.Append(volumen_ID, Variables.idioma.iloc[5,1])

        #MENU DE AJUSTES=================================================================
        ajustes = wx.Menu()

        espanol = ajustes.Append(espanol_ID, Variables.idioma.iloc[16,1])
        ajustes.AppendSeparator()
        ingles = ajustes.Append(ingles_ID, Variables.idioma.iloc[17,1])
        
        #AGREGAR ELEMENTOS===============================================================
        menu_bar.Append(conversor_menu, title=Variables.idioma.iloc[4,1])
        menu_bar.Append(ajustes, title=Variables.idioma.iloc[15,1])

        self.SetMenuBar(menu_bar)

        #PANEL CALCULADORA===============================================================
        menu_inicio = Calculadora(self)
        menu_inicio.estandar()
    #EVENTOS=============================================================================
        #===VENTANAS DE CONVERSION=======================================================
        self.Bind(wx.EVT_MENU, self.convVolumen, volumen)

        #CAMBIOS DE IDIOMA===============================================================
        self.Bind(wx.EVT_MENU, self.onEsp, espanol)
        self.Bind(wx.EVT_MENU, self.onEng, ingles)


        self.Show(True)
    
    #////////////////////////////////////////////////////////////////////////////////////
    def onCambioEstandar(self, evt):
        for child in self.GetChildren():
            if isinstance(child, wx.Panel):
                child.Destroy()

        self.cal_estand = Calculadora(self)
        self.cal_estand.estandar()
        self.actualizarPanel()
        
    #////////////////////////////////////////////////////////////////////////////////////
    def actualizarPanel(self):
        for child in self.GetChildren():
            if isinstance(child, wx.Panel):
                self.Layout()

    #////////////////////////////////////////////////////////////////////////////////////
    def convVolumen(self, evt):
        ventanaVol = Conversiones(self, title=Variables.idioma.iloc[18,1], size=self.size_conver)
        ventanaVol.volumen()
        ventanaVol.Show()

    #////////////////////////////////////////////////////////////////////////////////////
    def onEsp(self, evt):
        Variables.idioma = Variables.excel_idioma_esp

        nuevaWin = Window(None, title="The Calculator", size=(int(Variables.lenght_w), int(Variables.widht_w)), style=wx.CAPTION|wx.MINIMIZE_BOX|wx.CLOSE_BOX)
        self.Destroy()
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def onEng(self, evt):
        Variables.idioma = Variables.excel_idioma_eng
        
        nuevaWin = Window(None, title="The Calculator", size=(int(Variables.lenght_w), int(Variables.widht_w)), style=wx.CAPTION|wx.MINIMIZE_BOX|wx.CLOSE_BOX)
        self.Destroy()

#////////////////////////////////////////////////////////////////////////////////////////
if __name__ == "__main__":
    app = wx.App(False)
    screen = wx.ScreenDC()

    Variables.lenght_w , Variables.widht_w = screen.GetSize()
    L = Variables.lenght_w / 6

    Variables.lenght_w /= 4
    Variables.widht_w -= L

    window = Window(None, title="The Calculator", size=(int(Variables.lenght_w), int(Variables.widht_w)), style=wx.CAPTION|wx.MINIMIZE_BOX|wx.CLOSE_BOX)

    app.MainLoop()