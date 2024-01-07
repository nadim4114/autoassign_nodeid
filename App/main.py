import wx

from Menu import MainWindow
app = wx.App(False)
frame = MainWindow(None, title='Demo with Notebook')
app.MainLoop()