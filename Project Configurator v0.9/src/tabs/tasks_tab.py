from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget
from PyQt5.QtCore import Qt
from src.dialogs.task_dialog import TaskDialog

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
        # This method should be implemented in the main ProjectConfigurator class
        pass
