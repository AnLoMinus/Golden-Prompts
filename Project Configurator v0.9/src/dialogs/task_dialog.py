from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit, QComboBox, QDateEdit, QDialogButtonBox
from PyQt5.QtCore import Qt, QDate

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
