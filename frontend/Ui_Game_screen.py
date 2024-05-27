# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Game_screen.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Game_screen(object):
    def setupUi(self, Game_screen):
        if not Game_screen.objectName():
            Game_screen.setObjectName(u"Game_screen")
        Game_screen.resize(562, 269)
        Game_screen.setMinimumSize(QSize(562, 269))
        Game_screen.setMaximumSize(QSize(562, 269))
        self.verticalLayout = QVBoxLayout(Game_screen)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_Game = QWidget(Game_screen)
        self.widget_Game.setObjectName(u"widget_Game")
        self.widget_Game.setMinimumSize(QSize(562, 269))
        self.widget_Game.setMaximumSize(QSize(562, 269))
        self.widget_Game.setStyleSheet(u"#widget_Game{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0.005013 rgba(42, 180, 255, 255), stop:0.279732 rgba(70, 222, 255, 255), stop:0.517588 rgba(110, 225, 255, 255), stop:0.768844 rgba(81, 255, 235, 255), stop:1 rgba(28, 249, 255, 255));\n"
"}\n"
"\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.widget_Game)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_RegresiveCount = QWidget(self.widget_Game)
        self.widget_RegresiveCount.setObjectName(u"widget_RegresiveCount")
        self.widget_RegresiveCount.setMaximumSize(QSize(16777215, 269))
        self.widget_RegresiveCount.setStyleSheet(u"#lbl_numbers{\n"
"color: rgb(255, 85, 127);\n"
"font-family: verdana;\n"
"font-size:55px;\n"
"font-weight: bold;\n"
"font-style: italic;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.widget_RegresiveCount)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lbl_numbers = QLabel(self.widget_RegresiveCount)
        self.lbl_numbers.setObjectName(u"lbl_numbers")

        self.verticalLayout_3.addWidget(self.lbl_numbers, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_2.addWidget(self.widget_RegresiveCount)

        self.widget_Questions = QWidget(self.widget_Game)
        self.widget_Questions.setObjectName(u"widget_Questions")
        self.widget_Questions.setMaximumSize(QSize(16777215, 0))
        self.widget_Questions.setStyleSheet(u"QLabel{\n"
"	background:transparent;\n"
"}\n"
"\n"
"QWidget{\n"
"	background:transparent;\n"
"}\n"
"\n"
"QLineEdit {\n"
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
"}\n"
"\n"
"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0.005013 rgba(42, 180, 255, 255), stop:0.279732 rgba(70, 222, 255, 255), stop:0.517588 rgba(110, 225, 255, 255), stop:0.768844 rgba(81, 255, 235, 255), stop:1 rgba(28, 249, 255, 255));\n"
"border-style:inset;\n"
"border-width: 2px;\n"
"border-color: rgb(85, 170, 255);\n"
"border-radius: 3px;\n"
"color: black;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(57, 112, 2"
                        "55, 255));\n"
"border-color: rgb(0, 85, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(57, 255, 108, 255));\n"
"border-color: rgb(0, 255, 127);\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.widget_Questions)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lbl_Question = QLabel(self.widget_Questions)
        self.lbl_Question.setObjectName(u"lbl_Question")
        self.lbl_Question.setMinimumSize(QSize(0, 160))
        self.lbl_Question.setMaximumSize(QSize(1000, 1000))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        self.lbl_Question.setFont(font)
        self.lbl_Question.setScaledContents(False)
        self.lbl_Question.setWordWrap(True)
        self.lbl_Question.setStyleSheet("color:black;")

        self.verticalLayout_4.addWidget(self.lbl_Question, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_4 = QWidget(self.widget_Questions)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout = QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.txt_Question = QLineEdit(self.widget_4)
        self.txt_Question.setObjectName(u"txt_Question")
        self.txt_Question.setMinimumSize(QSize(100, 30))
        self.txt_Question.setMaximumSize(QSize(100, 22))
        self.txt_Question.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout.addWidget(self.txt_Question, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.btn_Question = QPushButton(self.widget_4)
        self.btn_Question.setObjectName(u"btn_Question")
        self.btn_Question.setMinimumSize(QSize(80, 30))
        self.btn_Question.setMaximumSize(QSize(100, 24))

        self.horizontalLayout.addWidget(self.btn_Question, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_4.addWidget(self.widget_4, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.lbl_MsgAnswer = QLabel(self.widget_Questions)
        self.lbl_MsgAnswer.setObjectName(u"lbl_MsgAnswer")
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.lbl_MsgAnswer.setFont(font1)
        self.lbl_MsgAnswer.setVisible(False)

        self.verticalLayout_4.addWidget(self.lbl_MsgAnswer, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_2.addWidget(self.widget_Questions)

        self.widget_Results = QWidget(self.widget_Game)
        self.widget_Results.setObjectName(u"widget_Results")
        self.widget_Results.setMaximumSize(QSize(16777215, 0))
        self.widget_Results.setStyleSheet(u"QLabel{\n"
"	background:transparent;\n"
"}\n"
"\n"
"QWidget{\n"
"	background:transparent;\n"
"}\n"
"\n"
"QLineEdit {\n"
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
"}\n"
"\n"
"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0.005013 rgba(42, 180, 255, 255), stop:0.279732 rgba(70, 222, 255, 255), stop:0.517588 rgba(110, 225, 255, 255), stop:0.768844 rgba(81, 255, 235, 255), stop:1 rgba(28, 249, 255, 255));\n"
"border-style:inset;\n"
"border-width: 2px;\n"
"border-color: rgb(85, 170, 255);\n"
"border-radius: 3px;\n"
"color: black;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(57, 112, 2"
                        "55, 255));\n"
"border-color: rgb(0, 85, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(57, 255, 108, 255));\n"
"border-color: rgb(0, 255, 127);\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.widget_Results)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.widget_Results)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lbl_ScoreMsg = QLabel(self.widget)
        self.lbl_ScoreMsg.setObjectName(u"lbl_ScoreMsg")
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(True)
        self.lbl_ScoreMsg.setFont(font2)
        self.lbl_ScoreMsg.setStyleSheet("color:black;")

        self.verticalLayout_6.addWidget(self.lbl_ScoreMsg, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_5.addWidget(self.widget)

        self.widget_2 = QWidget(self.widget_Results)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_7 = QVBoxLayout(self.widget_2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btn_FinishGame = QPushButton(self.widget_2)
        self.btn_FinishGame.setObjectName(u"btn_FinishGame")
        self.btn_FinishGame.setMinimumSize(QSize(75, 0))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.btn_FinishGame.setFont(font3)

        self.verticalLayout_7.addWidget(self.btn_FinishGame, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_5.addWidget(self.widget_2)


        self.verticalLayout_2.addWidget(self.widget_Results)


        self.verticalLayout.addWidget(self.widget_Game)


        self.retranslateUi(Game_screen)

        QMetaObject.connectSlotsByName(Game_screen)
    # setupUi

    def retranslateUi(self, Game_screen):
        Game_screen.setWindowTitle(QCoreApplication.translate("Game_screen", u"Game", None))
        self.lbl_numbers.setText(QCoreApplication.translate("Game_screen", u"3", None))
        self.lbl_Question.setText(QCoreApplication.translate("Game_screen", u"TextLabel", None))
        self.btn_Question.setText(QCoreApplication.translate("Game_screen", u"Responder", None))
        self.lbl_MsgAnswer.setText(QCoreApplication.translate("Game_screen", u"TextLabel", None))
        self.lbl_ScoreMsg.setText(QCoreApplication.translate("Game_screen", u"TextLabel", None))
        self.btn_FinishGame.setText(QCoreApplication.translate("Game_screen", u"Cancelar", None))
    # retranslateUi

