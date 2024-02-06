import tkinter as tk
from tkinter import ttk

def rot13(text):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            result += char
    return result

def on_click():
    text = text_input.get()
    text_output.set(rot13(text))

root = tk.Tk()
root.title("ROT13 Cypher")
root.resizable(False, False)

mainframe = ttk.Frame(root, padding="24 12 24 12")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

text_input = tk.StringVar()
text_output = tk.StringVar()

input_entry = ttk.Entry(mainframe, width=30, textvariable=text_input)
input_entry.grid(column=1, row=1)

output_entry = ttk.Entry(mainframe, width=30, textvariable=text_output, state="readonly")
output_entry.grid(column=1, row=2)

ttk.Button(mainframe, text="ROT13", command=on_click).grid(column=2, row=1)

ttk.Label(mainframe, text="Input:").grid(column=0, row=1, sticky=tk.W)
ttk.Label(mainframe, text="Output:").grid(column=0, row=2, sticky=tk.W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

input_entry.focus()
root.bind('<Return>', lambda e: on_click())

root.mainloop()

