# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Exit_screen.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Exit_Screen(object):
    def setupUi(self, Exit_Screen):
        if not Exit_Screen.objectName():
            Exit_Screen.setObjectName(u"Exit_Screen")
        Exit_Screen.setFixedSize(438, 219)
        Exit_Screen.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        Exit_Screen.setStyleSheet(u"QWidget{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(102, 148, 255, 255), stop:0.360465 rgba(89, 136, 255, 255), stop:0.677778 rgba(70, 165, 255, 255), stop:0.994987 rgba(42, 180, 255, 255), stop:1 rgba(7, 0, 92, 255));\n"
"}\n"
"\n"
"QLabel{\n"
"	background-color:transparent;\n"
"	font-weight: bold;\n"
"	font-size: 18px;\n"
"	font-family: Verdana;\n"
"}")
        self.verticalLayout = QVBoxLayout(Exit_Screen)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Exit_Screen)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.label_2 = QLabel(Exit_Screen)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.retranslateUi(Exit_Screen)

        QMetaObject.connectSlotsByName(Exit_Screen)
    # setupUi

    def retranslateUi(self, Exit_Screen):
        Exit_Screen.setWindowTitle(QCoreApplication.translate("Exit_Screen", u"Form", None))
        self.label.setText(QCoreApplication.translate("Exit_Screen", u"Muchas Gracias por haber Participado!", None))
        self.label_2.setText(QCoreApplication.translate("Exit_Screen", u"Esperamos verte pronto!!!", None))
    # retranslateUi

