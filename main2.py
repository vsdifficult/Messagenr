import sqlite3
import random
import string
from tkinter import *
from tkinter import PhotoImage
import tkinter as tk

def generate_token(length=28):
    characters = string.ascii_letters + string.digits
    token = ''.join(random.choice(characters) for _ in range(length))
    return token

conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, token TEXT)''')
conn.commit()
conn.close()


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
        token = generate_token()
        cursor.execute("INSERT INTO users (username, password, token) VALUES (?, ?, ?)", (username, password, token))
        conn.commit()
        conn.close()
        register_status.config(text="Регистрация успешна!")



def login():
    username = login_username_entry.get()
    password = login_password_entry.get()

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        print(user)  # Вывод структуры кортежа для определения правильного индекса
        login_status.config(text="Вход выполнен успешно.")
        if len(user) >= 3:
            open_token_window(user[2])  # Проверка, что индекс существует
        else:
            print("Неправильная структура кортежа")
    else:
        login_status.config(text="Неверное имя пользователя или пароль.")



def open_login_register_window():
    global register_username_entry, register_password_entry, login_username_entry, login_password_entry, register_status, login_status, login_register_window
    login_register_window = Toplevel(main_window)
    login_register_window.title("Вход и регистрация")
    login_register_window.geometry("300x300+{}+{}".format(int(main_window.winfo_screenwidth()/2 - 150), int(main_window.winfo_screenheight()/2 - 100)))
    login_register_window.resizable(False, False)
    logo = tk.PhotoImage(file='pngimage.png')
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
    logo = tk.PhotoImage(file='pngimage.png')
    messenger_window.iconphoto(False, logo)
    messenger_window.resizable(False, False)

    message_box = Text(messenger_window)
    message_box.pack()

    global entry_box
    entry_box = Entry(messenger_window)
    entry_box.pack()

    send_button = Button(messenger_window, text="Send", command=send_message)
    send_button.pack()

# Остальной код остается таким же, как в предыдущем сообщении.


def open_chat_window(token):
    global chat_window
    chat_window = Toplevel(main_window)
    chat_window.title("Чат")
    chat_window.geometry("300x150+{}+{}".format(int(main_window.winfo_screenwidth()/2 - 150), int(main_window.winfo_screenheight()/2 - 75)))
    chat_window.resizable(False, False)
    token_label = Label(chat_window, text="Токен пользователя: " + token)
    token_label.pack()

    message_box = Text(chat_window)
    message_box.pack()

    global entry_box
    entry_box = Entry(chat_window)
    entry_box.pack()

    send_button = Button(chat_window, text="Send", command=send_message)
    send_button.pack()

def open_token_window(token):
    global token_window
    token_window = Toplevel(main_window)
    token_window.title("Введите токен")
    token_window.geometry("300x150+{}+{}".format(int(main_window.winfo_screenwidth()/2 - 150), int(main_window.winfo_screenheight()/2 - 75)))
    token_window.resizable(False, False)
    token_label = Label(token_window, text="Введите токен пользователя:")
    token_label.pack()

    token_entry = Entry(token_window)
    token_entry.pack()

    open_chat_button = Button(token_window, text="Открыть чат", command=lambda: open_chat_window(token_entry.get()))
    open_chat_button.pack()

conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, token TEXT)''')
conn.commit()
conn.close()

def open_main_window():
    global main_window
    main_window = Tk()
    main_window.title("Enter Window")

    login_register_button = Button(main_window, text="Вход и регистрация", command=open_login_register_window)
    login_register_button.pack()

    main_window.geometry("300x200+{}+{}".format(int(main_window.winfo_screenwidth()/2 - 150), int(main_window.winfo_screenheight()/2 - 100)))
    main_window.resizable(False, False)
    logo = tk.PhotoImage(file='pngimage.png')
    main_window.iconphoto(False, logo)
    main_window.resizable(False, False)

    main_window.mainloop()

open_main_window()










