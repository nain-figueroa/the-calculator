import wx

import Variables

class Calculadora(wx.Panel):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

    #////////////////////////////////////////////////////////////////////////////////////
    def estandar(self):
        self.valor_final = 0
        self.suma = False
        self.resta = False
        self.multi = False
        self.div = False

        tam_textResult = (int(Variables.lenght_w),int(Variables.widht_w/10))
        tam_botones = (int(Variables.lenght_w/4),int(Variables.widht_w/8 - 5))
        #tam_memory_b = (int(Variables.lenght_w/6), int(Variables.widht_w/16))
        b_relleno= wx.Button(self, label='',size=tam_botones)

        fuente_botones = wx.Font(19, wx.FONTFAMILY_SCRIPT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_EXTRAHEAVY)

        #KEY EVENTS======================================================================
        self.key_event_Del = wx.KeyEvent(wx.wxEVT_KEY_DOWN)
        self.key_event_Del.SetKeyCode(wx.WXK_DELETE)
        

        #BOX SIZERS======================================================================
        sizer_general = wx.BoxSizer(wx.VERTICAL)
        sizer_calculos = wx.BoxSizer(wx.VERTICAL)
        sizer_M = wx.BoxSizer(wx.HORIZONTAL)            #MC, MR, M+, M-, MS, M(flecha para abajo)
        sizer_botones = wx.BoxSizer(wx.VERTICAL)
        sub_sizer_bontones_1 = wx.BoxSizer(wx.HORIZONTAL) #CE, C, /, Del
        sub_sizer_bontones_2 = wx.BoxSizer(wx.HORIZONTAL) #7, 8, 9, *
        sub_sizer_bontones_3 = wx.BoxSizer(wx.HORIZONTAL) #4, 5, 6, -
        sub_sizer_bontones_4 = wx.BoxSizer(wx.HORIZONTAL) #1, 2, 3, +
        sub_sizer_bontones_5 = wx.BoxSizer(wx.HORIZONTAL) #0, ., =

        #BOTONES=========================================================================
        #==NUMEROS=======================================================================
        b_0 = wx.Button(self, label='0', size=tam_botones)
        b_1 = wx.Button(self, label='1', size=tam_botones)
        b_2 = wx.Button(self, label='2', size=tam_botones)
        b_3 = wx.Button(self, label='3', size=tam_botones)
        b_4 = wx.Button(self, label='4', size=tam_botones)
        b_5 = wx.Button(self, label='5', size=tam_botones)
        b_6 = wx.Button(self, label='6', size=tam_botones)
        b_7 = wx.Button(self, label='7', size=tam_botones)
        b_8 = wx.Button(self, label='8', size=tam_botones)
        b_9 = wx.Button(self, label='9', size=tam_botones)

        #=====FUENTES====================================================================
        b_0.SetFont(fuente_botones)
        b_1.SetFont(fuente_botones)
        b_2.SetFont(fuente_botones)
        b_3.SetFont(fuente_botones)
        b_4.SetFont(fuente_botones)
        b_5.SetFont(fuente_botones)
        b_6.SetFont(fuente_botones)
        b_7.SetFont(fuente_botones)
        b_8.SetFont(fuente_botones)
        b_9.SetFont(fuente_botones)

        #==OPERACIONES===================================================================
        b_suma = wx.Button(self, label='+', size=tam_botones)
        b_resta = wx.Button(self, label='-', size=tam_botones)
        b_div = wx.Button(self, label='/', size=tam_botones)
        b_por = wx.Button(self, label='x', size=tam_botones)
        b_igual = wx.Button(self, label='=', size=tam_botones)

        #====FUENTES=====================================================================
        b_suma.SetFont(fuente_botones)
        b_resta.SetFont(fuente_botones)
        b_div.SetFont(fuente_botones)
        b_por.SetFont(fuente_botones)
        b_igual.SetFont(fuente_botones)

        #==ESPECIALES====================================================================
        b_dot = wx.Button(self, label='.', size=tam_botones)
        b_del = wx.Button(self, label='DEL', size=tam_botones)
        b_CE = wx.Button(self, label='CE', size=tam_botones)
        b_C = wx.Button(self, label='C', size=tam_botones)

        #====FUENTES=====================================================================
        b_dot.SetFont(fuente_botones)
        b_del.SetFont(fuente_botones)
        b_CE.SetFont(fuente_botones)
        b_C.SetFont(fuente_botones)

        #==M´S===========================================================================
        b_mc = wx.Button(self, label='MC')
        b_mr = wx.Button(self, label='MR')
        b_mp = wx.Button(self, label='M+')
        b_mn = wx.Button(self, label='M-')
        b_ms = wx.Button(self, label='MS')

        #CUADRO DE TEXTO=================================================================
        self.text_valores = wx.TextCtrl(self, value='', size=tam_textResult, style=wx.BOTTOM|wx.ALIGN_RIGHT|wx.TE_RICH|wx.TE_DONTWRAP|wx.TE_NOHIDESEL)
        self.text_operaciones = wx.TextCtrl(self, value='', size=tam_textResult, style=wx.BOTTOM|wx.ALIGN_RIGHT|wx.TE_RICH|wx.TE_DONTWRAP|wx.TE_NOHIDESEL)
        

        fuente = wx.Font(25, wx.FONTFAMILY_SCRIPT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_EXTRALIGHT)
        self.text_valores.SetFont(fuente)
        self.text_operaciones.SetFont(fuente)

        #ORDENACION DE LOS SIZERS========================================================
        #===Fila 5=======================================================================
        sub_sizer_bontones_5.Add(b_0)
        sub_sizer_bontones_5.Add(b_dot)
        sub_sizer_bontones_5.Add(b_igual)
        sub_sizer_bontones_5.Add(b_relleno)

        #===Fila 4=======================================================================
        sub_sizer_bontones_4.Add(b_1)
        sub_sizer_bontones_4.Add(b_2)
        sub_sizer_bontones_4.Add(b_3)
        sub_sizer_bontones_4.Add(b_suma)

        #===Fila 3=======================================================================
        sub_sizer_bontones_3.Add(b_4)
        sub_sizer_bontones_3.Add(b_5)
        sub_sizer_bontones_3.Add(b_6)
        sub_sizer_bontones_3.Add(b_resta)

        #==Fila 2========================================================================
        sub_sizer_bontones_2.Add(b_7)
        sub_sizer_bontones_2.Add(b_8)
        sub_sizer_bontones_2.Add(b_9)
        sub_sizer_bontones_2.Add(b_por)

        #==Fila 1========================================================================
        sub_sizer_bontones_1.Add(b_CE)
        sub_sizer_bontones_1.Add(b_C)
        sub_sizer_bontones_1.Add(b_div)
        sub_sizer_bontones_1.Add(b_del)

        #Fila M´s========================================================================
        sizer_M.Add(b_mc)
        sizer_M.Add(b_mr)
        sizer_M.Add(b_mp)
        sizer_M.Add(b_mn)
        sizer_M.Add(b_ms)

        #Texto de resultados=============================================================
        sizer_calculos.Add(self.text_valores)
        sizer_calculos.Add(self.text_operaciones)

        #UNION DE TODOS LOS SIZERS=======================================================
        #===BOTONES======================================================================
        sizer_botones.Add(sub_sizer_bontones_1)
        sizer_botones.Add(sub_sizer_bontones_2)
        sizer_botones.Add(sub_sizer_bontones_3)
        sizer_botones.Add(sub_sizer_bontones_4)
        sizer_botones.Add(sub_sizer_bontones_5)

        #===GENERAL======================================================================
        sizer_general.Add(sizer_calculos, flag=wx.LEFT|wx.RIGHT|wx.TOP, border=3)
        sizer_general.Add(sizer_M, flag=wx.LEFT|wx.RIGHT, border=3)
        sizer_general.Add(sizer_botones, flag=wx.LEFT|wx.RIGHT|wx.BOTTOM, border=10)

        self.SetSizer(sizer_general)

        #EVENTOS=========================================================================
        #==B_NUMEROS=====================================================================
        self.Bind(wx.EVT_BUTTON, self.boton_0, b_0)
        self.Bind(wx.EVT_BUTTON, self.boton_1, b_1)
        self.Bind(wx.EVT_BUTTON, self.boton_2, b_2)
        self.Bind(wx.EVT_BUTTON, self.boton_3, b_3)
        self.Bind(wx.EVT_BUTTON, self.boton_4, b_4)
        self.Bind(wx.EVT_BUTTON, self.boton_5, b_5)
        self.Bind(wx.EVT_BUTTON, self.boton_6, b_6)
        self.Bind(wx.EVT_BUTTON, self.boton_7, b_7)
        self.Bind(wx.EVT_BUTTON, self.boton_8, b_8)
        self.Bind(wx.EVT_BUTTON, self.boton_9, b_9)

        #==B_OPERACIONES=================================================================
        self.Bind(wx.EVT_BUTTON, self.boton_suma, b_suma)
        self.Bind(wx.EVT_BUTTON, self.boton_resta, b_resta)
        self.Bind(wx.EVT_BUTTON, self.boton_multiplicacion, b_por)
        self.Bind(wx.EVT_BUTTON, self.boton_division, b_div)

        self.Bind(wx.EVT_BUTTON, self.boton_igual, b_igual)

        #==B_ESPECIALES==================================================================
        self.Bind(wx.EVT_BUTTON, self.boton_delete, b_del)
        self.Bind(wx.EVT_BUTTON, self.boton_C, b_C)
        self.Bind(wx.EVT_BUTTON, self.boton_CE, b_CE)
        self.Bind(wx.EVT_BUTTON, self.boton_dot, b_dot)

        self.Layout()

    #////////////////////////////////////////////////////////////////////////////////////
    #FUNCION DE BOTONES==================================================================
    #==NUMEROS===========================================================================
    def boton_0(self, evt):
        self.text_valores.AppendText('0')
    
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def boton_1(self, evt):
        self.text_valores.AppendText('1')

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def boton_2(self, evt):
        self.text_valores.AppendText('2')

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def boton_3(self, evt):
        self.text_valores.AppendText('3')

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def boton_4(self, evt):
        self.text_valores.AppendText('4')

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def boton_5(self, evt):
        self.text_valores.AppendText('5')

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def boton_6(self, evt):
        self.text_valores.AppendText('6')

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def boton_7(self, evt):
        self.text_valores.AppendText('7')
    
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def boton_8(self, evt):
        self.text_valores.AppendText('8')

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def boton_9(self, evt):
        self.text_valores.AppendText('9')

    #==OPERACIONES=======================================================================
    def boton_suma(self, evt):
        self.suma = True

        text_cant = str(self.text_valores.GetLineText(0))
        if '.' in text_cant:
            num_cant = float(text_cant)
        else:
            num_cant = int(text_cant)


        self.text_valores.Clear()

        if self.suma and not self.resta and not self.multi and not self.div:

            if self.text_operaciones.IsEmpty():
                self.text_operaciones.AppendText(text_cant)
                self.valor_final = num_cant
            else:
                self.text_operaciones.AppendText(' + ' + text_cant)

                self.valor_final += num_cant

        elif self.resta:

            if self.text_operaciones.IsEmpty():
                self.text_operaciones.AppendText(text_cant)
                self.valor_final = num_cant
            else:
                self.text_operaciones.AppendText(' - ' + text_cant)
                self.valor_final -= num_cant

        elif self.div:

            if self.text_operaciones.IsEmpty():
                self.text_operaciones.AppendText(text_cant)
                self.valor_final = num_cant
            else:
                self.text_operaciones.AppendText(' ÷ ' + text_cant)
                self.valor_final /= num_cant

        elif self.multi:

            if self.text_operaciones.IsEmpty():
                self.text_operaciones.AppendText(text_cant)
                self.valor_final = num_cant
            else:
                self.text_operaciones.AppendText(' x ' + text_cant)    
                self.valor_final *= num_cant

        self.resta = False
        self.multi = False
        self.div = False

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def boton_resta(self, evt):
        self.resta = True
        text_cant = str(self.text_valores.GetLineText(0))
        if '.' in text_cant:
            num_cant = float(text_cant)
        else:
            num_cant = int(text_cant)


        self.text_valores.Clear()  

        if self.resta and not self.suma and not self.multi and not self.div:
            
            if self.text_operaciones.IsEmpty():
                self.text_operaciones.AppendText(text_cant)
                self.valor_final = num_cant
            else:
                self.text_operaciones.AppendText(' - ' + text_cant)
                self.valor_final -= num_cant

        if self.suma:

            if self.text_operaciones.IsEmpty():
                self.text_operaciones.AppendText(text_cant)
                self.valor_final = num_cant
            else:
                self.text_operaciones.AppendText(' + ' + text_cant)
                self.valor_final += num_cant

        if self.multi:
            
            if self.text_operaciones.IsEmpty():
                self.text_operaciones.AppendText(text_cant)
                self.valor_final = num_cant
            else:
                self.text_operaciones.AppendText(' x ' + text_cant)
                self.valor_final *= num_cant

        if self.div:

            if self.text_operaciones.IsEmpty():
                self.text_operaciones.AppendText(text_cant)
                self.valor_final = num_cant
            else:
                self.text_operaciones.AppendText(' ÷ ' + text_cant)
                self.valor_final /= num_cant

        self.suma = False
        self.multi = False
        self.div = False

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def boton_multiplicacion(self, evt):
        self.multi = True
        text_cant = str(self.text_valores.GetLineText(0))
        if '.' in text_cant:
            num_cant = float(text_cant)
        else:
            num_cant = int(text_cant)


        self.text_valores.Clear()


        if self.multi and not self.suma and not self.resta and not self.div:
            
            if self.text_operaciones.IsEmpty():
                self.text_operaciones.AppendText(text_cant)
                self.valor_final = num_cant
            else:
                self.text_operaciones.AppendText(' x ' + text_cant)
                self.valor_final *= num_cant

        elif self.suma:
            
            if self.text_operaciones.IsEmpty():
                self.text_operaciones.AppendText(text_cant)
                self.valor_final = num_cant
            else:
                self.text_operaciones.AppendText(' + ' + text_cant)
                self.valor_final += num_cant

        elif self.resta:
            
            if self.text_operaciones.IsEmpty():
                self.text_operaciones.AppendText(text_cant)
                self.valor_final = num_cant
            else:
                self.text_operaciones.AppendText(' - ' + text_cant)
                self.valor_final -= num_cant

        elif self.div:
            
            if self.text_operaciones.IsEmpty():
                self.text_operaciones.AppendText(text_cant)
                self.valor_final = num_cant
            else:
                self.text_operaciones.AppendText(' ÷ ' + text_cant)
                self.valor_final /= num_cant

        self.suma = False
        self.resta = False
        self.div = False

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def boton_division(self, evt):
        self.div = True
        text_cant = str(self.text_valores.GetLineText(0))
        if '.' in text_cant:
            num_cant = float(text_cant)
        else:
            num_cant = int(text_cant)


        self.text_valores.Clear()
    
        if self.div and not self.suma and not self.resta and not self.multi:
            
            if self.text_operaciones.IsEmpty():
                self.text_operaciones.AppendText(text_cant)
                self.valor_final = num_cant
            else:
                self.text_operaciones.AppendText(' ÷ ' + text_cant)
                self.valor_final /= num_cant

        elif self.suma:
            
            if self.text_operaciones.IsEmpty():
                self.text_operaciones.AppendText(text_cant)
                self.valor_final = num_cant
            else:
                self.text_operaciones.AppendText(' + ' + text_cant)
                self.valor_final += num_cant

        elif self.resta:
            
            if self.text_operaciones.IsEmpty():
                self.text_operaciones.AppendText(text_cant)
                self.valor_final = num_cant
            else:
                self.text_operaciones.AppendText(' - ' + text_cant)
                self.valor_final -= num_cant

        elif self.multi:
            
            if self.text_operaciones.IsEmpty():
                self.text_operaciones.AppendText(text_cant)
                self.valor_final = num_cant
            else:
                self.text_operaciones.AppendText(' x ' + text_cant)
                self.valor_final *= num_cant

        self.suma = False
        self.resta = False
        self.multi = False

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def boton_igual(self, evt):
        if self.suma:
            self.boton_suma(evt)
            self.text_operaciones.AppendText(' = ' + str(self.valor_final))
        elif self.resta:
            self.boton_resta(evt)
            self.text_operaciones.AppendText(' = ' + str(self.valor_final))
        elif self.multi:
            self.boton_multiplicacion(evt)
            self.text_operaciones.AppendText(' = ' + str(self.valor_final))
        if self.div:
            self.boton_division(evt)
            self.text_operaciones.AppendText(' = ' + str(self.valor_final))
      
    #==ESPECIALES========================================================================
    def boton_dot(self, evt):
        self.text_valores.AppendText('.')

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def boton_delete(self, evt):
        self.text_valores.Undo()

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def boton_CE(self, evt):
        self.valor_final = 0
        self.text_operaciones.Clear()
        self.text_valores.Clear()

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def boton_C(self, evt):
        self.text_valores.Clear()
#////////////////////////////////////////////////////////////////////////////////////////
class Memory:
    pass