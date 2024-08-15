from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QMessageBox, QVBoxLayout, QHBoxLayout, QLabel

app = QApplication([])
main = QWidget()
main.setWindowTitle('Викторина')
quest = QLabel('Какая самая большая страна в мире?')
ot1 = QRadioButton('Россия')
ot2 = QRadioButton('Китай')
ot3 = QRadioButton('Казахстан')
ot4 = QRadioButton('Америка')
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH1.addWidget(quest, alignment= Qt.AlignCenter)
layoutH2.addWidget(ot1, alignment=Qt.AlignCenter)
layoutH2.addWidget(ot2, alignment=Qt.AlignCenter)
layoutH3.addWidget(ot3, alignment=Qt.AlignCenter)
layoutH3.addWidget(ot4, alignment=Qt.AlignCenter)
layout_m = QVBoxLayout()
layout_m.addLayout(layoutH1)
layout_m.addLayout(layoutH2)
layout_m.addLayout(layoutH3)
main.setLayout(layout_m)

def winner():
    win = QMessageBox()
    win.setText('Верно!')
    win.exec_()

def lost():
    los = QMessageBox()
    los.setText('Не верно попробуй еще!')
    los.exec_()

ot1.clicked.connect(winner)
ot2.clicked.connect(lost)
ot3.clicked.connect(lost)
ot4.clicked.connect(lost)
main.show()
app.exec_()