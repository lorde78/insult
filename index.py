## Imports
import sys
sys.path.insert(0,"interface")
from PyQt5.QtWidgets import * 

#initiallize GUI application
from Mwindow import MWindow
app = QApplication(sys.argv)
window = MWindow()

# Load Page
from loadPage_0 import loadPage
loadPage.LoadPage(window)


sys.exit(app.exec_())