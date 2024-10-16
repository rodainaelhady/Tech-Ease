import customtkinter as ctk
import speedtest
from PIL import Image
from customtkinter import CTkImage
from tkinter import messagebox

class SpeedTest(ctk.CTkFrame):
    def __init__(self, parent, show_frame):
        super().__init__(parent)
        speed_image = ctk.CTkImage(Image.open("images/speed2.png"), size=(70, 70))
        
        # زر للعودة للقائمة الرئيسية في أقصى اليسار
        arrow_image = ctk.CTkImage(Image.open("images/home.png"), size=(24, 24))
        back_button = ctk.CTkButton(self, text="Home", image=arrow_image, font=("Comic Sans MS", 20), height=35,
                                     compound="left", command=lambda: show_frame(None))
        back_button.pack(side="top", anchor="nw", padx=10, pady=10)  # وضع الزر في أعلى اليسار

        # عنوان الصفحة في المنتصف
        label = ctk.CTkLabel(self, text="Speed Test", font=("Comic Sans MS", 60), image=speed_image, compound="right")
        label.pack(pady=(10, 20))  # وضعه تحت الزر

        # إنشاء فريم لتجميع المربعات جنبًا إلى جنب
        squares_frame = ctk.CTkFrame(self, fg_color="#2B2B2B")
        squares_frame.pack(pady=20)

        # إضافة مربعات لنتائج السرعة في فريمات منفصلة وتوزيعها باستخدام grid
        self.download_square = self.add_result_square(squares_frame, "Download", "images/download.png", size=(60, 60), row=0, column=0)
        self.upload_square = self.add_result_square(squares_frame, "Upload", "images/upload.png", size=(60, 60), row=0, column=1)
        self.ping_square = self.add_result_square(squares_frame, "Ping", "images/ping.png", size=(60, 60), row=0, column=2)

        # زر لبدء اختبار السرعة
        test_image = ctk.CTkImage(Image.open("images/test.png"), size=(30, 30))
        start_button = ctk.CTkButton(self, text="Test", font=("Comic Sans MS", 30), image=test_image, compound="right", command=self.start_speed_test)
        start_button.pack(pady=20)

    def start_speed_test(self):
        try:
            # تنفيذ اختبار السرعة
            download, upload, ping = self.test_internet_speed()

            # تحديث النتائج في المربعات
            self.update_result_square(self.download_square, f"Speed: {download:.2f} Mbps")
            self.update_result_square(self.upload_square, f"Speed: {upload:.2f} Mbps")
            self.update_result_square(self.ping_square, f"Ping: {ping} ms")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def test_internet_speed(self):
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000  # تحويل إلى ميغابت/ثانية
        upload_speed = st.upload() / 1_000_000  # تحويل إلى ميغابت/ثانية
        ping = st.results.ping

        return download_speed, upload_speed, ping

    def add_result_square(self, parent, text, image_path, size=(100, 100), row=0, column=0):
        # إنشاء مربع جديد
        square_frame = ctk.CTkFrame(parent, corner_radius=10, fg_color="#2B2B2B", width=500, height=300)
        square_frame.grid(row=row, column=column, padx=50, pady=10)

        # إضافة صورة باستخدام CTkImage
        image = Image.open(image_path)
        image = image.resize(size, Image.LANCZOS)  # ضبط حجم الصورة
        photo = CTkImage(light_image=image, dark_image=image, size=size)

        # إضافة الصورة للمربع
        image_label = ctk.CTkLabel(square_frame, image=photo, text="")
        image_label.pack(pady=(10, 5))

        # إضافة النص
        label = ctk.CTkLabel(square_frame, text=text, font=("Comic Sans MS", 20), text_color="white")
        label.pack(pady=(5, 10))

        return square_frame

    def update_result_square(self, square_frame, text):
        # تحديث النص في المربع
        for widget in square_frame.winfo_children():
            if isinstance(widget, ctk.CTkLabel) and widget.cget("text") != "":
                widget.configure(text=text)

def main():
    # إعداد نافذة التطبيق
    app = ctk.CTk()
    app.title("Internet Speed Test Tool")
    app.geometry("800x600")

    # إنشاء إطار لاختبار السرعة
    speed_test_frame = SpeedTest(app, show_frame=lambda x: None)
    speed_test_frame.pack(expand=True, fill="both")

    app.mainloop()

if __name__ == "__main__":
    main()
