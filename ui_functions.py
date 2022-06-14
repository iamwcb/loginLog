################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

## ==> GUI FILE
from PyQt5 import QtCore
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QSizeGrip

from main import *

## ==> GLOBALS

GLOBAL_STATE = 0


class UIFunctions:

    # ==> MAXIMIZE RESTORE FUNCTION
    # def maximize_restore(self):
    #     global GLOBAL_STATE
    #     status = GLOBAL_STATE
    #
    #     # IF NOT MAXIMIZED
    #     if status == 0:
    #         self.showMaximized()
    #
    #         # SET GLOBAL TO 1
    #         GLOBAL_STATE = 1
    #
    #         # IF MAXIMIZED REMOVE MARGINS AND BORDER RADIUS
    #         self.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
    #         self.drop_shadow_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255)); border-radius: 0px;")
    #         # self.btn_maximize.setToolTip("Restore")
    #     else:
    #         GLOBAL_STATE = 0
    #         self.showNormal()
    #         self.resize(self.width()+1, self.height()+1)
    #         self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
    #         self.drop_shadow_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255)); border-radius: 10px;")
    #         self.btn_maximize.setToolTip("Maximize")
    #
    def maximize_restore(self):
        if self.isMaximized():
            self.showNormal()
            self.btn_maximize.setToolTip("Maximize")

        else:
            self.showMaximized()
            self.btn_maximize.setToolTip("Restore")

    ## ==> UI DEFINITIONS
    def uiDefinitions(self):

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # SET DROPSHADOW WINDOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        # APPLY DROPSHADOW TO FRAME
        self.drop_shadow_frame.setGraphicsEffect(self.shadow)

        # MAXIMIZE / RESTORE
        self.btn_maximize.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # MINIMIZE
        self.btn_minimize.clicked.connect(lambda: self.showMinimized())

        # CLOSE
        self.btn_close.clicked.connect(lambda: self.close())

        # ==> CREATE SIZE GRIP TO RESIZE WINDOW

        # self.sizegrip = QSizeGrip(self.frame_grip)
        # self.sizegrip.setStyleSheet(
        #     "QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }")
        # self.sizegrip.setToolTip("Resize Window")

    # # RETURN STATUS IF WINDOWS IS MAXIMIZE OR RESTAURED
    # def returnStatus(self):
    #     return GLOBAL_STATE
