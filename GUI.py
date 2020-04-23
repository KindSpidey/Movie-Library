# Convert the resulting py file
from sample import Ui_Form
import sys
from PyQt5.QtWidgets import QMainWindow


# Inherited to the main window class of the interface file
class MyMainWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())