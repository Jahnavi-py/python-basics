import hashlib
import os

# File paths
USERS_FILE = "users.txt"
TASKS_FILE = "tasks.txt"

# Helper functions for file handling
def read_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, 'r') as file:
        users = {}
        for line in file.readlines():
            username, password = line.strip().split(",")
            users[username] = password
        return users

def save_user(username, password_hash):
    with open(USERS_FILE, 'a') as file:
        file.write(f"{username},{password_hash}\n")

def read_tasks(username):
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            for line in file.readlines():
                task_id, user, description, status = line.strip().split(",", 3)
                if user == username:
                    tasks.append([task_id, description, status])
    return tasks

def save_task(task_id, username, description, status="Pending"):
    with open(TASKS_FILE, 'a') as file:
        file.write(f"{task_id},{username},{description},{status}\n")

def update_task_status(task_id, new_status):
    with open(TASKS_FILE, 'r') as file:
        lines = file.readlines()
    with open(TASKS_FILE, 'w') as file:
        for line in lines:
            task_id_in_file, username, description, status = line.strip().split(",", 3)
            if task_id_in_file == task_id:
                file.write(f"{task_id_in_file},{username},{description},{new_status}\n")
            else:
                file.write(line)

def delete_task(task_id):
    with open(TASKS_FILE, 'r') as file:
        lines = file.readlines()
    with open(TASKS_FILE, 'w') as file:
        for line in lines:
            task_id_in_file, username, description, status = line.strip().split(",", 3)
            if task_id_in_file != task_id:
                file.write(line)

# User Authentication
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    users = read_users()
    username = input("Enter username: ")
    if username in users:
        print("Username already exists. Please choose another.")
        return
    password = input("Enter password: ")
    password_hash = hash_password(password)
    save_user(username, password_hash)
    print("Registration successful!")

def login():
    users = read_users()
    username = input("Enter username: ")
    password = input("Enter password: ")
    password_hash = hash_password(password)
    if username in users and users[username] == password_hash:
        print("Login successful!")
        return username
    else:
        print("Invalid credentials!")
        return None

# Task Management
def add_task(username):
    description = input("Enter task description: ")
    task_id = str(len(read_tasks(username)) + 1)  # Simple task ID generation
    save_task(task_id, username, description)
    print(f"Task '{description}' added with ID {task_id}.")

def view_tasks(username):
    tasks = read_tasks(username)
    if tasks:
        print(f"\nTasks for {username}:")
        for task in tasks:
            task_id, description, status = task
            print(f"ID: {task_id}, Description: {description}, Status: {status}")
    else:
        print("No tasks available.")

def mark_task_completed(username):
    view_tasks(username)
    task_id = input("Enter task ID to mark as completed: ")
    update_task_status(task_id, "Completed")
    print(f"Task {task_id} marked as completed.")

def delete_task(username):
    view_tasks(username)
    task_id = input("Enter task ID to delete: ")
    delete_task(task_id)
    print(f"Task {task_id} deleted.")

# Main Program
def main():
    while True:
        print("\nTask Manager")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            username = login()
            if username:
                while True:
                    print("\nTask Management")
                    print("1. Add Task")
                    print("2. View Tasks")
                    print("3. Mark Task as Completed")
                    print("4. Delete Task")
                    print("5. Logout")
                    action = input("Enter your choice: ")

                    if action == "1":
                        add_task(username)
                    elif action == "2":
                        view_tasks(username)
                    elif action == "3":
                        mark_task_completed(username)
                    elif action == "4":
                        delete_task(username)
                    elif action == "5":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice!")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
