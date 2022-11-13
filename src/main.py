from tkinter import *
def inputtoken():
    class Window(Frame):
        frame = Tk()
        frame.title("Add Tokens")
        root.iconbitmap('img/middle.ico')
        frame.geometry('400x200')
        entry= Entry(root, width= 40)
        entry.pack()

        
        root = Tk()
    app = Window(root)
    root.wm_title("HoodBot By: TheMiddleErmine")
    root.iconbitmap('img/middle.ico')
    root.mainloop()


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        menu = Menu(self.master)
        self.master.config(menu=menu)

        setupMenu = Menu(menu, tearoff=False)
        setupMenu.add_separator()

        sub_menu = Menu(setupMenu, tearoff=0)
        sub_menu.add_command(label='Add Token', command=inputtoken)
        sub_menu.add_command(label='Upload Tokens (Unavaliable)')
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
root.iconbitmap('img/middle.ico')
root.mainloop()

