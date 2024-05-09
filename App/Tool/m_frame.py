#!/usr/bin/env python

import wx
import wx.html
import wx.grid

import os
import sys
import time

from wx.lib.embeddedimage import PyEmbeddedImage

try:
    dirName = os.path.dirname(os.path.abspath(__file__))
except:
    dirName = os.path.dirname(os.path.abspath(sys.argv[0]))

sys.path.append(os.path.split(dirName)[0])

#try:
#    from agw import aui
#    from agw.aui import aui_switcherdialog as ASD
#except ImportError: # if it's not there locally, try the wxPython lib.
import wx.lib.agw.aui as aui
from wx.lib.agw.aui import aui_switcherdialog as ASD

import random
import images

ArtIDs = [ "wx.ART_ADD_BOOKMARK",
           "wx.ART_DEL_BOOKMARK",
           "wx.ART_HELP_SIDE_PANEL",
           "wx.ART_HELP_SETTINGS",
           "wx.ART_HELP_BOOK",
           "wx.ART_HELP_FOLDER",
           "wx.ART_HELP_PAGE",
           "wx.ART_GO_BACK",
           "wx.ART_GO_FORWARD",
           "wx.ART_GO_UP",
           "wx.ART_GO_DOWN",
           "wx.ART_GO_TO_PARENT",
           "wx.ART_GO_HOME",
           "wx.ART_FILE_OPEN",
           "wx.ART_PRINT",
           "wx.ART_HELP",
           "wx.ART_TIP",
           "wx.ART_REPORT_VIEW",
           "wx.ART_LIST_VIEW",
           "wx.ART_NEW_DIR",
           "wx.ART_HARDDISK",
           "wx.ART_FLOPPY",
           "wx.ART_CDROM",
           "wx.ART_REMOVABLE",
           "wx.ART_FOLDER",
           "wx.ART_FOLDER_OPEN",
           "wx.ART_GO_DIR_UP",
           "wx.ART_EXECUTABLE_FILE",
           "wx.ART_NORMAL_FILE",
           "wx.ART_TICK_MARK",
           "wx.ART_CROSS_MARK",
           "wx.ART_ERROR",
           "wx.ART_QUESTION",
           "wx.ART_WARNING",
           "wx.ART_INFORMATION",
           "wx.ART_MISSING_IMAGE",
           ]


# -- SizeReportCtrl --
# (a utility control that always reports it's client size)

class AuiFrame(wx.Frame):

    def __init__(self, parent, id=wx.ID_ANY, title="", pos= wx.DefaultPosition,
                 size=(1920,1200), style=wx.DEFAULT_FRAME_STYLE|wx.SUNKEN_BORDER, log=None):

        wx.Frame.__init__(self, parent, id, title, pos, size, style)

        self._mgr = aui.AuiManager()

        # tell AuiManager to manage this frame
        self._mgr.SetManagedWindow(self)

        # set frame icon
        self.SetIcon(images.Mondrian.GetIcon())

        # set up default notebook style
        self._notebook_style = aui.AUI_NB_DEFAULT_STYLE | aui.AUI_NB_TAB_EXTERNAL_MOVE | wx.NO_BORDER
        self._notebook_theme = 0
        # Attributes
        self._textCount = 1
        self._transparency = 255
        self._snapped = False
        self._custom_pane_buttons = False
        self._custom_tab_buttons = False
        self._pane_icons = False
        self._veto_tree = self._veto_text = False

        self.log = log

        self.CreateStatusBar()
        self.GetStatusBar().SetStatusText("Ready")

        #self.BuildPanes()
        #self.CreateMenuBar()
        #self.BindEvents()