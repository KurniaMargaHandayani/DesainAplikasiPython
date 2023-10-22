import tkinter as tk

# Fungsi untuk mengenkripsi teks
def encrypt():
    plaintext = entry_plain.get()
    key = int(entry_key.get())
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            is_upper = char.isupper()
            char = chr(((ord(char) - ord('A' if is_upper else 'a') + key) % 26) + ord('A' if is_upper else 'a'))
        encrypted_text += char
    result_label.config(text="Hasil Enkripsi: " + encrypted_text)

# Fungsi untuk mendekripsi teks
def decrypt():
    ciphertext = entry_cipher.get()
    key = int(entry_key.get())
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            char = chr(((ord(char) - ord('A' if is_upper else 'a') - key) % 26) + ord('A' if is_upper else 'a'))
        decrypted_text += char
    result_label.config(text="Hasil Dekripsi: " + decrypted_text)

# Membuat jendela aplikasi
app = tk.Tk()
app.title("Caesar Cipher")

# Membuat label dan input untuk masukkan teks, kunci, dan teks terenkripsi
label_plain = tk.Label(app, text="Masukkan Teks:")
entry_plain = tk.Entry(app)
label_key = tk.Label(app, text="Masukkan Kunci (angka):")
entry_key = tk.Entry(app)
encrypt_button = tk.Button(app, text="Enkripsi", command=encrypt)

label_cipher = tk.Label(app, text="Masukkan Teks Terenkripsi:")
entry_cipher = tk.Entry(app)
decrypt_button = tk.Button(app, text="Dekripsi", command=decrypt)

result_label = tk.Label(app, text="Hasil Enkripsi/Dekripsi:")

# Menampilkan elemen-elemen dalam grid
label_plain.grid(row=0, column=0)
entry_plain.grid(row=0, column=1)
label_key.grid(row=1, column=0)
entry_key.grid(row=1, column=1)
encrypt_button.grid(row=2, column=0, columnspan=2)
label_cipher.grid(row=3, column=0)
entry_cipher.grid(row=3, column=1)
decrypt_button.grid(row=4, column=0, columnspan=2)
result_label.grid(row=5, column=0, columnspan=2)

app.mainloop()
