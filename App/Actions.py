import wx


class ActionPanel(wx.Panel):
    ''' The Form class is a wx.Panel that creates a bunch of controls
        and handlers for callbacks. Doing the layout of the controls is
        the responsibility of subclasses (by means of the doLayout()
        method). '''

    def __init__(self, *args, **kwargs):
        super(ActionPanel, self).__init__(*args, **kwargs)
        self.referrers = ['16 Digital Input', '16 Digital Output', '8 TC', 'Coupler']
        self.createControls()
        self.bindEvents()
        self.doLayout()

    def createControls(self):
        self.logger = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.saveButton = wx.Button(self, label=" Add ")
        self.referrerComboBox = wx.ComboBox(self, choices=self.referrers,
                                            style=wx.CB_DROPDOWN)
        self.insuranceCheckBox = wx.CheckBox(self,
                                             label="Additional options")

    def bindEvents(self):
        for control, event, handler in \
                [(self.saveButton, wx.EVT_BUTTON, self.onSave),
                 (self.referrerComboBox, wx.EVT_COMBOBOX, self.onReferrerEntered),
                 (self.referrerComboBox, wx.EVT_TEXT, self.onReferrerEntered),
                 (self.insuranceCheckBox, wx.EVT_CHECKBOX, self.onInsuranceChanged),]:
            control.Bind(event, handler)

    def doLayout(self):
        ''' Layout the controls that were created by createControls().
            Form.doLayout() will raise a NotImplementedError because it
            is the responsibility of subclasses to layout the controls. '''
        raise NotImplementedError

        # Callback methods:

    def onColorchanged(self, event):
        self.__log('User wants color: %s' % self.colors[event.GetInt()])

    def onReferrerEntered(self, event):
        self.__log('User Added: %s' % event.GetString())

    def onSave(self, event):
        self.__log('User clicked on button with id %d' % event.GetId())

    def onNameEntered(self, event):
        self.__log('User entered name: %s' % event.GetString())

    def onNameChanged(self, event):
        self.__log('User typed character: %d' % event.GetKeyCode())
        event.Skip()

    def onInsuranceChanged(self, event):
        self.__log('Additional options: %s' % event.IsChecked())

    # Helper method(s):

    def __log(self, message):
        ''' Private method to append a string to the logger text
            control. '''
        self.logger.AppendText('%s\n' % message)


class FormWithAbsolutePositioning(ActionPanel):
    def doLayout(self):
        ''' Layout the controls by means of absolute positioning. '''
        for control, x, y, width, height in \
                [(self.logger, 1000, 400, 200, 200),
                 (self.saveButton, 1000, 200, -1, -1),
                 (self.referrerComboBox, 1000, 90, 95, -1),
                 (self.insuranceCheckBox, 1000, 180, -1, -1),]:
            control.SetDimensions(x=x, y=y, width=width, height=height)


class FormWithSizer(ActionPanel):
    def doLayout(self):
        ''' Layout the controls by means of sizers. '''

        # A horizontal BoxSizer will contain the GridSizer (on the left)
        # and the logger text control (on the right):
        boxSizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        # A GridSizer will contain the other controls:
        gridSizer = wx.FlexGridSizer(rows=5, cols=2, vgap=10, hgap=10)

        # Prepare some reusable arguments for calling sizer.Add():
        expandOption = dict(flag=wx.EXPAND)
        noOptions = dict()
        emptySpace = ((0, 0), noOptions)

        # Add the controls to the sizers:
        for control, options in \
                 [(self.saveButton, dict(flag=wx.ALIGN_CENTER)),
                 (self.referrerComboBox, expandOption),
                 emptySpace,
                 (self.insuranceCheckBox, noOptions),]:
            gridSizer.Add(control, **options)

        for control, options in \
                [(gridSizer, dict(border=5, flag=wx.ALL)),
                 (self.logger, dict(border=5, flag=wx.ALL | wx.EXPAND,
                                    proportion=1))]:
            boxSizer.Add(control, **options)

        self.SetSizerAndFit(boxSizer)


class FrameWithForms(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(FrameWithForms, self).__init__(*args, **kwargs)
        notebook = wx.Notebook(self)
        form1 = FormWithAbsolutePositioning(notebook)
        #form2 = FormWithSizer(notebook)
        notebook.AddPage(form1, 'Absolute Positioning')
        #notebook.AddPage(form2, 'Configurator')
        # We just set the frame to the right size manually. This is feasible
        # for the frame since the frame contains just one component. If the
        # frame had contained more than one component, we would use sizers
        # of course, as demonstrated in the FormWithSizer class above.
        self.SetClientSize(notebook.GetBestSize())
        self.Show()


if __name__ == '__main__':
    app = wx.App(0)
    frame = FrameWithForms(None, title='Configurator')
    app.MainLoop()
