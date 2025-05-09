# Python-Task-Manager
A basic task manager made in Python

Author: Timothy Johnson <br>
Date: November 2024

## Overview

A lightweight, command-line based task management application built in Python.
This simple tool allows users to add, view, complete, delete, and filter tasks with ease—perfect for basic to-do tracking directly from your terminal.

Python Task Manager is a beginner-friendly, functional command-line tool for managing personal tasks.
It features task addition, completion toggling, viewing all tasks, deletion, and basic filtering—all stored in a temporary in-memory list for quick usage without external dependencies.

🧩 Features

    ➕ Add new tasks with simple input

    ✅ Mark tasks as complete via index selection

    👀 View all tasks with completion status

    ❌ Delete tasks using task number

    🔎 Filter by completed or incomplete status

    🖥️ Console-based interface—simple and effective

🔄 User Workflow

    Run the script

    Choose an option from the main menu:

        1 --- Add a task

        2 --- Mark a task as complete

        3 --- View all tasks

        4 --- Delete a task

        5 --- Filter by task status

        6 --- Exit the program

    Interact with tasks through simple input

    Exit anytime and start fresh next time (no persistent storage)

📁 Code Structure

Python-Task-Manager/
├── task_manager.py &nbsp;&nbsp;&nbsp;---&nbsp;&nbsp;&nbsp; Main Python script containing task logic and CLI loop

⚙️ How It Works

    In-Memory Storage
    Tasks are stored in a list of dictionaries like:
    {"task": "Buy groceries", "completed": False}

    Menu System
    A while True loop shows the menu and handles user input via numbered options.

    Function Breakdown

        add_task() → prompts user input and appends to the list

        mark_task_complete() → allows marking tasks by index

        view_tasks() → prints all tasks with status

        delete_task() → removes task by number

        filter_tasks() → displays only completed/incomplete tasks

🖼️ Screenshots / Visuals

![pythontaskbanner](https://github.com/user-attachments/assets/8ae89f38-ee7e-4a09-adcd-21da330d69e5)

Welcome to the Task Manager Application!

1. Add Task
2. Mark Task as Complete
3. View Tasks
4. Delete Task
5. Filter Tasks
6. Exit
   
Please enter your choice:


🧰 Technologies Used

    🐍 Python 3 (No external libraries needed)

🚀 Getting Started

    To run locally:

      Clone the repo:

        git clone https://github.com/yourusername/Python-Task-Manager.git
        cd Python-Task-Manager

      Run the script:

        python task_manager.py

      Follow the menu prompts in your terminal.

🌱 Upcoming Features

    💾 Persistent storage with file saving (JSON or CSV)

    🕒 Task due dates and reminders

    🔁 Edit task descriptions

    📁 Group tasks by category or project

    📊 Task analytics or statistics

🪪 License

This project is open source and available under the [MIT License](https://opensource.org/license/mit).
