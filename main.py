# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import tkinter

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"NoteBook", pos = wx.DefaultPosition, size = wx.Size( 595,399 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        MainSizer = wx.BoxSizer( wx.VERTICAL )

        self.MainText = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.HSCROLL|wx.TE_MULTILINE )
        self.MainText.SetMaxSize( wx.Size( 1600,900 ) )

        MainSizer.Add( self.MainText, 1, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( MainSizer )
        self.Layout()
        self.MenuBar = wx.MenuBar( 0 )
        self.FileMenu = wx.Menu()
        self.MenuItem_New = wx.MenuItem( self.FileMenu, wx.ID_ANY, u"New", wx.EmptyString, wx.ITEM_NORMAL )
        self.FileMenu.Append( self.MenuItem_New )

        self.MenuItem_Open = wx.MenuItem( self.FileMenu, wx.ID_ANY, u"Open", wx.EmptyString, wx.ITEM_NORMAL )
        self.FileMenu.Append( self.MenuItem_Open )

        self.MenuItem_Save = wx.MenuItem( self.FileMenu, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL )
        self.FileMenu.Append( self.MenuItem_Save )

        self.MenuItem_SaveAs = wx.MenuItem( self.FileMenu, wx.ID_ANY, u"Save As", wx.EmptyString, wx.ITEM_NORMAL )
        self.FileMenu.Append( self.MenuItem_SaveAs )

        self.MenuBar.Append( self.FileMenu, u"File" )

        self.EditMenu = wx.Menu()
        self.MenuItem_Settings = wx.MenuItem( self.EditMenu, wx.ID_ANY, u"Settings", wx.EmptyString, wx.ITEM_NORMAL )
        self.EditMenu.Append( self.MenuItem_Settings )

        self.MenuBar.Append( self.EditMenu, u"Edit" )

        self.InfoMenu = wx.Menu()
        self.MenuItem_Creator = wx.MenuItem( self.InfoMenu, wx.ID_ANY, u"Creator", wx.EmptyString, wx.ITEM_NORMAL )
        self.InfoMenu.Append( self.MenuItem_Creator )

        self.MenuBar.Append( self.InfoMenu, u"Info" )

        self.SetMenuBar( self.MenuBar )


        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_MENU, self.MenuItem_New_Func, id = self.MenuItem_New.GetId() )
        self.Bind( wx.EVT_MENU, self.MenuItem_Open_Func, id = self.MenuItem_Open.GetId() )
        self.Bind( wx.EVT_MENU, self.MenuItem_Save_Func, id = self.MenuItem_Save.GetId() )
        self.Bind( wx.EVT_MENU, self.MenuItem_SaveAs_Func, id = self.MenuItem_SaveAs.GetId() )
        self.Bind( wx.EVT_MENU, self.MenuItem_Settings_Func, id = self.MenuItem_Settings.GetId() )
        self.Bind( wx.EVT_MENU, self.MenuItem_Creator_Func, id = self.MenuItem_Creator.GetId() )

        self.file_path = None

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def MenuItem_New_Func( self, event ):
        self.MainText.Clear()
        self.file_path = None

    def MenuItem_Open_Func( self, event ):
        file_dialog = wx.FileDialog(self, "Відкрити файл", "", "", "Текстові файли (*.txt)|*.txt", wx.FD_OPEN | wx.FD_FILE_MUST_EXSIST)

        if file_dialog.ShowModal() == wx.ID_CANCEL:
            file_dialog.Destroy()

        self.file_path = file_dialog.GetPath()

        try:
            with open(self.file_path, "rw") as file:
                content = file.read()
                self.MainText.SetValue(content)
        except IOError:
            wx.MessageBox("Помилка при відкритті файлу.", "Помилка", wx.OK | wx.ICON_ERROR)

        file_dialog.Destroy()

    def MenuItem_Save_Func( self, event ):
        if self.file_path is not None:
            try:
                with open(self.file_path, "w") as file:
                    file.write(self.MainText.GetValue())
                    wx.MessageBox("Текст збережено.")
            except IOError:
                wx.MessageBox("Помилка при збережінні файлу.", "Помилка", wx.OK | wx.ICON_ERROR)
        elif self.file_path is None:
            self.MenuItem_SaveAs_Func(wx.EVT_MENU)

    def MenuItem_SaveAs_Func( self, event ):
        file_dialog = wx.FileDialog(self, "Зберегти файл", "", "", "Текстові файли (*.txt)|*.txt", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if file_dialog.ShowModal() == wx.ID_CANCEL:
            file_dialog.Destroy()

        self.file_path = file_dialog.GetPath()

        try:
            with open(self.file_path, 'w') as file:
                file.write(self.MainText.GetValue())
                wx.MessageBox("Текст збережено.")
        except IOError:
            wx.MessageBox("Помилка при збереженні файлу.", "Помилка", wx.OK | wx.ICON_ERROR)

        file_dialog.Destroy()

    def MenuItem_Settings_Func( self, event ):
        event.Skip()

    def MenuItem_Creator_Func( self, event ):
        event.Skip()



class SettingsFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Settings", pos = wx.DefaultPosition, size = wx.Size( 243,160 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		MainSizer = wx.GridSizer( 0, 2, 0, 0 )

		self.FontSizeLabel = wx.StaticText( self, wx.ID_ANY, u"Font Size", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FontSizeLabel.Wrap( -1 )

		MainSizer.Add( self.FontSizeLabel, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.FontSizeSizer = wx.Slider( self, wx.ID_ANY, 18, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		MainSizer.Add( self.FontSizeSizer, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.FontFamilyLabel = wx.StaticText( self, wx.ID_ANY, u"Font Family", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FontFamilyLabel.Wrap( -1 )

		MainSizer.Add( self.FontFamilyLabel, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.FontPicker3 = wx.FontPickerCtrl( self, wx.ID_ANY, wx.NullFont, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FontPicker3.SetMaxPointSize( 100 )
		MainSizer.Add( self.FontPicker3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.FontColorLabel = wx.StaticText( self, wx.ID_ANY, u"Font Color", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FontColorLabel.Wrap( -1 )

		MainSizer.Add( self.FontColorLabel, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.ColourPicker = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		MainSizer.Add( self.ColourPicker, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.ResetButton = wx.Button( self, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0 )
		MainSizer.Add( self.ResetButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.ApplyButton = wx.Button( self, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		MainSizer.Add( self.ApplyButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( MainSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.ResetButton.Bind( wx.EVT_BUTTON, self.ResetButton_Func )
		self.ApplyButton.Bind( wx.EVT_BUTTON, self.ApplyButton_Func )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def ResetButton_Func( self, event ):
		event.Skip()

	def ApplyButton_Func( self, event ):
		event.Skip()




class MainApp(wx.App):
    def OnInit(self):
        mainFrame = MainFrame(None)
        mainFrame.Show(True)
        return True

if __name__== "__main__":
    app = MainApp()
    app.MainLoop()

