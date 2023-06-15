import wx
import wx.xrc
import json
import os
import appdirs
import webbrowser

print("Imported all libraries")

# Class MainFrame


class MainFrame(wx.Frame):

    def __init__(self, parent):

        # loaded settings from json file
        self.settings = load_settings()
        print("Loaded settings")
        print(self.settings)

        # if settings are empty, restorings to default
        if self.settings is None:
            self.settings = {
                "font-size": 11,
                "font-family": "Default",
                "font-color": "ButtonText",
                "language": "English"
            }
            print("Settings is NONE. Loading default settings.")

        # changing labels text to Ukrainian language
        if self.settings["language"] == "Ukrainian":
            self.labels = {
                "New": "Новий файл",
                "Open": "Відкрити",
                "Save": "Зберегти",
                "Save As": "Зберегти як",
                "File": "Файл",
                "Settings": "Налаштування",
                "Edit": "Редагувати",
                "Creator": "Творець",
                "Info": "Інформація",
                "Open File": "Відкрити файл",
                "Text Files": "Текстові файли (*.txt)|*.txt",
                "Error while opening the file": "Помилка при відкритті файлу.",
                "Error": "Помилка",
                "Text has been saved": "Текст збережено.",
                "Error while saving the file": "Помилка при збережінні файлу.",
                "Font Size": "Розмір шрифту",
                "Font Family": "Шрифт",
                "Font Color": "Колір шрифту",
                "Language": "Мова",
                "Reset": "Скинути",
                "Apply": "Застосувати",
                "Save File": "Зберегти файл",
                "Settings have been saved": "Налаштування збережено",
            }
            print("Loaded UKRAINIAN UI.")

        # loading default localization
        else:
            self.labels = {
                "New": "New",
                "Open": "Open",
                "Save": "Save",
                "Save As": "Save As",
                "File": "File",
                "Settings": "Settings",
                "Edit": "Edit",
                "Creator": "Creator",
                "Info": "Info",
                "Open File": "Open File",
                "Text Files": "Text Files (*.txt)|*.txt",
                "Error while opening the file": "Error while opening the file.",
                "Error": "Error",
                "Text has been saved": "Text has been saved.",
                "Error while saving the file": "Error while saving the file.",
                "Font Size": "Font Size",
                "Font Family": "Font Family",
                "Font Color": "Font Color",
                "Language": "Language",
                "Reset": "Reset",
                "Apply": "Apply",
                "Save File": "Save File",
                "Settings have been saved": "Settings have been saved",
            }
            print("Loaded ENGLISH UI.")

        # creating main window

        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"SimpleNoteBook", pos=wx.DefaultPosition,
                          size=wx.Size(595, 399), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        icon = wx.Icon("icon.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)

        MainSizer = wx.BoxSizer(wx.VERTICAL)

        self.MainText = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1),
                                    wx.HSCROLL | wx.TE_MULTILINE)
        self.MainText.SetForegroundColour(self.settings["font-color"])
        self.MainText.SetFont(wx.Font(self.settings["font-family"]))
        font = self.MainText.GetFont()
        font.SetPointSize(self.settings["font-size"])
        self.MainText.SetFont(font)

        self.MainText.SetMaxSize(wx.Size(1600, 900))

        MainSizer.Add(self.MainText, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(MainSizer)
        self.Layout()
        self.MenuBar = wx.MenuBar(0)
        self.FileMenu = wx.Menu()
        self.MenuItem_New = wx.MenuItem(self.FileMenu, wx.ID_ANY, self.labels["New"], wx.EmptyString, wx.ITEM_NORMAL)
        self.FileMenu.Append(self.MenuItem_New)

        self.MenuItem_Open = wx.MenuItem(self.FileMenu, wx.ID_ANY, self.labels["Open"], wx.EmptyString, wx.ITEM_NORMAL)
        self.FileMenu.Append(self.MenuItem_Open)

        self.MenuItem_Save = wx.MenuItem(self.FileMenu, wx.ID_ANY, self.labels["Save"], wx.EmptyString, wx.ITEM_NORMAL)
        self.FileMenu.Append(self.MenuItem_Save)

        self.MenuItem_SaveAs = wx.MenuItem(self.FileMenu, wx.ID_ANY, self.labels["Save As"], wx.EmptyString,
                                           wx.ITEM_NORMAL)
        self.FileMenu.Append(self.MenuItem_SaveAs)

        self.MenuBar.Append(self.FileMenu, self.labels["File"])

        self.EditMenu = wx.Menu()
        self.MenuItem_Settings = wx.MenuItem(self.EditMenu, wx.ID_ANY, self.labels["Settings"], wx.EmptyString,
                                             wx.ITEM_NORMAL)
        self.EditMenu.Append(self.MenuItem_Settings)

        self.MenuBar.Append(self.EditMenu, self.labels["Edit"])

        self.InfoMenu = wx.Menu()
        self.MenuItem_Creator = wx.MenuItem(self.InfoMenu, wx.ID_ANY, self.labels["Creator"], wx.EmptyString,
                                            wx.ITEM_NORMAL)
        self.InfoMenu.Append(self.MenuItem_Creator)

        self.MenuBar.Append(self.InfoMenu, self.labels["Info"])

        self.SetMenuBar(self.MenuBar)

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_MENU, self.MenuItem_New_Func, id=self.MenuItem_New.GetId())
        self.Bind(wx.EVT_MENU, self.MenuItem_Open_Func, id=self.MenuItem_Open.GetId())
        self.Bind(wx.EVT_MENU, self.MenuItem_Save_Func, id=self.MenuItem_Save.GetId())
        self.Bind(wx.EVT_MENU, self.MenuItem_SaveAs_Func, id=self.MenuItem_SaveAs.GetId())
        self.Bind(wx.EVT_MENU, self.MenuItem_Settings_Func, id=self.MenuItem_Settings.GetId())
        self.Bind(wx.EVT_MENU, self.MenuItem_Creator_Func, id=self.MenuItem_Creator.GetId())

        self.file_path = None
        print("Created MainWindow.")

    def __del__(self):
        pass

    # Virtual event handlers
    def MenuItem_New_Func(self, event):
        self.MainText.Clear()
        self.file_path = None
        print("Created new file.")

    def MenuItem_Open_Func(self, event):
        file_dialog = wx.FileDialog(self, self.labels["Open File"], "", "", self.labels["Text Files"],
                                    wx.FD_OPEN)

        if file_dialog.ShowModal() == wx.ID_CANCEL:
            file_dialog.Destroy()
            print("Destroyed file dialog.")

        self.file_path = file_dialog.GetPath()

        try:
            with open(self.file_path, "r") as file:
                content = file.read()
                self.MainText.SetValue(content)
                print("Succesfully open the file.")
        except IOError:
            wx.MessageBox(self.labels["Error while opening the file"], self.labels["Error"], wx.OK | wx.ICON_ERROR)
            print("Got error while opening the file (IOError).")

        file_dialog.Destroy()
        print("Destroyed file dialog.")

    def MenuItem_Save_Func(self, event):
        if self.file_path is not None:
            try:
                with open(self.file_path, "w") as file:
                    file.write(self.MainText.GetValue())
                    wx.MessageBox(self.labels["Text has been saved"])
                    print("Text has been saved.")
            except IOError:
                wx.MessageBox(self.labels["Error while saving the file"], self.labels["Error"], wx.OK | wx.ICON_ERROR)
                print("Got error while saving the file (IOError).")
        elif self.file_path is None:
            print("Path is NONE, so calling MenuItemSaveAs_Func.")
            self.MenuItem_SaveAs_Func(wx.EVT_MENU)

    def MenuItem_SaveAs_Func(self, event):
        file_dialog = wx.FileDialog(self, self.labels["Save File"], "", "", self.labels["Text Files"],
                                    wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if file_dialog.ShowModal() == wx.ID_CANCEL:
            file_dialog.Destroy()
            print("Destroyed file dialog.")

        self.file_path = file_dialog.GetPath()

        try:
            with open(self.file_path, 'w') as file:
                file.write(self.MainText.GetValue())
                wx.MessageBox(self.labels["Text has been saved"])
                print("Text has been saved.")
        except IOError:
            wx.MessageBox(self.labels["Error while saving the file"], self.labels["Error"], wx.OK | wx.ICON_ERROR)
            print("Got error while SavingAs file (IOError).")

        file_dialog.Destroy()
        print("Destroyed file dialog.")

    def MenuItem_Settings_Func(self, event):
        settings_window = SettingsFrame(None)
        settings_window.Show()
        print("Created settings window")

    def MenuItem_Creator_Func(self, event):
        url = "https://instagram.com/error_in_user.name?igshid=MzNlNGNkZWQ4Mg=="
        webbrowser.open(url)


# class SettingsFrame


class SettingsFrame(wx.Frame):

    def __init__(self, parent):

        self.settings = load_settings()
        print("Loaded settings.")
        print(self.settings)

        if self.settings is None:
            self.settings = {
                "font-size": 11,
                "font-family": "Default",
                "font-color": "ButtonText",
                "language": "English"
            }
            print("Settings are Empty. Restoring to default.")

        if self.settings["language"] == "Ukrainian":
            self.labels = {
                "New": "Новий файл",
                "Open": "Відкрити",
                "Save": "Зберегти",
                "Save As": "Зберегти як",
                "File": "Файл",
                "Settings": "Налаштування",
                "Edit": "Редагувати",
                "Creator": "Творець",
                "Info": "Інформація",
                "Open File": "Відкрити файл",
                "Text Files": "Текстові файли (*.txt)|*.txt",
                "Error while opening the file": "Помилка при відкритті файлу.",
                "Error": "Помилка",
                "Text has been saved": "Текст збережено.",
                "Error while saving the file": "Помилка при збережінні файлу.",
                "Font Size": "Розмір шрифту",
                "Font Family": "Шрифт",
                "Font Color": "Колір шрифту",
                "Language": "Мова",
                "Reset": "Скинути",
                "Apply": "Застосувати",
                "Save File": "Зберегти файл",
                "Settings have been saved": "Налаштування збережені. Перезапустіть щоб застосувати.",
            }
            print("Loaded UKRAINIAN UI")
        else:
            self.labels = {
                "New": "New",
                "Open": "Open",
                "Save": "Save",
                "Save As": "Save As",
                "File": "File",
                "Settings": "Settings",
                "Edit": "Редагувати",
                "Creator": "Edit",
                "Info": "Info",
                "Open File": "Open File",
                "Text Files": "Text Files (*.txt)|*.txt",
                "Error while opening the file": "Error while opening the file.",
                "Error": "Error",
                "Text has been saved": "Text has been saved.",
                "Error while saving the file": "Error while saving the file.",
                "Font Size": "Font Size",
                "Font Family": "Font Family",
                "Font Color": "Font Color",
                "Language": "Language",
                "Reset": "Reset",
                "Apply": "Apply",
                "Save File": "Save File",
                "Settings have been saved": "Settings have been saved. Restart to apply.",
            }
            print("Laded ENGLISH UI")

        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=self.labels["Settings"], pos=wx.DefaultPosition,
                          size=wx.Size(253, 249),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        icon = wx.Icon("icon.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)

        MainSizer = wx.GridSizer(0, 2, 0, 0)

        self.FontSizeLabel = wx.StaticText(self, wx.ID_ANY, self.labels["Font Size"], wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.FontSizeLabel.Wrap(-1)

        MainSizer.Add(self.FontSizeLabel, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.FontSizeSpin = wx.SpinCtrl(self, wx.ID_ANY, u"12", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 5,
                                        50, 0)
        MainSizer.Add(self.FontSizeSpin, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.FontFamilyLabel = wx.StaticText(self, wx.ID_ANY, self.labels["Font Family"], wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.FontFamilyLabel.Wrap(-1)

        MainSizer.Add(self.FontFamilyLabel, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.FontPicker3 = wx.FontPickerCtrl(self, wx.ID_ANY, wx.NullFont, wx.DefaultPosition, wx.DefaultSize, 0)
        self.FontPicker3.SetMaxPointSize(100)
        MainSizer.Add(self.FontPicker3, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.FontColorLabel = wx.StaticText(self, wx.ID_ANY, self.labels["Font Color"], wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.FontColorLabel.Wrap(-1)

        MainSizer.Add(self.FontColorLabel, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.ColourPicker = wx.ColourPickerCtrl(self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize,
                                                wx.CLRP_DEFAULT_STYLE)
        MainSizer.Add(self.ColourPicker, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.LanguageChoiceLabel = wx.StaticText(self, wx.ID_ANY, self.labels["Language"], wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
        self.LanguageChoiceLabel.Wrap(-1)

        MainSizer.Add(self.LanguageChoiceLabel, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        LanguageChoiceChoices = ["English", "Ukrainian"]
        self.LanguageChoice = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, LanguageChoiceChoices, 0)
        self.LanguageChoice.SetSelection(0)
        MainSizer.Add(self.LanguageChoice, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.ResetButton = wx.Button(self, wx.ID_ANY, self.labels["Reset"], wx.DefaultPosition, wx.DefaultSize, 0)
        MainSizer.Add(self.ResetButton, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.ApplyButton = wx.Button(self, wx.ID_ANY, self.labels["Apply"], wx.DefaultPosition, wx.DefaultSize, 0)
        MainSizer.Add(self.ApplyButton, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.ResetButton.Bind(wx.EVT_BUTTON, self.ResetButton_Func)
        self.ApplyButton.Bind(wx.EVT_BUTTON, self.ApplyButton_Func)
        print("Created settings window.")

        self.FontSizeSpin.SetValue(self.settings["font-size"])
        self.FontPicker3.SetFont(wx.Font(self.settings["font-family"]))
        self.ColourPicker.SetColour(self.settings["font-color"])
        self.LanguageChoice.SetStringSelection(self.settings["language"])

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def ResetButton_Func(self, event):
        self.settings = {
            "font-size": 11,
            "font-family": "Default",
            "font-color": "ButtonText",
            "language": "English"
        }

        print("Reseted settings to default.")
        save_settings(self.settings)
        print("Settings have been saved.")
        print(self.settings)
        wx.MessageBox(self.labels["Settings have been saved"])

    def ApplyButton_Func(self, event):

        selected_font = self.FontPicker3.GetSelectedFont()
        font_face = selected_font.GetFaceName()

        selected_color = self.ColourPicker.GetColour()
        color_string = selected_color.GetAsString(wx.C2S_HTML_SYNTAX)

        settings = {
            "font-size": int(self.FontSizeSpin.GetValue()),
            "font-family": font_face,
            "font-color": color_string,
            "language": self.LanguageChoice.GetStringSelection()
        }
        save_settings(settings)
        print("Settings saved.")
        print(settings)
        wx.MessageBox(self.labels["Settings have been saved"])


def save_settings(settings):
    # Отримати шлях до теці AppData
    appdata_dir = appdirs.user_data_dir("SimpleNoteBook", "JustErorr")
    os.makedirs(appdata_dir, exist_ok=True)

    # Створити шлях до файлу налаштувань
    settings_file = os.path.join(appdata_dir, "settings.json")

    # Зберегти налаштування у JSON-файлі
    with open(settings_file, "w") as file:
        json.dump(settings, file)


def load_settings():
    # Отримати шлях до теці AppData
    appdata_dir = appdirs.user_data_dir("SimpleNoteBook", "JustErorr")

    # Створити шлях до файлу налаштувань
    settings_file = os.path.join(appdata_dir, "settings.json")

    # Перевірити, чи файл існує
    if os.path.exists(settings_file):
        # Завантажити налаштування з JSON-файлу
        with open(settings_file, "r") as file:
            settings = json.load(file)
            return settings

    # Повернути пусті налаштування, якщо файл не існує
    return None


# creating MainApp class


class MainApp(wx.App):
    def OnInit(self):
        mainFrame = MainFrame(None)
        mainFrame.Show(True)
        return True

# launching app


if __name__ == "__main__":
    app = MainApp()
    app.MainLoop()
