from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QPlainTextEdit, QMessageBox
from PyQt5.QtGui import QClipboard
from PyQt5.QtCore import QDate

class SummaryTab(QWidget):
    def __init__(self, project_window, tasks_window):
        super().__init__()
        self.project_window = project_window
        self.tasks_window = tasks_window
        self.layout = QVBoxLayout(self)
        
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

        update_button = QPushButton("Update Summary")
        update_button.clicked.connect(self.update_summary)
        self.layout.addWidget(update_button)

    def copy_to_clipboard(self, text_edit):
        QClipboard().setText(text_edit.toPlainText())
        QMessageBox.information(self, "Copied", "Text copied to clipboard!")

    def update_summary(self):
        project_fields = self.project_window.fields
        overview = f"Project: {project_fields['📛 Project Name'].text()}\n"
        overview += f"ID: {project_fields['🆔 Project ID'].text()}\n"
        overview += f"Owner: {project_fields['👤 Project Owner'].text()}\n"
        overview += f"Status: {project_fields['🚦 Project Status'].currentText()}\n"
        overview += f"Start Date: {project_fields['🗓️ Project Start Date'].date().toString('yyyy-MM-dd')}\n"
        overview += f"End Date: {project_fields['🏁 Project End Date'].date().toString('yyyy-MM-dd')}"
        self.summary_fields["Project Overview"].setPlainText(overview)

        tech_details = f"Languages: {project_fields['🌐 Languages'].text()}\n"
        tech_details += f"Technologies: {project_fields['💻 Technologies'].text()}"
        self.summary_fields["Technical Details"].setPlainText(tech_details)

        task_list = self.tasks_window.centralWidget().task_list
        task_summary = "Tasks:\n"
        for i in range(task_list.count()):
            task_data = self.tasks_window.centralWidget().get_task_data(i)
            task_summary += f"- {task_data['task_name']} (Status: {task_data['task_status']})\n"
        self.summary_fields["Task Summary"].setPlainText(task_summary)

        full_description = f"Project Description:\n{project_fields['📝 Project Description'].toPlainText()}\n\n"
        full_description += overview + "\n\n" + tech_details + "\n\n" + task_summary
        self.summary_fields["Full Project Description"].setPlainText(full_description)
