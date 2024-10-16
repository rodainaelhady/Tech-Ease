import os
import platform
import shutil

def clear_temp_files():
    system_name = platform.system()  # تحديد نوع النظام
    if system_name == "Windows":
        temp_folder = os.getenv('TEMP')  # الحصول على مسار مجلد Temp
        if temp_folder:
            print(f"Cleaning temporary files in: {temp_folder}")
            try:
                # حذف جميع الملفات في مجلد TEMP
                for filename in os.listdir(temp_folder):
                    file_path = os.path.join(temp_folder, filename)
                    try:
                        if os.path.isfile(file_path) or os.path.islink(file_path):
                            os.unlink(file_path)
                        elif os.path.isdir(file_path):
                            shutil.rmtree(file_path)
                    except Exception as e:
                        print(f"Error deleting {file_path}: {e}")
                print("Temporary files cleaned successfully.")
            except Exception as e:
                print(f"Error accessing temp folder: {e}")
        else:
            print("Could not locate TEMP folder.")
    
    elif system_name == "Linux":
        temp_folder = "/tmp"  # مسار مجلد tmp
        print(f"Cleaning temporary files in: {temp_folder}")
        try:
            # حذف جميع الملفات في /tmp
            for filename in os.listdir(temp_folder):
                file_path = os.path.join(temp_folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")
            print("Temporary files cleaned successfully.")
        except Exception as e:
            print(f"Error accessing /tmp folder: {e}")
    else:
        print("Unsupported Operating System.")

# استدعاء الدالة لتنظيف الملفات المؤقتة
clear_temp_files()