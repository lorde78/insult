
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import QTimer
import A_variable as var
        
from A_homePage_0 import *
from A_Mwindow import MWindow



class loadPage:
    
    def LoadPage (self):
        
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(0, -15, 360, 661))
        label.setStyleSheet("background-color:"+var.degrade)
        label.setPixmap(QtGui.QPixmap(var.path+"/images/LOGO/logo-blue.png"))
        label.setAlignment(QtCore.Qt.AlignCenter)

        ## Progress bar
        progressBar = ProgressBar(self, self, minimum=0, maximum=3)
        progressBar.setGeometry(QtCore.QRect(120, 450, 125, 10))
        progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        progressBar.setAutoFillBackground(False)
        progressBar.setStyleSheet(
            "QProgressBar{"
            "border-radius: 5px;"
            "}"
            "QProgressBar::chunk {"
            "background-color:"+var.degrade+";"
            "border-radius: 2px;"
            "margin: 2.5px;"
            "}"
            "Qt::AlignCenter")
        progressBar.setTextVisible(False)
        self.show()
        

window = MWindow()



class ProgressBar(QProgressBar):
    
    timeEnd = False

    def __init__(self, windowloading, *args, **kwargs):
        super(ProgressBar, self).__init__(*args, **kwargs)
        #print(self.timeEnd)
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
            #print(self.timeEnd)
            self.windowloading.close()
            HomePage.__init__(window)
            
           
            

    
          
     
