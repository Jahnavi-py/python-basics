with open("file_log.txt", "w") as file:
    file.write("2024-12-28 10:30:45 INFO User logged in\n")
    file.write("2024-12-28 10:31:05 ERROR Failed to connect to database\n")
    file.write("2024-12-28 10:32:15 WARNING Disk space running low\n")
    file.write("2024-12-28 10:33:25 INFO File uploaded\n")
    file.write("2024-12-28 10:34:45 ERROR Timeout while accessing resource\n")
print(f"Log file '{"file_log.txt"}' created successfully.")