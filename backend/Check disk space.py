import subprocess

def bytes_to_gb(bytes_value):
    """تحويل من بايت إلى جيجابايت"""
    return round(bytes_value / (1024 ** 3), 2)  # تحويل bytes إلى GB مع تقريب القيم إلى منزلتين عشريتين

def check_all_drives_space():
    try:
        # استدعاء أمر PowerShell لفحص المساحة المستخدمة والمتبقية لكل الأقراص المتصلة
        result = subprocess.run(["powershell", "-Command", "Get-PSDrive -PSProvider FileSystem | Select-Object Name, Used, Free"], capture_output=True, text=True)

        # طباعة النتائج
        if result.returncode == 0:
            # تقسيم الناتج لأسطر
            output_lines = result.stdout.strip().splitlines()
            
            # معالجة البيانات بدءًا من السطر الثاني لأن السطر الأول هو العناوين
            for line in output_lines[2:]:
                # تقسيم السطر للحصول على اسم القرص، المساحة المستخدمة، والمساحة المتاحة
                columns = line.split()
                drive_name = columns[0]   # اسم القرص
                used_space = int(columns[1])  # المساحة المستخدمة بالـ Bytes
                free_space = int(columns[2])  # المساحة المتاحة بالـ Bytes

                # تحويل المساحة من Bytes إلى GB
                used_space_gb = bytes_to_gb(used_space)
                free_space_gb = bytes_to_gb(free_space)

                # طباعة المساحة المستخدمة والمتاحة لكل قرص بالـ GB
                print(f"Drive {drive_name}:")
                print(f"    Used space: {used_space_gb} GB")
                print(f"    Free space: {free_space_gb} GB")
                print()

        else:
            print("Failed to retrieve disk space information.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# استدعاء الدالة للتحقق من مساحة جميع الأقراص
check_all_drives_space()
