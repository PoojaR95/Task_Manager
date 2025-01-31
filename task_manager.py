import sqlite3

database_name = "tasks.db"

def create_table():
    """Creates the tasks table if it doesn't exist."""
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            deadline TEXT,
            status TEXT CHECK(status IN ('pending', 'completed')) DEFAULT 'pending'
        )
    """)
    conn.commit()
    conn.close()

def add_task(description, deadline=None):
    """Adds a new task to the database."""
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (description, deadline, status) VALUES (?, ?, 'pending')",
                   (description, deadline))
    conn.commit()
    conn.close()
    print("Task added successfully.")

def view_tasks(filter_status=None):
    """Displays all tasks or filters by status."""
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    if filter_status:
        cursor.execute("SELECT * FROM tasks WHERE status=?", (filter_status,))
    else:
        cursor.execute("SELECT * FROM tasks")

    tasks = cursor.fetchall()
    conn.close()

    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            print(f"[{task[0]}] {task[1]} | Deadline: {task[2] or 'N/A'} | Status: {task[3]}")

def update_task(task_id, description=None, status=None):
    """Updates a task's description or status."""
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    if description:
        cursor.execute("UPDATE tasks SET description=? WHERE id=?", (description, task_id))
    
    if status:
        cursor.execute("UPDATE tasks SET status=? WHERE id=?", (status, task_id))

    conn.commit()
    conn.close()
    print("Task updated successfully.")

def delete_task(task_id):
    """Deletes a task from the database."""
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
    print("Task deleted successfully.")

def main():
    """Main command-line interface."""
    create_table()

    while True:
        print("\nTask Manager")
        print("1. Add a Task")
        print("2. View All Tasks")
        print("3. View Pending Tasks")
        print("4. View Completed Tasks")
        print("5. Update a Task")
        print("6. Delete a Task")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter task description: ")
            deadline = input("Enter deadline (YYYY-MM-DD) or leave blank: ")
            add_task(description, deadline)

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            view_tasks("pending")

        elif choice == "4":
            view_tasks("completed")

        elif choice == "5":
            task_id = input("Enter Task ID to update: ")
            desc = input("Enter new description (leave blank to skip): ")
            status = input("Enter new status (pending/completed, leave blank to skip): ")
            update_task(task_id, desc if desc else None, status if status else None)

        elif choice == "6":
            task_id = input("Enter Task ID to delete: ")
            delete_task(task_id)

        elif choice == "7":
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "_main_":
    main()