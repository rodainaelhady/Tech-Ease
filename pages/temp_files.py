import os
import platform
import shutil
import customtkinter as ctk
import tkinter.messagebox as messagebox
from PIL import Image

class TempFiles(ctk.CTkFrame):
    def __init__(self, parent, show_frame):
        super().__init__(parent)

        arrow_image = ctk.CTkImage(Image.open("images/home.png"), size=(24, 24))
        back_button = ctk.CTkButton(self, text="Home", image=arrow_image, font=("Comic Sans MS", 20), height=35,
                                     compound="left", command=lambda: show_frame(None))
        back_button.place(x=10, y=10)  
        clean_image = ctk.CTkImage(Image.open("images/clean2.png"), size=(50, 50))
        label = ctk.CTkLabel(self, text="Temporary Files", font=("Comic Sans MS", 60), image=clean_image, compound="right")
        label.pack(pady=(60, 20)) 

        clean2_image = ctk.CTkImage(Image.open("images/clean3.png"), size=(30, 30))
        clean_button = ctk.CTkButton(self, text="Clean", font=("Comic Sans MS", 30), image=clean2_image,
                                      compound="right", command=self.clear_temp_files)
        clean_button.pack(pady=20)  

    def clear_temp_files(self):
        system_name = platform.system()  
        if system_name == "Windows":
            temp_folder = os.getenv('TEMP')  
            if temp_folder:
                messagebox.showinfo("Info", f"Cleaning temporary files in: {temp_folder}")
                try:
                    for filename in os.listdir(temp_folder):
                        file_path = os.path.join(temp_folder, filename)
                        try:
                            if os.path.isfile(file_path) or os.path.islink(file_path):
                                os.unlink(file_path)
                            elif os.path.isdir(file_path):
                                shutil.rmtree(file_path)
                        except Exception as e:
                            print(f"Error deleting {file_path}: {e}")
                    messagebox.showinfo("Success", "Temporary files cleaned successfully.")
                except Exception as e:
                    messagebox.showerror("Error", f"Error accessing temp folder: {e}")
            else:
                messagebox.showwarning("Warning", "Could not locate TEMP folder.")
        
        elif system_name == "Linux":
            temp_folder = "/tmp"  
            messagebox.showinfo("Info", f"Cleaning temporary files in: {temp_folder}")
            try:
                for filename in os.listdir(temp_folder):
                    file_path = os.path.join(temp_folder, filename)
                    try:
                        if os.path.isfile(file_path) or os.path.islink(file_path):
                            os.unlink(file_path)
                        elif os.path.isdir(file_path):
                            shutil.rmtree(file_path)
                    except Exception as e:
                        print(f"Error deleting {file_path}: {e}")
                messagebox.showinfo("Success", "Temporary files cleaned successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Error accessing /tmp folder: {e}")
        else:
            messagebox.showwarning("Warning", "Unsupported Operating System.")

def main():
    app = ctk.CTk()
    app.title("Temporary Files Cleaner")
    app.geometry("600x400")

    temp_files_frame = TempFiles(app, show_frame=lambda x: None)
    temp_files_frame.pack(expand=True, fill="both")

    app.mainloop()

if __name__ == "__main__":
    main()
