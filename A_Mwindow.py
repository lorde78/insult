#coding:utf-8
from PyQt5 import QtGui
import os
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
path = os.getcwd()

class MWindow(QMainWindow):

    def __init__(self,*args, **kwargs):
        super(MWindow, self).__init__(*args, **kwargs)
        self.setFixedWidth(360)
        self.setFixedHeight(640)
        self.setWindowTitle("Cannibale Dungo")
        self.setStyleSheet(
        "background-color: white"
        )
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(path+"/images/LOGO/logo-blue.png"))

        
