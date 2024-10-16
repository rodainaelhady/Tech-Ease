import customtkinter as ctk
from PIL import Image
from tkinter import messagebox
from pages.battery_check import BatteryCheck
from pages.check_disk_space import CheckDiskSpace
from pages.check_password_strength import CheckPasswordStrength
from pages.generate_strong_password import GenerateStrongPassword
from pages.cpu_ram import CPURAM
from pages.network_check import NetworkCheck
from pages.my_speed_test import SpeedTest
from pages.startup_programs import StartupPrograms
from pages.temp_files import TempFiles
from pages.uninstall_programs import UninstallPrograms

app = ctk.CTk()
app.title("TechEase")
app.geometry("800x600")    

main_frame = ctk.CTkFrame(app,fg_color="#2B2B2B")
main_frame.pack(fill="both", expand=True)
title_frame = ctk.CTkFrame(main_frame, fg_color="#2B2B2B") 
title_frame.pack(pady=20) 
title_label1 = ctk.CTkLabel(title_frame, text="Welcome to Tech", font=("Comic Sans MS", 60), text_color="white")
title_label1.pack(side="left")

title_label2 = ctk.CTkLabel(title_frame, text="Ease", font=("Comic Sans MS", 60), text_color="#1f6aa5")
title_label2.pack(side="left")

def show_frame(page_class):
    for widget in app.winfo_children():
        widget.pack_forget()

    if page_class is None:
        main_frame.pack(fill="both", expand=True)
    else:
        page = page_class(app, show_frame)
        page.pack(fill="both", expand=True)

def create_left_buttons(frame):
    battery_image = ctk.CTkImage(Image.open("images/battery.png"), size=(50, 50))

    button1 = ctk.CTkButton(frame, text="Battery Health", width=700, height=150, image=battery_image,compound="right",font=("Comic Sans MS",40),corner_radius=20,
                            command=lambda: show_frame(BatteryCheck))
    button1.pack(pady=20, padx=10)
    
    disk_image = ctk.CTkImage(Image.open("images/disk.png"), size=(50, 50))

    button2 = ctk.CTkButton(frame, text="Disk Space", width=700, height=150, image=disk_image,compound="right",font=("Comic Sans MS",40),corner_radius=20,
                            command=lambda: show_frame(CheckDiskSpace))
    button2.pack(pady=20, padx=10)

    password_image = ctk.CTkImage(Image.open("images/password.png"), size=(50, 50))

    button3 = ctk.CTkButton(frame, text="Password Strength", width=700, height=150,image=password_image,compound="right", font=("Comic Sans MS",40),corner_radius=20,
                            command=lambda: show_frame(CheckPasswordStrength))
    button3.pack(pady=20, padx=10)
    strong_password_image = ctk.CTkImage(Image.open("images/strong_password.png"), size=(50, 50))

    button4 = ctk.CTkButton(frame, text="Generate Password", width=700, height=150, image=strong_password_image,compound="right",font=("Comic Sans MS",40),corner_radius=20,
                            command=lambda: show_frame(GenerateStrongPassword))
    button4.pack(pady=20, padx=10)

    cpu_image = ctk.CTkImage(Image.open("images/cpu.png"), size=(50, 50))

    button5 = ctk.CTkButton(frame, text="CPU & RAM", width=700, height=150, image=cpu_image,compound="right",font=("Comic Sans MS",40),corner_radius=20,
                            command=lambda: show_frame(CPURAM))
    button5.pack(pady=20, padx=10)

def create_right_buttons(frame):
    network_image = ctk.CTkImage(Image.open("images/networking.png"), size=(50, 50))

    button6 = ctk.CTkButton(frame, text="Network Check", width=700, height=150, image=network_image,compound="right",font=("Comic Sans MS",40),corner_radius=20,
                            command=lambda: show_frame(NetworkCheck))
    button6.pack(pady=20, padx=10)

    speed_image = ctk.CTkImage(Image.open("images/speed.png"), size=(50, 50))

    button7 = ctk.CTkButton(frame, text="Speed Test", width=700, height=150, image=speed_image,compound="right",font=("Comic Sans MS",40),corner_radius=20,
                            command=lambda: show_frame(SpeedTest))
    button7.pack(pady=20, padx=10)
    
    programs_image = ctk.CTkImage(Image.open("images/programs.png"), size=(50, 50))

    button8 = ctk.CTkButton(frame, text="Startup Programs", width=700, height=150, image=programs_image,compound="right",font=("Comic Sans MS",40),corner_radius=20,
                            command=lambda: show_frame(StartupPrograms))
    button8.pack(pady=20, padx=10)
    
    file_image = ctk.CTkImage(Image.open("images/file.png"), size=(50, 50))

    button9 = ctk.CTkButton(frame, text="Temp files", width=700, height=150,image=file_image,compound="right", font=("Comic Sans MS",40), corner_radius=20,
                            command=lambda: show_frame(TempFiles))
    button9.pack(pady=20, padx=10)
    
    delete_image = ctk.CTkImage(Image.open("images/delete.png"), size=(50, 50))

    button10 = ctk.CTkButton(frame, text="Uninstall Programs", width=700, height=150,image=delete_image,compound="right", font=("Comic Sans MS",40),corner_radius=20,
                             command=lambda: show_frame(UninstallPrograms))
    button10.pack(pady=20, padx=10)

left_frame = ctk.CTkFrame(main_frame,fg_color="#2B2B2B")
left_frame.pack(side="left", fill="both", expand=True)

right_frame = ctk.CTkFrame(main_frame,fg_color="#2B2B2B")
right_frame.pack(side="right", fill="both", expand=True)

create_left_buttons(left_frame)
create_right_buttons(right_frame)

app.mainloop()
