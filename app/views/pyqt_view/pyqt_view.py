import threading
from ai.model_api import ModelApi
from views.app_view import AppView
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontMetrics
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QColor, QTextCharFormat, QFont, QSyntaxHighlighter
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtGui import QTextCursor

lock = threading.Lock()

class CodeHighlighter(QSyntaxHighlighter):
    def __init__(self, parent):
        super().__init__(parent)
        self.keyword_format = QTextCharFormat()
        self.keyword_format.setForeground(QColor('#0000ff'))
        self.keyword_format.setBackground(QColor('#808080'))
        self.keywords = ['print', 'for', 'while', 'if', 'else']
        self.keyword_pattern = QRegExp('\\b(?:' + '|'.join(self.keywords) + ')\\b\\s*\\([^)]*\\)')

    def highlightBlock(self, text):
        index = self.keyword_pattern.indexIn(text)
        while index >= 0:
            length = self.keyword_pattern.matchedLength()
            self.setFormat(index, length, self.keyword_format)
            index = self.keyword_pattern.indexIn(text, index + length)

class PyQtView(AppView, QWidget):
    def __init__(self, model_api: ModelApi):
        self.qapp = QApplication(sys.argv)
        AppView.__init__(self)
        QWidget.__init__(self)
        self.model_api = model_api

        # Set up the rest of the main window
        self.setWindowTitle("Personal Assistant")
        self.qapp.setStyle("Fusion")

        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Window, Qt.black)
        dark_palette.setColor(QPalette.WindowText, Qt.white)
        dark_palette.setColor(QPalette.Base, Qt.black)
        dark_palette.setColor(QPalette.AlternateBase, Qt.darkGray)
        dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
        dark_palette.setColor(QPalette.ToolTipText, Qt.white)
        dark_palette.setColor(QPalette.Text, Qt.white)
        dark_palette.setColor(QPalette.Button, Qt.black)
        dark_palette.setColor(QPalette.ButtonText, Qt.white)
        dark_palette.setColor(QPalette.BrightText, Qt.red)
        dark_palette.setColor(QPalette.Link, Qt.blue)
        dark_palette.setColor(QPalette.Highlight, Qt.blue)
        dark_palette.setColor(QPalette.HighlightedText, Qt.black)
        self.qapp.setPalette(dark_palette)

    def send_text(self):
        def _run_in_thread():
            with lock:
                # Get the text from the input text widget
                cursor = QTextCursor(self.output_text.document())
                # set the cursor position (defaults to 0 so this is redundant)
                cursor.setPosition(0)
                self.output_text.setTextCursor(cursor)
                text = self.model_api.get_answer(self.input_text.toPlainText())
                # append the text to the output text widget
                self.output_text.insertPlainText(self.input_text.toPlainText() + ":\n" + text)
                self.output_text.insertHtml("<hr>")
        threading.Thread(target=_run_in_thread).start()
        
    def input_key_press_event(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            if event.modifiers() & Qt.ControlModifier:
                self.input_text.insertPlainText("\n")
            else:
                # simulate a click on the send_button
                self.send_text()
        else:
            # call the original keyPressEvent method for other key press events
            QTextEdit.keyPressEvent(self.input_text, event)

    def resize_text_box(self):
        doc = self.input_text.document()
        self.input_text.setFixedHeight(int(doc.size().height()))

    def init_view(self):
        # create the input text widget
        self.input_text = QTextEdit(self)
        self.input_text.textChanged.connect(self.resize_text_box)
        self.input_text.keyPressEvent = self.input_key_press_event
        self.input_text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        palette = self.input_text.palette()
        palette.setColor(QPalette.Base, QColor('#353531'))
        self.input_text.setPalette(palette)

        font = self.input_text.font()
        font_metrics = QFontMetrics(font)
        bounding_rect = font_metrics.boundingRect("ABCDEF")
        self.input_text.setFixedHeight(bounding_rect.height())

        # create the output text widget
        self.output_text = QTextEdit(self)
        self.output_text.setReadOnly(True)
        self.output_text.highlighter = CodeHighlighter(self.output_text.document())
        # connect the send button's clicked signal to the send_text slot

        # lay out the widgets in a vertical layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.output_text)
        layout.addWidget(self.input_text)

    def run(self):
        screen_resolution = self.qapp.desktop().screenGeometry()
        width, height = screen_resolution.width(), screen_resolution.height()
        self.resize(int(width/2), int(height/2))
        self.show()
        sys.exit(self.qapp.exec_())

