import os
import wx
import wx.xrc
import img2pdf

class MainFrame ( wx.Frame ):
        def __init__( self, parent ):
                wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PicToPdf", pos = wx.DefaultPosition, size = wx.Size( 360,315 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

                #ico = wx.IconBundle()
                #ico.AddIcon("icon.ico", wx.BITMAP_TYPE_ANY)
                #self.SetIcons(ico)
                
                self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
                self.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

                bSizer1 = wx.BoxSizer( wx.VERTICAL )

                self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Choose the folder with the images:", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText1.Wrap( -1 )

                self.m_staticText1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Segoe Print" ) )
                self.m_staticText1.SetForegroundColour( wx.Colour( 0, 255, 0 ) )

                bSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

                self.m_dirPicker1 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Choose the folder", wx.DefaultPosition, wx.Size( 330,30 ), wx.DIRP_DEFAULT_STYLE)
                picker1_label = self.m_dirPicker1.GetPickerCtrl()
                picker1_label.SetLabel("Browse")
                bSizer1.Add( self.m_dirPicker1, 0, wx.ALL, 5 )

                self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Choose the folder of the save path:", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText3.Wrap( -1 )

                self.m_staticText3.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Segoe Print" ) )
                self.m_staticText3.SetForegroundColour( wx.Colour( 0, 255, 0 ) )

                bSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )

                self.m_dirPicker2 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Choose the folder", wx.DefaultPosition, wx.Size( 330,-1 ), wx.DIRP_DEFAULT_STYLE)
                picker2_label = self.m_dirPicker2.GetPickerCtrl()
                picker2_label.SetLabel("Browse")
                bSizer1.Add( self.m_dirPicker2, 0, wx.ALL, 5 )

                self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Write here the name of the PDF file:", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText2.Wrap( -1 )

                self.m_staticText2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Segoe Print" ) )
                self.m_staticText2.SetForegroundColour( wx.Colour( 0, 255, 0 ) )

                bSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )

                bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

                self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
                bSizer2.Add( self.m_textCtrl4, 0, wx.ALL, 5 )

                self.m_button4 = wx.Button( self, wx.ID_ANY, u"Convert", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
                self.m_button4.Bind(wx.EVT_BUTTON, self.OnClicked, self.m_button4)
                bSizer2.Add( self.m_button4, 0, wx.ALL, 5 )
                
                bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

                bSizer3 = wx.BoxSizer( wx.VERTICAL )

                self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Made by: PrhckSpc", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText8.Wrap( -1 )

                self.m_staticText8.SetForegroundColour( wx.Colour( 0, 255, 0 ) )

                bSizer3.Add( self.m_staticText8, 0, wx.ALL, 5 )

                self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"https://github.com/prhckspc", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText9.Wrap( -1 )

                self.m_staticText9.SetForegroundColour( wx.Colour( 0, 255, 0 ) )

                bSizer3.Add( self.m_staticText9, 0, wx.ALL, 5 )

                bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )

                self.SetSizer( bSizer1 )
                self.Layout()

                self.Centre( wx.BOTH )
        def OnClicked( self, event ):
                btn = event.GetEventObject().GetLabelText()
                img_source = self.m_dirPicker1.GetPath()
                pdf_destination = self.m_dirPicker2.GetPath()
                pdf_name = self.m_textCtrl4.GetValue()
                if (str(btn)=="Konvertálás"):
                 self.Convert( img_source, pdf_destination, pdf_name)
                 
        def Convert( self, img_source, pdf_destination, pdf_name ):
               imgs = []
               for fname in os.listdir(img_source):
                       print(fname)
                       if not fname.endswith((".jpg",".png",".tiff")):
                               continue
                       path = os.path.join(img_source, fname)
                       if os.path.isdir(path):
                               continue
                       imgs.append(path)
               with open(pdf_destination+"\\"+pdf_name+".pdf", "wb") as f:
                       f.write(img2pdf.convert(imgs))        
        
        def __del__( self ):
                pass


def main():

    app = wx.App()
    ex = MainFrame(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
