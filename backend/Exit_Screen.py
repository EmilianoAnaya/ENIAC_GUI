from PySide6.QtWidgets import QWidget
from frontend.Ui_Exit_screen import Ui_Exit_Screen
from resources.tools.Tools import center_window
from PySide6.QtCore import QTimer

class Exit_Screen(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Exit_Screen()
        self.ui.setupUi(self)
        center_window(self)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.close)
        self.timer.start(3000)