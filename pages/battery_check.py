import subprocess
import os
import webbrowser
import customtkinter as ctk
from PIL import Image

class BatteryCheck(ctk.CTkFrame):
    def __init__(self, parent, show_frame):
        super().__init__(parent)

        arrow_image = ctk.CTkImage(Image.open("images/home.png"), size=(24, 24))

        back_button = ctk.CTkButton(self, text="Home", image=arrow_image, font=("Comic Sans MS", 20), height=35,
                                    compound="left",  
                                    command=lambda: show_frame(None))
        back_button.pack(anchor="w", padx=5, pady=10)

        battery2_image = ctk.CTkImage(Image.open("images/battery2.png"), size=(50, 50))
        label = ctk.CTkLabel(self, text="Battery Check", image=battery2_image, compound="right", font=("Comic Sans MS", 60))
        label.pack(pady=20)

        report_image = ctk.CTkImage(Image.open("images/report.png"), size=(30, 30))

        generate_button = ctk.CTkButton(self, text="Generate Battery Report", image=report_image, font=("Comic Sans MS", 30), height=40, corner_radius=10,
                                        compound="right",  
                                        command=self.generate_and_open_battery_report)
        generate_button.pack(pady=20, padx=5)

        self.message_label = ctk.CTkLabel(self, text="", font=("Comic Sans MS", 15))
        self.message_label.pack(pady=10, padx=5)

    def generate_and_open_battery_report(self):
        try:
            report_path = os.path.join(os.getcwd(), 'battery-report.html')

            subprocess.run(['powercfg', '/batteryreport', '/output', report_path], check=True)

            if os.path.exists(report_path):
                self.message_label.configure(text="      Battery report generated successfully! Opening the report...        ", fg_color="green")
                webbrowser.open(report_path)
            else:
                self.message_label.configure(text=" Battery report was not found. Something went wrong. ", fg_color="red")

        except subprocess.CalledProcessError as e:
            self.message_label.configure(text=f"An error occurred: {e}", fg_color="red")
