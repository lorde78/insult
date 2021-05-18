import os
from nameenemy import *
### Couleurs :
degrade ='''qradialgradient(
        radius:3,
        stop:0 #3CE3B1, 
        stop:0.5 #3763FF,
        stop:1 rgb(200, 58, 180))
'''

path = os.getcwd()

styleButtonHome = "QPushButton {background-color: white; border: 1px solid "+degrade+"; border-radius: 15px; color: "+degrade+";font-weight:bold}""QPushButton:pressed {background-color: "+degrade+"; border: 1px solid "+degrade+"; border-radius: 15px; color: white}"
stylePointGame = "QProgressBar{border-radius: 10px;border: 2px solid #2196F3}QProgressBar::chunk {background-color:"+degrade+";margin: 3.5px;border-radius: 4px;padding:1px}"


#PointUser = 0

UserEnnemy = ChoixNameEnemy()
#PointEnnemy = 0
PicEnnemy = path+"/images/LOGO/logo-blue.png"
styleProfilPic = "border: 3px solid "+degrade+";border-radius: 20px;"

sentenceHole = "Hello___!!"

