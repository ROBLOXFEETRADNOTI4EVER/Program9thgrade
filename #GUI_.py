import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MY COOL FIRST GUI")
        self.setGeometry(0, 0, 1000, 1000)
        self.setWindowIcon(QIcon("pythongui.jpg"))

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 50))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: #162923;"
                            "background-color: #f07a05;"
                            "font-style: italic;"
                            "text-decoration: underline;")

        #label.setAlignment(Qt.AlignTop) #alligned verticly top
        #label.setAlignment(Qt.AlignBottom) #alligned at the bottom        
        #label.setAlignment(Qt.AlignVCenter)   #verticly centered (orginal boom) 
        #label.setAlignment(Qt.AlignRight)   #horrizanitly right 
        #label.setAlignment(Qt.AlignHCenter) #horizantally center
        #label.setAlignment(Qt.AlignLeft) #horizantly left

        label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) #center and bottom
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) #center #center
        label.setAlignment(Qt.AlignCenter)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()