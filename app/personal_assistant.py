import os
import sys
from ai.chatgpt.chatgpy import ChatGpt
from view.views.pyqt_view import PyQtView
# make all the files of the app to have the app directory as one of the directories in the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

class PersonalAssistant:
    def __init__(self):
        self.chatgpt = ChatGpt()
        self.app_view = PyQtView(model_api=self.chatgpt)

    def start_app(self):
        self.app_view.init_view()
        self.app_view.run()


if __name__ == '__main__':
    personal_assistant = PersonalAssistant()
    personal_assistant.start_app()




