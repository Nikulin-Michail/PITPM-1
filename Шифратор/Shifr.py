import tkinter
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import ttk




# Азбука Морзе
morse_code = {'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..', 'Е': '.', 'Ё': '.', 'Ж': '...-', 'З': '--..',
              'И': '..', 'Й': '.---', 'К': '-.-',
              'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---', 'П': '.--.', 'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-',
              'Ф': '..-.', 'Х': '....', 'Ц': '-.-.',
              'Ч': '---.', 'Ш': '----', 'Щ': '--.-', 'Ь': '-..-', 'Ъ': '-..-', 'Ы': '-.--', 'Э': '..-..', 'Ю': '..--',
              'Я': '.-.-',

              '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
              '7': '--...', '8': '---..', '9': '----.',
              '.': '......', ',': '.-.-.-', ';': '-.-.-.', ':': '---...', '?': '..--..', '!': '--..--', '-': '-....-',
              '"': '.-..-.', '(': '-.--.', ')': '-.--.-',
              '/': '-..-.', '+': '.-.-.', '=': '-...-', '@': '.--.-.'
              }

morse_code_2 = {'.-': 'А'

                }

# Английский алфавит для проверки ввода
ingl_alphabet = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z'}


# Функция конвертации
def convert_to_morse(text):
    text = input_text.get("1.0", END).upper()
    morse_text = ''
    for char in text:
        if char in ingl_alphabet:
            showinfo(title="Предупреждение", message="Введён неверный формат.")
            clear_text1()
            clear_text2()
            return "break"
        elif char in morse_code:
            morse_text += morse_code[char] + ' '
        elif char == ' ':
            morse_text += '/'
        output_text.delete("1.0", END)
        output_text.insert(END, morse_text)

def caesar_cipher(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            cipher_text += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            cipher_text += char
        output_text.delete("1.0", END)
        output_text.insert(END, cipher_text)

def convert_to_language(message):
    message = input_text.get("1.0", END)
    decipher = ''
    citext = ''
    for letter in message:
        if letter != ' ':
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(morse_code.keys())[list(morse_code.values()).index(citext)]
                citext = ''
            output_text.delete("1.0", END)
            output_text.insert(END, decipher)

def selected_item(event):
    selected_value = combo.get()
    print("Selected Item:", selected_value)

# Функция копирования кода Морзе
def copy():
    root.clipboard_clear()
    root.clipboard_append(output_text.get('1.0', tkinter.END).rstrip())


# Очистка полей ввода и вывода
def clear_texts():
    clear_text1()
    clear_text2()


def clear_text1():
    input_text.delete("1.0", END)

def clear_text2():
    output_text.delete("1.0", END)

# Функция выхода из программы
def exit_func():
    quit()

def encrypt():
    text = input_text.get("1.0", tkinter.END).strip()
    selected_cipher = combo.get()
    if selected_cipher == "Азбука Морзе":
        output_text = convert_to_morse(text)
    elif selected_cipher == "Шифр Цезаря":
        shift = key_entry.get("1.0", END).strip()
        output_text = caesar_cipher(text, shift)

def encrypt_lang():
    message = input_text.get("1.0", tkinter.END).strip()
    selected_cipher = combo.get()
    if selected_cipher == "Азбука Морзе":
        output_text = convert_to_language(message)

# Оформление окна
root = Tk()
root.title("Шифратор азбуки Морзе")
root.geometry("740x400")

input_label = Label(text="Ввод:")
input_label.place(x=50, y=120)

input_text = Text(root, height=5, width=30)
input_text.place(x=50, y=140)

input_label = tkinter.Label(root, text="Ключ:")
input_label.place(x=360, y=140)

key_entry = tkinter.Text(root, height=1, width=4)
key_entry.place(x=360, y=160)

output_label = Label(text="Вывод:")
output_label.place(x=450, y=120)

output_text = Text(root, height=5, width=30)
output_text.place(x=450, y=140)

convert_button = Button(root, text="Зашифровать", command=encrypt)
convert_button.place(x=205, y=240)

button_clear = Button(text="Копировать", command=copy)
button_clear.place(x=290, y=290)

button_clear = Button(text="Очистить", command=clear_texts)
button_clear.place(x=390, y=290)

button_exit = Button(text="Выход", command=exit_func)
button_exit.place(x=680, y=10)

button_exit = Button(text="Дешифрация", command=encrypt_lang)
button_exit.place(x=448, y=240)

combo_label = tkinter.Label(root, text="Выберите шифр:")
combo_label.place(x=320, y=40)
combo = ttk.Combobox(root, values=["Азбука Морзе", "Шифр Цезаря", "Simple Substitution Cipher"])
combo.set("...")
combo.place(x=300, y=60)

root.mainloop()


