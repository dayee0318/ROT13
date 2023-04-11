import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("ROT13 Decoder")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.message_label = tk.Label(self, text="Message to decode:")
        self.message_label.pack(side="left")

        self.message_entry = tk.Entry(self)
        self.message_entry.pack(side="left")

        self.decode_button = tk.Button(self, text="Decode", command=self.decode_message)
        self.decode_button.pack(side="left")

        self.result_label = tk.Label(self, text="")
        self.result_label.pack(side="left")

    def decode_message(self):
        message = self.message_entry.get()
        result = ""

        for char in message:
            if char.isalpha():
                if char.isupper():
                    result += chr((ord(char) - 65 + 13) % 26 + 65)
                else:
                    result += chr((ord(char) - 97 + 13) % 26 + 97)
            else:
                result += char

        self.result_label.config(text=result)

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
