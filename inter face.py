import pygame
from PyQt5.QtWidgets import*

app = QApplication([])
window = QWidget()
window.resize(400,400)


mainline = QVBoxLayout()
menubut = QPushButton('')
restbtn = QPushButton('')
timespn = QSpinBox()
timlb = QLabel('')
redaguvaty = QPushButton('')

firstnoline = QVBoxLayout()
firstline = QHBoxLayout()
firstline.addWidget(menubut)
firstline.addWidget(restbtn)
firstline.addWidget(timespn)
firstline.addWidget(timlb)
firstline.addWidget(redaguvaty)
mainline.addLayout(firstline)

window.setLayout(mainline)
window.show()
app.exec()
