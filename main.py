import tkinter as tk

def delete_note_func():
    content = note.get("1.0", tk.END)
    content_key = content[:10].strip()
    if content_key in notes:
        del notes[content_key]
        show_history_notes()

def save_note_func():
    content = note.get("1.0", tk.END)
    content_key = content[:10].strip()
    notes[content_key] = content
    show_history_notes()

def show_note_func(t):
    note.delete("1.0", tk.END)
    note.insert('1.0', notes[t])

def show_history_notes():
    for button in history_notes:
        button.destroy()

    for note_key in notes.keys():
        history_notes.append(tk.Button(
            text=note_key,
            master=notes_list,
            command=lambda t=note_key: show_note_func(t)
        ))
        history_notes[-1].pack(fill=tk.X)

notes = {}
window = tk.Tk()
window.rowconfigure([0, 1], minsize=50)
window.columnconfigure([0, 1, 2], minsize=50)

notes_list = tk.Frame(width=50, height=50)
history_notes = []

delete_note = tk.Button(text="Delete", command=delete_note_func)
save_note = tk.Button(text="Save", command=save_note_func)
note = tk.Text(width=100, height=50)

delete_note.grid(row=0, column=0)
save_note.grid(row=0, column=2)
notes_list.grid(row=1, column=0)
note.grid(row=1, column=1)

window.mainloop()
