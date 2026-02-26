# app.py
import sys
import json
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
                             QPushButton, QFileDialog, QScrollArea, QMessageBox, QComboBox, QTextEdit,
                             QDateEdit, QTabWidget, QListWidget, QDialog, QDialogButtonBox, QPlainTextEdit,
                             QMainWindow, QDesktopWidget)
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont, QIcon, QFontDatabase
from datetime import datetime

class TaskDialog(QDialog):
    task_statuses = ["Not Started", "In Progress", "Completed"]  # Default statuses

    def __init__(self, parent=None, task=None):
        super().__init__(parent)
        self.setWindowTitle("Task Details")
        self.layout = QVBoxLayout(self)

        self.task_id = QLineEdit(self)
        self.task_name = QLineEdit(self)
        self.task_description = QTextEdit(self)
        self.task_status = QComboBox(self)
        self.task_status.addItems(self.task_statuses)
        self.task_due_date = QDateEdit(self)
        self.task_due_date.setCalendarPopup(True)

        self.layout.addWidget(QLabel("Task ID:"))
        self.layout.addWidget(self.task_id)
        self.layout.addWidget(QLabel("Task Name:"))
        self.layout.addWidget(self.task_name)
        self.layout.addWidget(QLabel("Task Description:"))
        self.layout.addWidget(self.task_description)
        self.layout.addWidget(QLabel("Task Status:"))
        self.layout.addWidget(self.task_status)
        self.layout.addWidget(QLabel("Due Date:"))
        self.layout.addWidget(self.task_due_date)

        self.buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        self.layout.addWidget(self.buttons)

        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

        if task:
            self.task_id.setText(task.get('task_id', ''))
            self.task_name.setText(task.get('task_name', ''))
            self.task_description.setPlainText(task.get('task_description', ''))
            self.task_status.setCurrentText(task.get('task_status', 'Not Started'))
            self.task_due_date.setDate(QDate.fromString(task.get('task_due_date', ''), 'yyyy-MM-dd'))

    def get_task_data(self):
        return {
            'task_id': self.task_id.text(),
            'task_name': self.task_name.text(),
            'task_description': self.task_description.toPlainText(),
            'task_status': self.task_status.currentText(),
            'task_due_date': self.task_due_date.date().toString('yyyy-MM-dd')
        }

class ProjectWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Project Details")
        self.setCentralWidget(ProjectTab())
        self.resize(600, 400)

class TasksWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Tasks")
        self.setCentralWidget(TasksTab())
        self.resize(600, 400)

class SummaryWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Summary")
        self.setCentralWidget(SummaryTab())
        self.resize(600, 400)

class ProjectTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        content = QWidget()
        scroll_layout = QVBoxLayout(content)

        self.fields = {}
        labels = [
            "🆔 Project ID", "📛 Project Name", "👤 Project Owner", "📝 Project Description",
            "🗓️ Project Start Date", "🏁 Project End Date"
        ]

        for label in labels:
            if 'Date' in label:
                widget = QDateEdit()
                widget.setCalendarPopup(True)
            else:
                widget = QLineEdit() if "Description" not in label else QTextEdit()
            self.add_field(label, widget, scroll_layout)

        self.add_field("🚦 Project Status", QComboBox(), scroll_layout)
        self.fields["🚦 Project Status"].addItems(["Not Started", "In Progress", "Completed", "On Hold"])

        self.add_field("🌐 Languages", QLineEdit(), scroll_layout)
        self.add_field("💻 Technologies", QLineEdit(), scroll_layout)

        scroll.setWidget(content)
        self.layout.addWidget(scroll)

    def add_field(self, label, widget, layout):
        field_layout = QHBoxLayout()
        label_widget = QLabel(label)
        label_widget.setFont(QFont("Arial", 18, QFont.Bold))
        field_layout.addWidget(label_widget)
        field_layout.addWidget(widget)
        layout.addLayout(field_layout)
        self.fields[label] = widget

class TasksTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.task_list = QListWidget()
        self.layout.addWidget(self.task_list)

        button_layout = QHBoxLayout()
        add_task_button = QPushButton("➕ Add Task")
        add_task_button.clicked.connect(self.add_task)
        button_layout.addWidget(add_task_button)

        edit_task_button = QPushButton("✏️ Edit Task")
        edit_task_button.clicked.connect(self.edit_task)
        button_layout.addWidget(edit_task_button)

        remove_task_button = QPushButton("❌ Remove Task")
        remove_task_button.clicked.connect(self.remove_task)
        button_layout.addWidget(remove_task_button)

        self.layout.addLayout(button_layout)

    def add_task(self):
        dialog = TaskDialog(self)
        if dialog.exec_():
            task_data = dialog.get_task_data()
            self.task_list.addItem(f"{task_data['task_id']}: {task_data['task_name']}")
            self.task_list.setCurrentRow(self.task_list.count() - 1)
            self.log_change(f"Task added: {task_data['task_id']}")

    def edit_task(self):
        current_item = self.task_list.currentItem()
        if current_item:
            index = self.task_list.row(current_item)
            task_data = self.get_task_data(index)
            dialog = TaskDialog(self, task_data)
            if dialog.exec_():
                new_task_data = dialog.get_task_data()
                self.update_task_data(index, new_task_data)
                current_item.setText(f"{new_task_data['task_id']}: {new_task_data['task_name']}")
                self.log_change(f"Task edited: {new_task_data['task_id']}")

    def remove_task(self):
        current_item = self.task_list.currentItem()
        if current_item:
            task_text = current_item.text()
            self.task_list.takeItem(self.task_list.row(current_item))
            self.log_change(f"Task removed: {task_text}")

    def get_task_data(self, index):
        item = self.task_list.item(index)
        if item:
            task_id, task_name = item.text().split(': ', 1)
            return {
                'task_id': task_id,
                'task_name': task_name,
                'task_description': item.data(Qt.UserRole),
                'task_status': item.data(Qt.UserRole + 1),
                'task_due_date': item.data(Qt.UserRole + 2)
            }
        return None

    def update_task_data(self, index, new_data):
        item = self.task_list.item(index)
        if item:
            item.setText(f"{new_data['task_id']}: {new_data['task_name']}")
            item.setData(Qt.UserRole, new_data['task_description'])
            item.setData(Qt.UserRole + 1, new_data['task_status'])
            item.setData(Qt.UserRole + 2, new_data['task_due_date'])

    def log_change(self, change_description):
        try:
            # Load existing changes
            try:
                with open(self.changes_log_file, 'r') as file:
                    changes = json.load(file)
            except FileNotFoundError:
                changes = {}

            # Add new change
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if self.version not in changes:
                changes[self.version] = []
            changes[self.version].append({
                "timestamp": current_time,
                "description": change_description
            })

            # Save updated changes
            with open(self.changes_log_file, 'w') as file:
                json.dump(changes, file, indent=4)

        except Exception as e:
            print(f"Error logging change: {str(e)}")

class SummaryTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        
        # יצירת תיבות טקסט לסיכומים שונים
        self.summary_fields = {}
        summaries = [
            "Project Overview",
            "Technical Details",
            "Task Summary",
            "Full Project Description"
        ]
        
        for summary in summaries:
            text_edit = QPlainTextEdit()
            text_edit.setReadOnly(True)
            copy_button = QPushButton(f"Copy {summary}")
            copy_button.clicked.connect(lambda checked, t=text_edit: self.copy_to_clipboard(t))
            
            field_layout = QVBoxLayout()
            field_layout.addWidget(QLabel(summary))
            field_layout.addWidget(text_edit)
            field_layout.addWidget(copy_button)
            
            self.layout.addLayout(field_layout)
            self.summary_fields[summary] = text_edit

        # כפתור לעדכון הסיכום
        update_button = QPushButton("Update Summary")
        update_button.clicked.connect(self.update_summary)
        self.layout.addWidget(update_button)

    def copy_to_clipboard(self, text_edit):
        QApplication.clipboard().setText(text_edit.toPlainText())
        QMessageBox.information(self, "Copied", "Text copied to clipboard!")

    def update_summary(self):
        # Project Overview
        overview = f"Project: {self.fields['📛 Project Name'].text()}\n"
        overview += f"ID: {self.fields['🆔 Project ID'].text()}\n"
        overview += f"Owner: {self.fields['👤 Project Owner'].text()}\n"
        overview += f"Status: {self.fields['🚦 Project Status'].currentText()}\n"
        overview += f"Start Date: {self.fields['🗓️ Project Start Date'].date().toString('yyyy-MM-dd')}\n"
        overview += f"End Date: {self.fields['🏁 Project End Date'].date().toString('yyyy-MM-dd')}"
        self.summary_fields["Project Overview"].setPlainText(overview)

        # Technical Details
        tech_details = f"Languages: {self.fields['🌐 Languages'].text()}\n"
        tech_details += f"Technologies: {self.fields['💻 Technologies'].text()}"
        self.summary_fields["Technical Details"].setPlainText(tech_details)

        # Task Summary
        task_summary = "Tasks:\n"
        for i in range(self.task_list.count()):
            task_data = self.get_task_data(i)
            task_summary += f"- {task_data['task_name']} (Status: {task_data['task_status']})\n"
        self.summary_fields["Task Summary"].setPlainText(task_summary)

        # Full Project Description
        full_description = f"Project Description:\n{self.fields['📝 Project Description'].toPlainText()}\n\n"
        full_description += overview + "\n\n" + tech_details + "\n\n" + task_summary
        self.summary_fields["Full Project Description"].setPlainText(full_description)

class ProjectConfigurator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.version = "0.7"
        self.changes_log_file = "version_changes.json"
        self.presets_file = "presets.json"
        self.load_presets()
        self.initUI()

        self.project_window = ProjectWindow(self)
        self.tasks_window = TasksWindow(self)
        self.summary_window = SummaryWindow(self)

    def load_presets(self):
        try:
            with open(self.presets_file, 'r') as file:
                self.presets = json.load(file)
            print(f"Presets loaded successfully: {list(self.presets.keys())}")
        except FileNotFoundError:
            self.presets = {}
            print(f"Presets file {self.presets_file} not found.")
        except json.JSONDecodeError:
            self.presets = {}
            print(f"Error decoding JSON from {self.presets_file}.")

    def initUI(self):
        # Set a larger base font for the entire application
        font = QFont("Arial", 18)
        self.setFont(font)

        self.setWindowTitle('🚀 Project Configurator v0.7')
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

    def open_project_window(self):
        self.project_window.show()

    def open_tasks_window(self):
        self.tasks_window.show()

    def open_summary_window(self):
        self.summary_window.show()

    def save_configuration(self):
        try:
            data = {
                "project_id": self.project_window.fields["🆔 Project ID"].text(),
                "project_name": self.project_window.fields["📛 Project Name"].text(),
                "project_owner": self.project_window.fields["👤 Project Owner"].text(),
                "project_description": self.project_window.fields["📝 Project Description"].toPlainText(),
                "project_start_date": self.project_window.fields["🗓️ Project Start Date"].date().toString('yyyy-MM-dd'),
                "project_end_date": self.project_window.fields["🏁 Project End Date"].date().toString('yyyy-MM-dd'),
                "project_status": self.project_window.fields["🚦 Project Status"].currentText(),
                "project_tasks": [self.tasks_window.get_task_data(i) for i in range(self.tasks_window.task_list.count())],
                "languages": [lang.strip() for lang in self.project_window.fields["🌐 Languages"].text().split(',')],
                "technologies": [tech.strip() for tech in self.project_window.fields["💻 Technologies"].text().split(',')]
            }

            options = QFileDialog.Options()
            file_name, _ = QFileDialog.getSaveFileName(self, "Save Configuration", "", "JSON Files (*.json)", options=options)
            if file_name:
                with open(file_name, 'w') as file:
                    json.dump(data, file, indent=4)
                QMessageBox.information(self, "Success", "Configuration saved successfully!")
                self.log_change("Configuration saved")
                self.summary_window.update_summary()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while saving: {str(e)}")
            self.log_change(f"Error saving configuration: {str(e)}")

    def load_configuration(self):
        try:
            options = QFileDialog.Options()
            file_name, _ = QFileDialog.getOpenFileName(self, "Load Configuration", "", "JSON Files (*.json)", options=options)
            if file_name:
                with open(file_name, 'r') as file:
                    data = json.load(file)
                
                for key, value in data.items():
                    if key in self.project_window.fields:
                        if isinstance(self.project_window.fields[key], QLineEdit):
                            self.project_window.fields[key].setText(str(value))
                        elif isinstance(self.project_window.fields[key], QTextEdit):
                            self.project_window.fields[key].setPlainText(str(value))
                        elif isinstance(self.project_window.fields[key], QComboBox):
                            index = self.project_window.fields[key].findText(str(value))
                            if index >= 0:
                                self.project_window.fields[key].setCurrentIndex(index)
                        elif isinstance(self.project_window.fields[key], QDateEdit):
                            self.project_window.fields[key].setDate(QDate.fromString(value, 'yyyy-MM-dd'))
                
                self.tasks_window.task_list.clear()
                for task in data.get('project_tasks', []):
                    self.tasks_window.task_list.addItem(f"{task['task_id']}: {task['task_name']}")

                QMessageBox.information(self, "Success", "Configuration loaded successfully!")
                self.log_change("Configuration loaded")
                self.summary_window.update_summary()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while loading: {str(e)}")
            self.log_change(f"Error loading configuration: {str(e)}")

    def clear_all_fields(self):
        for field in self.project_window.fields.values():
            if isinstance(field, (QLineEdit, QTextEdit)):
                field.clear()
            elif isinstance(field, QComboBox):
                field.setCurrentIndex(0)
            elif isinstance(field, QDateEdit):
                field.setDate(QDate.currentDate())
        
        self.tasks_window.task_list.clear()
        
        QMessageBox.information(self, "Success", "All fields have been cleared!")
        self.log_change("All fields cleared")
        self.summary_window.update_summary()

    def log_change(self, change_description):
        try:
            # Load existing changes
            try:
                with open(self.changes_log_file, 'r') as file:
                    changes = json.load(file)
            except FileNotFoundError:
                changes = {}

            # Add new change
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if self.version not in changes:
                changes[self.version] = []
            changes[self.version].append({
                "timestamp": current_time,
                "description": change_description
            })

            # Save updated changes
            with open(self.changes_log_file, 'w') as file:
                json.dump(changes, file, indent=4)

        except Exception as e:
            print(f"Error logging change: {str(e)}")

    def export_to_template(self):
        try:
            data = {
                "project_id": self.project_window.fields["🆔 Project ID"].text(),
                "project_name": self.project_window.fields["📛 Project Name"].text(),
                "project_owner": self.project_window.fields["👤 Project Owner"].text(),
                "project_description": self.project_window.fields["📝 Project Description"].toPlainText(),
                "project_start_date": self.project_window.fields["🗓️ Project Start Date"].date().toString('yyyy-MM-dd'),
                "project_end_date": self.project_window.fields["🏁 Project End Date"].date().toString('yyyy-MM-dd'),
                "project_status": self.project_window.fields["🚦 Project Status"].currentText(),
                "project_tasks": [self.tasks_window.get_task_data(i) for i in range(self.tasks_window.task_list.count())],
                "languages": [lang.strip() for lang in self.project_window.fields["🌐 Languages"].text().split(',')],
                "technologies": [tech.strip() for tech in self.project_window.fields["💻 Technologies"].text().split(',')]
            }

            options = QFileDialog.Options()
            file_name, _ = QFileDialog.getSaveFileName(self, "Export to Template", "", "JSON Files (*.json)", options=options)
            if file_name:
                with open(file_name, 'w') as file:
                    json.dump(data, file, indent=2)
                QMessageBox.information(self, "Success", "Project exported to template successfully!")
                self.log_change("Project exported to template")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while exporting: {str(e)}")
            self.log_change(f"Error exporting to template: {str(e)}")

    def apply_preset(self):
        selected_preset = self.preset_selector.currentText()
        print(f"Selected preset: {selected_preset}")
        if selected_preset != "Select Preset":
            preset_data = self.presets.get(selected_preset)
            if preset_data:
                print(f"Applying preset: {selected_preset}")
                
                # Apply preset data to fields
                self.project_window.fields["🆔 Project ID"].setText(preset_data.get("project_id", ""))
                self.project_window.fields["📛 Project Name"].setText(preset_data.get("project_name", ""))
                self.project_window.fields["👤 Project Owner"].setText(preset_data.get("project_owner", ""))
                self.project_window.fields["📝 Project Description"].setPlainText(preset_data.get("project_description", ""))
                
                # Update project status options
                status_field = self.project_window.fields["🚦 Project Status"]
                status_field.clear()
                status_field.addItems(preset_data.get("project_status", []))
                if preset_data.get("project_status"):
                    status_field.setCurrentIndex(0)
                
                # Update languages and technologies
                self.project_window.fields["🌐 Languages"].setText(", ".join(preset_data.get("languages", [])))
                self.project_window.fields["💻 Technologies"].setText(", ".join(preset_data.get("technologies", [])))
                
                # Update task statuses in TaskDialog
                TaskDialog.task_statuses = preset_data.get("task_statuses", ["Not Started", "In Progress", "Completed"])
                
                self.log_change(f"Applied preset: {selected_preset}")
                QMessageBox.information(self, "Preset Applied", f"The {selected_preset} preset has been applied.")

                # Reset dates to current date
                current_date = QDate.currentDate()
                self.project_window.fields["🗓️ Project Start Date"].setDate(current_date)
                self.project_window.fields["🏁 Project End Date"].setDate(current_date)

                # Clear existing tasks
                self.tasks_window.task_list.clear()
                self.summary_window.update_summary()
            else:
                print(f"Preset data not found for: {selected_preset}")
        else:
            print("No preset selected")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # Set the default font for the entire application
    font = QFont("Arial", 18)
    app.setFont(font)
    
    ex = ProjectConfigurator()
    ex.show()
    sys.exit(app.exec_())
