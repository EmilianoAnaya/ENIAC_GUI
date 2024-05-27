from PySide6.QtWidgets import QApplication
from backend.Welcome_screen import Welcome_Screen

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Welcome_Screen()
    window.show()
    app.exec()