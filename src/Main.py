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
        potencia_ID = self.NewControlId()
        presion_ID = self.NewControlId()
        angulo_ID = self.NewControlId()

        self.CenterOnScreen()

    #BARRA DE MENU=======================================================================
        menu_bar = wx.MenuBar()
        #MENU DE CALCULADORAS============================================================
        calculator_menu = wx.Menu()
        estandar = calculator_menu.Append(estandar_ID, 'Estándar\tCtrl+E')
        cientifica = calculator_menu.Append(cientific_ID, 'Cientifica\tCtrl+I')

        #MENU DE CONVERSIONES============================================================
        conversor_menu = wx.Menu()
        volumen = conversor_menu.Append(volumen_ID, '&Volumen')
        longitud = conversor_menu.Append(longitud_ID, '&Longitud')
        peso_masa = conversor_menu.Append(peso_masa_ID, '&Peso y masa')
        temperatura = conversor_menu.Append(temperatura_ID, '&Temperatura')
        energia = conversor_menu.Append(energia_ID, '&Energia')
        area = conversor_menu.Append(area_ID, '&Area')
        velocidad = conversor_menu.Append(velocidad_ID, 'Velo&cidad')
        tiempo = conversor_menu.Append(tiempo_ID, 'T&iempo')
        potencia = conversor_menu.Append(potencia_ID, 'Pote&ncia')
        presion = conversor_menu.Append(presion_ID, 'P&resion')
        angulo = conversor_menu.Append(angulo_ID, 'Ang&ulo')

        
        menu_bar.Append(calculator_menu, '&Calculadora')
        menu_bar.Append(conversor_menu, 'Con&version')


        self.SetMenuBar(menu_bar)

        menu_inicio = wx.Panel(self)
        identificador = wx.StaticText(menu_inicio, label='MENU INICIAL')

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
        self.Bind(wx.EVT_MENU, self.convPotencia, potencia)
        self.Bind(wx.EVT_MENU, self.convPresion, presion)
        self.Bind(wx.EVT_MENU, self.convAngulo, angulo)

        

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
        ventanaVol = Conversiones(self, title='Volumen', size=(300,200))
        ventanaVol.Show()

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def convLongitud(self, evt):
        ventanaLong = Conversiones(self, title='Longitud', size=(300, 200))
        ventanaLong.Show()

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def convPeso_Masa(self, evt):
        ventanaPesoyMasa = Conversiones(self, title='Peso Y masa', size=(300,200))
        ventanaPesoyMasa.Show()

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def convTemperatura(self, evt):
        ventanaTemp = Conversiones(self, title='Temperatura', size=(300,200))
        ventanaTemp.Show()

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def convEnergia(self, evt):
        ventanaEn = Conversiones(self, title='Energía', size=(300,200))
        ventanaEn.Show()

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def convArea(self, evt):
        ventanaAr = Conversiones(self, title='Area', size=(300,200))
        ventanaAr.Show()

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def convVelocidad(self, evt):
        ventanaVel = Conversiones(self, title='Velocidad', size=(300,200))
        ventanaVel.Show()

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def convTiempo(self, evt):
        ventanaTiempo = Conversiones(self, title='Tiempo', size=(300,200))
        ventanaTiempo.Show()

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def convPotencia(self, evt):
        ventanaPot = Conversiones(self, title='Potencia', size=(300,200))
        ventanaPot.Show()

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def convPresion(self, evt):
        ventanaPres = Conversiones(self, title='Presión', size=(300,200))
        ventanaPres.Show()
    
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def convAngulo(self, evt):
        ventanaAng = Conversiones(self, title='Angulo', size=(300,200))
        ventanaAng.Show()


#////////////////////////////////////////////////////////////////////////////////////////
if __name__ == "__main__":
    app = wx.App(False)

    window = Window(None, title="The Calculator", size=Variables.l_and_w)

    app.MainLoop()