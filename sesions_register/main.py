import tkinter as tk
import sqlite3


conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)''')
conn.commit()


def register():
    username = username_entry.get()
    password = password_entry.get()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    status_label.config(text="Регистрация успешна!")


window = tk.Tk()

username_label = tk.Label(window, text="Имя пользователя:")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

password_label = tk.Label(window, text="Пароль:")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

register_button = tk.Button(window, text="Зарегистрироваться", command=register)
register_button.pack()

status_label = tk.Label(window, text="")
status_label.pack()

window.mainloop()
