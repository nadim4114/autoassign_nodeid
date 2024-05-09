import wx
class Menubar:

    def __init__(self, frame):
        self.frame = frame

    def CreateMenu(self):
        menu = wx.MenuBar()

        file_menu = wx.Menu()
        file_menu.Append(wx.ID_FILE, "New")
        file_menu.Append(wx.ID_EXIT, "Exit")

        view_menu = wx.Menu()
        view_menu.Append(wx.ID_EDIT, "Format")
        view_menu.Append(wx.ID_VIEW_LIST, "List")

        menu.Append(file_menu,"&File")
        menu.Append(view_menu,"&View")
        self.frame.SetMenuBar(menu)

        
