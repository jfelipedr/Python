#!/usr/bin/env python

"""GUI_wxPython.py is a starting point for a wxPython program."""

import wx

class Frame(wx.Frame):
    pass

class App(wx.App):
    """Application class."""

    def OnInit(self):
        self.frame = Frame(parent=None, title='Ventana de Ejemplo')
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

def main():
    app = App()
    app.MainLoop()

if __name__=="__main__":
    main()
