# from hash_maker import HashMaker
# import tkinter as tk

# def main():
#     temp = tk.Button()
#     temp["text"] = "Click this"
#     temp["command"] = "Nice Job!"
#     temp.pack(side="top")


#     root = tk.Tk()
#     super().__init__(root)


#     print("This is a test")

# if __name__ == "__main__":
#     main

import tkinter as tk

from hash_maker import HashMaker


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.hash_obj = HashMaker()

    def create_widgets(self):
        self.canvas = tk.Canvas(self,height=50, width=100,bg="Black")
        self.text_id = self.canvas.create_text(50,25,anchor=tk.CENTER, text="", fill="Yellow")
        self.hash_button = tk.Button(self,bg = "Yellow", height = 2, bd = 10,activeforeground='red')
        self.hash_button["text"] = "Create Hash"
        self.hash_button["command"] = self.obtain_hash
        self.hash_button.pack(side="top")
        self.canvas.pack()

        self.quit_button = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit_button.pack(side="bottom")

    def obtain_hash(self):
        self.hash_obj = HashMaker()
        self.hash_obj.create_hash()
        hash_value = self.hash_obj.get_hash()
        #format(hash_value,'x')
        self.canvas.itemconfigure(self.text_id, text = format(hash_value,'x') )
        #print(format(hash_value,'x'))

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
root.resizable(False,False)
root.title("Hash")
app = Application(master=root)
app.mainloop()