import sqlite3

# Connect to SQLite database (or create one if it doesn't exist)
conn = sqlite3.connect("todo.db")
cursor = conn.cursor()

# Create the tasks table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        status TEXT CHECK(status IN ('Pending', 'Completed')) NOT NULL DEFAULT 'Pending'
    )
''')
conn.commit()

def add_task():
    """Add a new task to the list."""
    task = input("Enter the task description: ").strip()
    if task:
        cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
        conn.commit()
        print("Task added successfully.")
    else:
        print("Task description cannot be empty!")

def view_tasks():
    """Display all tasks in the list."""
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    if not tasks:
        print("No tasks found.")
    else:
        print("\nTo-Do List:")
        for task in tasks:
            print(f"{task[0]}. {task[1]} - [{task[2]}]")

def update_task():
    """Mark a task as completed."""
    view_tasks()
    task_id = input("\nEnter Task ID to mark as completed: ").strip()
    if task_id.isdigit():
        cursor.execute("UPDATE tasks SET status = 'Completed' WHERE id = ?", (task_id,))
        conn.commit()
        print("Task updated successfully.")
    else:
        print("Invalid Task ID!")

def delete_task():
    """Delete a task from the list."""
    view_tasks()
    task_id = input("\nEnter Task ID to delete: ").strip()
    if task_id.isdigit():
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        print("Task deleted successfully.")
    else:
        print("Invalid Task ID!")

def main():
    """Main loop for the To-Do List application."""
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("\nEnter your choice: ").strip()
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

    conn.close()

# Run the application
if __name__ == "__main__":
    main()
