from tkinter import *
from tkinter import filedialog, messagebox
from pathlib import Path
from PIL import Image, ImageTk
from RSA import encryption_image
import tkinter as tk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"..\assets\encryption")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

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

        encrypt_image_button = PhotoImage(file=relative_to_assets("encrypt.png"))
        self.encrypt_image_button = encrypt_image_button  

        encrypt_button = Button(
            self.main_frame,  
            image=encrypt_image_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.encrypt(),
            relief="flat",
        )
        encrypt_button.grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")

        self.selected_image_label = Label(self.image_frame)
        self.selected_image_label.pack()

        select_image_button = Button(self.main_frame, text="Chọn ảnh", command=self.select_image)
        select_image_button.grid(row=1, column=0, padx=(0, 10), sticky="ew")
        
        self.file_label = Label(self.main_frame, text="", fg="black", font=("arial", 10))
        self.file_label.grid(row=1, column=1, sticky="ew")
        
        # encrypt_button = Button(self.button_frame, text="MÃ HÓA", height=2, width=23, bg="#ed3833", fg="white", bd=0, command=self.encrypt)

        # encrypt_button.place(x=10, y=270)
        # encrypt_button.grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")

    def select_image(self):
        filepath = filedialog.askopenfilename(title="Chọn ảnh", filetypes=(("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*")))

        if filepath:
            selected_image = Image.open(filepath)
            selected_image.thumbnail((400, 400))
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
            key_path = encryption_image(self.selected_image_path)
            messagebox.showinfo("Thông báo", f"Khóa đã được ghi ra file: {key_path}")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Có lỗi xảy ra khi mã hóa: {e}")

def main_screen():
    screen = Tk()
    screen.geometry("300x300")
    screen.title("Encryption")

    encryption_button = EncryptionButton(screen)

    screen.mainloop()

if __name__ == "__main__":
    main_screen()
