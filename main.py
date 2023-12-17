from tkinter import *
import pyperclip 
import random

root = Tk()
root.geometry("450x250")
root.title('Генератор паролей')
root.resizable(width=False,height=False)
root.configure(background="#000")
passwrd = StringVar()
passlen = IntVar()
passlen.set(0)


def generate_password():
    """функция которая генерирует пароль """
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
             'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
             'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
             '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
             '*', '(', ')']
    password = ''
    for x in range(passlen.get()):
        password = password + random.choice(pass1)
    passwrd.set(password)

def copyclipboard():
	'''функция для копирования в буфер обмена'''
	random_password = passwrd.get()
	pyperclip.copy(random_password)

#Label


Label(root, text="Генератор паролей", font="Courier 30 bold",background= '#000',fg='#fff').pack()

Label(root, text="Выберите длинну пароля",font="Courier 14 bold",background= '#000',fg='#fff').pack(pady=3)

Entry(root, textvariable=passlen,background='#a6aab3').pack(pady=3)
Button(root, text="Сгенерировать пароль", command=generate_password,background='#0048ff',fg='#fff').pack(pady=7)


Entry(root, textvariable=passwrd,background='#a6aab3').pack(pady=3)

Button(root, text="Нажмите чтобы скопировать", command=copyclipboard,background='#0048ff',fg='#fff').pack()



root.mainloop()
