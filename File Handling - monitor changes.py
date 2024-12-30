#Write a program to monitor changes to a file (e.g., real-time updates to a log file).
import time


def monitor_file(file_path):
    try:
        with open(file_path, "r") as file:
            file.seek(0, 2)  # Move the cursor to the end of the file
            print(f"Monitoring changes to '{file_path}'... Press Ctrl+S to stop.")

            while True:
                try:
                    line = file.readline()
                    if line:  # If a new line is read
                        print(line, end="")
                    else:
                        time.sleep(0.5)  # Wait before checking for updates
                except KeyboardInterrupt:
                    print("\nMonitoring stopped by user.")  # Handle Ctrl+C during reading
                    break  # Exit the loop
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Specify the file to monitor
file_to_monitor = "file_monitor.txt"
with open(file_to_monitor, "w") as file:
    file.write("Log started...\n")
    file.write("New log entry 1\n")
    file.write("New log entry 2\n")
# Start monitoring
try:
    monitor_file(file_to_monitor)
except KeyboardInterrupt:
    print("\nProgram terminated.")
