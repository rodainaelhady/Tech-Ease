import customtkinter as ctk
from PIL import Image
import random
import string

def generate_password(length=12):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = '!@#$%^&*()_+-=[]{}|;:,.<>?'
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    password = ''.join(random.sample(all_characters, length))
    return password

class GenerateStrongPassword(ctk.CTkFrame):
    def __init__(self, parent, show_frame):
        super().__init__(parent)
        
        back_icon = ctk.CTkImage(Image.open("images/home.png"), size=(20, 20))
        back_button = ctk.CTkButton(self, text="Home", font=("Comic Sans MS", 20), height=35,
                                    image=back_icon, compound="left", 
                                    command=lambda: show_frame(None))
        back_button.pack(pady=10, padx=10, anchor="w")

        lock_icon = ctk.CTkImage(Image.open("images/security.png"), size=(50, 50))
        label = ctk.CTkLabel(self, text="Generate Strong Password ", image=lock_icon, compound="right",font=("Comic Sans MS", 60))
        label.pack(pady=20, anchor="center")

        frame = ctk.CTkFrame(self,fg_color="#2B2B2B")
        frame.pack(pady=20, anchor="center")
        
        self.length_entry = ctk.CTkEntry(frame, placeholder_text="Password length", height=50,
                                         width=200, font=("Comic Sans MS", 20))
        self.length_entry.pack(side="left", padx=10)
        generate_image=ctk.CTkImage(Image.open("images/generate.png"),size=(30,30))
        generate_button = ctk.CTkButton(frame, text="Generate", font=("Comic Sans MS", 30), image=generate_image,compound="right",
                                        command=self.generate_and_display_password)
        generate_button.pack(side="left", padx=10)

        self.result_label = ctk.CTkLabel(self, text="", font=("Comic Sans MS", 18), text_color="blue")
        self.result_label.pack(pady=20)
        copy_image=ctk.CTkImage(Image.open("images/copy.png"),size=(30,30))
        self.copy_button = ctk.CTkButton(self, text="Copy to Clipboard", font=("Comic Sans MS", 30), image=copy_image,compound="right",
                                         command=self.copy_to_clipboard)
        self.copy_button.pack(pady=20)

    def generate_and_display_password(self):
        length = self.length_entry.get()
        if length.isdigit():
            length = int(length)
        else:
            length = 12
        password = generate_password(length)
        self.result_label.configure(text=f"Generated Password: {password}",text_color="white",font=("Comic Sans MS",30))
        self.generated_password = password  

    def copy_to_clipboard(self):
        self.clipboard_clear()
        self.clipboard_append(self.generated_password)
        self.result_label.configure(text=f"Password copied to clipboard!", text_color="green",font=("Comic Sans MS",30))
