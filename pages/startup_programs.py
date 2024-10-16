import customtkinter as ctk
import winreg
import tkinter.messagebox as messagebox
from PIL import Image

class StartupPrograms(ctk.CTkFrame):
    def __init__(self, parent, show_frame):
        super().__init__(parent)

        # Back button to return to the main menu
        arrow_image = ctk.CTkImage(Image.open("images/home.png"), size=(24, 24))
        back_button = ctk.CTkButton(self, text="Home", image=arrow_image, font=("Comic Sans MS", 20), height=35,
                                     compound="left", command=lambda: show_frame(None))
        back_button.pack(pady=10, padx=10, anchor="nw")  # Place it at the top left

        # Page title
        startup_image = ctk.CTkImage(Image.open("images/startup.png"), size=(50, 50))
        label = ctk.CTkLabel(self, text="Startup Programs", image=startup_image, compound="right", font=("Comic Sans MS", 60))
        label.pack(pady=10)

        # Frame to store the programs
        self.programs_frame = ctk.CTkFrame(self)
        self.programs_frame.pack(pady=10, fill="both", expand=True)

        # Load startup programs when the page opens
        self.load_startup_programs()

    def load_startup_programs(self):
        # Load startup programs and display them
        programs = self.list_startup_programs()
        
        for name, path in programs:
            program_frame = ctk.CTkFrame(self.programs_frame)
            program_frame.pack(pady=5, padx=10, fill="x")

            label = ctk.CTkLabel(program_frame, text=name, width=400, height=50, font=("Comic Sans MS", 20))
            label.pack(side="left", padx=(0, 10))

            disable_image = ctk.CTkImage(Image.open("images/disaple.png"))
            disable_button = ctk.CTkButton(program_frame, text="Disable", font=("Comic Sans MS", 20), image=disable_image, compound="right", command=lambda name=name: self.disable_startup_program(name))
            disable_button.pack(side="right")

    def list_startup_programs(self):
        # Registry paths for startup programs
        keys = [
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            r"Software\Microsoft\Windows\CurrentVersion\RunOnce"
        ]

        startup_programs = []

        for key_path in keys:
            try:
                with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ) as key:
                    i = 0
                    while True:
                        try:
                            name, value, _ = winreg.EnumValue(key, i)
                            startup_programs.append((name, value))
                            i += 1
                        except OSError:
                            break
            except FileNotFoundError:
                pass

        return startup_programs

    def disable_startup_program(self, program_name):
        keys = [
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            r"Software\Microsoft\Windows\CurrentVersion\RunOnce"
        ]

        for key_path in keys:
            try:
                with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE) as key:
                    try:
                        winreg.DeleteValue(key, program_name)
                        messagebox.showinfo("Success", f"Disabled program: {program_name}")
                        self.load_startup_programs()  # Reload the program list
                        return
                    except FileNotFoundError:
                        continue
            except FileNotFoundError:
                pass

        messagebox.showwarning("Warning", "Program not found.")

def main():
    # Setting up the application window
    app = ctk.CTk()
    app.title("Startup Programs Management")
    app.geometry("600x400")

    # Create the Startup Programs frame
    startup_programs_frame = StartupPrograms(app, show_frame=lambda x: None)
    startup_programs_frame.pack(expand=True, fill="both")

    app.mainloop()

if __name__ == "__main__":
    main()
