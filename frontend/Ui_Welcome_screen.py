from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Welcome_Screen(object):
    def setupUi(self, Welcome_Screen):
        if not Welcome_Screen.objectName():
            Welcome_Screen.setObjectName(u"Welcome_Screen")
        Welcome_Screen.setStyleSheet(u"")
        Welcome_Screen.setFixedSize(438, 219)
        Welcome_Screen.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.centralwidget = QWidget(Welcome_Screen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"background-color: qlineargradient(spread:pad, x1:0.033, y1:0.965909, x2:1, y2:0, stop:0 rgba(102, 254, 255, 255), stop:0.333333 rgba(61, 139, 235, 255), stop:0.994987 rgba(81, 81, 92, 255), stop:1 rgba(7, 0, 92, 255))\n"
"}\n"
"\n"
"QFrame{\n"
"background-color:transparent\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setMaximumSize(QSize(16777215, 50))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.label.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 100))
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout.addWidget(self.frame)

        Welcome_Screen.setCentralWidget(self.centralwidget)

        self.retranslateUi(Welcome_Screen)

        QMetaObject.connectSlotsByName(Welcome_Screen)
    # setupUi

    def retranslateUi(self, Welcome_Screen):
        Welcome_Screen.setWindowTitle(QCoreApplication.translate("Welcome_Screen", u"ENIAC - WELCOME", None))
        self.label.setText(QCoreApplication.translate("Welcome_Screen", u"\u00a1Bienvenido!", None))
        self.label_2.setText(QCoreApplication.translate("Welcome_Screen", u"Prueba tu conocimiento con\n"
"Acertijos Matem\u00e1ticos", None))
    # retranslateUi