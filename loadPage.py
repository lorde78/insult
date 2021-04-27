
    ## Imports
import sys
import os
##PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
    ##Variables
import variable as var
#Pour le chemin
path = os.getcwd()


class Ui_homeWindow(object):
    def setupUi(self, homeWindow):
        homeWindow.setObjectName("homeWindow")
        homeWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        homeWindow.resize(360, 640)
        homeWindow.setMinimumSize(QtCore.QSize(360, 640))
        homeWindow.setMaximumSize(QtCore.QSize(360, 640))
        homeWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        homeWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        homeWindow.setAcceptDrops(False)
        homeWindow.setWindowTitle("10\'Quêtes")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(path+"/images/LOGO/logo_colore.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        homeWindow.setWindowIcon(icon)
        homeWindow.setToolTip("")
        homeWindow.setToolTipDuration(0)
        homeWindow.setAutoFillBackground(False)
        homeWindow.setStyleSheet("")
        homeWindow.setAnimated(False)
        homeWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        homeWindow.setProperty("home", "")
        self.centralwidget = QtWidgets.QWidget(homeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -15, 360, 661))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color:"+var.degrade)
        self.label.setPixmap(QtGui.QPixmap(path+"/images/LOGO/logo_blanc_smoke.png"))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setIndent(0)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(120, 410, 125, 10))
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet(
            "QProgressBar{"
            "border-radius: 5px;"
            "}"
            "QProgressBar::chunk {"
            "background-color:"+var.degrade+";"
            "border-radius: 10px;"
            "margin: 2.5px;"
            "}"
            "Qt::AlignCenter")
        self.progressBar.setProperty("value", 39)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setProperty("colorMain", QtGui.QColor(255, 0, 36))
        self.progressBar.setObjectName("progressBar")
        homeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(homeWindow)
        QtCore.QMetaObject.connectSlotsByName(homeWindow)

    def retranslateUi(self, homeWindow):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    homeWindow = QtWidgets.QMainWindow()
    ui = Ui_homeWindow()
    ui.setupUi(homeWindow)
    homeWindow.show()
    sys.exit(app.exec_())
