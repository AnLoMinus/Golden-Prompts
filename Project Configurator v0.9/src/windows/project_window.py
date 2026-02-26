from PyQt5.QtWidgets import QMainWindow
from src.tabs.project_tab import ProjectTab

class ProjectWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Project Details")
        self.central_widget = ProjectTab()
        self.setCentralWidget(self.central_widget)
        self.resize(600, 400)

    @property
    def fields(self):
        return self.central_widget.fields
