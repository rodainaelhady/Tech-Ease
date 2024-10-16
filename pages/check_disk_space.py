import subprocess
import customtkinter as ctk
from PIL import Image

def bytes_to_gb(bytes_value):
    return round(bytes_value / (1024 ** 3), 2)

def check_all_drives_space():
    try:
        result = subprocess.run(["powershell", "-Command", "Get-PSDrive -PSProvider FileSystem | Select-Object Name, Used, Free"], capture_output=True, text=True)

        if result.returncode == 0:
            output_lines = result.stdout.strip().splitlines()
            drive_info = []

            for line in output_lines[2:]:
                columns = line.split()
                drive_name = columns[0]
                used_space = int(columns[1])
                free_space = int(columns[2])

                used_space_gb = bytes_to_gb(used_space)
                free_space_gb = bytes_to_gb(free_space)

                if used_space_gb > 100:  
                    drive_type = "hard-disk"
                else:
                    drive_type = "flash"

                drive_info.append({
                    "drive_name": drive_name,
                    "used_space": used_space_gb,
                    "free_space": free_space_gb,
                    "drive_type": drive_type
                })
            
            return drive_info
        else:
            return [{"error": "Failed to retrieve disk space information."}]
    
    except Exception as e:
        return [{"error": f"An error occurred: {e}"}]

class CheckDiskSpace(ctk.CTkFrame):
    def __init__(self, parent, show_frame):
        super().__init__(parent)
        arrow_image = ctk.CTkImage(Image.open("images/home.png"), size=(24, 24))

        back_button = ctk.CTkButton(self, text="Home", image=arrow_image, font=("Comic Sans MS", 20), height=35,
                                    command=lambda: show_frame(None))
        back_button.pack(pady=10, padx=10, anchor="w")  
        space_image= ctk.CTkImage(Image.open("images/space.png"),size=(50,50))
        label = ctk.CTkLabel(self, text="Disk Space ", image=space_image,compound="right",font=("Comic Sans MS", 60))
        label.pack(pady=20)

        calc_image = ctk.CTkImage(Image.open("images/calc.png"), size=(30, 30))

        check_button = ctk.CTkButton(self, text="Calculate", compound="right", command=self.display_drive_space,
                                     image=calc_image, font=("Comic Sans MS", 30), height=40, corner_radius=10)
        check_button.pack(pady=20)

        self.result_frame = ctk.CTkFrame(self, fg_color="#2B2B2B")
        self.result_frame.pack(pady=20)

    def display_drive_space(self):
        for widget in self.result_frame.winfo_children():
            widget.destroy()

        drive_info = check_all_drives_space()

        for drive in drive_info:
            if "error" in drive:
                result_label = ctk.CTkLabel(self.result_frame, text=drive["error"], font=("Comic Sans MS", 20), text_color="white")
                result_label.pack(pady=5, anchor="w")
            else:
                if drive["drive_type"] == "hard-disk":
                    image_path = "images/hard-disk.png"
                else:
                    image_path = "images/flash.png"

                drive_image = ctk.CTkImage(Image.open(image_path), size=(30, 30))

                result_frame = ctk.CTkFrame(self.result_frame, fg_color="#2B2B2B")
                result_frame.pack(fill="x", pady=5)

                result_label = ctk.CTkLabel(result_frame, text=f"Drive {drive['drive_name']}: Used space: {drive['used_space']} GB, Free space: {drive['free_space']} GB",
                                            font=("Comic Sans MS", 20), text_color="white")
                result_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

                image_label = ctk.CTkLabel(result_frame, image=drive_image, text="")
                image_label.grid(row=0, column=1, padx=10, pady=5, sticky="e")
