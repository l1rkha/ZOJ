from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Тест для бабушек ')
main_win.resize(1400 , 700)

line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(but, alignment = Qt.AlignCenter)
main_win.setLayout(line)

but.clicked.connect(show_winner)
main_win.show()
app.exec_()