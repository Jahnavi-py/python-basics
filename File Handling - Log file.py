#implement a program to read a log file and generate a summary report (e.g., count errors, warnings).
import re
from collections import Counter
log_file = "file_log.txt"
def generate_log_report(log_file, report_file):
    try:
        total_entries = 0
        log_levels = Counter()
        error_details = []

        # Read the log file
        with open(log_file, "r") as file:
            for line in file:
                total_entries += 1
                match = re.search(r'\b(INFO|ERROR|WARNING)\b', line)
                if match:
                    log_level = match.group(0)
                    log_levels[log_level] += 1
                    if log_level == "ERROR":
                        error_details.append(line.strip())
        with open(report_file, "w") as report:
            report.write(f"Log Report for {log_file}\n")
            report.write("=" * 40 + "\n")
            report.write(f"Total log entries: {total_entries}\n")
            report.write("\nLog Level Counts:\n")
            for level, count in log_levels.items():
                report.write(f"  {level}: {count}\n")
            report.write("\nError Details:\n")
            if error_details:
                for error in error_details:
                    report.write(f"  {error}\n")
            else:
                report.write("  No errors found.\n")
        print(f"Log report generated: {report_file}")
    except FileNotFoundError:
        print(f"Error: The file '{log_file}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
report_file = "file_log_report.txt"
generate_log_report(log_file, report_file)
