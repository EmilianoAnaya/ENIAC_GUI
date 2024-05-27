from resources.tools.Tools import clear_entries, HideLabel
from resources.constants import GameQuestions as resources
from PySide6.QtWidgets import QMessageBox, QWidget, QLabel
from frontend.Ui_Menu_screen import Ui_Menu_Screen
from frontend.Ui_Game_screen import Ui_Game_screen
from PySide6.QtCore import QTimer
from PySide6.QtCore import Qt
from random import sample
from re import match
   
def StartGame(self: Ui_Menu_Screen, Players_list: list) -> str:
    TmpPlayer: str = self.txt_Player.text().strip()
    msgbox = QMessageBox()
    if TmpPlayer not in Players_list:
        msgbox.setWindowTitle("Jugador no Existente")
        msgbox.setIcon(QMessageBox.Icon.Critical)
        msgbox.setText("Este jugador no se ha registrado aún.\nRegistrese antes de jugar.")
        msgbox.exec()
        return None
    msgbox.setWindowTitle("Empezar Juego")
    msgbox.setIcon(QMessageBox.Icon.Information)
    msgbox.setText(f"El Jugador {TmpPlayer} dara comienzo a una nueva partida, Es correcto?.")
    msgbox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    
    res = msgbox.exec()
    if res == QMessageBox.StandardButton.Yes:
        return TmpPlayer
    
class Game_Screen(QWidget):
    def __init__(self, parent: object, TmpPlayer: str):
        super().__init__()
        self.ui = Ui_Game_screen()
        self.ui.setupUi(self)

        self.Tmp_Player = TmpPlayer

        self.WindowBackgrounds: list = resources.get_color_backgrounds()
        self.easy_questions:list = sample(resources.get_easy_questions(), 4)
        self.avrg_questions:list = sample(resources.get_avrg_questions(), 2)
        self.hard_questions:list = sample(resources.get_hard_questions(), 2)
        self.tmp_score:int = 0
        self.tmp_tries:int = 3
        self.game_over:bool = False
        self.question_counter:int = 0

        self.countdown_counter: int = 0
        self.countdown_strings = ["2","1","¡INICIO!"]
        self.CountDown = QTimer()
        self.CountDown.timeout.connect(self.label_Countdown)
        self.CountDown.start(1000)

        self.SwapWidgets = QTimer()
        self.SwapWidgets.setInterval(4000)
        self.SwapWidgets.timeout.connect(lambda: self.Swap_Widgets( self.SwapWidgets,
                                                                    self.ui.widget_RegresiveCount,
                                                                    self.ui.widget_Questions))
        self.SwapWidgets.setSingleShot(True)
        self.SwapWidgets.start()

        self.AnswerTimer = QTimer()
        self.AnswerTimer.setInterval(2000)
        self.AnswerTimer.setSingleShot(True)

        self.question: tuple[str, int] = self.easy_questions.pop(0)
        self.ui.lbl_Question.setText(self.question[0])

        self.ui.btn_Question.pressed.connect(lambda: self.CheckAnswer(parent))
        self.ui.btn_FinishGame.pressed.connect(lambda: self.CloseWindow(parent))

    def NextQuestion(self):
        self.SetScorePoints()
        if len(self.easy_questions) > 0:
            self.question = self.easy_questions.pop(0)  
        elif len(self.avrg_questions) > 0:
            self.question = self.avrg_questions.pop(0)
        elif len(self.hard_questions) > 0:
            self.question = self.hard_questions.pop(0)
        HideLabel(self.ui.lbl_MsgAnswer)
        self.ui.lbl_Question.setText(self.question[0])
        self.ui.lbl_Question.adjustSize()
        self.ui.txt_Question.clear()
        self.ui.txt_Question.setReadOnly(False)
        self.ui.btn_Question.setDisabled(False)
        self.AnswerTimer.timeout.disconnect()
    
    def SetScorePoints(self):
        if self.question_counter < 4:
            self.tmp_score = self.tmp_score + 10
        elif self.question_counter < 6:
            self.tmp_score = self.tmp_score + 20
        elif self.question_counter < 8:
            self.tmp_score = self.tmp_score + 30
        self.question_counter += 1

    def CheckAnswer(self, parent):
        Answer = self.ui.txt_Question.text().strip()
        if not match(r'^[+-]?(\d+(\.\d*)?|\.\d+)$', Answer):
            return
        Answer = float(self.ui.txt_Question.text().strip())
        if Answer == self.question[1]:
            self.Show_AnswerMessage(0)
            self.AnswerTimer.timeout.connect(self.NextQuestion)
            self.ui.txt_Question.setReadOnly(True)
            self.ui.btn_Question.setDisabled(True)
            if self.question_counter == 7:
                self.AnswerTimer.stop()
                self.ui.lbl_MsgAnswer.setText("GAME OVER!")
                self.ui.lbl_MsgAnswer.setStyleSheet("color: green;")
                self.ui.txt_Question.setReadOnly(True)
                self.ui.btn_Question.setDisabled(True)
                self.CheckScore(parent)
        else:
            self.AnswerTimer.timeout.connect(lambda: HideLabel(self.ui.lbl_MsgAnswer))
            self.Show_AnswerMessage(1)
            self.tmp_tries = self.tmp_tries - 1
            if self.tmp_tries <= 0:
                self.AnswerTimer.stop()
                self.ui.lbl_MsgAnswer.setText("GAME OVER!")
                self.ui.lbl_MsgAnswer.setStyleSheet("color: red;")
                self.ui.txt_Question.setReadOnly(True)
                self.ui.btn_Question.setDisabled(True)
                self.CheckScore(parent)
            else:
                self.ui.widget_Game.setStyleSheet(self.WindowBackgrounds.pop(0))

    def label_Countdown(self):
        self.ui.lbl_numbers.setText(self.countdown_strings.pop(0))
        self.countdown_counter += 1
        if self.countdown_counter == 3:
            self.CountDown.stop()
    
    def Swap_Widgets(self, timer: QTimer, OldWindow: QWidget, NewWindow: QWidget):
        timer.stop()
        OldWindow.setMaximumHeight(0)
        NewWindow.setMaximumHeight(269)

    def Show_AnswerMessage(self, option: int):
        self.ui.lbl_MsgAnswer.setVisible(True)
        if option == 0:
            self.ui.lbl_MsgAnswer.setText("CORRECT!")
            self.ui.lbl_MsgAnswer.setStyleSheet("color: green;")
        else:
            self.ui.lbl_MsgAnswer.setText("WRONG!")
            self.ui.lbl_MsgAnswer.setStyleSheet("color: red;")
            clear_entries([self.ui.txt_Question])
        self.AnswerTimer.start()

    def CheckScore(self,parent):
        self.SwapWidgets.timeout.disconnect()
        self.SwapWidgets.timeout.connect(lambda: self.Swap_Widgets(self.SwapWidgets,
                                                                   self.ui.widget_Questions,
                                                                   self.ui.widget_Results))
        self.SwapWidgets.start()
        if self.question_counter == 7 and self.tmp_tries == 3:
            self.tmp_score = self.tmp_score*2
            self.ui.lbl_ScoreMsg.setText(f"¡Acertaste {self.question_counter+1} de 8 acertijos\ntu puntuación final es {self.tmp_score} y no te equivocaste ninguna vez, eres Asombroso!")
        elif self.question_counter == 7 and self.tmp_tries == 2:
            self.tmp_score = self.tmp_score + 30
            self.ui.lbl_ScoreMsg.setText(f"¡Acertaste {self.question_counter+1} de 8 acertijos\ntu puntuación final es {self.tmp_score} y solo te equivocaste una vez, buen trabajo!")
        elif self.question_counter == 7 and self.tmp_tries == 1:
            self.tmp_score = self.tmp_score + 25
            self.ui.lbl_ScoreMsg.setText(f"¡Acertaste {self.question_counter+1} de 8 acertijos, tu puntuación final es {self.tmp_score}!")
        elif self.question_counter == 6:
            self.tmp_score = self.tmp_score + 20
            self.ui.lbl_ScoreMsg.setText(f"¡Casí perfecto!, acertaste {self.question_counter+1} de 8 acertijos\ntu puntuación final es {self.tmp_score}!")
        elif self.question_counter == 5:
            self.tmp_score = self.tmp_score + 15
            self.ui.lbl_ScoreMsg.setText(f"¡Acertaste {self.question_counter+1} de 8 acertijos\ntu puntuación final es {self.tmp_score}!")
        elif self.question_counter == 4:
            self.tmp_score = self.tmp_score + 10
            self.ui.lbl_ScoreMsg.setText(f"¡Acertaste {self.question_counter+1} de 8 acertijos\ntu puntuación final es {self.tmp_score}!")
        elif self.question_counter == 3:
            self.tmp_score = self.tmp_score + 5
            self.ui.lbl_ScoreMsg.setText(f"¡Acertaste {self.question_counter+1} de 8 acertijos\ntu puntuación final es {self.tmp_score}!")
        elif self.question_counter == 2:
            self.tmp_score = self.tmp_score - 5 
            self.ui.lbl_ScoreMsg.setText(f"¡Acertaste {self.question_counter+1} de 8 acertijos\ntu puntuación final es {self.tmp_score}!")
        elif self.question_counter == 1:
            self.tmp_score = self.tmp_score - 10
            self.ui.lbl_ScoreMsg.setText(f"¡Acertaste {self.question_counter+1} de 8 acertijos\ntu puntuación final es {self.tmp_score}!")
        else:
            self.tmp_score = 1
            self.ui.lbl_ScoreMsg.setText(f"¡Acertaste {self.question_counter+1} de 8 acertijos\ntu puntuación final es {self.tmp_score}!")
        self.ui.lbl_ScoreMsg.adjustSize()
        parent.Scores.append((self.Tmp_Player, self.tmp_score))

    def CloseWindow(self, parent):
        self.close()
        parent.show()
        tmpLabel = QLabel(f"{self.Tmp_Player} - - - - - {self.tmp_score} PTS")
        parent.ui.verticalLayout_10.addWidget(tmpLabel, 0, Qt.AlignHCenter)