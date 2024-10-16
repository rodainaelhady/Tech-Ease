import customtkinter as ctk
from PIL import Image

# الدالة التي تتحقق من قوة كلمة المرور
def check_password_strength(password):
    if len(password) < 8:
        return "weak"
    elif not any(char.isupper() for char in password):
        return "weak"
    elif not any(char.islower() for char in password):
        return "weak"
    elif not any(char.isdigit() for char in password):
        return "weak"
    elif not any(char in '!@#$%^&*()-_=+[]{}|;:,.<>?`~' for char in password):
        return "weak"
    else:
        return "strong"

# واجهة المستخدم للتحقق من قوة كلمة المرور
class CheckPasswordStrength(ctk.CTkFrame):
    def __init__(self, parent, show_frame):
        super().__init__(parent)
        arrow_image = ctk.CTkImage(Image.open("images/home.png"), size=(24, 24))

        # زر الرجوع إلى القائمة الرئيسية (محاذاة في الأعلى أقصى الشمال)
        back_button = ctk.CTkButton(self, text="Home", image=arrow_image, font=("Comic Sans MS", 20), height=35,
                                    compound="left", command=lambda: show_frame(None))
        back_button.pack(pady=10, padx=10, anchor="w")  # زر في أقصى الشمال العلوي

        storng_password_image = ctk.CTkImage(Image.open("images/strong_password2.png"), size=(50, 50))
        # العنوان في المنتصف
        label = ctk.CTkLabel(self, text="Password Strength", image=storng_password_image, compound="right", font=("Comic Sans MS", 60))
        label.pack(pady=20, anchor="center")  # العنوان في المنتصف

        # إدخال كلمة المرور
        self.password_entry = ctk.CTkEntry(self, show="*", placeholder_text="Enter your password", width=290, font=("Comic Sans MS", 20))
        self.password_entry.pack(pady=20, anchor="center")

        check_image = ctk.CTkImage(Image.open("images/check.png"), size=(30, 30))
        # زر التحقق من قوة كلمة المرور
        check_button = ctk.CTkButton(self, text="Check", font=("Comic Sans MS", 30), image=check_image, compound="right", height=40, corner_radius=10, command=self.display_password_strength)
        check_button.pack(pady=20, anchor="center")

        # منطقة عرض النتيجة
        self.result_label = ctk.CTkLabel(self, text="", font=("Arial", 20), compound="right")
        self.result_label.pack(pady=20, anchor="center")

    # دالة لعرض قوة كلمة المرور مع الصورة
    def display_password_strength(self):
        password = self.password_entry.get()
        strength = check_password_strength(password)

        # إعداد النص حسب قوة كلمة المرور
        self.result_label.configure(text=f"Password is {strength} ", font=("Comic Sans MS",30),text_color="green" if strength == "strong" else "red")

        # إعداد الصورة حسب قوة كلمة المرور
        if strength == "strong":
            result_image = ctk.CTkImage(Image.open("images/strong.png"), size=(50, 50))
        else:
            result_image = ctk.CTkImage(Image.open("images/weak.png"), size=(50, 50))

        # تحديث النص والصورة معًا
        self.result_label.configure(image=result_image)
        self.result_label.image = result_image  # للحفاظ على الصورة
