## Imports
import sys
from PyQt5.QtWidgets import * 

#initiallize GUI application
from Mwindow import MWindow
app = QApplication(sys.argv)
window = MWindow()

# Load Page
from loadPage_0 import loadPage
loadPage.LoadPage(window)


# window.show()
sys.exit(app.exec_())