from tkinter import *

class ScrollbarFrame():
    def __init__(self, parent):
        self.canvas = Canvas(parent, width=parent.winfo_width(), height=parent.winfo_height())
        self.frame = Frame(self.canvas)
        self.frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.scrollbar = Scrollbar(parent, orient=HORIZONTAL, command=self.canvas.xview)
        self.scrollbar.pack(side=BOTTOM, fill=X)
        
        self.canvas.create_window((0,0), window=self.frame, anchor="nw")
        self.canvas.configure(xscrollcommand=self.scrollbar.set)
        self.canvas.pack()

        self.canvas.bind("<MouseWheel>", self._on_mousewheel)

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
