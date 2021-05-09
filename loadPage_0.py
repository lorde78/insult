
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import QTimer
import variable as var


class loadPage:
    
    def LoadPage (self):
        
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, -15, 360, 661))
        self.label.setStyleSheet("background-color:"+var.degrade)
        self.label.setPixmap(QtGui.QPixmap(var.path+"/images/LOGO/logo-blue.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        ## Progress bar
        self.progressBar = ProgressBar(self, self, minimum=0, maximum=3)
        self.progressBar.setGeometry(QtCore.QRect(120, 450, 125, 10))
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet(
            "QProgressBar{"
            "border-radius: 5px;"
            "}"
            "QProgressBar::chunk {"
            "background-color:"+var.degrade+";"
            "border-radius: 2px;"
            "margin: 2.5px;"
            "}"
            "Qt::AlignCenter")
        self.progressBar.setTextVisible(False)
        self.show()
        
        
from homePage_0 import *
from Mwindow import MWindow

window = MWindow()



class ProgressBar(QProgressBar):
    
    timeEnd = False

    def __init__(self, windowloading, *args, **kwargs):
        super(ProgressBar, self).__init__(*args, **kwargs)
        print(self.timeEnd)
        self.setValue(0)
        if self.minimum() != self.maximum():
            self.timer = QTimer(self, timeout = self.onTimeout)
            self.timer.start(1000)
        self.windowloading = windowloading        


    def onTimeout(self):
        self.setValue(self.value()+1)
        if self.value() >= self.maximum() :
            self.timer.stop()
            self.timeEnd = True
            print(self.timeEnd)
            self.windowloading.close()
            HomePage.HomePage_init(window)
            
           
            

    
          
     
