from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from RSA import encryption_image
import tkinter as tk
from tkinter import ttk

class EncryptionButton(tk.Toplevel):
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.title("Encryption")
        self.main_window.geometry("1280x720")

        self.main_frame = Frame(self.main_window)
        self.main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        self.selected_image_path = None
        self.file_name = None

        self.image_frame = Frame(self.main_frame)
        self.image_frame.grid(row=0, column=0, columnspan=2, pady=(0, 10), sticky="ew")

        self.button_frame = Frame(self.main_frame)
        self.button_frame.grid(row=2, column=0, columnspan=2, pady=10, sticky="ew")

        self.setup_gui()

    def setup_gui(self):
        self.selected_image_label = Label(self.image_frame)
        self.selected_image_label.pack()

        select_image_button = Button(self.main_frame, text="Chọn ảnh", command=self.select_image)
        select_image_button.grid(row=1, column=0, padx=(0, 10), sticky="ew")
        
        self.file_label = Label(self.main_frame, text="", fg="black", font=("arial", 10))
        self.file_label.grid(row=1, column=1, sticky="ew")
        
        encrypt_button = Button(self.button_frame, text="MÃ HÓA", height=2, width=23, bg="#ed3833", fg="white", bd=0, command=self.encrypt)
        encrypt_button.place(x=10, y=270)
        encrypt_button.grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")

    def select_image(self):
        filepath = filedialog.askopenfilename(title="Chọn ảnh", filetypes=(("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*")))

        if filepath:
            selected_image = Image.open(filepath)
            selected_image.thumbnail((300, 300))
            photo = ImageTk.PhotoImage(selected_image)
            
            self.selected_image_label.config(image=photo)
            self.selected_image_label.image = photo
            
            self.file_name = filepath.split("/")[-1]
            self.file_label.config(text=" " + self.file_name)
            self.selected_image_path = filepath

    def encrypt(self):
        if not self.selected_image_path:
            messagebox.showerror("Lỗi", "Vui lòng chọn ảnh cần mã hóa.")
            return
        
        try:
            encryption_image(self.selected_image_path)
            key_path = encryption_image(self.selected_image_path)
            messagebox.showinfo("Thông báo", f"Khóa đã được ghi ra file: {key_path}")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Có lỗi xảy ra khi mã hóa: {e}")

