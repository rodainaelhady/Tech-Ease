import subprocess

def list_installed_programs():
    # Command to list installed programs using wmic
    command = 'wmic product get name'
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        programs = result.stdout.splitlines()
        programs = [p.strip() for p in programs if p.strip()]  # Clean and filter the output
        print("Installed programs:")
        for idx, program in enumerate(programs[1:], 1):  # Skip the first line (header)
            print(f"{idx}. {program}")
        return programs[1:]  # Return program list without the header
    except Exception as e:
        print(f"An error occurred while listing the installed programs: {e}")
        return []

def uninstall_program(program_name):
    # Command to uninstall a program using wmic
    command = f'wmic product where "name=\'{program_name}\'" call uninstall'
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        if "ReturnValue = 0" in result.stdout:
            print(f"{program_name} uninstalled successfully!")
        else:
            print(f"Failed to uninstall {program_name}. It might require manual removal.")
    except Exception as e:
        print(f"An error occurred while trying to uninstall {program_name}: {e}")

def main():
    programs = list_installed_programs()
    if programs:
        try:
            choice = int(input("Enter the number of the program you want to uninstall (or 0 to cancel): "))
            if 0 < choice <= len(programs):
                program_to_uninstall = programs[choice - 1]
                confirm = input(f"Are you sure you want to uninstall '{program_to_uninstall}'? (y/n): ")
                if confirm.lower() == 'y':
                    uninstall_program(program_to_uninstall)
                else:
                    print("Uninstallation cancelled.")
            else:
                print("Invalid selection. Exiting...")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        print("No programs found or an error occurred.")

# Run the main function
main()
