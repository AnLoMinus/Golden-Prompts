from PyQt5.QtWidgets import QMainWindow
from src.tabs.summary_tab import SummaryTab

class SummaryWindow(QMainWindow):
    def __init__(self, parent=None, project_window=None, tasks_window=None):
        super().__init__(parent)
        self.setWindowTitle("Summary")
        self.setCentralWidget(SummaryTab(project_window, tasks_window))
        self.resize(600, 400)
