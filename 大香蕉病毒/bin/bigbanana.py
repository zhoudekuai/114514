import os,time
import tkinter as tk
from tkinter import messagebox


print("点击右上角关闭       →")

def aa():
    root = tk.Tk()
    root.withdraw()

    messagebox.showinfo("警告", "这是一个无害病毒！如果造成任何财损失，如财产损失，小脑萎缩……本作者概不负责")

    root.destroy()

if __name__ == "__main__":
    aa()


def edit():
    root = tk.Tk()
    root.withdraw()

    messagebox.showinfo("询问", "是否关闭它？")

    root.destroy()



while True:
    os.system(r"C:\Users\Administrator\Desktop\大香蕉病毒\bin\bigbananaVideo.avi")
    time.sleep(2)
    if __name__ == "__main__":
        edit()