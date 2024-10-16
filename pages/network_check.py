import subprocess
import customtkinter as ctk
from PIL import Image

class NetworkCheck(ctk.CTkFrame):
    def __init__(self, parent, show_frame):
        super().__init__(parent)

        back_icon = ctk.CTkImage(Image.open("images/home.png"), size=(20, 20))

        back_button = ctk.CTkButton(self, text="Home", font=("Comic Sans MS", 20), height=35, image=back_icon, compound="left",
                                     command=lambda: show_frame(None))
        back_button.pack(side=ctk.TOP, anchor=ctk.W, padx=(10, 0), pady=(10, 0))

        network_image=ctk.CTkImage(Image.open("images/network2.png"),size=(50,50))        
        label = ctk.CTkLabel(self, text="Network Check ", font=("Comic Sans MS", 60),image=network_image,compound='right')
        label.pack(pady=(20, 20))

        self.result_textbox = ctk.CTkTextbox(self, 
                                              width=600, 
                                              height=300, 
                                              corner_radius=10, 
                                              fg_color="#2B2B2B",  
                                              text_color="white",   
                                              font=("Comic Sans MS", 15))   
        self.result_textbox.pack(pady=20)

        reset_image=ctk.CTkImage(Image.open("images/reset.png"),size=(30,30))
        reset_button = ctk.CTkButton(self, text="Reset Network", font=("Comic Sans MS", 30),command=self.reset_network,image=reset_image,compound="right")
        reset_button.pack(pady=20)

    def reset_network(self):
        self.result_textbox.delete('1.0', ctk.END)  
        try:
            self.result_textbox.insert(ctk.END, "Releasing IP address...\n")
            release_result = subprocess.run(["ipconfig", "/release"], capture_output=True, text=True, check=True)
            self.result_textbox.insert(ctk.END, release_result.stdout)  
            
            self.result_textbox.insert(ctk.END, "Renewing IP address...\n")
            renew_result = subprocess.run(["ipconfig", "/renew"], capture_output=True, text=True, check=True)
            self.result_textbox.insert(ctk.END, renew_result.stdout)  
            
            self.result_textbox.insert(ctk.END, "Network settings reset successfully.\n")
        except subprocess.CalledProcessError as e:
            self.result_textbox.insert(ctk.END, f"An error occurred while resetting network settings: {e}\n")

def main():
    app = ctk.CTk()
    app.title("Network Reset Tool")
    app.geometry("800x600")

    network_check_frame = NetworkCheck(app, show_frame=lambda x: None)
    network_check_frame.pack(expand=True, fill="both")

    app.mainloop()

if __name__ == "__main__":
    main()
