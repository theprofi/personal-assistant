import threading
import tkinter as tk
from ai.model_api import ModelApi
from view.app_view import AppView


class TkView(AppView):
    def __init__(self, model_api: ModelApi):
        self.root = tk.Tk()
        self.model_api = model_api

    def update_output(self, output_field, output_str: str):
        output_field.configure(state='normal')
        output_field.insert('1.0', output_str + "\n" + "=" * 50)
        output_field.configure(state='disabled')

    def init_view(self):
        # create a text input widget
        input_field = tk.Text(self.root, height=10, width=50)
        input_field.pack()

        # create a text field widget to display the output
        output_field = tk.Text(self.root)
        output_field.pack()

        # Function to resize the textbox when the window is resized
        def resize_textbox(event):
            output_field.config(width=event.width)

        # Bind the resize_textbox function to the root window
        self.root.bind('<Configure>', resize_textbox)

        # create a button widget
        def show_output(*args, **kwargs):
            def __thread_func():
                # get the input text
                input_str = input_field.get("1.0", tk.END)
                self.update_output(output_field, self.model_api.get_answer(input_str))

            threading.Thread(target=__thread_func).start()

        button = tk.Button(self.root, text="Show Output", command=show_output)
        self.root.bind('<Return>', show_output)
        button.pack()

    def run(self):
        self.root.mainloop()