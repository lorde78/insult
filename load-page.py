#coding:utf-8
#pip install PyQt5

### python3 -m PyQt5.uic.pyuic -x 10quetes.ui -o testafter.py

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
# from subprocess import call

# call("pip install PyQt5")


path = os.getcwd() ### Pour les images les chemins

degrade ='''qradialgradient(
        radius:3,
        stop:0 rgb(255, 119, 55), 
        stop:0.3 rgb(255, 48, 108),
        stop:0.6 rgb(200, 58, 180))
'''

class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setFixedWidth(360)
        self.setFixedHeight(640)
        self.setWindowTitle("10'Quêtes")
        self.setStyleSheet(
        "background-color: "+degrade
        )
        
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, -15, 360, 661))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color:"+degrade)
        self.label.setPixmap(QtGui.QPixmap(path+"/images/LOGO/logo_blanc_smoke.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("logo page chargement")
        


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec_()
