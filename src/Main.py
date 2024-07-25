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
        #ID´s============================================================================
        #===OPCIONES=======================
        estandar_ID = self.NewControlId()
        cientific_ID = self.NewControlId()

        #==CONVERSIONES====================
        volumen_ID = self.NewControlId()
        longitud_ID = self.NewControlId()
        peso_masa_ID = self.NewControlId()
        temperatura_ID = self.NewControlId()
        energia_ID = self.NewControlId()
        area_ID = self.NewControlId()
        velocidad_ID = self.NewControlId()
        tiempo_ID = self.NewControlId()
        presion_ID = self.NewControlId()
        angulo_ID = self.NewControlId()

        #==IDIOMAS=========================
        espanol_ID = self.NewControlId()
        ingles_ID = self.NewControlId()

        self.CenterOnScreen()

    #BARRA DE MENU=======================================================================
        menu_bar = wx.MenuBar()
        #MENU DE CALCULADORAS============================================================
        calculator_menu = wx.Menu()

        calculator_menu.AppendSeparator()
        estandar = calculator_menu.Append(estandar_ID, Variables.idioma.iloc[2,1])
        cientifica = calculator_menu.Append(cientific_ID, Variables.idioma.iloc[3,1])

        #MENU DE CONVERSIONES============================================================
        conversor_menu = wx.Menu()
        volumen = conversor_menu.Append(volumen_ID, Variables.idioma.iloc[5,1])
        longitud = conversor_menu.Append(longitud_ID, Variables.idioma.iloc[6,1])
        peso_masa = conversor_menu.Append(peso_masa_ID, Variables.idioma.iloc[7,1])
        temperatura = conversor_menu.Append(temperatura_ID, Variables.idioma.iloc[8,1])
        energia = conversor_menu.Append(energia_ID, Variables.idioma.iloc[9,1])
        area = conversor_menu.Append(area_ID, Variables.idioma.iloc[10,1])
        velocidad = conversor_menu.Append(velocidad_ID, Variables.idioma.iloc[11,1])
        tiempo = conversor_menu.Append(tiempo_ID, Variables.idioma.iloc[12,1])
        presion = conversor_menu.Append(presion_ID, Variables.idioma.iloc[13,1])
        angulo = conversor_menu.Append(angulo_ID, Variables.idioma.iloc[14,1])

        #MENU DE AJUSTES=================================================================
        ajustes = wx.Menu()

        espanol = ajustes.Append(espanol_ID, Variables.idioma.iloc[16,1])
        ajustes.AppendSeparator()
        ingles = ajustes.Append(ingles_ID, Variables.idioma.iloc[17,1])
        
        #AGREGAR ELEMENTOS===============================================================
        menu_bar.Append(calculator_menu, title=Variables.idioma.iloc[0,1])
        menu_bar.Append(conversor_menu, Variables.idioma.iloc[4,1])
        menu_bar.Append(ajustes, Variables.idioma.iloc[15,1])


        self.SetMenuBar(menu_bar)

        #PANEL INICIAL POR DEFAULT=======================================================
        menu_inicio = Calculadora(self)
        menu_inicio.estandar()

        #EVENTOS=========================================================================
        #===CAMBIO DE TIPO===============================================================
        self.Bind(wx.EVT_MENU, self.onCambioEstandar, estandar)
        self.Bind(wx.EVT_MENU, self.onCambioCientific, cientifica)

        #===VENTANAS DE CONVERSION=======================================================
        self.Bind(wx.EVT_MENU, self.convVolumen, volumen)
        self.Bind(wx.EVT_MENU, self.convLongitud, longitud)
        self.Bind(wx.EVT_MENU, self.convPeso_Masa, peso_masa)
        self.Bind(wx.EVT_MENU, self.convTemperatura, temperatura)
        self.Bind(wx.EVT_MENU, self.convEnergia, energia)
        self.Bind(wx.EVT_MENU, self.convArea, area)
        self.Bind(wx.EVT_MENU, self.convVelocidad, velocidad)
        self.Bind(wx.EVT_MENU, self.convTiempo, tiempo)
        self.Bind(wx.EVT_MENU, self.convPresion, presion)
        self.Bind(wx.EVT_MENU, self.convAngulo, angulo)
        
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
    def onCambioCientific(self, evt):
        for child in self.GetChildren():
            if isinstance(child, wx.Panel):
                child.Destroy()

        self.cal_cient = Calculadora(self)
        self.cal_cient.cientifica()
        self.actualizarPanel()
        
    #////////////////////////////////////////////////////////////////////////////////////
    def actualizarPanel(self):
        for child in self.GetChildren():
            if isinstance(child, wx.Panel):
                self.Layout()

    #////////////////////////////////////////////////////////////////////////////////////
    def convVolumen(self, evt):
        ventanaVol = Conversiones(self, title=Variables.idioma.iloc[18,1])
        ventanaVol.Show()

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def convLongitud(self, evt):
        ventanaLong = Conversiones(self,  title=Variables.idioma.iloc[19,1])
        ventanaLong.Show()

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def convPeso_Masa(self, evt):
        ventanaPesoyMasa = Conversiones(self, title=Variables.idioma.iloc[20,1])
        ventanaPesoyMasa.Show()

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def convTemperatura(self, evt):
        ventanaTemp = Conversiones(self, title=Variables.idioma.iloc[21,1])
        ventanaTemp.Show()

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def convEnergia(self, evt):
        ventanaEn = Conversiones(self, title=Variables.idioma.iloc[22,1])
        ventanaEn.Show()

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def convArea(self, evt):
        ventanaAr = Conversiones(self, title=Variables.idioma.iloc[23,1])
        ventanaAr.Show()

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def convVelocidad(self, evt):
        ventanaVel = Conversiones(self, title=Variables.idioma.iloc[24,1])
        ventanaVel.Show()

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def convTiempo(self, evt):
        ventanaTiempo = Conversiones(self, title=Variables.idioma.iloc[25,1])
        ventanaTiempo.Show()

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def convPresion(self, evt):
        ventanaPres = Conversiones(self, title=Variables.idioma.iloc[26,1])
        ventanaPres.Show()
    
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def convAngulo(self, evt):
        ventanaAng = Conversiones(self, title=Variables.idioma.iloc[27,1])
        ventanaAng.Show()

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