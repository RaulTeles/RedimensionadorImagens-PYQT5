import sys
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap #Manipular a imagem

class Redimensionar(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnEscolherArquivo.clicked.connect(self.abrirImagem) #Definindo a função para abrir com o clicked
        self.btnRedimensionar.clicked.connect(self.redimensionar) #Definindo a função para abrir com o clicked
        self.btnSalvar.clicked.connect(self.salvar) #Definindo a função para abrir com o clicked

#criando método para abrir a imagem
    def abrirImagem(self):
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir Imagem',
            r'C:\Users'
            # options=QFileDialog.DontUseNativeDialog
        )
        self.inputAbrirArquivo.setText(imagem)
        #criando uma self para criar uma nova imagem, para nao salvar no lugar da original
        self.originalImagem = QPixmap(imagem)
        self.labelImagem.setPixmap(self.originalImagem)
        self.inputLargura.setText(str(self.originalImagem.width()))
        self.inputAltura.setText(str(self.originalImagem.height()))

    def redimensionar(self):
        largura = int(self.inputLargura.text())
        altura = int(self.inputAltura.text())
        # self.novaImagem = self.originalImagem.scaledToWidth(largura)
        self.novaImagem = self.originalImagem.scaled(largura,altura)
        self.labelImagem.setPixmap(self.novaImagem)
        self.inputLargura.setText(str(self.novaImagem.width()))
        self.inputAltura.setText(str(self.novaImagem.height()))

    def salvar(self):
        imagem, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Salvar Imagem',
            r'C:\Users'
            # options=QFileDialog.DontUseNativeDialog
        )
        self.novaImagem.save(imagem, 'PNG')
#bloco Padrão
if __name__ == '__main__':
    qt = QApplication(sys.argv)
    redimensionar = Redimensionar()
    redimensionar.show()
    qt.exec_()