import re
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, qApp, QTableWidgetItem, QFileDialog, QHeaderView

from mainWindow import Ui_MainWindow
from ui_functions import *
import resources_rc


class LoginLog(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(LoginLog, self).__init__(parent)
        self.setupUi(self)
        self.openBtn.clicked.connect(self.load_log)
        # 列宽自动分配
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        UIFunctions.uiDefinitions(self)

    def mousePressEvent(self, event):  # 以下3个函数用来使窗口可以拖动
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() and Qt.LeftButton:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False

    def load_log(self):
        openfile_name, ok = QFileDialog.getOpenFileName(self, '选择文件', '', 'log file(*.log)')
        if ok:
            self.tableWidget.clear()
            self.tableWidget.setRowCount(0)
            fo = open(openfile_name, "rb")  # 一定要用'rb'因为seek 是以bytes来计算的
            rowcount = 0
            for line in fo.readlines():
                # rowcount = self.tableWidget.rowCount()
                mat1 = re.search(r"(\d{4}[-/]\d{1,2}[-/]\d{1,2})", str(line.decode("gbk")))
                mat2 = re.search(r"(\d{2}:\d{2}:\d{2},\d{3})", str(line.decode("gbk")))
                mat3 = re.search('assigned to (.*)~', str(line.decode("gbk")))
                if mat1 and mat2 and mat3:
                    self.tableWidget.insertRow(rowcount)
                    item1 = QTableWidgetItem(mat1.group(0))
                    item2 = QTableWidgetItem(mat2.group(0))
                    item3 = QTableWidgetItem(mat3.group(1))
                    item1.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    item2.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    item3.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.tableWidget.setItem(rowcount, 0, item3)
                    self.tableWidget.setItem(rowcount, 1, item1)
                    self.tableWidget.setItem(rowcount, 2, item2)
                    rowcount = rowcount + 1
            fo.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = LoginLog()
    myWin.show()
    sys.exit(app.exec_())
