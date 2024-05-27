from frontend.Ui_Menu_screen import Ui_Menu_Screen
from backend.Exit_Screen import Exit_Screen
from backend.Game_Widget import Game_Screen
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QTimer
from backend.Register_Widget import SavePlayer
from backend.Game_Widget import StartGame
from resources.tools.Tools import clear_entries, HideLabel

class MenuScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Menu_Screen()
        self.ui.setupUi(self)

        self.Scores: list = []
        self.Players: list = []
        
        self.ui.btn_SavePlayer.pressed.connect(self.RegisterPlayer)
        self.ui.btn_StartGame.pressed.connect(self.StartGame)

        self.ui.btn_GameScreen.pressed.connect(lambda: self.ChangeScreen(0))
        self.ui.btn_RegisterScreen.pressed.connect(lambda: self.ChangeScreen(1))
        self.ui.btn_RankingScreen.pressed.connect(lambda: self.ChangeScreen(2))
        self.ui.btn_Exit.pressed.connect(self.ExitApp)

        self.SuccessTimer = QTimer()
        self.SuccessTimer.setInterval(2000)
        self.SuccessTimer.setSingleShot(True)
        self.SuccessTimer.timeout.connect(lambda: HideLabel(self.ui.lbl_SuccessMsg))
    
    def StartGame(self):
        TmpPlayer: str = StartGame(self.ui, self.Players)
        if TmpPlayer:
            self.hide()
            self.WindowGame = Game_Screen(self, TmpPlayer)
            self.WindowGame.show()
    
    def RegisterPlayer(self) -> None:
        if SavePlayer(self.ui, self.Players):
            self.ui.lbl_SuccessMsg.setVisible(True)
            self.SuccessTimer.start()
        clear_entries([self.ui.txt_SavePlayer])
            
    def ChangeScreen(self,index: int) -> None:
        self.ui.stackedWidget.setCurrentIndex(index)
        clear_entries([self.ui.txt_SavePlayer,
                      self.ui.txt_Player])
    
    def ExitApp(self) -> None:
        self.close()
        self.Exit_Screen = Exit_Screen()
        self.Exit_Screen.show()