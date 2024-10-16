import psutil
import time

def get_top_processes(n=5):
    # الحصول على جميع العمليات
    processes = [(proc.info['pid'], proc.info['name'], proc.info['cpu_percent'], proc.info['memory_info'].rss)
                 for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info'])]

    # فرز العمليات حسب استهلاك المعالج ثم الذاكرة
    sorted_processes = sorted(processes, key=lambda proc: (proc[2], proc[3]), reverse=True)

    return sorted_processes[:n]

def terminate_process(pid):
    try:
        proc = psutil.Process(pid)
        proc.terminate()
        proc.wait()  # الانتظار حتى يتم إنهاء العملية
        return True
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return False

def display_process_info(process):
    pid, name, cpu, memory = process
    print(f"PID: {pid}, Name: {name}, CPU Usage: {cpu}%, Memory Usage: {memory / (1024 * 1024):.2f} MB")

def get_system_usage():
    # الحصول على معلومات استخدام المعالج والذاكرة
    cpu_usage = psutil.cpu_percent(interval=1)  # الحصول على استخدام المعالج
    memory_info = psutil.virtual_memory()  # الحصول على معلومات الذاكرة
    memory_usage = memory_info.percent
    return cpu_usage, memory_usage

def main():
    while True:
        print("Top resource-consuming processes:")
        top_processes = get_top_processes()

        print(f"{'PID':<10} {'Name':<30} {'CPU (%)':<10} {'Memory (MB)':<15}")
        for pid, name, cpu, memory in top_processes:
            display_process_info((pid, name, cpu, memory))

        # عرض استخدام النظام
        cpu_usage, memory_usage = get_system_usage()
        print(f"\nSystem CPU Usage: {cpu_usage}%")
        print(f"System Memory Usage: {memory_usage}%")

        # خيار لإغلاق عملية
        terminate_pid = input("\nEnter PID to terminate (or press Enter to quit, 'q' to quit): ").strip()
        if terminate_pid == '' or terminate_pid.lower() == 'q':
            print("Exiting the program.")
            break
        else:
            try:
                pid = int(terminate_pid)
                if terminate_process(pid):
                    print(f"Process with PID {pid} terminated successfully.")
                else:
                    print(f"Failed to terminate process with PID {pid}.")
            except ValueError:
                print("Invalid PID. Please enter a valid integer.")
        
        # الانتظار لمدة 5 ثوانٍ قبل التحديث لتقليل التكرار
        time.sleep(5)

if __name__ == "__main__":
    main()

