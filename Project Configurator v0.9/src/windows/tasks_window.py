from PyQt5.QtWidgets import QMainWindow
from src.tabs.tasks_tab import TasksTab

class TasksWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Tasks")
        self.setCentralWidget(TasksTab())
        self.resize(600, 400)
