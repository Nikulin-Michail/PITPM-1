import tkinter as tk
from tkinter import ttk

def caesar_cipher(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            cipher_text += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            cipher_text += char
    return cipher_text

def vigenere_cipher(plain_text, key):
    cipher_text = ""
    key_idx = 0
    for char in plain_text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            key_shift = ord(key[key_idx]) - ascii_offset
            cipher_text += chr((ord(char) - ascii_offset + key_shift) % 26 + ascii_offset)
            key_idx = (key_idx + 1) % len(key)
        else:
            cipher_text += char
    return cipher_text

def simple_substitution_cipher(plain_text, substitution_dict):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            if char.isupper():
                cipher_text += substitution_dict[char.lower()].upper()
            else:
                cipher_text += substitution_dict[char]
        else:
            cipher_text += char
    return cipher_text

def encrypt():
    plain_text = input_text.get("1.0", tk.END).strip()

    selected_cipher = combo.get()
    if selected_cipher == "Caesar Cipher":
        shift = int(shift_entry.get())
        output = caesar_cipher(plain_text, shift)
    elif selected_cipher == "Vigenere Cipher":
        key = key_entry.get().strip()
        output = vigenere_cipher(plain_text, key)
    elif selected_cipher == "Simple Substitution Cipher":
        substitution_dict = dict(substitution_entry.get().strip().split(","))
        output = simple_substitution_cipher(plain_text, substitution_dict)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, output)

window = tk.Tk()
window.title("Cipher Program")

# Создание выпадающего списка с видами шифров
combo_label = tk.Label(window, text="Select Cipher:")
combo_label.pack()
combo = ttk.Combobox(window, values=["Caesar Cipher", "Vigenere Cipher", "Simple Substitution Cipher"])
combo.set("Select Cipher")
combo.pack()

input_label = tk.Label(window, text="Input:")
input_label.pack()
input_text = tk.Text(window, height=5, width=50)
input_text.pack()

shift_label = tk.Label(window, text="Shift (Caesar Cipher):")
shift_label.pack()
shift_entry = tk.Entry(window)
shift_entry.pack()

key_label = tk.Label(window, text="Key (Vigenere Cipher):")
key_label.pack()
key_entry = tk.Entry(window)
key_entry.pack()

substitution_label = tk.Label(window, text="Substitution Dictionary (Simple Substitution Cipher):")
substitution_label.pack()
substitution_entry = tk.Entry(window)
substitution_entry.pack()

encrypt_button = tk.Button(window, text="Encrypt", command=encrypt)
encrypt_button.pack()

output_label = tk.Label(window, text="Output:")
output_label.pack()
output_text = tk.Text(window, height=5, width=50)
output_text.pack()

window.mainloop()