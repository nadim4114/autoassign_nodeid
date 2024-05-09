import wx
import wx.aui
import string

class NewFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)

        Menubar = wx.MenuBar()

        File_menu = wx.Menu()
        File_item1 = File_menu.Append(wx.ID_ANY, "&Open", "Open a file")
        self.Bind(wx.EVT_MENU, self.OnOpen, File_item1)
        File_item2 = File_menu.Append(wx.ID_ANY, "&Close", "CLose a file")
        self.Bind(wx.EVT_MENU, self.OnClose, File_item2)

        Menubar.Append(File_menu, "&File")

        Edit_menu = wx.Menu()
        Edit_item1 = Edit_menu.Append(wx.ID_ANY, "&Undo", "Undo changes")
        self.Bind(wx.EVT_MENU, self.OnOpen, Edit_item1)
        Edit_menu.Append(wx.ID_ANY, "&Redo", "Redo changes")
        Menubar.Append(Edit_menu, "&Edit")

        Info_menu = wx.Menu()
        Info_menu.Append(wx.ID_ANY, "&About", "About menu")
        Menubar.Append(Info_menu, "&About")

        self.SetMenuBar(Menubar)

        self.Show()


    def OnOpen(self, event):

        print("item2")

    def OnClose(self, event):


        print("item")

app = wx.App()
frame = NewFrame(None, wx.ID_ANY, "My app")
app.MainLoop()