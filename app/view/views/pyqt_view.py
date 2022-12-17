import threading
from ai.model_api import ModelApi
from view.app_view import AppView
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt


class PyQtView(AppView, QWidget):
    def __init__(self, model_api: ModelApi):
        self.qapp = QApplication(sys.argv)
        AppView.__init__(self)
        QWidget.__init__(self)
        self.model_api = model_api

        # Set up the rest of the main window
        self.setWindowTitle("Personal Assistant")

    def send_text(self):
        def _run_in_thread():
            # Get the text from the input text widget
            text = self.model_api.get_answer(self.input_text.toPlainText())
            # Append the text to the output text widget
            self.output_text.append(text)
        threading.Thread(target=_run_in_thread).start()
        
    def input_key_press_event(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            if event.modifiers() & Qt.ControlModifier:
                self.input_text.insertPlainText("\n")
            else:
                # Simulate a click on the send_button
                self.send_button.click()
        else:
            # Call the original keyPressEvent method for other key press events
            QTextEdit.keyPressEvent(self.input_text, event)

    def init_view(self):
        # Create the input text widget
        self.input_text = QTextEdit(self)
        self.input_text.keyPressEvent = self.input_key_press_event

        # Create the send button
        self.send_button = QPushButton('Send', self)

        # Create the output text widget
        self.output_text = QTextEdit(self)
        self.output_text.setReadOnly(True)
        # Connect the send button's clicked signal to the send_text slot
        self.send_button.clicked.connect(self.send_text)

        # Lay out the widgets in a vertical layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.input_text)
        layout.addWidget(self.send_button)
        layout.addWidget(self.output_text)

    def run(self):
        self.show()
        sys.exit(self.qapp.exec_())

