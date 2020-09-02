from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont , QPixmap , QIcon
from PyQt5.QtCore import QTimer
from random import randint
import sys

score_font = QFont('CalibriBold' , 10)
buttons = QFont('Times' , 10)

class Window(QWidget) : 
    def __init__(self) : 
        super().__init__()
        self.setGeometry(350 ,150,500, 600)
        self.setWindowTitle('Game')
        self.setWindowIcon(QIcon('./Resources/gamer.png'))
        self.UI()
        
        
    def UI(self) : 
        ################ Scores ##################################
        self.PC_score = 0
        self.Player_score = 0
        
        self.PC_scoreText = QLabel('Computer Score : ' , self)
        self.PC_scoreText.move(30 , 20)
        self.PC_scoreText.setFont(score_font)
        
        self.PCscore = QLabel(f'{self.PC_score}' , self)
        self.PCscore.move(200 , 20)
        self.PCscore.setFont(score_font)
        
        
        
        
        self.Player_scoreText = QLabel('Your Score : ', self)
        self.Player_scoreText.move(320 , 20)
        self.Player_scoreText.setFont(score_font)
        
        self.Playerscore = QLabel(f'{self.Player_score}', self)
        self.Playerscore.move(450 , 20)
        self.Playerscore.setFont(score_font)
        
        ################# Images ###################################
        
        self.PC_Img = QLabel(self)
        self.PC_Img.setPixmap(QPixmap('./Resources/rock.png'))
        self.PC_Img.move(50 , 100)
        
        self.VS = QLabel(self)
        self.VS.setPixmap(QPixmap('./Resources/game.png'))
        self.VS.move(230 , 150)
        
        self.Player_Img = QLabel(self)
        self.Player_Img.setPixmap(QPixmap('./Resources/rock.png'))
        self.Player_Img.move(320 , 100)
        
        self.Mark = QLabel(self)
        self.Mark.setPixmap(QPixmap('./Resources/rps3.png'))
        self.Mark.move(56 , 450)
        
        ################ Buttons ######################################
        
        self.stop_valid = 0
        
        start = QPushButton('Start' , self)
        start.move(190 , 300)
        start.setFont(buttons)
        start.clicked.connect(self.start)
        start.setStyleSheet('background-color:#333;color:White;')
        
        stop = QPushButton('Stop' , self)
        stop.move(190 , 350)
        stop.setFont(buttons)
        stop.clicked.connect(self.stop)
        stop.setStyleSheet('background-color:#333;color:White;')
        
        ############### Timer #########################################
        
        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.ChangeImg)
        
        self.show()
        
        
    def ChangeImg(self) : 
        self.PC_rand = randint(1,3)
        self.Player_rand = randint(1,3)
                
        if self.PC_rand==1 : self.PC_Img.setPixmap(QPixmap('./Resources/paper.png'))
        elif self.PC_rand == 2 : self.PC_Img.setPixmap(QPixmap('./Resources/rock.png'))            
        else : self.PC_Img.setPixmap(QPixmap('./Resources/scissors.png'))
        
        
        if self.Player_rand==1 : self.Player_Img.setPixmap(QPixmap('./Resources/paper.png'))
        elif self.Player_rand == 2 : self.Player_Img.setPixmap(QPixmap('./Resources/rock.png'))            
        else : self.Player_Img.setPixmap(QPixmap('./Resources/scissors.png'))
        
        
    
    def start(self) : 
        self.timer.start()
        self.stop_valid = 1
        
    def stop(self) :
        if self.stop_valid : 
            self.timer.stop()
            self.judge()
            self.stop_valid = 0
        else : pass
        
        
    def judge(self) : 
        PC = self.PC_rand
        you = self.Player_rand
        
        if PC == you : self.Win('')
        elif(PC , you) == (1,2) : self.Win('Computer')  ; self.score('Computer') ;
        elif(PC , you) == (2,1) : self.Win('You')       ; self.score('You')      ;
        elif(PC , you) == (1,3) : self.Win('You')       ; self.score('You')      ;
        elif(PC , you) == (3,1) : self.Win('Computer')  ; self.score('Computer') ;
        elif(PC , you) == (2,3) : self.Win('Computer')  ; self.score('Computer') ;
        elif(PC , you) == (3,2) : self.Win('You')       ; self.score('You')      ;
        
        
        
    def Win(self , Winner) : 
        if Winner == '' : 
            self.win_Message = QMessageBox.information(self, 'Result ' , 'Draw Game !  .....  Play again !' )
        else :
            self.win_Message = QMessageBox.information(self,'Result ' , Winner+' Won the Game !' )
     
    def score(self , Who) : 
        if Who == 'Computer' : 
            self.PC_score +=1
            self.PCscore.setText(str(self.PC_score))
            self.PCscore.resize(10 , 20)
            
        elif Who == 'You' :  
            self.Player_score +=1
            self.Playerscore.setText(str(self.Player_score))
            self.Playerscore.resize(10,20)

def main() : 
    App = QApplication(sys.argv)
    window = Window()
    window.setStyleSheet('background-color:#ddd')
    sys.exit(App.exec_())
    
    
if __name__ =='__main__' : 
    main()