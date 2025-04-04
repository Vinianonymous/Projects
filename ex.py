import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QComboBox
from PyQt6.QtWidgets import QLabel

def funcao1():
        label.setText("aaaaaaaaaaa")
        label.adjustSize()


def funcao2():
    label.setText("aaaaaaaaaaa2")
    label.adjustSize()

def funcao3():
    dado = le.text()
    label.setText(dado)
    label.adjustSize()

def lercombo():
    valor = combo.currentText()
    label.setText(valor)
    label.adjustSize()


app = QApplication(sys.argv)

janela = QWidget()
janela.resize(800, 600)
janela.setWindowTitle("Teste")



#tem como meter CSS pra estilizar os elementos.
# \btn.setStyleSheet('background-color: blue;color:white')

label = QLabel("Texto", janela)
label.move(400, 100)
label.setStyleSheet('font-size: 30px')

btn = QPushButton("Botão 1", janela)
btn.setGeometry(100, 100, 150, 80)
btn.clicked.connect(funcao1)

btn = QPushButton("Botão 2", janela)
btn.setGeometry(100, 300, 150, 80)
btn.clicked.connect(funcao2)

btn = QPushButton("Botão 3", janela)
btn.setGeometry(100, 500, 150, 80)
btn.clicked.connect(funcao3)

combo = QComboBox(janela)
combo.addItem("Selecione uma opção: ")
combo.addItem("rust")
combo.addItem("Kotlin")
combo.move(600, 500)

botao4 = QPushButton("Mostrar opção ", janela)
botao4.setGeometry(300, 600, 130, 90)
botao4.clicked.connect(lercombo)




le = QLineEdit("", janela)
le.setGeometry(500, 300, 150, 40)


#Colocar elementos antes dessa instrução.
janela.show()

app.exec()
