"""
Demonstrates how to get controls and a Dialog to size correctly when
attaching custom controls using AttachUnknownControl().
"""
from wx import *
from wx.xrc import *
import os
class Dialog(wx.DialogPtr):
        def __init__(self, parent, resource):
                w = resource.LoadDialog(parent, 'Dialog')
                wxDialogPtr.__init__(self, w.this)
                self.thisown = 1
                self.Center()
                ctrlTable = [
                        ('ID_CUSTOM_CTRL', 'Ctrl 1'),
                        ('ID_CUSTOM_CTRL_WIDTH_SPECIFIED', 'Ctrl 2'),
                ]
                sizer = self.GetSizer()
                sizer.SetVirtualSizeHints(self)
                self.SetAutoLayout(True)
                for idText, lable in ctrlTable:
                        id = XRCID(idText)
                        idCtrl = wxNewId()
                        ctrl = wxButton(self, idCtrl, lable)
                        if ctrl is not None:
                                resource.AttachUnknownControl(idText, ctrl, self)
                                EVT_BUTTON(self, id, self.OnButton)
                                size = ctrl.GetSize()
                                print (size)
                                sizeBest = ctrl.GetBestSize()
                                print (sizeBest)
                                sizeBest.width = size.width
                                container = ctrl.GetParent()
                                sizer.SetItemMinSize(container,
                                        sizeBest.width, sizeBest.height)
                sizeMin = sizer.CalcMin()
                self.SetSizeHints(sizeMin.width, sizeMin.height)
                sizer.Fit(self)
                EVT_BUTTON(self, XRCID("ID_OK"), self.OnOk)
                EVT_BUTTON(self, XRCID("ID_CANCEL"), self.OnCancel)
        def OnButton(self, event):
                print ('OnButton')
        def OnCancel(self, event):
                self.EndModal(wxID_CANCEL)
        def OnOk(self, event):
                self.EndModal(wxID_OK)
def testPreferencesDialog():
        class MyApp(wxApp):
                def __init__(self, num):
                        wxApp.__init__(self, num)
                def OnInit(self):
                        RESFILE_DIALOGS = "SizeXrc.xrc"
                        import types
                        wxInitAllImageHandlers()
                        resourceText = open(RESFILE_DIALOGS).read()
                        resource = wxEmptyXmlResource()
                        resource.LoadFromString(resourceText)
                        dialog = Dialog(None, resource)
                        dialog.ShowModal()
                        dialog.Destroy()
                        return True
        app = MyApp(0)
#----------------------------------------------------------------------------
if __name__ == '__main__':
        testPreferencesDialog()