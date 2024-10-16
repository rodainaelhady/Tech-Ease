import subprocess

def reset_network():
    try:
        # تنفيذ ipconfig /release
        print("Releasing IP address...")
        subprocess.run(["ipconfig", "/release"], check=True)
        
        # تنفيذ ipconfig /renew
        print("Renewing IP address...")
        subprocess.run(["ipconfig", "/renew"], check=True)
        
        print("Network settings reset successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while resetting network settings: {e}")

if __name__ == "__main__":
    reset_network()
