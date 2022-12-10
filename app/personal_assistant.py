import tkinter as tk








# the openchat
from pyChatGPT import Chat, Options
options = Options()

# Track conversation
options.track = True 

# Optionally, you can pass a file path to save the conversation
# They're created if they don't exist
options.chat_log = "chat_log.txt"
options.id_log = "id_log.txt"

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




