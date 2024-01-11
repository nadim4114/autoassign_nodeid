import wx
from Actions import *




from FileMenu import *

app = wx.App(False)
frame = MainWindow(None, title='Module Config')
app.MainLoop()