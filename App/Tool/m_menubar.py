import wx

ID_CreateTree = wx.ID_HIGHEST + 1
ID_CreateGrid = ID_CreateTree + 1
ID_CreateText = ID_CreateTree + 2
ID_CreateHTML = ID_CreateTree + 3
ID_CreateNotebook = ID_CreateTree + 4
ID_CreateSizeReport = ID_CreateTree + 5
ID_GridContent = ID_CreateTree + 6
ID_TextContent = ID_CreateTree + 7
ID_TreeContent = ID_CreateTree + 8
ID_HTMLContent = ID_CreateTree + 9
ID_NotebookContent = ID_CreateTree + 10
ID_SizeReportContent = ID_CreateTree + 11
ID_SwitchPane = ID_CreateTree + 12
ID_CreatePerspective = ID_CreateTree + 13
ID_CopyPerspectiveCode = ID_CreateTree + 14
ID_CreateNBPerspective = ID_CreateTree + 15
ID_CopyNBPerspectiveCode = ID_CreateTree + 16
ID_AllowFloating = ID_CreateTree + 17
ID_AllowActivePane = ID_CreateTree + 18
ID_TransparentHint = ID_CreateTree + 19
ID_VenetianBlindsHint = ID_CreateTree + 20
ID_RectangleHint = ID_CreateTree + 21
ID_NoHint = ID_CreateTree + 22
ID_HintFade = ID_CreateTree + 23
ID_NoVenetianFade = ID_CreateTree + 24
ID_TransparentDrag = ID_CreateTree + 25
ID_NoGradient = ID_CreateTree + 26
ID_VerticalGradient = ID_CreateTree + 27
ID_HorizontalGradient = ID_CreateTree + 28
ID_LiveUpdate = ID_CreateTree + 29
ID_AnimateFrames = ID_CreateTree + 30
ID_PaneIcons = ID_CreateTree + 31
ID_TransparentPane = ID_CreateTree + 32
ID_DefaultDockArt = ID_CreateTree + 33
ID_ModernDockArt = ID_CreateTree + 34
ID_SnapToScreen = ID_CreateTree + 35
ID_SnapPanes = ID_CreateTree + 36
ID_FlyOut = ID_CreateTree + 37
ID_CustomPaneButtons = ID_CreateTree + 38
ID_Settings = ID_CreateTree + 39
ID_CustomizeToolbar = ID_CreateTree + 40
ID_DropDownToolbarItem = ID_CreateTree + 41
ID_MinimizePosSmart = ID_CreateTree + 42
ID_MinimizePosTop = ID_CreateTree + 43
ID_MinimizePosLeft = ID_CreateTree + 44
ID_MinimizePosRight = ID_CreateTree + 45
ID_MinimizePosBottom = ID_CreateTree + 46
ID_MinimizeCaptSmart = ID_CreateTree + 47
ID_MinimizeCaptHorz = ID_CreateTree + 48
ID_MinimizeCaptHide = ID_CreateTree + 49
ID_NotebookNoCloseButton = ID_CreateTree + 50
ID_NotebookCloseButton = ID_CreateTree + 51
ID_NotebookCloseButtonAll = ID_CreateTree + 52
ID_NotebookCloseButtonActive = ID_CreateTree + 53
ID_NotebookCloseOnLeft = ID_CreateTree + 54
ID_NotebookAllowTabMove = ID_CreateTree + 55
ID_NotebookAllowTabExternalMove = ID_CreateTree + 56
ID_NotebookAllowTabSplit = ID_CreateTree + 57
ID_NotebookTabFloat = ID_CreateTree + 58
ID_NotebookTabDrawDnd = ID_CreateTree + 59
ID_NotebookDclickUnsplit = ID_CreateTree + 60
ID_NotebookWindowList = ID_CreateTree + 61
ID_NotebookScrollButtons = ID_CreateTree + 62
ID_NotebookTabFixedWidth = ID_CreateTree + 63
ID_NotebookArtGloss = ID_CreateTree + 64
ID_NotebookArtSimple = ID_CreateTree + 65
ID_NotebookArtVC71 = ID_CreateTree + 66
ID_NotebookArtFF2 = ID_CreateTree + 67
ID_NotebookArtVC8 = ID_CreateTree + 68
ID_NotebookArtChrome = ID_CreateTree + 69
ID_NotebookAlignTop = ID_CreateTree + 70
ID_NotebookAlignBottom = ID_CreateTree + 71
ID_NotebookHideSingle = ID_CreateTree + 72
ID_NotebookSmartTab = ID_CreateTree + 73
ID_NotebookUseImagesDropDown = ID_CreateTree + 74
ID_NotebookCustomButtons = ID_CreateTree + 75
ID_NotebookMinMaxWidth = ID_CreateTree + 76

ID_SampleItem = ID_CreateTree + 77
ID_StandardGuides = ID_CreateTree + 78
ID_AeroGuides = ID_CreateTree + 79
ID_WhidbeyGuides = ID_CreateTree + 80
ID_NotebookPreview = ID_CreateTree + 81
ID_PreviewMinimized = ID_CreateTree + 82

ID_SmoothDocking = ID_CreateTree + 83
ID_NativeMiniframes = ID_CreateTree + 84

ID_FirstPerspective = ID_CreatePerspective + 1000
ID_FirstNBPerspective = ID_CreateNBPerspective + 10000

ID_PaneBorderSize = ID_SampleItem + 100
ID_SashSize = ID_PaneBorderSize + 2
ID_CaptionSize = ID_PaneBorderSize + 3
ID_BackgroundColour = ID_PaneBorderSize + 4
ID_SashColour = ID_PaneBorderSize + 5
ID_InactiveCaptionColour = ID_PaneBorderSize + 6
ID_InactiveCaptionGradientColour = ID_PaneBorderSize + 7
ID_InactiveCaptionTextColour = ID_PaneBorderSize + 8
ID_ActiveCaptionColour = ID_PaneBorderSize + 9
ID_ActiveCaptionGradientColour = ID_PaneBorderSize + 10
ID_ActiveCaptionTextColour = ID_PaneBorderSize + 11
ID_BorderColour = ID_PaneBorderSize + 12
ID_GripperColour = ID_PaneBorderSize + 13
ID_SashGrip = ID_PaneBorderSize + 14
ID_HintColour = ID_PaneBorderSize + 15

ID_VetoTree = ID_PaneBorderSize + 16
ID_VetoText = ID_PaneBorderSize + 17
ID_NotebookMultiLine = ID_PaneBorderSize + 18


class Menus:
    def __init__(self,frame):
        self.frame = frame
    
    def CreateMenuBar(self):

            # create menu
            mb = wx.MenuBar()

            file_menu = wx.Menu()
            file_menu.Append(wx.ID_EXIT, "Exit")

            view_menu = wx.Menu()
            view_menu.Append(ID_CreateText, "Create Text Control")
            view_menu.Append(ID_CreateHTML, "Create HTML Control")
            view_menu.Append(ID_CreateTree, "Create Tree")
            view_menu.Append(ID_CreateGrid, "Create Grid")
            view_menu.Append(ID_CreateNotebook, "Create Notebook")
            view_menu.Append(ID_CreateSizeReport, "Create Size Reporter")
            view_menu.AppendSeparator()
            view_menu.Append(ID_GridContent, "Use a Grid for the Content Pane")
            view_menu.Append(ID_TextContent, "Use a Text Control for the Content Pane")
            view_menu.Append(ID_HTMLContent, "Use an HTML Control for the Content Pane")
            view_menu.Append(ID_TreeContent, "Use a Tree Control for the Content Pane")
            view_menu.Append(ID_NotebookContent, "Use a AuiNotebook control for the Content Pane")
            view_menu.Append(ID_SizeReportContent, "Use a Size Reporter for the Content Pane")
            view_menu.AppendSeparator()

    ##        if wx.Platform == "__WXMAC__":
    ##            switcherAccel = "Alt+Tab"
    ##        elif wx.Platform == "__WXGTK__":
    ##            switcherAccel = "Ctrl+/"
    ##        else:
    ##            switcherAccel = "Ctrl+Tab"
    ##
    ##        view_menu.Append(ID_SwitchPane, _("S&witch Window...") + "\t" + switcherAccel)

            options_menu = wx.Menu()
            options_menu.AppendRadioItem(ID_TransparentHint, "Transparent Hint")
            options_menu.AppendRadioItem(ID_VenetianBlindsHint, "Venetian Blinds Hint")
            options_menu.AppendRadioItem(ID_RectangleHint, "Rectangle Hint")
            options_menu.AppendRadioItem(ID_NoHint, "No Hint")
            options_menu.AppendSeparator()
            options_menu.AppendCheckItem(ID_HintFade, "Hint Fade-in")
            options_menu.AppendCheckItem(ID_AllowFloating, "Allow Floating")
            options_menu.AppendCheckItem(ID_NoVenetianFade, "Disable Venetian Blinds Hint Fade-in")
            options_menu.AppendCheckItem(ID_TransparentDrag, "Transparent Drag")
            options_menu.AppendCheckItem(ID_AllowActivePane, "Allow Active Pane")
            options_menu.AppendCheckItem(ID_LiveUpdate, "Live Resize Update")
            options_menu.AppendCheckItem(ID_NativeMiniframes, "Use Native wx.MiniFrames")
            options_menu.AppendSeparator()
            options_menu.AppendRadioItem(ID_MinimizePosSmart, "Minimize in Smart mode").Check()
            options_menu.AppendRadioItem(ID_MinimizePosTop, "Minimize on Top")
            options_menu.AppendRadioItem(ID_MinimizePosLeft, "Minimize on the Left")
            options_menu.AppendRadioItem(ID_MinimizePosRight, "Minimize on the Right")
            options_menu.AppendRadioItem(ID_MinimizePosBottom, "Minimize at the Bottom")
            options_menu.AppendSeparator()
            options_menu.AppendRadioItem(ID_MinimizeCaptSmart, "Smart Minimized Caption")
            options_menu.AppendRadioItem(ID_MinimizeCaptHorz, "Horizontal Minimized Caption")
            options_menu.AppendRadioItem(ID_MinimizeCaptHide, "Hidden Minimized Caption").Check()
            options_menu.AppendSeparator()
            options_menu.AppendCheckItem(ID_PaneIcons, "Set Icons On Panes")
            options_menu.AppendCheckItem(ID_AnimateFrames, "Animate Dock/Close/Minimize Of Floating Panes")
            options_menu.AppendCheckItem(ID_SmoothDocking, "Smooth Docking Effects (PyQT Style)")
            options_menu.AppendSeparator()
            options_menu.Append(ID_TransparentPane, "Set Floating Panes Transparency")
            options_menu.AppendSeparator()
            options_menu.AppendRadioItem(ID_DefaultDockArt, "Default DockArt")
            options_menu.AppendRadioItem(ID_ModernDockArt, "Modern Dock Art")
            options_menu.AppendSeparator()
            options_menu.Append(ID_SnapToScreen, "Snap To Screen")
            options_menu.AppendCheckItem(ID_SnapPanes, "Snap Panes To Managed Window")
            options_menu.AppendCheckItem(ID_FlyOut, "Use Fly-Out Floating Panes")
            options_menu.AppendSeparator()
            options_menu.AppendCheckItem(ID_CustomPaneButtons, "Set Custom Pane Button Bitmaps")
            options_menu.AppendSeparator()
            options_menu.AppendRadioItem(ID_NoGradient, "No Caption Gradient")
            options_menu.AppendRadioItem(ID_VerticalGradient, "Vertical Caption Gradient")
            options_menu.AppendRadioItem(ID_HorizontalGradient, "Horizontal Caption Gradient")
            options_menu.AppendSeparator()
            options_menu.AppendCheckItem(ID_PreviewMinimized, "Preview Minimized Panes")
            options_menu.AppendSeparator()
            options_menu.Append(ID_Settings, "Settings Pane")

            notebook_menu = wx.Menu()
            notebook_menu.AppendRadioItem(ID_NotebookArtGloss, "Glossy Theme (Default)")
            notebook_menu.AppendRadioItem(ID_NotebookArtSimple, "Simple Theme")
            notebook_menu.AppendRadioItem(ID_NotebookArtVC71, "VC71 Theme")
            notebook_menu.AppendRadioItem(ID_NotebookArtFF2, "Firefox 2 Theme")
            notebook_menu.AppendRadioItem(ID_NotebookArtVC8, "VC8 Theme")
            notebook_menu.AppendRadioItem(ID_NotebookArtChrome, "Chrome Theme")
            notebook_menu.AppendSeparator()
            notebook_menu.AppendRadioItem(ID_NotebookNoCloseButton, "No Close Button")
            notebook_menu.AppendRadioItem(ID_NotebookCloseButton, "Close Button At Right")
            notebook_menu.AppendRadioItem(ID_NotebookCloseButtonAll, "Close Button On All Tabs")
            notebook_menu.AppendRadioItem(ID_NotebookCloseButtonActive, "Close Button On Active Tab")
            notebook_menu.AppendSeparator()
            notebook_menu.AppendCheckItem(ID_NotebookCloseOnLeft, "Close Button On The Left Of Tabs")
            notebook_menu.AppendSeparator()
            notebook_menu.AppendRadioItem(ID_NotebookAlignTop, "Tab Top Alignment")
            notebook_menu.AppendRadioItem(ID_NotebookAlignBottom, "Tab Bottom Alignment")
            notebook_menu.AppendSeparator()
            notebook_menu.AppendCheckItem(ID_NotebookAllowTabMove, "Allow Tab Move")
            notebook_menu.AppendCheckItem(ID_NotebookAllowTabExternalMove, "Allow External Tab Move")
            notebook_menu.AppendCheckItem(ID_NotebookAllowTabSplit, "Allow Notebook Split")
            notebook_menu.AppendCheckItem(ID_NotebookTabFloat, "Allow Single Tab Floating")
            notebook_menu.AppendSeparator()
            notebook_menu.AppendCheckItem(ID_NotebookDclickUnsplit, "Unsplit On Sash Double-Click")
            notebook_menu.AppendCheckItem(ID_NotebookTabDrawDnd, "Draw Tab Image On Drag 'n' Drop")
            notebook_menu.AppendSeparator()
            notebook_menu.AppendCheckItem(ID_NotebookScrollButtons, "Scroll Buttons Visible")
            notebook_menu.AppendCheckItem(ID_NotebookWindowList, "Window List Button Visible")
            notebook_menu.AppendCheckItem(ID_NotebookTabFixedWidth, "Fixed-Width Tabs")
            notebook_menu.AppendSeparator()
            notebook_menu.AppendCheckItem(ID_NotebookHideSingle, "Hide On Single Tab")
            notebook_menu.AppendCheckItem(ID_NotebookSmartTab, "Use Smart Tabbing")
            notebook_menu.AppendCheckItem(ID_NotebookUseImagesDropDown, "Use Tab Images In Dropdown Menu")
            notebook_menu.AppendCheckItem(ID_NotebookCustomButtons, "Show Custom Buttons In Tab Area")
            notebook_menu.AppendSeparator()
            notebook_menu.Append(ID_NotebookMinMaxWidth, "Set Min/Max Tab Widths")
            notebook_menu.Append(ID_NotebookMultiLine, "Add A Multi-Line Label Tab")
            notebook_menu.AppendSeparator()
            notebook_menu.Append(ID_NotebookPreview, "Preview Of All Notebook Pages")

            guides_menu = wx.Menu()
            guides_menu.AppendRadioItem(ID_StandardGuides, "Standard Docking Guides")
            guides_menu.AppendRadioItem(ID_AeroGuides, "Aero-Style Docking Guides")
            guides_menu.AppendRadioItem(ID_WhidbeyGuides, "Whidbey-Style Docking Guides")


            action_menu = wx.Menu()
            action_menu.AppendCheckItem(ID_VetoTree, "Veto Floating Of Tree Pane")
            action_menu.AppendCheckItem(ID_VetoText, "Veto Docking Of Fixed Pane")
            action_menu.AppendSeparator()

            attention_menu = wx.Menu()

            self.frame._requestPanes = {}
            for indx, pane in enumerate(self.frame._mgr.GetAllPanes()):
                if pane.IsToolbar():
                    continue
                if not pane.caption or not pane.name:
                    continue
                ids = wx.ID_HIGHEST + 12345 + indx
                self.frame._requestPanes[ids] = pane.name
                attention_menu.Append(ids, pane.caption)

            action_menu.Append(wx.ID_ANY, "Request User Attention For", attention_menu)

            help_menu = wx.Menu()
            help_menu.Append(wx.ID_ABOUT, "About...")

            mb.Append(file_menu, "&File")
            mb.Append(view_menu, "&View")
            
            mb.Append(options_menu, "&Options")
            mb.Append(notebook_menu, "&Notebook")
            mb.Append(action_menu, "&Actions")
            mb.Append(help_menu, "&Help")

            self.frame.SetMenuBar(mb)