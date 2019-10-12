from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
import os
import sys


class MainWindow(QMainWindow):

    # browser = ...  # type: QWebEngineView

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("D34D K4GGl3")

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.kaggle.com/"))

        self.setCentralWidget(self.browser)

        navtab = QToolBar("Navigation")
        self.addToolBar(navtab)

        back_btn = QAction(QIcon(os.path.join('icons', 'icons8-back-to-48.png')), "Back", self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(self.browser.back)
        navtab.addAction(back_btn)

        next_btn = QAction(QIcon(os.path.join('icons', 'icons8-next-page-48.png')), "Next", self)
        next_btn.setStatusTip("Next page")
        next_btn.triggered.connect(self.browser.forward)
        navtab.addAction(next_btn)

        stop_btn = QAction(QIcon(os.path.join('icons', 'icons8-multiply-30.png')), "Stop", self)
        stop_btn.setStatusTip("Stop")
        stop_btn.triggered.connect(self.browser.stop)
        navtab.addAction(stop_btn)

        refresh_btn = QAction(QIcon(os.path.join('icons', 'icons8-rotate-48.png')), "Refresh", self)
        refresh_btn.setStatusTip("Back to previous page")
        refresh_btn.triggered.connect(self.browser.reload)
        navtab.addAction(refresh_btn)

        self.show()


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()