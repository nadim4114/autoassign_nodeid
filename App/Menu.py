




import wx
import os


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(1024, 600))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)

        self.CreateStatusBar()  # Create a status bar in the bottom of the window

        # setting up file menu
        filemenu = wx.Menu()

        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
        menuopen = filemenu.Append(wx.ID_OPEN , item="&Open", helpString="Open a File")
        filemenu.AppendSeparator()
        menusave = filemenu.Append(wx.ID_SAVE , item="&Save", helpString="Save a File")
        filemenu.AppendSeparator()
        menuabout = filemenu.Append(wx.ID_ABOUT, item="&About", helpString="Know about this program")
        filemenu.AppendSeparator()
        menuexit = filemenu.Append(wx.ID_EXIT, item="&Exit", helpString="Exit this program")

        modulemenu = wx.Menu()
        modulemenu.Append(wx.ID_ADD, item="&Add", helpString="Add a Module")
        modulemenu.AppendSeparator()
        modulemenu.Append(wx.ID_REMOVE, item="&Remove", helpString="Remove a Module")

        menubar = wx.MenuBar()
        menubar.Append(filemenu, "&File")  # Adding the "filemenu" to the MenuBar
        menubar.Append(modulemenu, "&Modules") # Adding the "modulemenu" to the MenuBar
        self.SetMenuBar(menubar)  # Adding the MenuBar to the Frame content.

        self.Bind(wx.EVT_MENU, self.OnOpen, menuopen)
        self.Bind(wx.EVT_MENU, self.OnSave, menusave)
        self.Bind(wx.EVT_MENU, self.OnExit, menuexit)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuabout)


        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.buttons = []
        for i in range(0, 6):
            self.buttons.append(wx.Button(self, -1, "Button &"+str(i)))
            self.sizer2.Add(self.buttons[i], 1, wx.EXPAND)

        # Use some sizers to see layout options
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.control, 1, wx.EXPAND)
        self.sizer.Add(self.sizer2, 0, wx.EXPAND)

        #Layout sizers
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)
        self.Show()

        self.Show()

    def OnOpen(self,e):
        # Todo
        """ Open a file"""
        dlg = wx.FileDialog(self, "Choose a file", "", "*.*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()


    def OnSave(self,e):
        # Todo
        pass




    def OnExit(self,e):
        self.Close(True)

    def OnAbout(self,e):
        dlg = wx.MessageDialog(self, "Modules Configurator", "About", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()