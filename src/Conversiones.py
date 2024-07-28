import wx
import math

import Variables

class Conversiones(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.main()
    
    #////////////////////////////////////////////////////////////////////////////////////
    def main(self):
        self.SetWindowStyleFlag(wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX)
        self.CenterOnScreen()

    #////////////////////////////////////////////////////////////////////////////////////
    def volumen(self):
        panel = wx.Panel(self)
        s = wx.StaticText(panel, label='INICIO')
        #ID´S============================================================================
        cubo_ID = self.NewControlId()
        p__ID = self.NewControlId()
        cilindro_ID = self.NewControlId()
        esfera_ID = self.NewControlId()
        cono_ID = self.NewControlId()
        piramide_ID = self.NewControlId()

        #BARRA DE MENU===================================================================
        barra_menu = wx.MenuBar()
        #SUB MENUS=======================================================================
        forma = wx.Menu()
        cubo = forma.Append(cubo_ID, Variables.idioma.iloc[29, 1])
        prisma = forma.Append(p__ID, Variables.idioma.iloc[31, 1])
        cilindro = forma.Append(cilindro_ID, Variables.idioma.iloc[36, 1])
        esfera = forma.Append(esfera_ID, Variables.idioma.iloc[32, 1])
        cono = forma.Append(cono_ID, Variables.idioma.iloc[33, 1])
        piramide = forma.Append(piramide_ID, Variables.idioma.iloc[34, 1])

        #AGREGAR A MENU BAR==============================================================
        barra_menu.Append(forma, title=Variables.idioma.iloc[35, 1])
        self.SetMenuBar(barra_menu)

        #EVENTOS=========================================================================
        self.Bind(wx.EVT_MENU, self.cubo, cubo)
        self.Bind(wx.EVT_MENU, self.prism_rect, prisma)
        self.Bind(wx.EVT_MENU, self.cilindro, cilindro)
        self.Bind(wx.EVT_MENU, self.esfera, esfera)
        self.Bind(wx.EVT_MENU, self.cono, cono)
        self.Bind(wx.EVT_MENU, self.piramide, piramide)
    
    #||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    def cubo(self, evt):
        #ELIMINAR INSTANCIA ANTERIOR======================================================
        for child in self.GetChildren():
            if isinstance(child, wx.Panel):
                child.Destroy()

        largo, ancho = self.GetSize()

        size_b = (int(largo/4), int(ancho/8))
        self.size_border = int(largo/20)

        panel = wx.Panel(self)
        #SIZERS==========================================================================
        sizer_general = wx.BoxSizer(wx.VERTICAL)  #Donde irán todos los sizers
        sizer_op = wx.BoxSizer(wx.HORIZONTAL)  #Donde irán todo lo interactuable
        sizer_datos = wx.BoxSizer(wx.VERTICAL)      #Donde irán los bloques de entrada de datos
        sizer_resultados = wx.BoxSizer(wx.VERTICAL) #Donde irán los sizers de muestra de resultados
        sizer_titulo = wx.BoxSizer(wx.VERTICAL)     #Donde irá el titulo

        #TITULO==========================================================================
        titulo = wx.StaticText(panel, label=Variables.idioma.iloc[29, 1])

        #ENTRADA DE DATOS================================================================
        self.aristas = wx.TextCtrl(panel, value=Variables.idioma.iloc[28, 1], size=size_b)

        #Muestra resultados==============================================================
        self.resultado = wx.TextCtrl(panel, value='0', style=wx.TE_READONLY, size=size_b)
        b_resolver = wx.Button(panel, label=Variables.idioma.iloc[30, 1], size=size_b)

        #ACOMODO=========================================================================
        sizer_datos.Add(self.aristas, flag=wx.LEFT, border=int(self.size_border/2))
        sizer_datos.Add(b_resolver, flag=wx.TOP|wx.LEFT, border=int(self.size_border/2))

        sizer_resultados.Add(self.resultado)

        sizer_titulo.Add(titulo)

        sizer_op.Add(sizer_datos, flag=wx.ALL, border=self.size_border)
        sizer_op.Add(sizer_resultados, flag=wx.ALL, border=self.size_border)

        sizer_general.Add(sizer_titulo)
        sizer_general.Add(sizer_op)

        panel.SetSizer(sizer_general)

        #EVENTOS=========================================================================
        self.Bind(wx.EVT_BUTTON, self.vol_cubo, b_resolver)

        panel.Layout()
        self.Layout()

    #****************************************************************
    def vol_cubo(self, evt):
        a_str = self.aristas.GetLineText(0)
        if '.' in a_str:
            a = float(a_str)
        else:
            a = int(a_str)

        result = math.pow(a, 3)

        self.resultado.Clear()
        self.resultado.AppendText(str(result))
        self.respuesta.SetInsertionPoint(0)

    #||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    def prism_rect(self, evt):
        largo, ancho = self.GetSize()
        size_border = int(largo/20)
        #ELIMINAR INSTANCIA ANTERIOR======================================================
        for child in self.GetChildren():
            if isinstance(child, wx.Panel):
                child.Destroy()
        
        panel = wx.Panel(self)

        #SIZERS==========================================================================
        sizer_general = wx.BoxSizer(wx.VERTICAL)
        sizer_titulo = wx.BoxSizer(wx.VERTICAL)
        sizer_datos = wx.BoxSizer(wx.HORIZONTAL)
        sizer_entrada = wx.BoxSizer(wx.VERTICAL)
        sizer_salida = wx.BoxSizer(wx.VERTICAL)

        #TITULO==========================================================================
        titulo = wx.StaticText(panel, label=Variables.idioma.iloc[31, 1])

        #ENTRADA DE DATOS================================================================
        self.longitud_ent = wx.TextCtrl(panel, value='l')
        self.ancho_ent = wx.TextCtrl(panel, value='w')
        self.alto_ent = wx.TextCtrl(panel, value='h')

        #SALIDA DE DATOS=================================================================
        self.resultado = wx.TextCtrl(panel, style=wx.TE_READONLY)
        b_aceptar = wx.Button(panel, label=Variables.idioma.iloc[30, 1])

        #ACOMODO DE ELEMENTOS============================================================
        sizer_titulo.Add(titulo)

        sizer_entrada.Add(self.longitud_ent)
        sizer_entrada.Add(self.ancho_ent)
        sizer_entrada.Add(self.alto_ent)
        sizer_entrada.Add(b_aceptar)

        sizer_salida.Add(self.resultado)

        sizer_datos.Add(sizer_entrada)
        sizer_datos.Add(sizer_salida, flag=wx.LEFT, border=size_border)

        sizer_general.Add(sizer_titulo)
        sizer_general.Add(sizer_datos, flag=wx.LEFT|wx.RIGHT, border=size_border)

        panel.SetSizer(sizer_general)
        
        #EVENTOS=========================================================================
        self.Bind(wx.EVT_BUTTON, self.vol_prisma, b_aceptar)

        panel.Layout()
        self.Layout()

    #****************************************************************
    def vol_prisma(self, evt):
        l_srt = self.longitud_ent.GetLineText(0)
        w_srt = self.ancho_ent.GetLineText(0)
        h_srt = self.alto_ent.GetLineText(0)

        if '.' in l_srt:
            l = float(l_srt)
        elif '.' in w_srt:
            w = float(w_srt)
        elif '.' in h_srt:
            h = float(h_srt)
        else:
            l = int(l_srt)
            w = int(w_srt)
            h = int(h_srt)

        resultado = l * w * h

        self.resultado.Clear()
        self.resultado.SetValue(str(resultado))
        self.resultado.SetInsertionPoint(0)

    #||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    def cilindro(self, evt):
        #pixr2xh
        for child in self.GetChildren():
            if isinstance(child, wx.Panel):
                child.Destroy()
        
        panel = wx.Panel(self)

        #SIZERS==========================================================================
        sizer_general = wx.BoxSizer(wx.VERTICAL)
        sizer_titulo = wx.BoxSizer(wx.VERTICAL)
        sizer_datos = wx.BoxSizer(wx.HORIZONTAL)
        sizer_entrada = wx.BoxSizer(wx.VERTICAL)
        sizer_salida = wx.BoxSizer(wx.VERTICAL)

        #TITULO==========================================================================
        titulo = wx.StaticText(panel, label=Variables.idioma.iloc[36, 1])

        #ENTRADA DE DATOS================================================================
        self.radio_ent = wx.TextCtrl(panel, value='r')
        self.alto_ent = wx.TextCtrl(panel, value='h')

        #SALIDA DE DATOS=================================================================
        self.res_final = wx.TextCtrl(panel, style=wx.TE_READONLY)
        b_aceptar = wx.Button(panel, label=Variables.idioma.iloc[30, 1])

        #ACOMODO DE BLOQUES==============================================================
        sizer_titulo.Add(titulo)
        
        sizer_entrada.Add(self.radio_ent)
        sizer_entrada.Add(self.alto_ent)
        sizer_entrada.Add(b_aceptar)

        sizer_salida.Add(self.res_final)

        sizer_datos.Add(sizer_entrada)
        sizer_datos.Add(sizer_salida)

        sizer_general.Add(sizer_titulo)
        sizer_general.Add(sizer_datos)

        #EVENTOS=========================================================================
        self.Bind(wx.EVT_BUTTON, self.vol_cilindro, b_aceptar)

        panel.SetSizer(sizer_general)
        panel.Layout()
        self.Layout()

    #****************************************************************
    def vol_cilindro(self, evt):
        r_str = self.radio_ent.GetLineText(0)
        h_str = self.alto_ent.GetLineText(0)

        if '.' in r_str:
            r = float(r_str)
        elif '.' in h_str:
            h = float(h_str)
        else:
            r = int(r_str)
            h = int(h_str)

        vol = math.pi * (math.pow(r, 2)*h)
        self.res_final.Clear()
        self.res_final.AppendText(str(vol))
        self.res_final.SetInsertionPoint(0)

    #||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    def esfera(self, evt):
        #ELIMINAR INSTANCIAS ANTERIORES==================================================
        for child in self.GetChildren():
            if isinstance(child, wx.Panel):
                child.Destroy()
        
        panel = wx.Panel(self)
        #SIZERS==========================================================================
        sizer_general = wx.BoxSizer(wx.VERTICAL)
        sizer_titulo = wx.BoxSizer(wx.VERTICAL)
        sizer_datos = wx.BoxSizer(wx.HORIZONTAL)
        sizer_entrada = wx.BoxSizer(wx.VERTICAL)
        sizer_salida = wx.BoxSizer(wx.VERTICAL)

        #TITULO==========================================================================
        tiulo = wx.StaticText(panel, label=Variables.idioma.iloc[32, 1])

        #Entrada de datos================================================================
        self.radio_esf = wx.TextCtrl(panel, value='r')

        #Salida de datos=================================================================
        self.respuesta = wx.TextCtrl(panel, style=wx.TE_READONLY)
        b_aceptar = wx.Button(panel, label=Variables.idioma.iloc[30, 1])

        #ACOMODO DE OBJETOS==============================================================
        sizer_titulo.Add(tiulo)

        sizer_entrada.Add(self.radio_esf)
        sizer_entrada.Add(b_aceptar)

        sizer_salida.Add(self.respuesta)

        sizer_datos.Add(sizer_entrada)
        sizer_datos.Add(sizer_salida)

        sizer_general.Add(sizer_titulo)
        sizer_general.Add(sizer_datos)

        panel.SetSizer(sizer_general)

        #EVENTOS=========================================================================
        self.Bind(wx.EVT_BUTTON, self.vol_esfera, b_aceptar)

        panel.Layout()
        self.Layout()
    #****************************************************************
    def vol_esfera(self, evt):
        r_str = self.radio_esf.GetLineText(0)

        if '.' in r_str:
            r = float(r_str)
        else:
            r = int(r_str)

        vol = (4 * (math.pi * (math.pow(r, 3)))) / 3

        self.respuesta.Clear()
        self.respuesta.AppendText(str(vol))
        self.respuesta.SetInsertionPoint(0)

    #||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    def cono(self, evt):
        #ELIMINAR INSTANCIAS ANTERIORES==================================================
        for child in self.GetChildren():
            if isinstance(child, wx.Panel):
                child.Destroy()

        panel = wx.Panel(self)

        #SIZERS==========================================================================
        sizer_general = wx.BoxSizer(wx.VERTICAL)
        sizer_titulo = wx.BoxSizer(wx.VERTICAL)
        sizer_datos = wx.BoxSizer(wx.HORIZONTAL)
        sizer_entrada = wx.BoxSizer(wx.VERTICAL)
        sizer_salida = wx.BoxSizer(wx.VERTICAL)

        #TITULO==========================================================================
        titulo = wx.StaticText(panel, label=Variables.idioma.iloc[34, 1])

        #ENTRADA DE DATOS================================================================
        self.radio_cono = wx.TextCtrl(panel, value='r')
        self.alto_cono = wx.TextCtrl(panel, value='h')

        #SALIDA DE DATOS=================================================================
        self.res_esfera = wx.TextCtrl(panel, style=wx.TE_READONLY)
        b_aceptar = wx.Button(panel, label=Variables.idioma.iloc[30, 1])

        #ACOMODO DE OBJETOS==============================================================
        sizer_titulo.Add(titulo)

        sizer_entrada.Add(self.radio_cono)
        sizer_entrada.Add(self.alto_cono)
        sizer_entrada.Add(b_aceptar)

        sizer_salida.Add(self.res_esfera)

        sizer_datos.Add(sizer_entrada)
        sizer_datos.Add(sizer_salida)

        sizer_general.Add(sizer_titulo)
        sizer_general.Add(sizer_datos)

        panel.SetSizer(sizer_general)

        #EVENTOS=========================================================================
        self.Bind(wx.EVT_BUTTON, self.vol_cono, b_aceptar)

        panel.Layout()
        self.Layout()

    #****************************************************************
    def vol_cono(self, evt):
        r_str = self.radio_cono.GetLineText(0)
        h_str = self.alto_cono.GetLineText(0)

        if '.' in r_str:
            r = float(r_str)
        elif '.' in h_str:
            h = float(h_str)
        else:
            r = int(r_str)
            h = int(h_str)

        vol = (math.pi * (math.pow(r, 2) * h)) / 3

        self.res_esfera.Clear()
        self.res_esfera.AppendText(str(vol))
        self.res_esfera.SetInsertionPoint(0)

    #||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    def piramide(self, evt):
        #ELIMINAR INSTANCIAS ANTERIORES==================================================
        for child in self.GetChildren():
            if isinstance(child, wx.Panel):
                child.Destroy()
        
        panel = wx.Panel(self)

        #SIZERS==========================================================================
        sizer_general = wx.BoxSizer(wx.VERTICAL)
        sizer_titulo = wx.BoxSizer(wx.VERTICAL)
        sizer_datos = wx.BoxSizer(wx.HORIZONTAL)
        sizer_entrada = wx.BoxSizer(wx.VERTICAL)
        sizer_salida = wx.BoxSizer(wx.VERTICAL)

        #TTULO===========================================================================
        titulo = wx.StaticText(panel, label=Variables.idioma.iloc[34, 1])

        #ENTRADA DE DATOS================================================================
        self.largo_p = wx.TextCtrl(panel, value='l')
        self.ancho_p = wx.TextCtrl(panel, value='w')
        self.alto_p = wx.TextCtrl(panel, value='h')

        #SALIDA DE DATOS ================================================================
        self.resp = wx.TextCtrl(panel, style=wx.TE_READONLY)
        b_aceptar = wx.Button(panel, label=Variables.idioma.iloc[30, 1])

        #ACOMODO DE ELEMENTOS============================================================
        sizer_titulo.Add(titulo)

        sizer_entrada.Add(self.largo_p)
        sizer_entrada.Add(self.ancho_p)
        sizer_entrada.Add(self.alto_p)
        sizer_entrada.Add(b_aceptar)

        sizer_salida.Add(self.resp)

        sizer_datos.Add(sizer_entrada)
        sizer_datos.Add(sizer_salida)

        sizer_general.Add(sizer_titulo)
        sizer_general.Add(sizer_datos)

        panel.SetSizer(sizer_general)

        #EVENTOS=========================================================================
        self.Bind(wx.EVT_BUTTON, self.vol_piramide, b_aceptar)

        panel.Layout()
        self.Layout()
    #****************************************************************
    def vol_piramide(self, evt):
        l_str = self.largo_p.GetLineText(0)
        w_str = self.ancho_p.GetLineText(0)
        h_str = self.alto_p.GetLineText(0)

        if '.' in l_str:
            l = float(l_str)
        elif '.' in w_str:
            w = float(w_str)
        elif '.' in l_str:
            h = float(h_str)
        else:
            l = int(l_str)
            w = int(w_str)
            h = int(h_str)

        area = l * w
        vol = (area * h)/3

        self.resp.Clear()
        self.resp.AppendText(str(vol))
        self.resp.SetInsertionPoint(0)


