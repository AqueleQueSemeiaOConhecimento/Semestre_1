import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton


class MinhaApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minha Aplicação")
        
        label = QLabel("Olá, mundo!", self)
        label.move(50, 50)
        
        botao = QPushButton("Clique Aqui", self)
        botao.move(50, 80)
        botao.clicked.connect(self.fechar_janela)
        
    def fechar_janela(self):
        self.close()

# Instanciar e executar a aplicação
app = QApplication(sys.argv)
janela = MinhaApp()
janela.show()
sys.exit(app.exec_())
