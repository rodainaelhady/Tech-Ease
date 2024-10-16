import subprocess
import customtkinter as ctk
from PIL import Image

class NetworkCheck(ctk.CTkFrame):
    def __init__(self, parent, show_frame):
        super().__init__(parent)

        # زر للعودة للقائمة الرئيسية في أعلى يسار الشاشة
        back_icon = ctk.CTkImage(Image.open("images/home.png"), size=(20, 20))

        back_button = ctk.CTkButton(self, text="Home", font=("Comic Sans MS", 20), height=35, image=back_icon, compound="left",
                                     command=lambda: show_frame(None))
        back_button.pack(side=ctk.TOP, anchor=ctk.W, padx=(10, 0), pady=(10, 0))

        # عنوان الصفحة في المنتصف
        network_image=ctk.CTkImage(Image.open("images/network2.png"),size=(50,50))        
        label = ctk.CTkLabel(self, text="Network Check ", font=("Comic Sans MS", 60),image=network_image,compound='right')
        label.pack(pady=(20, 20))

        # إعداد التيسكت بوكس مع تغيير اللون ونوع الخط
        self.result_textbox = ctk.CTkTextbox(self, 
                                              width=600, 
                                              height=300, 
                                              corner_radius=10, 
                                              fg_color="#2B2B2B",  # لون خلفية التيسكت بوكس
                                              text_color="white",   # لون النص
                                              font=("Comic Sans MS", 15))   # نوع الخط وحجمه
        self.result_textbox.pack(pady=20)

        # زر لبدء عملية إعادة تعيين الشبكة
        reset_image=ctk.CTkImage(Image.open("images/reset.png"),size=(30,30))
        reset_button = ctk.CTkButton(self, text="Reset Network", font=("Comic Sans MS", 30),command=self.reset_network,image=reset_image,compound="right")
        reset_button.pack(pady=20)

    def reset_network(self):
        self.result_textbox.delete('1.0', ctk.END)  # مسح النص الموجود
        try:
            # تنفيذ ipconfig /release
            self.result_textbox.insert(ctk.END, "Releasing IP address...\n")
            release_result = subprocess.run(["ipconfig", "/release"], capture_output=True, text=True, check=True)
            self.result_textbox.insert(ctk.END, release_result.stdout)  # إدراج ناتج الأمر
            
            # تنفيذ ipconfig /renew
            self.result_textbox.insert(ctk.END, "Renewing IP address...\n")
            renew_result = subprocess.run(["ipconfig", "/renew"], capture_output=True, text=True, check=True)
            self.result_textbox.insert(ctk.END, renew_result.stdout)  # إدراج ناتج الأمر
            
            self.result_textbox.insert(ctk.END, "Network settings reset successfully.\n")
        except subprocess.CalledProcessError as e:
            self.result_textbox.insert(ctk.END, f"An error occurred while resetting network settings: {e}\n")

def main():
    # إعداد نافذة التطبيق
    app = ctk.CTk()
    app.title("Network Reset Tool")
    app.geometry("800x600")

    # إنشاء إطار لتطبيق الواجهة
    network_check_frame = NetworkCheck(app, show_frame=lambda x: None)
    network_check_frame.pack(expand=True, fill="both")

    app.mainloop()

if __name__ == "__main__":
    main()
