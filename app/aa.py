from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QHBoxLayout, QVBoxLayout, QWidget

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the input text field and output textbox
        self.input_text = QTextEdit(self)
        self.output_text = QTextEdit(self)
        self.output_text.setReadOnly(True)

        # Create the send button
        self.send_button = QPushButton('Send', self)

        # Set up the layout
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.input_text)
        hlayout.addWidget(self.send_button)

        vlayout = QVBoxLayout()
        vlayout.addLayout(hlayout)
        vlayout.addWidget(self.output_text)

        central_widget = QWidget(self)
        central_widget.setLayout(vlayout)
        self.setCentralWidget(central_widget)

        # Connect the send button to a slot
        self.send_button.clicked.connect(self.send)

    def send(self):
        # Copy the text from the input text field to the output textbox
        text = self.input_text.toPlainText()
        self.output_text.setText(text)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
