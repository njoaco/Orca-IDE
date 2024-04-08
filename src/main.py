import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qsci import *

import sys
from pathlib import Path

class MainWindow(QMainWindow):

    def __init__(self):
        super(QMainWindow, self).__init__()
        self.side_bar_color = "#282c34"
        self.tree_frame_color = "#2125b"
        self.init_ui()

        self.current_file = None

    def init_ui(self):
        #Cuerpo
        self.setWindowTitle("Orca | v0.1")
        self.resize(1300, 900)

        self.setStyleSheet(open("./src/css/style.qss", "r").read())


        self.window_font = QFont("Tahoma")
        self.window_font.setPointSize(10)
        self.setFont(self.window_font)

        self.set_up_menu()
        self.set_up_body()
        self.statusBar().showMessage("ORCA V0.1 BETA")

        self.show()

    def get_edit(self) -> QsciScintilla:
        pass

    def set_up_menu(self):
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("File")

        #File Menu Bar
        new_file = file_menu.addAction("New")
        new_file.setShortcut("Ctrl+N")
        new_file.triggered.connect(self.new_file)

        open_file = file_menu.addAction("Open File")
        open_file.setShortcut("Ctrl+O")
        open_file.triggered.connect(self.open_file)

        open_folder = file_menu.addAction("Open Folder")
        open_folder.setShortcut("Ctrl+F")
        open_folder.triggered.connect(self.open_folder)

        #Edit Actions Menu
        edit_menu = menu_bar.addMenu("Edit")

        copy_action = edit_menu.addAction("Copy")
        copy_action.setShortcut("Ctrl+C")
        copy_action.triggered.connect(self.copy)

        cut_action = edit_menu.addAction("Cut")
        cut_action.setShortcut("Ctrl+X")
        cut_action.triggered.connect(self.cut)

    def new_file(self):
        ...

    def open_file(self):
        ...

    def open_folder(self):
        ...

    def copy(self):
        ...

    def cut(self):
        ...

    def set_up_body(self):

        #Body
        body_frame = QFrame()
        body_frame.setFrameShape(QFrame.NoFrame)
        body_frame.setFrameShadow(QFrame.Plain)
        body_frame.setLineWidth(0)
        body_frame.setMidLineWidth(0)
        body_frame.setContentsMargins(0, 0, 0, 0)
        body_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        body = QHBoxLayout()
        body.setContentsMargins(0, 0, 0, 0)
        body.setSpacing(0)
        body_frame.setLayout(body)

        #Side Bar
        self.side_bar = QFrame()
        self.side_bar.setFrameShape(QFrame.StyledPanel)
        self.side_bar.setFrameShadow(QFrame.Plain)
        self.side_bar.setStyleSheet(''' 
            background-color: #15171c;
        ''')
        
        side_bar_layout = QHBoxLayout()
        side_bar_layout.setContentsMargins(5, 10, 5, 0)
        side_bar_layout.setSpacing(0)
        side_bar_layout.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        self.side_bar.setLayout(side_bar_layout)

        body.addWidget(self.side_bar)

        #Split View
        self.hsplit = QSplitter(Qt.Horizontal)

        #File Manager
        self.tree_frame = QFrame()
        self.tree_frame.setLineWidth(1)
        self.tree_frame.setMaximumWidth(400)
        self.tree_frame.setMaximumHeight(200)
        self.tree_frame.setBaseSize(100, 0)
        self.tree_frame.setContentsMargins(0, 0, 0, 0)
        tree_frame_layout = QVBoxLayout()
        tree_frame_layout.setContentsMargins(0, 0, 0, 0)
        tree_frame_layout.setSpacing(0)
        self.tree_frame.setStyleSheet('''
                QFrame{
                    background-color: #21252b;
                    border-radius: 5px;
                    border: none;
                    padding: 5px;
                    color:  #D3D3D3;
                }
                QFrame:hover {
                    color: white;
                }
        ''')

        #Show Tree View
        self.model = QFileSystemModel()
        self.model.setRootPath(os.getcwd())

        #Filters
        self.model.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs | QDir.Files)

        #Tree View
        self.tree_view = QTreeView()
        self.tree_view.setFont(QFont("Tahoma", 13))
        self.tree_view.setModel(self.model)
        self.tree_view.setRootIndex(self.model.index(os.getcwd()))
        self.tree_view.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tree_view.setSelectionBehavior(QTreeView.SelectRows)
        self.tree_view.setEditTriggers(QTreeView.NoEditTriggers)

        #Custom Context Menu
        self.tree_view.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tree_view.customContextMenuRequested.connect(self.tree_view_context_menu)

        #Handling Click
        self.tree_view.clicked.connect(self.tree_view_clicked)
        self.tree_view.setIndentation(10)
        self.tree_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        #Hide Headers
        self.tree_view.setHeaderHidden(True)
        self.tree_view.setColumnHidden(1, True)
        self.tree_view.setColumnHidden(2, True)
        self.tree_view.setColumnHidden(3, True)

        #Setup Layout
        tree_frame_layout.addWidget(self.tree_view)
        self.tree_frame.setLayout(tree_frame_layout)

        #Tree View and Tab View
        self.hsplit.addWidget(self.tree_frame)

        body.addWidget(self.hsplit)
        body_frame.setLayout(body)

        self.setCentralWidget(body_frame)





    def tree_view_context_menu(self, pos):
        ...

    def tree_view_clicked(self):
        ...

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec_())
    
