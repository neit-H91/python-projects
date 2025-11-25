import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QStackedWidget
from PyQt6.QtCore import Qt

class HomePage(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        layout = QVBoxLayout()
        label = QLabel("Welcome to the Vet App Home!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        button1 = QPushButton("Go to Page 1")
        button2 = QPushButton("Go to Page 2")
        button3 = QPushButton("Go to Page 3")
        button1.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        button2.clicked.connect(lambda: self.stack.setCurrentIndex(2))
        button3.clicked.connect(lambda: self.stack.setCurrentIndex(3))
        layout.addWidget(label)
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        self.setLayout(layout)

class Page1(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        layout = QVBoxLayout()
        label = QLabel("This is Page 1: Add Animal")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        back_button = QPushButton("Back to Home")
        back_button.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        layout.addWidget(label)
        layout.addWidget(back_button)
        self.setLayout(layout)

class Page2(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        layout = QVBoxLayout()
        label = QLabel("This is Page 2: View Appointments")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        back_button = QPushButton("Back to Home")
        back_button.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        layout.addWidget(label)
        layout.addWidget(back_button)
        self.setLayout(layout)

class Page3(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        layout = QVBoxLayout()
        label = QLabel("This is Page 3: Medicine History")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        back_button = QPushButton("Back to Home")
        back_button.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        layout.addWidget(label)
        layout.addWidget(back_button)
        self.setLayout(layout)

class VetApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vet App")
        self.setGeometry(100, 100, 400, 300)

        # Create the stacked widget
        self.stack = QStackedWidget()

        # Create pages
        home = HomePage(self.stack)
        page1 = Page1(self.stack)
        page2 = Page2(self.stack)
        page3 = Page3(self.stack)

        # Add to stack
        self.stack.addWidget(home)  # Index 0
        self.stack.addWidget(page1)  # Index 1
        self.stack.addWidget(page2)  # Index 2
        self.stack.addWidget(page3)  # Index 3

        # Set the stacked widget as central
        self.setCentralWidget(self.stack)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VetApp()
    window.show()
    sys.exit(app.exec())
