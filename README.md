Task Management Application-

A simple command-line Task Management Application built with Python and SQLite.
It allows users to add, view, update, and delete tasks, with persistent storage.

Features-

1. Add a Task (Description, Deadline, Status)
2. View All Tasks
3. View Pending Tasks
4. View Completed Tasks
5. Update a Task (Change description or mark as completed)
6. Delete a Task
7. Data Persistence with SQLite

Installation and setup-

1. Install Python
2. Create folder taskmanager and a python file, task_manager.py in it
3. Run the application using the command- python task_manager.py

Main Menu-
Task Management System
1. Add a Task
2. View All Tasks
3. View Pending Tasks
4. View Completed Tasks
5. Update a Task
6. Delete a Task
7. Exit

CRUD Operations-

Add a Task-
Select option 1
Enter details:
Task Description: Finish Python Assignment
Deadline (YYYY-MM-DD): 2025-02-05
Status: pending

View Tasks-
Option 2: View all tasks
Option 3: View only pending tasks
Option 4: View only completed tasks
✏ Update a Task
Select option 5
Enter the Task ID
Choose:
1 to change the description
2 to mark as completed

Delete a Task-
Select option 6
Enter the Task ID to delete the task.

Exit-
Select option 7 to quit the program.


How to view the database-
1.
run- sqlite3 tasks.db
SELECT * FROM tasks;

2. Using DB Browser for SQLite, open tasks.db and navigate to browse data
