import re
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, qApp, QTableWidgetItem

from mainWindow import Ui_MainWindow


class LoginLog(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(LoginLog, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.load_log)

    def load_log(self):
        fo = open("test.log", "rb")  # 一定要用'rb'因为seek 是以bytes来计算的
        print("文件名为: ", fo.name)
        for line in fo.readlines():
            print("读取的数据为:" + str(line.decode()))


        test_str = """
           平安夜圣诞节的日子与去年2015/12/24的是有不同哦10:01:51,473.
           """

        mat1 = re.search(r"(\d{4}[-/]\d{1,2}[-/]\d{1,2})", test_str)
        mat2 = re.search(r"(\d{1,2}:\d{1,2},:\d{3})", test_str)
        print(mat1)
        print(mat2)
        # row = self.tableWidget.rowCount()
        # self.tableWidget.insertRow(row)
        # item = QTableWidgetItem("fasdf","ssssda")
        # self.tableWidget.setItem(0, 0, item)
        # fo.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = LoginLog()
    myWin.show()
    sys.exit(app.exec_())
