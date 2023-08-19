import sqlite3
from tkinter import *
from tkinter import PhotoImage
import tkinter as tk
def register():
    username = register_username_entry.get()
    password = register_password_entry.get()

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        register_status.config(text="Пользователь с таким именем уже существует.")
    else:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        register_status.config(text="Регистрация успешна!")
        login_register_window.destroy()


def login():
    username = login_username_entry.get()
    password = login_password_entry.get()

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        login_status.config(text="Вход выполнен успешно.")
        open_messenger_window()
        login_register_window.destroy()

    else:
        login_status.config(text="Неверное имя пользователя или пароль.")

def open_login_register_window():
    global register_username_entry, register_password_entry, login_username_entry, login_password_entry, register_status, login_status, login_register_window
    login_register_window = Toplevel(main_window)
    login_register_window.title("Вход и регистрация")
    login_register_window.geometry("300x300+{}+{}".format(int(main_window.winfo_screenwidth()/2 - 150), int(main_window.winfo_screenheight()/2 - 100)))
    login_register_window.resizable(False, False)
    logo = tk.PhotoImage(file='C:/Users/Maksim/Desktop/Python/graphic interface/pngimage.png')
    login_register_window.iconphoto(False, logo)

    register_username_label = Label(login_register_window, text="Имя пользователя:")
    register_username_label.pack()
    register_username_entry = Entry(login_register_window)
    register_username_entry.pack()

    register_password_label = Label(login_register_window, text="Пароль:")
    register_password_label.pack()
    register_password_entry = Entry(login_register_window, show="*")
    register_password_entry.pack()

    register_button = Button(login_register_window, text="Зарегистрироваться", command=register)
    register_button.pack()

    register_status = Label(login_register_window, text="")
    register_status.pack()

    login_username_label = Label(login_register_window, text="Имя пользователя:")
    login_username_label.pack()
    login_username_entry = Entry(login_register_window)
    login_username_entry.pack()

    login_password_label = Label(login_register_window, text="Пароль:")
    login_password_label.pack()
    login_password_entry = Entry(login_register_window, show="*")
    login_password_entry.pack()

    login_button = Button(login_register_window, text="Войти", command=login)
    login_button.pack()

    login_status = Label(login_register_window, text="")
    login_status.pack()
    main_window.withdraw()
def send_message():
    message = entry_box.get()

    conn = sqlite3.connect('messenger.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO messages (sender, receiver, message) VALUES (?, ?, ?)', ('Sender', 'Receiver', message))
    conn.commit()
    conn.close()
    entry_box.delete(0, END)

def open_messenger_window():
    global messenger_window
    messenger_window = Toplevel(main_window)
    messenger_window.title("Мессенджер")
    messenger_window.geometry("500x550+{}+{}".format(int(main_window.winfo_screenwidth()/2 - 250), int(main_window.winfo_screenheight()/2 - 275)))
    logo = tk.PhotoImage(file='C:/Users/Maksim/Desktop/Python/graphic interface/pngimage.png')
    messenger_window.iconphoto(False, logo)

    message_box = Text(messenger_window)
    message_box.pack()

    global entry_box
    entry_box = Entry(messenger_window)
    entry_box.pack()

    send_button = Button(messenger_window, text="Send", command=send_message)
    send_button.pack()

conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)''')
conn.commit()
conn.close()

conn = sqlite3.connect('messenger.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY AUTOINCREMENT, sender TEXT, receiver TEXT, message TEXT)')
conn.commit()
conn.close()

main_window = Tk()
main_window.title("Main Window")

login_register_button = Button(main_window, text="Вход и регистрация", command=open_login_register_window)
login_register_button.pack()
main_window.geometry("300x100+{}+{}".format(int(main_window.winfo_screenwidth()/2 - 150), int(main_window.winfo_screenheight()/2 - 50)))
main_window.resizable(False, False)
logo = tk.PhotoImage(file='C:/Users/Maksim/Desktop/Python/graphic interface/pngimage.png')
main_window.iconphoto(False, logo)

main_window.mainloop()




