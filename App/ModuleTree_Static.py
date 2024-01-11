# Sample_one_a.py

"""

"""

import wx

from wx.tools.dbg import Logger



# class MyFrame
# class MyApp

# ---------------------------------------------------------------------------

class ModuleTreeFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title,
                          wx.DefaultPosition, wx.Size(800, 680))

        #self.SetIcon(wx.Icon('./icons/wxwin.ico', wx.BITMAP_TYPE_ICO))

        # ------------
        self.window_1 = wx.SplitterWindow(self, wx.ID_ANY, style=wx.SP_3D | wx.SP_BORDER)
        panel1 = wx.Panel(self.window_1)
        panel2 = wx.Panel(self.window_1)
        #panel3 = wx.Panel(self, -1, style=wx.WANTS_CHARS)
        panel2.SetBackgroundColour('#c4c4c4')

        # ------------

        self.tree = wx.TreeCtrl(panel1, 1,
                                wx.DefaultPosition,
                                wx.DefaultSize,
                                wx.TR_LINES_AT_ROOT |
                                wx.TR_TWIST_BUTTONS |
                                wx.TR_HAS_BUTTONS)
        self.tree.SetBackgroundColour('#cce8ff')

        root = self.tree.AddRoot('PLC')

        mtcp = self.tree.AppendItem(root, 'Modbus TCP coupler')
        can = self.tree.AppendItem(root, 'CAN coupler')
        mbus = self.tree.AppendItem(root, 'Modbus 485 coupler')

        m1 = self.tree.AppendItem(mtcp, 'DI 16 Module')
        m2 = self.tree.AppendItem(mtcp, 'DI 16 Module')
        m3 = self.tree.AppendItem(mtcp, 'DO 16 Module')
        m4 = self.tree.AppendItem(mtcp, 'DO 16 Module')
        m5 = self.tree.AppendItem(mtcp, 'Thermocouple 8 Jtype Module')
        m6 = self.tree.AppendItem(mtcp, 'DO 16 Module')

        c1 = self.tree.AppendItem(can, 'Thermocouple 8 Jtype Module')
        c2 = self.tree.AppendItem(can, 'Thermocouple 8 Jtype Module')


        self.tree.AppendItem(mbus, 'DI 16 Module')
        self.tree.AppendItem(mbus, 'DI 16 Module')
        self.tree.AppendItem(mbus, 'DI 16 Module')


        self.tree.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged, self.tree)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

        # ------------

        self.display = wx.StaticText(panel2, -1, '', (10, 10), style=wx.ALIGN_CENTRE)

        # ------------

        hbox = wx.BoxSizer(wx.VERTICAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        vbox.Add(self.tree, 1, wx.EXPAND)

        self.window_1.SplitVertically(panel1, panel2)
        hbox.Add(self.window_1, 1, wx.EXPAND, 0)
        #hbox.Add(self.window_1, 1, wx.EXPAND)
        #hbox.Add(panel2, 1, wx.EXPAND)
        #hbox.Add(panel3, 1, wx.EXPAND)

        self.SetSizer(hbox)
        hbox.Fit(self)

        #self.SetSizer(hbox)

        # ------------

        self.Layout()

    # -----------------------------------------------------------------------

    def OnSelChanged(self, event):
        self.item = event.GetItem()
        #print(self.item)
        self.display.SetLabel(self.tree.GetItemText(self.item))
        self.tree.GetItemText(self.item)

        event.Skip()

    def OnCloseWindow(self, event):
        self.Destroy()


# ---------------------------------------------------------------------------



class MyApp(wx.App):
    def OnInit(self):
        frame = ModuleTreeFrame(None, -1, 'Module Configurator')
        frame.Show(True)
        self.SetTopWindow(frame)

        return True


# ---------------------------------------------------------------------------

#if __name__ == '__main__':
app = MyApp(0)
app.MainLoop()
dbg = Logger()
dbg('something to print')
dbg(enable=1)