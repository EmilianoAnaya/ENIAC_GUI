from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QScreen

def center_window(self: QWidget) -> None:
    screen = QScreen.availableGeometry(QApplication.primaryScreen())
    window = self.frameGeometry()
    center_screen = screen.center()
    window.moveCenter(center_screen)
    self.move(window.topLeft())
    return

def clear_entries(Entries: list) -> None:
    for entry in Entries:
        entry.clear()
    return

def HideLabel(Label: QLabel):
    Label.setVisible(False)