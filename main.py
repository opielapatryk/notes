#import tkinter
import tkinter as tk 
window = tk.Tk()
window.rowconfigure([0, 1], minsize=50)
window.columnconfigure([0, 1], minsize=50)
notes = []
delete_note = tk.Button(text="Delete")
create_note = tk.Button(text="Create")
notes_list = tk.Frame(width=50,height=50)
note = tk.Text(width=100,height=50)

delete_note.grid(row=0,column=0)
create_note.grid(row=0,column=1)
notes_list.grid(row=1,column=0)
note.grid(row=1,column=1)

window.mainloop()
#create layout
#when write automatically save
#add new notes
#delete old notes

# def print_url(event):
#     url = ent_url.get()
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, "html.parser")
#     page_txt.delete(1.0, tk.END)  # Clear previous content
#     page_txt.insert(tk.END, soup.text)

# search_btn.bind("<Button-1>", print_url)
