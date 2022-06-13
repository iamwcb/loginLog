import re
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, qApp, QTableWidgetItem, QFileDialog, QHeaderView

from mainWindow import Ui_MainWindow


class LoginLog(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(LoginLog, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.load_log)
        # 列宽自动分配
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def load_log(self):
        openfile_name, ok = QFileDialog.getOpenFileName(self, '选择文件', '', 'log file(*.log)')
        if ok:
            fo = open(openfile_name, "rb")  # 一定要用'rb'因为seek 是以bytes来计算的
            index = 0
            for line in fo.readlines():
                mat1 = re.search(r"(\d{4}[-/]\d{1,2}[-/]\d{1,2})", str(line.decode()))
                mat2 = re.search(r"(\d{2}:\d{2}:\d{2},\d{3})", str(line.decode()))
                mat3 = re.search('assigned to (.*)~', str(line.decode()))
                if mat1 and mat2 and mat3:
                    self.tableWidget.insertRow(index)
                    item1 = QTableWidgetItem(mat1.group(0))
                    item2 = QTableWidgetItem(mat2.group(0))
                    item3 = QTableWidgetItem(mat3.group(1))
                    self.tableWidget.setItem(index, 0, item3)
                    self.tableWidget.setItem(index, 1, item1)
                    self.tableWidget.setItem(index, 2, item2)
                    index = index + 1

            fo.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = LoginLog()
    myWin.show()
    sys.exit(app.exec_())
