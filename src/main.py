from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

        setupMenu = Menu(menu, tearoff=False)
        setupMenu.add_separator()

        sub_menu = Menu(setupMenu, tearoff=0)
        sub_menu.add_command(label='Add Token')
        sub_menu.add_command(label='Upload Tokens')
        setupMenu.add_cascade(
            label="Tokens",
            menu=sub_menu
)

        menu.add_cascade(label="Setup", menu=setupMenu)

    def exitProgram(self):
        exit()
        
root = Tk()
app = Window(root)
root.wm_title("HoodBot By: TheMiddleErmine")
root.iconbitmap("middle.ico")
root.mainloop()