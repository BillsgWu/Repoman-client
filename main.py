from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import pyqtSlot,QTimer,QRect
from requests import get
from mainform import Ui_Form
import dialogs
from lib import *
from settings import *
from sys import argv as qarguments
class Window(QWidget):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_message)
        self.timer.setInterval(INTERVAL)
        self.timer.start(INTERVAL)
    @pyqtSlot()
    def on_bin_clicked(self):
        dialogs.Din(self).exec()
    @pyqtSlot()
    def on_bout_clicked(self):
        dialogs.Dout(self).exec()
    @pyqtSlot()
    def on_bget_clicked(self):
        dialogs.Dexist(self).exec()
    @pyqtSlot()
    def on_blog_clicked(self):
        dialogs.Dlog(self).exec()
    @pyqtSlot()
    def on_bsettings_clicked(self):
        dialogs.Dset(self).exec()
    @pyqtSlot()
    def update_message(self):
        res = get(f"{SCHEME}://{SERVERHOST}:{SERVERPORT}/api/query",{"db":"messageq"}).json()
        if res["status"] != "OK":
            return
        self.ui.messageq.clear()
        self.ui.messageq.addItems([i[1] for i in decodedata(res["data"])])
    def resizeEvent(self,event):
        size = event.size()
        size = [size.width(),size.height()]
        self.ui.bsettings.setGeometry(QRect(30,size[1] - 70,150,40))
        self.ui.messageq.setGeometry(QRect(210,30,size[0] - 240,size[1] - 60))
app = QApplication(qarguments)
base = Window()
base.show()
app.exec_()