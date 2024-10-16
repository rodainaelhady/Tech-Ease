import subprocess
import os
import webbrowser

def generate_and_open_battery_report():
    try:
        # Run the powercfg /batteryreport command
        subprocess.run(['powercfg', '/batteryreport'], check=True)

        # Define the path where the report is saved
        report_path = os.path.join(os.environ['HOMEPATH'], 'battery-report.html')

        # Check if the report exists
        if os.path.exists(report_path):
            print(f"Battery report generated successfully! Opening the report at: {report_path}")
            
            # Open the report in the default web browser
            webbrowser.open(report_path)
        else:
            print("Battery report was not found. Something went wrong.")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while generating the battery report: {e}")

# Call the function to generate and open the battery report
generate_and_open_battery_report()
