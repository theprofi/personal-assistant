import os
import sys
import threading
from ai.chatgpt.chatgpy import ChatGpt
from view.tk_view.tk_view import TkView

APP_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(APP_DIR)

class PersonalAssistant:
    def __init__(self):
        self.chatgpt = ChatGpt()
        self.app_view = TkView(model_api=self.chatgpt)

    def start_app(self):
        self.app_view.init_view()
        self.app_view.run()


if __name__ == '__main__':
    personal_assistant = PersonalAssistant()
    personal_assistant.start_app()




