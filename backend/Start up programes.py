import winreg
import os

def list_startup_programs():
    # مسارات مفاتيح التسجيل لبرامج بدء التشغيل
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

def disable_startup_program(program_name):
    keys = [
        r"Software\Microsoft\Windows\CurrentVersion\Run",
        r"Software\Microsoft\Windows\CurrentVersion\RunOnce"
    ]

    for key_path in keys:
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE) as key:
                try:
                    winreg.DeleteValue(key, program_name)
                    print(f"Disabled: {program_name}")
                    return
                except FileNotFoundError:
                    continue
        except FileNotFoundError:
            pass

    print(f"Program not found: {program_name}")

def main():
    print("Listing startup programs...")
    programs = list_startup_programs()
    for name, path in programs:
        print(f"Name: {name}, Path: {path}")
    
    print("\nEnter the name of the program to disable (or 'exit' to quit):")
    while True:
        program_name = input().strip()
        if program_name.lower() == 'exit':
            break
        disable_startup_program(program_name)

if __name__ == "__main__":
    main()
