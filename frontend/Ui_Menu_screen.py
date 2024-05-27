# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Menu_screen.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_Menu_Screen(object):
    def setupUi(self, Menu_Screen):
        if not Menu_Screen.objectName():
            Menu_Screen.setObjectName(u"Menu_Screen")
        Menu_Screen.resize(674, 372)
        Menu_Screen.setMinimumSize(QSize(674, 372))
        Menu_Screen.setMaximumSize(QSize(674, 372))
        self.centralwidget = QWidget(Menu_Screen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(200, 0))
        palette = QPalette()
        gradient = QLinearGradient(0, 0, 1, 0)
        gradient.setSpread(QGradient.PadSpread)
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient.setColorAt(0, QColor(102, 148, 255, 255))
        gradient.setColorAt(0.360465, QColor(89, 136, 255, 255))
        gradient.setColorAt(0.677778, QColor(70, 165, 255, 255))
        gradient.setColorAt(1, QColor(42, 180, 255, 255))
        brush = QBrush(gradient)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        gradient1 = QLinearGradient(0, 0, 1, 0)
        gradient1.setSpread(QGradient.PadSpread)
        gradient1.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient1.setColorAt(0, QColor(102, 148, 255, 255))
        gradient1.setColorAt(0.360465, QColor(89, 136, 255, 255))
        gradient1.setColorAt(0.677778, QColor(70, 165, 255, 255))
        gradient1.setColorAt(1, QColor(42, 180, 255, 255))
        brush1 = QBrush(gradient1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        gradient2 = QLinearGradient(0, 0, 1, 0)
        gradient2.setSpread(QGradient.PadSpread)
        gradient2.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient2.setColorAt(0, QColor(102, 148, 255, 255))
        gradient2.setColorAt(0.360465, QColor(89, 136, 255, 255))
        gradient2.setColorAt(0.677778, QColor(70, 165, 255, 255))
        gradient2.setColorAt(1, QColor(42, 180, 255, 255))
        brush2 = QBrush(gradient2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush2)
        gradient3 = QLinearGradient(0, 0, 1, 0)
        gradient3.setSpread(QGradient.PadSpread)
        gradient3.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient3.setColorAt(0, QColor(102, 148, 255, 255))
        gradient3.setColorAt(0.360465, QColor(89, 136, 255, 255))
        gradient3.setColorAt(0.677778, QColor(70, 165, 255, 255))
        gradient3.setColorAt(1, QColor(42, 180, 255, 255))
        brush3 = QBrush(gradient3)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        gradient4 = QLinearGradient(0, 0, 1, 0)
        gradient4.setSpread(QGradient.PadSpread)
        gradient4.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient4.setColorAt(0, QColor(102, 148, 255, 255))
        gradient4.setColorAt(0.360465, QColor(89, 136, 255, 255))
        gradient4.setColorAt(0.677778, QColor(70, 165, 255, 255))
        gradient4.setColorAt(1, QColor(42, 180, 255, 255))
        brush4 = QBrush(gradient4)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        gradient5 = QLinearGradient(0, 0, 1, 0)
        gradient5.setSpread(QGradient.PadSpread)
        gradient5.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient5.setColorAt(0, QColor(102, 148, 255, 255))
        gradient5.setColorAt(0.360465, QColor(89, 136, 255, 255))
        gradient5.setColorAt(0.677778, QColor(70, 165, 255, 255))
        gradient5.setColorAt(1, QColor(42, 180, 255, 255))
        brush5 = QBrush(gradient5)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        gradient6 = QLinearGradient(0, 0, 1, 0)
        gradient6.setSpread(QGradient.PadSpread)
        gradient6.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient6.setColorAt(0, QColor(102, 148, 255, 255))
        gradient6.setColorAt(0.360465, QColor(89, 136, 255, 255))
        gradient6.setColorAt(0.677778, QColor(70, 165, 255, 255))
        gradient6.setColorAt(1, QColor(42, 180, 255, 255))
        brush6 = QBrush(gradient6)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        gradient7 = QLinearGradient(0, 0, 1, 0)
        gradient7.setSpread(QGradient.PadSpread)
        gradient7.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient7.setColorAt(0, QColor(102, 148, 255, 255))
        gradient7.setColorAt(0.360465, QColor(89, 136, 255, 255))
        gradient7.setColorAt(0.677778, QColor(70, 165, 255, 255))
        gradient7.setColorAt(1, QColor(42, 180, 255, 255))
        brush7 = QBrush(gradient7)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        gradient8 = QLinearGradient(0, 0, 1, 0)
        gradient8.setSpread(QGradient.PadSpread)
        gradient8.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient8.setColorAt(0, QColor(102, 148, 255, 255))
        gradient8.setColorAt(0.360465, QColor(89, 136, 255, 255))
        gradient8.setColorAt(0.677778, QColor(70, 165, 255, 255))
        gradient8.setColorAt(1, QColor(42, 180, 255, 255))
        brush8 = QBrush(gradient8)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        self.widget.setPalette(palette)
        self.widget.setStyleSheet(u"QWidget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(102, 148, 255, 255), stop:0.360465 rgba(89, 136, 255, 255), stop:0.677778 rgba(70, 165, 255, 255), stop:1 rgba(42, 180, 255, 255))\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(102, 148, 255, 255), stop:0.360465 rgba(89, 136, 255, 255), stop:0.677778 rgba(70, 165, 255, 255), stop:0.994987 rgba(42, 180, 255, 255), stop:1 rgba(7, 0, 92, 255));\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 5px;\n"
"border-color: rgb(32, 62, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:repeat, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(68, 167, 169, 255), stop:0.266129 rgba(58, 168, 149, 255), stop:0.497312 rgba(30, 203, 178, 255), stop:0.755376 rgba(30, 221, 200, 255), stop:1 rgba(0, 255, 255, 255));\n"
"border-color: rgb(85, 255, 255);\n"
"border-style: inset;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-colo"
                        "r:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(78, 0, 135, 255), stop:0.25 rgba(126, 47, 185, 255), stop:0.497253 rgba(159, 74, 222, 255), stop:0.747253 rgba(212, 88, 220, 255), stop:1 rgba(218, 92, 219, 255));\n"
"border-color: rgb(255, 0, 255);\n"
"border-style: ridge;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_GameScreen = QPushButton(self.widget)
        self.btn_GameScreen.setObjectName(u"btn_GameScreen")
        self.btn_GameScreen.setMinimumSize(QSize(150, 50))
        palette1 = QPalette()
        gradient9 = QLinearGradient(0, 1, 1, 0)
        gradient9.setSpread(QGradient.PadSpread)
        gradient9.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient9.setColorAt(0, QColor(102, 148, 255, 255))
        gradient9.setColorAt(0.360465, QColor(89, 136, 255, 255))
        gradient9.setColorAt(0.677778, QColor(70, 165, 255, 255))
        gradient9.setColorAt(0.994987, QColor(42, 180, 255, 255))
        gradient9.setColorAt(1, QColor(7, 0, 92, 255))
        brush9 = QBrush(gradient9)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush9)
        gradient10 = QLinearGradient(0, 1, 1, 0)
        gradient10.setSpread(QGradient.PadSpread)
        gradient10.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient10.setColorAt(0, QColor(102, 148, 255, 255))
        gradient10.setColorAt(0.360465, QColor(89, 136, 255, 255))
        gradient10.setColorAt(0.677778, QColor(70, 165, 255, 255))
        gradient10.setColorAt(0.994987, QColor(42, 180, 255, 255))
        gradient10.setColorAt(1, QColor(7, 0, 92, 255))
        brush10 = QBrush(gradient10)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush10)
        gradient11 = QLinearGradient(0, 1, 1, 0)
        gradient11.setSpread(QGradient.PadSpread)
        gradient11.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient11.setColorAt(0, QColor(102, 148, 255, 255))
        gradient11.setColorAt(0.360465, QColor(89, 136, 255, 255))
        gradient11.setColorAt(0.677778, QColor(70, 165, 255, 255))
        gradient11.setColorAt(0.994987, QColor(42, 180, 255, 255))
        gradient11.setColorAt(1, QColor(7, 0, 92, 255))
        brush11 = QBrush(gradient11)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush11)
        gradient12 = QLinearGradient(0, 1, 1, 0)
        gradient12.setSpread(QGradient.PadSpread)
        gradient12.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient12.setColorAt(0, QColor(102, 148, 255, 255))
        gradient12.setColorAt(0.360465, QColor(89, 136, 255, 255))
        gradient12.setColorAt(0.677778, QColor(70, 165, 255, 255))
        gradient12.setColorAt(0.994987, QColor(42, 180, 255, 255))
        gradient12.setColorAt(1, QColor(7, 0, 92, 255))
        brush12 = QBrush(gradient12)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        gradient13 = QLinearGradient(0, 1, 1, 0)
        gradient13.setSpread(QGradient.PadSpread)
        gradient13.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient13.setColorAt(0, QColor(102, 148, 255, 255))
        gradient13.setColorAt(0.360465, QColor(89, 136, 255, 255))
        gradient13.setColorAt(0.677778, QColor(70, 165, 255, 255))
        gradient13.setColorAt(0.994987, QColor(42, 180, 255, 255))
        gradient13.setColorAt(1, QColor(7, 0, 92, 255))
        brush13 = QBrush(gradient13)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        gradient14 = QLinearGradient(0, 1, 1, 0)
        gradient14.setSpread(QGradient.PadSpread)
        gradient14.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient14.setColorAt(0, QColor(102, 148, 255, 255))
        gradient14.setColorAt(0.360465, QColor(89, 136, 255, 255))
        gradient14.setColorAt(0.677778, QColor(70, 165, 255, 255))
        gradient14.setColorAt(0.994987, QColor(42, 180, 255, 255))
        gradient14.setColorAt(1, QColor(7, 0, 92, 255))
        brush14 = QBrush(gradient14)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush14)
        gradient15 = QLinearGradient(0, 1, 1, 0)
        gradient15.setSpread(QGradient.PadSpread)
        gradient15.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient15.setColorAt(0, QColor(102, 148, 255, 255))
        gradient15.setColorAt(0.360465, QColor(89, 136, 255, 255))
        gradient15.setColorAt(0.677778, QColor(70, 165, 255, 255))
        gradient15.setColorAt(0.994987, QColor(42, 180, 255, 255))
        gradient15.setColorAt(1, QColor(7, 0, 92, 255))
        brush15 = QBrush(gradient15)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        gradient16 = QLinearGradient(0, 1, 1, 0)
        gradient16.setSpread(QGradient.PadSpread)
        gradient16.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient16.setColorAt(0, QColor(102, 148, 255, 255))
        gradient16.setColorAt(0.360465, QColor(89, 136, 255, 255))
        gradient16.setColorAt(0.677778, QColor(70, 165, 255, 255))
        gradient16.setColorAt(0.994987, QColor(42, 180, 255, 255))
        gradient16.setColorAt(1, QColor(7, 0, 92, 255))
        brush16 = QBrush(gradient16)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush16)
        gradient17 = QLinearGradient(0, 1, 1, 0)
        gradient17.setSpread(QGradient.PadSpread)
        gradient17.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient17.setColorAt(0, QColor(102, 148, 255, 255))
        gradient17.setColorAt(0.360465, QColor(89, 136, 255, 255))
        gradient17.setColorAt(0.677778, QColor(70, 165, 255, 255))
        gradient17.setColorAt(0.994987, QColor(42, 180, 255, 255))
        gradient17.setColorAt(1, QColor(7, 0, 92, 255))
        brush17 = QBrush(gradient17)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush17)
        self.btn_GameScreen.setPalette(palette1)

        self.verticalLayout.addWidget(self.btn_GameScreen, 0, Qt.AlignmentFlag.AlignHCenter)

        self.btn_RegisterScreen = QPushButton(self.widget)
        self.btn_RegisterScreen.setObjectName(u"btn_RegisterScreen")
        self.btn_RegisterScreen.setMinimumSize(QSize(150, 50))

        self.verticalLayout.addWidget(self.btn_RegisterScreen, 0, Qt.AlignmentFlag.AlignHCenter)

        self.btn_RankingScreen = QPushButton(self.widget)
        self.btn_RankingScreen.setObjectName(u"btn_RankingScreen")
        self.btn_RankingScreen.setMinimumSize(QSize(150, 50))

        self.verticalLayout.addWidget(self.btn_RankingScreen, 0, Qt.AlignmentFlag.AlignHCenter)

        self.btn_Exit = QPushButton(self.widget)
        self.btn_Exit.setObjectName(u"btn_Exit")
        self.btn_Exit.setMinimumSize(QSize(150, 50))

        self.verticalLayout.addWidget(self.btn_Exit, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignHCenter)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QLineEdit {\n"
"    background-color: white;\n"
"    border: 1px solid gray;\n"
"    border-radius: 4px;\n"
"    color: black;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: rgb(213, 213, 213);\n"
"    border: 1px solid blue;\n"
"    color: black;\n"
"}\n"
"\n"
"QLineEdit:!focus {\n"
"    color: black;\n"
"}")
        self.page_Game = QWidget()
        self.page_Game.setObjectName(u"page_Game")
        self.page_Game.setStyleSheet(u"#page_Game{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.005013 rgba(42, 180, 255, 255), stop:0.278388 rgba(74, 202, 255, 255), stop:0.481685 rgba(89, 253, 255, 255), stop:0.787476 rgba(55, 255, 250, 255), stop:1 rgba(15, 255, 249, 255))\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(0, 170, 255);\n"
"border-style: outset;\n"
"border-width: 5px;\n"
"border-radius: 5px;\n"
"border-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 255, 127);\n"
"border-color: rgb(85, 255, 127);\n"
"color: black;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(170, 0, 255);\n"
"border-color: rgb(170, 85, 255);\n"
"color: white;\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 55, 63);\n"
"}\n"
"\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.page_Game)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_JugarTitle = QLabel(self.page_Game)
        self.lbl_JugarTitle.setObjectName(u"lbl_JugarTitle")
        self.lbl_JugarTitle.setMinimumSize(QSize(0, 200))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setStrikeOut(False)
        self.lbl_JugarTitle.setFont(font)

        self.verticalLayout_3.addWidget(self.lbl_JugarTitle, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.widget_2 = QWidget(self.page_Game)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(250, 0))
        self.widget_2.setBaseSize(QSize(0, 0))
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_PlayerMessage = QLabel(self.widget_2)
        self.lbl_PlayerMessage.setObjectName(u"lbl_PlayerMessage")
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setItalic(False)
        self.lbl_PlayerMessage.setFont(font1)

        self.verticalLayout_2.addWidget(self.lbl_PlayerMessage)

        self.txt_Player = QLineEdit(self.widget_2)
        self.txt_Player.setObjectName(u"txt_Player")
        self.txt_Player.setInputMask(u"")
        self.txt_Player.setText(u"")

        self.verticalLayout_2.addWidget(self.txt_Player)


        self.verticalLayout_3.addWidget(self.widget_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.btn_StartGame = QPushButton(self.page_Game)
        self.btn_StartGame.setObjectName(u"btn_StartGame")
        self.btn_StartGame.setMinimumSize(QSize(150, 30))

        self.verticalLayout_3.addWidget(self.btn_StartGame, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.stackedWidget.addWidget(self.page_Game)
        self.page_Register = QWidget()
        self.page_Register.setObjectName(u"page_Register")
        self.page_Register.setStyleSheet(u"#page_Register{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(42, 180, 255, 255), stop:0.258333 rgba(139, 107, 255, 255), stop:0.529167 rgba(165, 99, 255, 255), stop:0.795833 rgba(192, 89, 255, 255), stop:1 rgba(255, 50, 227, 255))\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(78, 0, 135, 255), stop:0.25 rgba(126, 47, 185, 255), stop:0.497253 rgba(159, 74, 222, 255), stop:0.747253 rgba(212, 88, 220, 255), stop:1 rgba(218, 92, 219, 255));\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width: 2px;\n"
"border-color: rgb(170, 0, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(218, 92, 219, 255), stop:0.252747 rgba(212, 88, 220, 255), stop:0.502747 rgba(222, 43, 189, 255), stop:0.75 rgba(185, 47, 71, 255), stop:1 rgba(135, 0, 0, 255));\n"
"border-color: rgb(255, 0, 127);\n"
"}\n"
"\n"
"QPushButton:Pressed{\n"
"bac"
                        "kground-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(135, 35, 35, 255), stop:0.25 rgba(185, 57, 80, 255), stop:0.497253 rgba(207, 90, 222, 255), stop:0.748031 rgba(201, 142, 208, 255), stop:1 rgba(219, 210, 219, 255));\n"
"border-color: rgb(255, 170, 255);\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.page_Register)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.page_Register)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setEnabled(True)
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lbl_RegisterMessage = QLabel(self.widget_3)
        self.lbl_RegisterMessage.setObjectName(u"lbl_RegisterMessage")
        self.lbl_RegisterMessage.setMinimumSize(QSize(0, 200))
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setItalic(True)
        self.lbl_RegisterMessage.setFont(font2)

        self.verticalLayout_5.addWidget(self.lbl_RegisterMessage, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(200, 0))
        self.verticalLayout_6 = QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lbl_SavePlayer = QLabel(self.widget_4)
        self.lbl_SavePlayer.setObjectName(u"lbl_SavePlayer")
        font3 = QFont()
        font3.setFamilies([u"Verdana"])
        font3.setPointSize(9)
        font3.setBold(True)
        self.lbl_SavePlayer.setFont(font3)

        self.verticalLayout_6.addWidget(self.lbl_SavePlayer, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.txt_SavePlayer = QLineEdit(self.widget_4)
        self.txt_SavePlayer.setObjectName(u"txt_SavePlayer")
        self.txt_SavePlayer.setMinimumSize(QSize(250, 0))
        self.txt_SavePlayer.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_6.addWidget(self.txt_SavePlayer, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_5.addWidget(self.widget_4, 0, Qt.AlignmentFlag.AlignTop)

        self.btn_SavePlayer = QPushButton(self.widget_3)
        self.btn_SavePlayer.setObjectName(u"btn_SavePlayer")
        self.btn_SavePlayer.setMinimumSize(QSize(150, 30))

        self.verticalLayout_5.addWidget(self.btn_SavePlayer, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.lbl_SuccessMsg = QLabel(self.widget_3)
        self.lbl_SuccessMsg.setObjectName(u"lbl_SuccessMsg")
        self.lbl_SuccessMsg.setEnabled(True)
        font4 = QFont()
        font4.setFamilies([u"Verdana"])
        font4.setPointSize(7)
        font4.setBold(True)
        self.lbl_SuccessMsg.setFont(font4)
        self.lbl_SuccessMsg.setVisible(False)

        self.verticalLayout_5.addWidget(self.lbl_SuccessMsg, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_4.addWidget(self.widget_3)

        self.stackedWidget.addWidget(self.page_Register)
        self.page_Rankings = QWidget()
        self.page_Rankings.setObjectName(u"page_Rankings")
        self.page_Rankings.setStyleSheet(u"#page_Rankings{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(42, 180, 255, 255), stop:0.263713 rgba(24, 237, 143, 255), stop:0.529167 rgba(66, 178, 75, 255), stop:0.795833 rgba(35, 175, 32, 255), stop:1 rgba(0, 140, 0, 255));\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.page_Rankings)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_5 = QWidget(self.page_Rankings)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_9 = QVBoxLayout(self.widget_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lbl_RankingMessage = QLabel(self.widget_5)
        self.lbl_RankingMessage.setObjectName(u"lbl_RankingMessage")
        self.lbl_RankingMessage.setMinimumSize(QSize(0, 50))
        font5 = QFont()
        font5.setFamilies([u"Verdana"])
        font5.setPointSize(18)
        font5.setBold(True)
        font5.setItalic(True)
        self.lbl_RankingMessage.setFont(font5)

        self.verticalLayout_9.addWidget(self.lbl_RankingMessage, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.wid_PlayersScores = QWidget(self.widget_5)
        self.wid_PlayersScores.setObjectName(u"wid_PlayersScores")
        self.wid_PlayersScores.setMinimumSize(QSize(0, 300))
        self.wid_PlayersScores.setStyleSheet(u"QLabel{\n"
"color: black;\n"
"font-weight: bold;\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.wid_PlayersScores)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")

        self.verticalLayout_9.addWidget(self.wid_PlayersScores)


        self.verticalLayout_8.addWidget(self.widget_5)

        self.stackedWidget.addWidget(self.page_Rankings)

        self.horizontalLayout.addWidget(self.stackedWidget)

        Menu_Screen.setCentralWidget(self.centralwidget)

        self.retranslateUi(Menu_Screen)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Menu_Screen)
    # setupUi

    def retranslateUi(self, Menu_Screen):
        Menu_Screen.setWindowTitle(QCoreApplication.translate("Menu_Screen", u"ENIAC", None))
        self.btn_GameScreen.setText(QCoreApplication.translate("Menu_Screen", u"Jugar", None))
        self.btn_RegisterScreen.setText(QCoreApplication.translate("Menu_Screen", u"Registro", None))
        self.btn_RankingScreen.setText(QCoreApplication.translate("Menu_Screen", u"Marcadores", None))
        self.btn_Exit.setText(QCoreApplication.translate("Menu_Screen", u"Salir", None))
        self.lbl_JugarTitle.setText(QCoreApplication.translate("Menu_Screen", u"\u00bfEstas preparado para jugar?", None))
        self.lbl_PlayerMessage.setText(QCoreApplication.translate("Menu_Screen", u"\u00bfQuien Jugar\u00e1 en esta Partida?", None))
#if QT_CONFIG(accessibility)
        self.txt_Player.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.txt_Player.setPlaceholderText(QCoreApplication.translate("Menu_Screen", u"Ingrese el nombre del jugador", None))
        self.btn_StartGame.setText(QCoreApplication.translate("Menu_Screen", u"Jugar", None))
        self.lbl_RegisterMessage.setText(QCoreApplication.translate("Menu_Screen", u"REGISTRO DE NUEVOS JUGADORES", None))
        self.lbl_SavePlayer.setText(QCoreApplication.translate("Menu_Screen", u"Ingrese el Nombre del Nuevo Jugador", None))
        self.txt_SavePlayer.setPlaceholderText(QCoreApplication.translate("Menu_Screen", u"Ingrese su Nombre", None))
        self.btn_SavePlayer.setText(QCoreApplication.translate("Menu_Screen", u"Registrar", None))
        self.lbl_SuccessMsg.setText(QCoreApplication.translate("Menu_Screen", u"\u00a1Registro con \u00c9xito!", None))
        self.lbl_RankingMessage.setText(QCoreApplication.translate("Menu_Screen", u"RANKING GLOBAL", None))
    # retranslateUi

