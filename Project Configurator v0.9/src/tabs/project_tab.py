from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit, QComboBox, QDateEdit, QScrollArea
from PyQt5.QtGui import QFont

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
