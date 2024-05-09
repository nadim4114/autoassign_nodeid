import wx
from m_frame import AuiFrame as mainwindow
from m_gauge import ProgressGauge
from m_menubar import Menus
#from test_menu import Menubar

if __name__ == '__main__':
    val = None
    app = wx.App()
    frame = mainwindow(None, log=val)

    menu = Menus(frame)
    menu.CreateMenuBar()

    
    frame.Show()
    app.MainLoop()