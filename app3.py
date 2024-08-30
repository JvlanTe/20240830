import tkinter as tk
from tkinter import Label

# ウィンドウの作成
root = tk.Tk()

# ウィンドウタイトル設定
root.title("メイン画面")

# ラベル作成
hello_label = Label(root, text="Hello World", font=("PlemolJP Regular", 100))

# 表示する（何を？
hello_label.pack(padx=20, pady=30)

root.mainloop()
