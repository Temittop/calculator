import tkinter as tk

window = tk.Tk()
def increase():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"

def decrease():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 1}"


window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

frame_a = tk.Frame(master=window, relief='flat', borderwidth=8)
frame_a.pack()
frame_b = tk.Frame(master=window, relief='flat', borderwidth=8)
frame_b.pack()
btn_decrease = tk.Button(master=frame_b, text="-", command=decrease)
btn_decrease.grid(row=0, column=0, sticky="nwse")

lbl_value = tk.Label(master=frame_b, text="0", width=10)
lbl_value.grid(row=0, column=1)

btn_increase = tk.Button(master=frame_b, text="+", bg='red', fg='green', width=25, command=increase)
btn_increase.grid(row=0, column=2, sticky="nwse")
entry = tk.Entry(master=frame_a, width=50)
entry.grid(row=1, column=0, sticky='nswe')
window.mainloop()