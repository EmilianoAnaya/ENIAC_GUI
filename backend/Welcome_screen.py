from frontend.Ui_Welcome_screen import Ui_Welcome_Screen
from resources.tools.Tools import center_window
from backend.Menu_screen import MenuScreen
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QTimer

class Welcome_Screen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Welcome_Screen()
        self.ui.setupUi(self)
        center_window(self)

        self.timer = QTimer()
        self.timer.timeout.connect(self.OpenMain)
        self.timer.start(3000)

    def OpenMain(self):
        self.close()
        self.timer.stop()
        MainWindow = MenuScreen()
        MainWindow.show()
