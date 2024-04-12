import tkinter as tk
from tkinter import Button
from encryption import EncryptionButton
from decryption import DecryptionButton

class SelectionApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("250x200")
        self.root.title("RSA Image Encryption/Decryption")

        # Set a custom background color for the main window
        self.root.configure(bg="#f2f2f2")

        # Create and place buttons for encryption and decryption
        self.encrypt_button = Button(
            self.root,
            text="MÃ HÓA",
            height=2,
            width=20,
            bg="#ed3833",
            fg="white",
            bd=0,
            relief=tk.RAISED,
            font=("Helvetica", 12, "bold"),
            command=self.open_encryption_screen
        )
        self.encrypt_button.place(x=20, y=40)
        
        self.decrypt_button = Button(
            self.root,
            text="GIẢI MÃ",
            height=2,
            width=20,
            bg="#00bd56",
            fg="white",
            bd=0,
            relief=tk.RAISED,
            font=("Helvetica", 12, "bold"),
            command=self.open_decryption_screen
        )
        self.decrypt_button.place(x=20, y=100)

    def open_encryption_screen(self):
        main_window = tk.Toplevel(self.root)
        encryption_screen = EncryptionButton(main_window)

    def open_decryption_screen(self):
        main_window = tk.Toplevel(self.root)
        main_window.geometry("812x350")
        decryption_screen = DecryptionButton(main_window)

    def run(self):
        self.root.mainloop()

def main_screen():
    app = SelectionApp()
    app.run()

if __name__ == "__main__":
    main_screen()
