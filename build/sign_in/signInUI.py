
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import selection

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"..\assets\signin")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1024x768")     
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 768,
    width = 1024,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    821.0,
    384.0,
    image=image_image_1
)

canvas.create_text(
    759.0,
    144.0,
    anchor="nw",
    text="LOGIN",
    fill="#4F159A",
    font=("IstokWeb Bold", 40 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    824.0,
    386.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    824.0,
    290.0,
    image=image_image_3
)

def login():
    default_username = "admin"
    default_password = "12345"
    username = entry_1.get()
    password = entry_2.get()
    if(username==default_username and  password == default_password):
        messagebox.showinfo(title='Success',message='Login Successful')
        window.destroy()
        selection.main_screen()
    else:
        messagebox.showerror(title='Error',message='Invalid Username or Password')
        

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: login(),
    relief="flat"
)
window.bind('<Return>', lambda event: login())
button_1.place(
    x=746.0,
    y=489.0,
    width=148.0,
    height=50.11640167236328
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    705.2000122070312,
    288.75,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    704.6221923828125,
    386.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    309.0,
    384.0,
    image=image_image_6
)

canvas.create_text(
    106.0,
    266.0,
    anchor="nw",
    text="WELCOME TO ",
    fill="#FFFFFF",
    font=("IstokWeb Bold", 60 * -1)
)

canvas.create_rectangle(
    99.0,
    358.0,
    515.9999128541531,
    362.04020078364374,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    128.0,
    384.0,
    anchor="nw",
    text="THE ENCRYPTER",
    fill="#FFFFFF",
    font=("IstokWeb Bold", 45 * -1)
)

# button_image_2 = PhotoImage(
#     file=relative_to_assets("button_2.png"))
# button_2 = Button(
#     image=button_image_2,
#     borderwidth=0,
#     highlightthickness=0,
#     relief="flat"
# )
# button_2.place(
#     x=765.0,
#     y=569.0,
#     width=112.0,
#     height=29.0
# )

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    836.5,
    290.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#CBCDDB",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=729.0,
    y=273.0,
    width=215.0,
    height=32.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    836.5,
    386.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#CBCDDB",
    fg="#000716",
    show="*",
    highlightthickness=0
)
entry_2.place(
    x=729.0,
    y=369.0,
    width=215.0,
    height=32.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    1188.5,
    642.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#CBCDDB",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=1025.0,
    y=617.0,
    width=327.0,
    height=48.0
)

window.resizable(False, False)
window.mainloop()
