import os
import tkinter as tk
import datetime







# the openchat
from pyChatGPT import Chat, Options
options = Options()

# Track conversation
options.track = True 

# Optionally, you can pass a file path to save the conversation
# They're created if they don't exist
# get current time
import datetime
cur_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
cur_time = cur_time.replace(":", "-")
options.chat_log = os.path.join("app", "run_time_files", f"{cur_time}_chat_log.txt")
options.id_log = os.path.join("app", "run_time_files", f"{cur_time}_id_log.txt")

# Create a Chat object
chat = Chat(email="kirat77@gmail.com", password="Progriri1!", options=options)












import tkinter as tk

# Create the root window
root = tk.Tk()

# Create a text input widget
input_text = tk.StringVar()
input_field = tk.Text(root, height=10, width=50)
input_field.pack()

# Create a text field widget to display the output
output_field = tk.Text(root, height=10, width=50)
output_field.pack()

# Create a button widget
def show_output():
    # Get the input text
    input_str = input_field.get("1.0", tk.END)
    input_str = input_field.get("1.0", tk.END)
    answer = chat.ask(input_str)
    output_field.insert(tk.INSERT, answer)

button = tk.Button(root, text="Show Output", command=show_output)
button.pack()

# Run the main loop
root.mainloop()












# Run the main loop
root.mainloop()




