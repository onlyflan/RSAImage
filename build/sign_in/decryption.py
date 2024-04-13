from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from RSA import decryption_image
import tkinter as tk
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"..\assets\decryption")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class DecryptionButton(tk.Toplevel):
    def __init__(self, main_window):
        self.main_window = main_window

        self.main_window.title("Encryption")
        self.main_window.geometry("1280x720")

        self.main_frame = Frame(self.main_window)
        self.main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        
        self.selected_image_path = None
        self.file_name = None
        
        self.n_code = StringVar()
        self.d_code = StringVar()
        
        self.setup_gui()
    
    def setup_gui(self):
        Label(self.main_window, text="Nhập N:", fg="black", font=("arial", 13)).place(x=10, y=10)
        Entry(self.main_window, textvariable=self.n_code, width=19, bd=1, font=("arial", 25), relief="solid").place(x=10, y=50)
        # self.n_text.place(x=10, y=50, width=350, height=40)

        Label(self.main_window, text="Nhập khóa riêng tư D:", fg="black", font=("arial", 13)).place(x=10, y=130)
        Entry(self.main_window, textvariable=self.d_code, width=19, bd=1, font=("arial", 25), relief="solid").place(x=10, y=160)
        
        self.select_image_button = Button(self.main_window, text="Chọn ảnh", command=self.select_image)
        self.select_image_button.place(x=10, y=220)

        # self.decrypt_button = Button(self.main_window, text="GIẢI MÃ", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=self.decrypt)
        # self.decrypt_button.place(x=290, y=270)

        decrypt_image_button = PhotoImage(file=relative_to_assets("decrypt.png"))
        self.encrypt_image_button = decrypt_image_button  

        decrypt_button = Button(
            self.main_frame,  
            image=decrypt_image_button,
            borderwidth=0,
            highlightthickness=0,
            command=self.decrypt,
            relief="flat",
        )
        
        decrypt_button.place(x=290, y=270)


        self.selected_image_label = Label(self.main_window)
        self.file_label = Label(self.main_window, text="", fg="black", font=("arial", 10))
        self.file_label.place(x=100, y=220)
    
    def select_image(self):
        filepath = filedialog.askopenfilename(title="Chọn ảnh", filetypes=(("Image files", "*.bmp"), ("All files", "*.*")))

        if filepath:
            selected_image = Image.open(filepath)
            selected_image.thumbnail((400, 400))
            photo = ImageTk.PhotoImage(selected_image)
            self.selected_image_label.config(image=photo)
            self.selected_image_label.image = photo
            self.selected_image_label.place(x=400, y=50)

            self.file_name = filepath.split("/")[-1]
            self.file_label.config(text=" " + self.file_name)
            self.selected_image_path = filepath
    
    def decrypt(self):
        if not self.selected_image_path:
            messagebox.showerror("Lỗi", "Vui lòng chọn ảnh cần giải mã.")
            return
        
        n_str = self.n_code.get().strip()
        d_str = self.d_code.get().strip()

        if not n_str or not d_str:
            messagebox.showerror("Lỗi", "Vui lòng nhập đủ mã khóa.")
            return
        
        try:
            n = int(n_str)
            d = int(d_str)
        except ValueError:
            messagebox.showerror("Lỗi", "Nhập N hoặc D không hợp lệ.")
            return
        
        try:
            decryption_path = decryption_image(n, d, self.selected_image_path, self.file_name)
            messagebox.showinfo("Thông báo", f"Hình ảnh đã được giải mã và lưu tại: {decryption_path}")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Có lỗi xảy ra khi giải mã: {e}")
            print(e)
            print( self.selected_image_path, self.file_name)

def main_screen():
    screen = Tk()
    screen.geometry("812x350")
    screen.title("Decryption")

    DecryptionButton(screen)

    screen.mainloop()

if __name__ == "__main__":
    main_screen()
