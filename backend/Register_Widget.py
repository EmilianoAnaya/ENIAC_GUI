from PySide6.QtWidgets import QMessageBox
from frontend.Ui_Menu_screen import Ui_Menu_Screen

def SavePlayer(self: Ui_Menu_Screen, Players_List: list) -> bool:
    PlayerName: str = self.txt_SavePlayer.text().strip()
    if not PlayerName:
        return False
    msgbox = QMessageBox()
    msgbox.setIcon(QMessageBox.Icon.Question)
    msgbox.setWindowTitle("Guardando al Jugador")
    msgbox.setText(f"Estas seguro de querer guardar al jugador {PlayerName}?\nEl nombre de este no podra ser cambiado.")
    msgbox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    
    result = msgbox.exec()
    
    if result == QMessageBox.StandardButton.Yes:
        if not PlayerName in Players_List:
            Players_List.append(PlayerName)
            return True
        else:
            msgbox.setIcon(QMessageBox.Icon.Critical)
            msgbox.setWindowTitle("Error al Guardar Jugador")
            msgbox.setText(f"El Jugador {PlayerName} ya se ha guardado anteriormente.")
            msgbox.exec()
            return False
