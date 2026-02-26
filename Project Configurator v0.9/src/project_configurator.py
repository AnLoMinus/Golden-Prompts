from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
                             QPushButton, QFileDialog, QScrollArea, QMessageBox, QComboBox, QTextEdit,
                             QDateEdit, QTabWidget, QListWidget, QDialog, QDialogButtonBox, QPlainTextEdit,
                             QDesktopWidget, QInputDialog)
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont, QIcon
from datetime import datetime
import json
from src.windows.project_window import ProjectWindow
from src.windows.tasks_window import TasksWindow
from src.windows.summary_window import SummaryWindow

class ProjectConfigurator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.version = "0.9"
        self.changes_log_file = "version_changes.json"
        self.presets_file = "presets.json"
        self.load_presets()
        self.initUI()

        self.project_window = ProjectWindow(self)
        self.tasks_window = TasksWindow(self)
        self.summary_window = SummaryWindow(self, self.project_window, self.tasks_window)
        self.windows_open = False

    def initUI(self):
        self.setWindowTitle('🚀 Project Configurator v0.9')
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Add preset selector
        preset_layout = QHBoxLayout()
        preset_label = QLabel("Select Preset:")
        self.preset_selector = QComboBox()
        self.preset_selector.addItem("Select Preset")
        for preset in self.presets.keys():
            self.preset_selector.addItem(preset)
        self.preset_selector.currentIndexChanged.connect(self.apply_preset)
        preset_layout.addWidget(preset_label)
        preset_layout.addWidget(self.preset_selector)
        main_layout.addLayout(preset_layout)

        # Create buttons for opening windows
        project_button = QPushButton("Open Project Details")
        project_button.clicked.connect(self.open_project_window)
        main_layout.addWidget(project_button)

        tasks_button = QPushButton("Open Tasks")
        tasks_button.clicked.connect(self.open_tasks_window)
        main_layout.addWidget(tasks_button)

        summary_button = QPushButton("Open Summary")
        summary_button.clicked.connect(self.open_summary_window)
        main_layout.addWidget(summary_button)

        # Buttons
        button_layout = QHBoxLayout()
        save_button = QPushButton('💾 Save Configuration')
        save_button.clicked.connect(self.save_configuration)
        button_layout.addWidget(save_button)

        load_button = QPushButton('📂 Load Configuration')
        load_button.clicked.connect(self.load_configuration)
        button_layout.addWidget(load_button)

        clear_button = QPushButton('🧹 Clear All')
        clear_button.clicked.connect(self.clear_all_fields)
        button_layout.addWidget(clear_button)

        export_button = QPushButton('📤 Export to Template')
        export_button.clicked.connect(self.export_to_template)
        button_layout.addWidget(export_button)

        main_layout.addLayout(button_layout)

        self.resize(400, 300)
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def load_presets(self):
        try:
            with open(self.presets_file, 'r') as file:
                self.presets = json.load(file)
        except FileNotFoundError:
            self.presets = {}
        except json.JSONDecodeError:
            self.presets = {}

    def apply_preset(self):
        selected_preset = self.preset_selector.currentText()
        if selected_preset != "Select Preset":
            preset_data = self.presets.get(selected_preset)
            if preset_data:
                # Apply preset data to fields
                self.log_change(f"Applied preset: {selected_preset}")
                QMessageBox.information(self, "Preset Applied", f"The {selected_preset} preset has been applied.")
            else:
                print(f"Preset data not found for: {selected_preset}")
        else:
            print("No preset selected")

    def open_project_window(self):
        self.project_window.show()

    def open_tasks_window(self):
        self.tasks_window.show()

    def open_summary_window(self):
        self.summary_window.show()

    def save_configuration(self):
        # Implementation for saving configuration
        pass

    def load_configuration(self):
        # Implementation for loading configuration
        pass

    def clear_all_fields(self):
        # Implementation for clearing all fields
        pass

    def export_to_template(self):
        # Implementation for exporting to template
        pass

    def log_change(self, change_description):
        try:
            with open(self.changes_log_file, 'r+') as file:
                changes = json.load(file)
                if self.version not in changes:
                    changes[self.version] = []
                changes[self.version].append({
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "description": change_description
                })
                file.seek(0)
                json.dump(changes, file, indent=4)
                file.truncate()
        except FileNotFoundError:
            with open(self.changes_log_file, 'w') as file:
                json.dump({self.version: [{
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "description": change_description
                }]}, file, indent=4)
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {self.changes_log_file}")
