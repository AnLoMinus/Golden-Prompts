import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFont
from src.project_configurator import ProjectConfigurator

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # Set the default font for the entire application
    font = QFont("Arial", 18)
    app.setFont(font)
    
    ex = ProjectConfigurator()
    ex.setWindowTitle('🚀 Project Configurator v0.9')
    ex.show()
    sys.exit(app.exec_())
