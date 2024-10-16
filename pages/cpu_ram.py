import psutil
import time
import customtkinter as ctk
import subprocess
from PIL import Image

class CPURAM(ctk.CTkFrame):
    def __init__(self, parent, show_frame):
        super().__init__(parent)

        # زر للعودة للقائمة الرئيسية في أعلى يسار الشاشة
        back_icon = ctk.CTkImage(Image.open("images/home.png"), size=(20, 20))
        back_button = ctk.CTkButton(self, text="Home", font=("Comic Sans MS", 20), height=35, image=back_icon, compound="left",
                                     command=lambda: show_frame(None))
        back_button.pack(side=ctk.TOP, anchor=ctk.W, padx=(10, 0), pady=(10, 0))

        # عنوان الصفحة في المنتصف
        cpu_image = ctk.CTkImage(Image.open("images/cpu2.png"), size=(50, 50))
        label = ctk.CTkLabel(self, text="CPU & RAM Usage ", font=("Comic Sans MS", 60), image=cpu_image, compound="right")
        label.pack(pady=(10, 20))

        # قائمة لعرض العمليات مع تغيير نوع الخط والحجم
        self.process_listbox = ctk.CTkTextbox(self, width=600, height=300, corner_radius=10, font=("Comic Sans MS", 15), fg_color="#2B2B2B")
        self.process_listbox.pack(pady=10)

        # إطار لمدخل PID وزر الترميانات ليكونا جنب بعض
        button_frame = ctk.CTkFrame(self,fg_color="#2B2B2B")
        button_frame.pack(pady=10)

        # مدخل PID
        self.terminate_entry = ctk.CTkEntry(button_frame, placeholder_text="Enter PID to terminate", font=("Comic Sans MS", 20), width=195, height=50)
        self.terminate_entry.pack(side=ctk.LEFT, padx=(10, 0), pady=10)  # وضع المدخل في الجانب الأيسر

        # زر ترميانات
        kill_image = ctk.CTkImage(Image.open("images/kill.png"), size=(30, 30))
        terminate_button = ctk.CTkButton(button_frame, text="Terminate", image=kill_image, compound="right", font=("Comic Sans MS", 30), command=self.terminate_process)
        terminate_button.pack(side=ctk.LEFT, padx=(10, 0), pady=10)  # وضع الزر في الجانب الأيسر أيضًا

        # تحديث المعلومات بشكل دوري
        self.update_process_info()

    def update_process_info(self):
        # مسح القائمة الحالية
        self.process_listbox.delete('1.0', ctk.END)

        # الحصول على أعلى العمليات
        top_processes = self.get_top_processes()

        # عرض المعلومات في القائمة
        for pid, name, cpu, memory in top_processes:
            self.process_listbox.insert(ctk.END, f"PID: {pid}, Name: {name}, CPU Usage: {cpu}%, Memory Usage: {memory / (1024 * 1024):.2f} MB\n")
        
        # تحديث الاستخدام العام للنظام
        cpu_usage, memory_usage = self.get_system_usage()
        self.process_listbox.insert(ctk.END, f"\nSystem CPU Usage: {cpu_usage}%\n")
        self.process_listbox.insert(ctk.END, f"System Memory Usage: {memory_usage}%\n")

        # إعادة جدولة التحديث كل 5 ثواني
        self.after(5000, self.update_process_info)

    def get_top_processes(self, n=5):
        processes = [(proc.info['pid'], proc.info['name'], proc.info['cpu_percent'], proc.info['memory_info'].rss)
                     for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info'])]
        sorted_processes = sorted(processes, key=lambda proc: (proc[2], proc[3]), reverse=True)
        return sorted_processes[:n]

    def terminate_process(self):
        terminate_pid = self.terminate_entry.get().strip()
        if terminate_pid:
            try:
                pid = int(terminate_pid)
                if self.terminate_process_by_pid(pid):
                    self.process_listbox.insert(ctk.END, f"Process with PID {pid} terminated successfully.\n")
                else:
                    self.process_listbox.insert(ctk.END, f"Failed to terminate process with PID {pid}.\n")
            except ValueError:
                self.process_listbox.insert(ctk.END, "Invalid PID. Please enter a valid integer.\n")

    def terminate_process_by_pid(self, pid):
        try:
            # استخدام taskkill لإنهاء العملية
            subprocess.run(['taskkill', '/F', '/PID', str(pid)], check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def get_system_usage(self):
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        memory_usage = memory_info.percent
        return cpu_usage, memory_usage

def main():
    # إعداد نافذة التطبيق
    app = ctk.CTk()
    app.title("Resource Monitor")
    app.geometry("800x600")

    # إنشاء إطار لتطبيق الواجهة
    cpu_ram_frame = CPURAM(app, show_frame=lambda x: None)
    cpu_ram_frame.pack(expand=True, fill="both")

    app.mainloop()

if __name__ == "__main__":
    main()
