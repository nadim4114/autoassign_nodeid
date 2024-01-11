import wx
import wx.aui


class Mywin(wx.Frame):

    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title=title, size=(800, 600))

        self.mgr = wx.aui.AuiManager(self)

        lpnl = wx.Panel(self)

        info1 = wx.aui.AuiPaneInfo()
        info1.Right()
        info1.BestSize(300,300)
        info1.MinSize(100, 300)
        info1.PinButton()
        info1.MaximizeButton()
        info1.MinimizeButton()
        info1.Caption("Actions")
        info1.CaptionVisible(True)


        Rpanel = wx.Panel(self)

        info2 = wx.aui.AuiPaneInfo()
        info2.Left()
        info2.BestSize(300,300)
        info2.MinSize(100, 300)
        info2.PinButton()
        info2.MaximizeButton()
        info2.MinimizeButton()
        info2.Caption("Module Tree")
        info2.CaptionVisible(True)

        Cpanel = wx.Panel(self)

        info3 = wx.aui.AuiPaneInfo()
        info3.Centre()
        info3.BestSize(300,300)
        info3.MinSize(100, 300)
        info3.PinButton()
        info3.MaximizeButton()
        info3.MinimizeButton()
        info3.Caption("Details")
        info3.CaptionVisible(True)

        Bpanel = wx.Panel(self)

        info4 = wx.aui.AuiPaneInfo()
        info4.Bottom()
        info4.BestSize(300,300)
        #info4.MinSize(100, 300)
        info4.PinButton()
        info4.MaximizeButton()
        info4.MinimizeButton()
        info4.Caption("Console")
        info4.CaptionVisible(True)

        self.mgr.AddPane(lpnl, info1)

        self.mgr.AddPane(Rpanel, info2)
        self.mgr.AddPane(Cpanel, info3)
        self.mgr.AddPane(Bpanel, info4)

        self.mgr.Update()
        #self.Bind(wx.EVT_CLOSE, OnClose)
        self.Centre()
        self.Show(True)

        referrers = ['16 Digital Input', '16 Digital Output', '8 TC', 'Coupler']
        logger = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY)
        AddButton = wx.Button(self, label=" Add ")
        DelButton = wx.Button(self, label=" Delete ")
        ComboBox = wx.ComboBox(self, choices=referrers,style=wx.CB_DROPDOWN)
        CheckBox = wx.CheckBox(self,label="Additional options")

        info5 = wx.aui.AuiPaneInfo()
        self.mgr.AddPane(AddButton, wx.aui.AuiPaneInfo().Left().Caption("Add Button"))
        self.mgr.Update()

'''        for control, options in \
                [(gridSizer, dict(border=5, flag=wx.ALL)),
                 (self.logger, dict(border=5, flag=wx.ALL | wx.EXPAND,
                                    proportion=1))]:
            #boxSizer.Add(control, **options)
        # self.SetSizerAndFit(boxSizer)

            self.mgr.AddPane(control, **options)
        self.mgr.Update()
'''
def onColorchanged(self, event):
    self.__log('User wants color: %s' % self.colors[event.GetInt()])


def onSelected(self, event):
    self.__log('User Selected: %s' % event.GetString())


def onAdd(self, event):
    self.__log('User Added Module %d' % event.GetId())


def onDel(self, event):
    self.__log('User Deleted Module %d' % event.GetId())


def onNameEntered(self, event):
    self.__log('User entered name: %s' % event.GetString())


def onNameChanged(self, event):
    self.__log('User typed character: %d' % event.GetKeyCode())
    event.Skip()


def onCheckbox(self, event):
    self.__log('Additional options: %s' % event.IsChecked())


def __log(self, message):
    ''' Private method to append a string to the logger text
        control. '''
    self.logger.AppendText('%s\n' % message)

    def OnClose(self, event):
        self.mgr.UnInit()
        self.Destroy()

app = wx.App()
Mywin(None, "Dock Demo")
app.MainLoop()