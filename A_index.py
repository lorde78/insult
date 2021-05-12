## Imports
import sys
from PyQt5.QtWidgets import * 

#initiallize GUI application
from A_Mwindow import MWindow
app = QApplication(sys.argv)
window = MWindow()

# Load Page
from A_loadPage_0 import loadPage
loadPage.LoadPage(window)


sys.exit(app.exec_())