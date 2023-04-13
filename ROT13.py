import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("ROT13 Decoder")
        self.pack(fill="both", expand=True, padx=20, pady=20)  # 전체 창을 꽉 채우도록 설정

        # 입력창과 라벨
        self.message_label = tk.Label(self, text="Message to decode:", font=("Helvetica", 14))
        self.message_label.grid(row=0, column=0, sticky="w", pady=10)

        self.message_entry = tk.Entry(self, font=("Helvetica", 14))
        self.message_entry.grid(row=1, column=0, padx=10, pady=10, sticky="wens")
        self.message_entry.focus()  # 입력창에 포커스 설정

        # 디코드 버튼
        self.decode_button = tk.Button(self, text="Decode", font=("Helvetica", 14), command=self.decode_message)
        self.decode_button.grid(row=2, column=0, pady=10)

        # 결과창과 라벨
        self.result_label = tk.Label(self, text="", font=("Helvetica", 14))
        self.result_label.grid(row=0, column=1, rowspan=3, padx=10, pady=10, sticky="wens")

        # 창 크기 설정
        self.master.geometry("600x200")

        # 창 크기 조절 불가능하게 설정
        self.master.resizable(False, False)

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

        self.result_label.config(text=result, justify="left", anchor="nw", wraplength=300, width=25)

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
