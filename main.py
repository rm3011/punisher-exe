import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
)


class PunisherApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PUNISHER.EXE")
        self.resize(600, 420)

        self.setStyleSheet("""
            QWidget {
                background-color: #0B0D12;
                color: #F5F5F5;
                font-family: Segoe UI;
                font-size: 14px;
            }

            QLabel#title {
                font-size: 30px;
                font-weight: 800;
            }

            QLabel#subtitle {
                color: #A1A1AA;
                font-size: 13px;
            }

            QPushButton {
                background-color: #E63946;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 12px;
                font-weight: 700;
            }

            QPushButton:hover {
                background-color: #FF4D5A;
            }
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(32, 32, 32, 32)
        layout.setSpacing(18)

        title = QLabel("PUNISHER.EXE")
        title.setObjectName("title")
        layout.addWidget(title)

        subtitle = QLabel(
            "Your distractions have consequences."
        )
        subtitle.setObjectName("subtitle")
        layout.addWidget(subtitle)

        layout.addStretch()

        self.status = QLabel(
            "No focus session running."
        )
        self.status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.status)

        self.start_button = QPushButton("START SESSION")
        self.start_button.clicked.connect(self.start_session)
        layout.addWidget(self.start_button)

        layout.addStretch()

        footer = QLabel(
            "FOCUS  /  BUILD  /  REPEAT"
        )
        footer.setObjectName("subtitle")
        footer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(footer)

    def start_session(self):
        self.status.setText(
            "Session setup is the next step."
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PunisherApp()
    window.show()
    sys.exit(app.exec())
