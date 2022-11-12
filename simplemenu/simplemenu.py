#!/usr/bin/env python3

#### v 0.8

from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os, time
from shutil import which as sh_which
from cfg import *
sys.path.append("modules")
from pop_menu import getMenu


# width and height of the program
WINW = 0
WINH = 0

# the size of the current screen
screen_w = 0
screen_h = 0

# program position
sx = 0
sy = 0

PROG_DIR = os.getcwd()

#### main application categories
Development = []
Education = []
Game = []
Graphics = []
Multimedia = []
Network = []
Office = []
Settings = []
System = []
Utility = []
Other = []

# the dirs of the application files
app_dirs_user = [os.path.expanduser("~")+"/.local/share/applications"]
app_dirs_system = ["/usr/share/applications", "/usr/local/share/applications"]


def f_on_pop_menu(el):
    # category
    cat = el[1]
    if cat == "Multimedia":
        # label - executable - icon - comment - path - terminal - file full path
        Multimedia.append([el[0],el[2],el[3],el[4],el[5],el[6],el[7]])
    elif cat == "Development":
        Development.append([el[0],el[2],el[3],el[4],el[5],el[6],el[7]])
    elif cat == "Education":
        Education.append([el[0],el[2],el[3],el[4],el[5],el[6],el[7]])
    elif cat == "Game":
        Game.append([el[0],el[2],el[3],el[4],el[5],el[6],el[7]])
    elif cat == "Graphics":
        Graphics.append([el[0],el[2],el[3],el[4],el[5],el[6],el[7]])
    elif cat == "Network":
        Network.append([el[0],el[2],el[3],el[4],el[5],el[6],el[7]])
    elif cat == "Office":
        Office.append([el[0],el[2],el[3],el[4],el[5],el[6],el[7]])
    elif cat == "Settings":
        Settings.append([el[0],el[2],el[3],el[4],el[5],el[6],el[7]])
    elif cat == "System":
        System.append([el[0],el[2],el[3],el[4],el[5],el[6],el[7]])
    elif cat == "Utility":
        Utility.append([el[0],el[2],el[3],el[4],el[5],el[6],el[7]])
    else:
        Other.append([el[0],el[2],el[3],el[4],el[5],el[6],el[7]])

# populate the menu
def on_pop_menu(app_dirs_user, app_dirs_system):
    #
    global Development
    Development = []
    global Education
    Education = []
    global Game
    Game = []
    global Graphics
    Graphics = []
    global Multimedia
    Multimedia = []
    global Network
    Network = []
    global Office
    Office = []
    global Settings
    Settings = []
    global System
    System = []
    global Utility
    Utility = []
    global Other
    Other = []
    #
    if int(MENU_FROM_FILE) == 0:
        menu = getMenu(app_dirs_user, app_dirs_system).retList()
        for el in menu:
            f_on_pop_menu(el)
        return
    elif int(MENU_FROM_FILE) == 1:
        menu_tmp = []
        menu = []
        try:
            ffile = open(os.path.join(PROG_DIR, "menu_list.txt"), "r")
            tt = ffile.readline()
            while tt:
                if tt == "#####\n":
                    menu.append(menu_tmp)
                    menu_tmp = []
                else:
                    if tt.strip("\n") == "True":
                        tt = True
                    elif tt.strip("\n") == "False":
                        tt = False
                    else:
                        tt2 = tt.strip("\n")
                    menu_tmp.append(tt2)
                tt = ffile.readline()
            ffile.close()
        except:
            pass
        #
        for el in menu:
            f_on_pop_menu(el)
    
if not os.path.exists(os.path.join(PROG_DIR, "menu_list.txt")):
    import subprocess
    subprocess.check_call(os.path.join(PROG_DIR, "createmenu.sh"), shell=True)

on_pop_menu(app_dirs_user, app_dirs_system)

#############

# type - message - parent
class MyDialog(QtWidgets.QMessageBox):
    def __init__(self, *args):
        super(MyDialog, self).__init__(args[-1])
        if args[0] == "Info":
            self.setIcon(QtWidgets.QMessageBox.Information)
            self.setStandardButtons(QtWidgets.QMessageBox.Ok)
        elif args[0] == "Error":
            self.setIcon(QtWidgets.QMessageBox.Critical)
            self.setStandardButtons(QtWidgets.QMessageBox.Ok)
        elif args[0] == "Question":
            self.setIcon(QtWidgets.QMessageBox.Question)
            self.setStandardButtons(QtWidgets.QMessageBox.Ok|QtWidgets.QMessageBox.Cancel)
        self.setWindowIcon(QtGui.QIcon("icons/file-manager-red.svg"))
        self.setWindowTitle(args[0])
        self.resize(DIALOGWIDTH,100)
        self.setText(args[1])
        retval = self.exec_()
    
    def event(self, e):
        result = QtWidgets.QMessageBox.event(self, e)
        #
        self.setMinimumHeight(0)
        self.setMaximumHeight(16777215)
        self.setMinimumWidth(0)
        self.setMaximumWidth(16777215)
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        # 
        return result


# menu
class menuWin(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(menuWin, self).__init__(parent)
        #
        self.setWindowIcon(QtGui.QIcon("icons/menu.png"))
        self.setWindowTitle("Simplemenu")
        #
        if win_no_deco:
            self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        if win_on_top:
            self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        ####### 
        self.mainBox = QtWidgets.QHBoxLayout()
        self.setLayout(self.mainBox)
        #
        sw = menu_width
        sh = 200
        self.setGeometry(0,0,sw,sh)
        #
        self.hbox = QtWidgets.QHBoxLayout()
        # 
        if with_compositor:
            self.frame=QtWidgets.QFrame(self)
            self.frame.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            self.mainBox.addWidget(self.frame)
            self.frame.setStyleSheet("background: palette(window); border-radius:{}px".format(border_radius))
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            self.mainBox.setContentsMargins(blur_effect,blur_effect,blur_effect,blur_effect)
            shadow_effect = QtWidgets.QGraphicsDropShadowEffect(
                    blurRadius=blur_radius,
                    offset=QtCore.QPointF(0, 0)
                )
            self.setGraphicsEffect(shadow_effect)
            #
            self.frame.setLayout(self.hbox)
        else:
            self.mainBox.setContentsMargins(2,2,2,2)
            self.mainBox.addLayout(self.hbox)
        
        ##### left box
        self.lbox = QtWidgets.QVBoxLayout()
        self.lbox.setContentsMargins(0,0,0,0)
        self.hbox.addLayout(self.lbox)
        #
        self.listWidget = QtWidgets.QListWidget(self)
        self.listWidget.itemClicked.connect(self.listwidgetclicked)
        self.lbox.addWidget(self.listWidget)
        hpalette = self.palette().highlight().color().name()
        csaa = ("QListWidget::item:hover {")
        csab = ("background-color: {};".format(hpalette))
        csac = ("}")
        csa = csaa+csab+csac
        self.listWidget.setStyleSheet(csa)
        ###########
        cssa = ("QScrollBar:vertical {"
    "border: 0px solid #999999;"
    "background:white;"
    "width:8px;"
    "margin: 0px 0px 0px 0px;"
"}"
"QScrollBar::handle:vertical {")       
        cssb = ("min-height: 0px;"
    "border: 0px solid red;"
    "border-radius: 4px;"
    "background-color: {};".format(scroll_handle_col))
        cssc = ("}"
"QScrollBar::add-line:vertical {"       
    "height: 0px;"
    "subcontrol-position: bottom;"
    "subcontrol-origin: margin;"
"}"
"QScrollBar::sub-line:vertical {"
    "height: 0 px;"
    "subcontrol-position: top;"
    "subcontrol-origin: margin;"
"}")
        css = cssa+cssb+cssc
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.verticalScrollBar().setStyleSheet(css)
        ###########
        self.line_edit = QtWidgets.QLineEdit("")
        self.line_edit.setFrame(True)
        if search_field_bg:
            if with_compositor:
                # self.line_edit.setStyleSheet("color: black; background-color: white")
                self.line_edit.setStyleSheet("padding: 4px; border-radius: 6px; background-color: {}".format(search_field_bg))
            else:
                self.line_edit.setStyleSheet("background-color: {}".format(search_field_bg))
        self.line_edit.textChanged.connect(self.on_line_edit)
        self.line_edit.setClearButtonEnabled(True)
        self.lbox.addWidget(self.line_edit)
        # self.line_edit.setFocus(True)
        self.listWidget.setFocus(True)
        self.listWidget.setIconSize(QtCore.QSize(menu_app_icon_size, menu_app_icon_size))
        ##### right box
        self.rbox = QtWidgets.QVBoxLayout()
        self.rbox.setContentsMargins(0,0,0,0)
        self.hbox.addLayout(self.rbox)
        #############
        self.fake_btn = QtWidgets.QPushButton()
        self.fake_btn.setCheckable(True)
        self.fake_btn.setAutoExclusive(True)
        self.rbox.addWidget(self.fake_btn)
        self.fake_btn.hide()
        #
        self.pref = QtWidgets.QPushButton("Bookmarks")
        self.pref.setIcon(QtGui.QIcon("icons/bookmark.svg"))
        self.pref.setIconSize(QtCore.QSize(menu_icon_size, menu_icon_size))
        self.pref.setFlat(True)
        #
        hpalette = self.palette().mid().color().name()
        if with_compositor:
            csaa = ("QPushButton::hover:!pressed { border: none;")
            csab = ("background-color: {};".format(hpalette))
            csac = ("border-radius: 10px;")
            csad = ("text-align: left; }")
            csae = ("QPushButton { text-align: left;  padding: 5px;}")
            csaf = ("QPushButton::checked { text-align: left; ")
            csag = ("background-color: {};".format(self.palette().midlight().color().name()))
            csah = ("padding: 5px; border-radius: 10px;}")
            csa = csaa+csab+csac+csad+csae+csaf+csag+csah
        else:
            csaa = ("QPushButton::hover:!pressed { border: none;")
            csab = ("background-color: {};".format(hpalette))
            csac = ("border-radius: 3px;")
            csad = ("text-align: left; }")
            csae = ("QPushButton { text-align: left;  padding: 5px;}")
            csaf = ("QPushButton::checked { text-align: left; ")
            csag = ("background-color: {};".format(self.palette().midlight().color().name()))
            csah = ("padding: 5px; border-radius: 3px;}")
            csa = csaa+csab+csac+csad+csae+csaf+csag+csah
        self.pref.setStyleSheet(csa)
        #
        self.pref.setCheckable(True)
        self.pref.setAutoExclusive(True)
        self.pref.clicked.connect(self.on_pref_clicked)
        self.rbox.addWidget(self.pref)
        #############
        sepLine = QtWidgets.QFrame()
        sepLine.setFrameShape(QtWidgets.QFrame.HLine)
        sepLine.setFrameShadow(QtWidgets.QFrame.Plain)
        self.rbox.addWidget(sepLine)
        #
        self.rboxBtn = QtWidgets.QVBoxLayout()
        self.rboxBtn.setContentsMargins(0,0,0,0)
        self.rbox.addLayout(self.rboxBtn)
        #
        self.populate_menu()
        #
        self.rbox.addStretch(1)
        #
        ##### buttons
        self.btn_box = QtWidgets.QHBoxLayout()
        self.rbox.addLayout(self.btn_box)
        ## add custom applications
        if app_prog:
            self.menu_btn = QtWidgets.QPushButton()
            self.menu_btn.setIcon(QtGui.QIcon("icons/menu.png"))
            self.menu_btn.setIconSize(QtCore.QSize(service_icon_size, service_icon_size))
            self.menu_btn.setFlat(False)
            #
            if with_compositor:
                self.menu_btn.setFlat(True)
                self.menu_btn.setStyleSheet("padding: 2px; border: 1px solid {}; border-radius: 8px;".format(service_border_color))
            self.menu_btn.clicked.connect(self.f_appWin)
            self.btn_box.addWidget(self.menu_btn)
        ## exit from the program
        self.quit_btn = QtWidgets.QPushButton()
        self.quit_btn.setIcon(QtGui.QIcon("icons/close.svg"))
        self.quit_btn.setIconSize(QtCore.QSize(service_icon_size, service_icon_size))
        self.quit_btn.setFlat(False)
        #
        if with_compositor:
            self.quit_btn.setFlat(True)
            self.quit_btn.setStyleSheet("padding: 2px; border: 1px solid {}; border-radius: 8px;".format(service_border_color))
        self.quit_btn.clicked.connect(self.close)
        self.btn_box.addWidget(self.quit_btn)
        ###
        self.show()
        ###
        if win_position == "center":
            win_width = self.size().width()
            hgap = int((screen_w-win_width)/2)
            win_height = self.size().height()
            vgap = int((screen_h-win_height)/2)
            self.move(hgap, vgap)
        else:
            sx, sy = win_position.split("/")
            self.move(int(sx), int(sy))
        #
        self.emulate_clicked(self.pref, 100)
        self.pref.setChecked(True)
        #
        if item_highlight_color:
            ics = "QListWidget:item::hover:!pressed { "+"background-color: {}".format(item_highlight_color)+";}"
            self.listWidget.setStyleSheet(ics)
        self.listWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listWidget.customContextMenuRequested.connect(self.itemClicked)
        # the bookmark button has been pressed
        self.itemBookmark = 1
        # while an item is been searching
        self.itemSearching = 0
        
        
    #
    def f_appWin(self):
        os.system("{} &".format(app_prog))
        self.close()
    
    # button category clicked
    def itemClicked(self, QPos):
        self.itemSearching = 0
        item_idx = self.listWidget.indexAt(QPos)
        _item = self.listWidget.itemFromIndex(item_idx)
        if _item == None:
            self.listWidget.clearSelection()
            self.listWidget.clearFocus()
            return
        if self.itemBookmark:
            self.listItemRightClickedToRemove(QPos)
        else:
            self.listItemRightClicked(QPos)
    
    def emulate_clicked(self, button, ms):
        QtCore.QTimer.singleShot(ms, button.clicked.emit)
    
    #
    def on_line_edit(self, text):
        self.listWidget.clear()
        self.fake_btn.setChecked(True)
        self.search_program(text)
        
    
    # seeking in the program lists
    def search_program(self, text):
        self.itemBookmark = 0
        self.itemSearching = 1
        if len(text) == 0:
            self.listWidget.clear()
            # self.emulate_clicked(self.pref, 100)
            # self.pref.setChecked(True)
        elif len(text) > 2:
            self.listWidget.clear()
            app_list = ["Development", "Education","Game",
                        "Graphics", "Multimedia", "Network",
                        "Office","Settings","System","Utility", "Other"]
            #
            for ell in app_list:
                if globals()[ell] == []:
                    continue
                for el in globals()[ell]:
                    if (text.casefold() in el[1].casefold()) or (text.casefold() in el[3].casefold()):
                        exe_path = sh_which(el[1].split(" ")[0])
                        # file_info = QtCore.QFileInfo(exe_path)
                        if exe_path:
                            # search for the icon by executable
                            icon = QtGui.QIcon.fromTheme(el[1])
                            if icon.isNull() or icon.name() == "":
                                # set the icon by desktop file - not full path
                                icon = QtGui.QIcon.fromTheme(el[2])
                                if icon.isNull() or icon.name() == "":
                                    # set the icon by desktop file - full path
                                    if os.path.exists(el[2]):
                                        icon = QtGui.QIcon(el[2])
                                        if icon.isNull():
                                            # set a generic icon
                                            icon = QtGui.QIcon("icons/none.svg")
                                            litem = QtWidgets.QListWidgetItem(icon, el[0])
                                            litem.picon = "none"
                                        else:
                                            litem = QtWidgets.QListWidgetItem(icon, el[0])
                                            litem.picon = el[2]
                                    else:
                                        # set a generic icon
                                        icon = QtGui.QIcon("icons/none.svg")
                                        litem = QtWidgets.QListWidgetItem(icon, el[0])
                                        litem.picon = "none"
                                else:
                                    litem = QtWidgets.QListWidgetItem(icon, el[0])
                                    litem.picon = icon.name()
                            else:
                                litem = QtWidgets.QListWidgetItem(icon, el[0])
                                litem.picon = el[1]
                            
                            # set the exec name as property
                            litem.exec_n = el[1]
                            litem.ppath = el[4]
                            litem.setToolTip(el[3])
                            litem.tterm = el[5]
                            litem.fpath = el[6]
                            self.listWidget.addItem(litem)
                            #
                    self.listWidget.scrollToTop()
        else:
            self.listWidget.clear()
    
    # populate the main categories
    def populate_menu(self):
        # remove all widgets
        for i in reversed(range(self.rboxBtn.count())): 
            self.rboxBtn.itemAt(i).widget().deleteLater()
        #
        app_list = ["Development", "Education","Game",
                    "Graphics", "Multimedia", "Network",
                    "Office","Settings","System","Utility","Other"]
        for el in app_list:
            if globals()[el] == []:
                continue
            btn = QtWidgets.QPushButton(el)
            btn.setIcon(QtGui.QIcon("icons/{}".format(el+".svg")))
            btn.setIconSize(QtCore.QSize(menu_icon_size, menu_icon_size))
            btn.setFlat(True)
            ##########
            hpalette = self.palette().mid().color().name()
            if with_compositor:
                csaa = ("QPushButton::hover:!pressed { border: none;")
                csab = ("background-color: {};".format(hpalette))
                csac = ("border-radius: 10px;")
                csad = ("text-align: left; }")
                csae = ("QPushButton { text-align: left;  padding: 5px;}")
                csaf = ("QPushButton::checked { text-align: left; ")
                csag = ("background-color: {};".format(self.palette().midlight().color().name()))
                csah = ("padding: 5px; border-radius: 10px;}")
                csa = csaa+csab+csac+csad+csae+csaf+csag+csah
            else:
                csaa = ("QPushButton::hover:!pressed { border: none;")
                csab = ("background-color: {};".format(hpalette))
                csac = ("border-radius: 3px;")
                csad = ("text-align: left; }")
                csae = ("QPushButton { text-align: left;  padding: 5px;}")
                csaf = ("QPushButton::checked { text-align: left; ")
                csag = ("background-color: {};".format(self.palette().midlight().color().name()))
                csah = ("padding: 5px; border-radius: 3px;}")
                csa = csaa+csab+csac+csad+csae+csaf+csag+csah
            btn.setStyleSheet(csa)
            ##########
            btn.setCheckable(True)
            btn.setAutoExclusive(True)
            self.rboxBtn.addWidget(btn)
            btn.clicked.connect(self.on_btn_clicked)
            
    
    # category button clicked - populate the selected category
    def on_btn_clicked(self):
        # clear the search field
        if self.line_edit.text():
            self.line_edit.disconnect()
            self.line_edit.clear()
            self.line_edit.setClearButtonEnabled(False)
            self.line_edit.setClearButtonEnabled(True)
            self.line_edit.textChanged.connect(self.on_line_edit)
            self.itemSearching = 0
        #
        self.itemBookmark = 0
        cat_name = self.sender().text()
        # remove the ampersand eventually added by alien programs
        if "&" in cat_name:
            cat_name = cat_name.strip("&")
        #
        cat_list = globals()[cat_name]
        self.listWidget.clear()
        #
        for el in cat_list:
            # 0 name - 1 executable - 2 icon - 3 comment - 4 path
            exe_path = 1
            if not SHOW_ALL_PROG:
                exe_path = sh_which(el[1].split(" ")[0])
            # file_info = QtCore.QFileInfo(exe_path)
            #
            if exe_path:
                # search for the icon by executable
                icon = QtGui.QIcon.fromTheme(el[1])
                if icon.isNull() or icon.name() == "":
                    # set the icon by desktop file - not full path
                    icon = QtGui.QIcon.fromTheme(el[2])
                    if icon.isNull() or icon.name() == "":
                        # set the icon by desktop file - full path
                        if os.path.exists(el[2]):
                            icon = QtGui.QIcon(el[2])
                            if icon.isNull():
                                # set a generic icon
                                icon = QtGui.QIcon("icons/none.svg")
                                litem = QtWidgets.QListWidgetItem(icon, el[0])
                                litem.picon = "none"
                            else:
                                litem = QtWidgets.QListWidgetItem(icon, el[0])
                                litem.picon = el[2]
                        else:
                            # set a generic icon
                            icon = QtGui.QIcon("icons/none.svg")
                            litem = QtWidgets.QListWidgetItem(icon, el[0])
                            litem.picon = "none"
                    else:
                        litem = QtWidgets.QListWidgetItem(icon, el[0])
                        litem.picon = icon.name()
                else:
                    litem = QtWidgets.QListWidgetItem(icon, el[0])
                    litem.picon = el[1]
                
                # set the exec name as property
                litem.exec_n = el[1]
                litem.ppath = el[4]
                litem.setToolTip(el[3])
                litem.tterm = el[5]
                litem.fpath = el[6]
                self.listWidget.addItem(litem)
                #
        self.listWidget.scrollToTop()
        self.listWidget.setFocus(True)
        
    
    # add the bookmark after right click
    def listItemRightClicked(self, QPos):
        # check if a bookmark is already present
        item_idx = self.listWidget.indexAt(QPos)
        _item = self.listWidget.itemFromIndex(item_idx)
        pret = self.check_bookmarks(_item)
        #
        self.listMenu= QtWidgets.QMenu()
        if pret == 1:
            item_b = self.listMenu.addAction("Add to bookmark")
        if app_mod_prog:
            item_d = self.listMenu.addAction("Modify")
        else:
            item_d = "None"
        action = self.listMenu.exec_(self.listWidget.mapToGlobal(QPos))
        if pret == 1 and action == item_b:
            item_idx = self.listWidget.indexAt(QPos)
            _item = self.listWidget.itemFromIndex(item_idx)
            if _item == None:
                return
            # 
            new_book = str(int(time.time()))
            icon_name = _item.picon
            # ICON - NAME - EXEC - TOOLTIP - PATH - TERMINAL
            new_book_content = """{0}
{1}
{2}
{3}
{4}
{5}""".format(icon_name, _item.text(), _item.exec_n, _item.toolTip() or _item.text(), _item.ppath, str(_item.tterm))
            with open(os.path.join("bookmarks", new_book), "w") as fbook:
                fbook.write(new_book_content)
        # modify action
        elif action == item_d:
            item_idx = self.listWidget.indexAt(QPos)
            _item = self.listWidget.itemFromIndex(item_idx)
            # item desktop file full path
            item_fpath = _item.fpath
            os.system("{} {} &".format(app_prog, item_fpath))
        #
        self.listWidget.clearSelection()
        self.listWidget.clearFocus()
        self.listWidget.setFocus(True)
        #
        self.close()
    
    # check whether the bookmark already exists
    def check_bookmarks(self, _item):
        is_found = 0
        if _item == None:
            return 1
        list_prog = os.listdir("bookmarks")
        if not list_prog:
            return 1
        for el in list_prog:
            cnt = []
            file_to_read = os.path.join("bookmarks", el)
            with open(file_to_read, "r") as f:
                cnt = f.readlines()
            #
            if cnt[2].strip("\n") == _item.exec_n:
                is_found = 1
        #
        if is_found:
            return 3
        else:
            return 1
    
    # execute the program from the menu
    def listwidgetclicked(self, item):
        if item.tterm:
            tterminal = None
            if USER_TERMINAL:
                tterminal = USER_TERMINAL
            else:
                try:
                    tterminal = os.environ['TERMINAL']
                except KeyError:
                    pass
            #
            if not tterminal or not sh_which(tterminal):
                MyDialog("Error", "Terminal not found or not setted.", self)
                return
            else:
                try:
                    os.system("cd {} && {} -e {} & cd {}".format(str(item.ppath), tterminal, str(item.exec_n), os.getenv("HOME")))
                except Exception as E:
                    MyDialog("Error", "Terminal error: {}.".format(str(E)), self)
        else:
            if not sh_which(item.exec_n):
                MyDialog("Info", "Command not found:\n{}".format(item.exec_n), self)
            else:
                if item.ppath:
                    os.system("cd {} && {} & cd {} &".format(str(item.ppath), str(item.exec_n), os.getenv("HOME")))
                else:
                    os.system("cd {} && {} &".format(os.getenv("HOME"), str(item.exec_n)))
            # close the menu window
            self.close()
        
    # the bookmark button - populate
    def on_pref_clicked(self):
        # clear the search field
        if self.line_edit.text():
            self.line_edit.clear()
            self.itemSearching = 0
        #
        self.itemBookmark = 1
        self.listWidget.clear()
        # self.line_edit.clear()
        bookmark_files = os.listdir("bookmarks")
        prog_list = []
        for bb in bookmark_files:
            with open(os.path.join("bookmarks",bb), "r") as fbook:
                cnt = fbook.readlines()
                # add the filename
                cnt.append(bb)
                prog_list.append(cnt)
        # populate listWidget
        # ICON - NAME - EXEC - TOOLTIP - PATH - TERMINAL
        for el in prog_list:
            ICON = el[0].strip("\n")
            NAME = el[1].strip("\n")
            EXEC = el[2].strip("\n")
            TOOLTIP = el[3].strip("\n")
            PATH = el[4].strip("\n")
            TTERM = el[5].strip("\n")
            FILENAME = el[6].strip("\n")
            #
            exe_path = sh_which(EXEC.split(" ")[0])
            file_info = QtCore.QFileInfo(exe_path)
            if file_info.exists():
                # if os.path.exists(ICON):
                    # icon = QtGui.QIcon(ICON)
                # else:
                    # icon = QtGui.QIcon.fromTheme(ICON)
                    # if icon.name() == "none":
                        # icon = QtGui.QIcon("icons/none.svg")
                icon = QtGui.QIcon.fromTheme(ICON, QtGui.QIcon("icons/none.svg"))
                litem = QtWidgets.QListWidgetItem(icon, NAME)
                litem.exec_n = EXEC
                litem.setToolTip(TOOLTIP)
                litem.file_name = FILENAME
                litem.ppath = PATH
                if TTERM == "True":
                    litem.tterm = True
                else:
                    litem.tterm = False
                self.listWidget.addItem(litem)
                #
        self.listWidget.sortItems(QtCore.Qt.AscendingOrder)
        self.listWidget.scrollToTop()
        if self.listWidget.count():
            self.listWidget.item(0).setSelected(False)
            self.listWidget.setFocus(True)
        
    #
    def listItemRightClickedToRemove(self, QPos):
        self.listMenuR= QtWidgets.QMenu()
        item_b = self.listMenuR.addAction("Remove from bookmark")
        action = self.listMenuR.exec_(self.listWidget.mapToGlobal(QPos))
        if action == item_b:
            item_idx = self.listWidget.indexAt(QPos)
            item_row = item_idx.row()
            item_removed = self.listWidget.takeItem(item_row)
            #
            try:
                os.remove(os.path.join("bookmarks", item_removed.file_name))
            except:
                pass
        self.listWidget.clearSelection()
        self.listWidget.clearFocus()
        self.listWidget.setFocus(True)


################

app = QtWidgets.QApplication(sys.argv)
#
screen = app.primaryScreen()
size = screen.size()
#
if win_position == "center":
    screen_w = size.width()
    screen_h = size.height()
else:
    screen_w, screen_h = win_position.split("/")
####
window = menuWin()
# set new style globally
if theme_style:
    s = QtWidgets.QStyleFactory.create(theme_style)
    app.setStyle(s)
# set the icon style globally
if icon_theme:
    QtGui.QIcon.setThemeName(icon_theme)
#
sys.exit(app.exec_())
    
###################
