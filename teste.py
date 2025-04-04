#programa de incrementar presses no botão

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QComboBox
from PyQt6.QtWidgets import QLabel



amount = 0

def add():
    amount += 1
    label.setText(f"{amount}")
    label.adjustSize()


app = QApplication(sys.argv)

window = QWidget()
window.resize(500, 500)

label = QLabel(window)
label.setGeometry(400, 100, 150, 100)



button = QPushButton(window)
button.setGeometry(100, 100, 150, 100)
button.setText("Press me!")
button.clicked.connect(add(amount))




window.show()

app.exec()