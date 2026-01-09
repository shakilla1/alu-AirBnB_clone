# alu-AirBnB_clone - The console

# The AirBnB clone project!

# Project Description

This project is for craeting an AiRBnB_clone application, where we will be creating a command-line console that allows sers to interact with the backend of the system.

The console is written in python and is used to manage differnt objects such as Users, places, states and cities. All data created in console are saved in a json file, allowing it to persist between sessions.

# The purpose of this project

The main purpose of this app is to:
- practice object oriented programming in python
- Build a command interpreter 
- Store and reterive data using JSON, and etc.

Description of command interpreter

The command interpreter works the same way as a basic shell.
Instead of system commands, It understands a specific set of commands designed to manage the project's data.

Using the console a user can:

a) Create new objects( example a user)
b) View existing objects 
c) Modify object attributes
d) Deletes objects
e) count how many objects exists of a given type

# How to start a console

# Requirements

- Python3
- Git
- A linux or Unix-based environment

# Installation steps
You must clone the repository from github like this:

git clone https://github.com/shakilla1/alu-AirBnB_clone

Move into directory of the project:

cd alu-AirBnB_clone

Run the console:

./console.py

or

python3 console.py

after running it, you will see something like this : (hbnb)

Project structure

console.py            - Entry point of the application
models/               - Contains all data models
models/engine/        - Handles file storage
file_storage.py       - Saves and loads data using JSON

# How to use the console

the cosole can be used in two different modes

1. Interactive mode

In this mode the console remain open and waits for commands.

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

you can exit using quit or EOF

2. Non_interactive mode

In this mode the commands are passed directly to console. In this mode no prompt will appear, and no further input will be expected from the user.

$ echo "create User" | ./console.py

This is for testing

Available commands and what they does

| Command      | What it Does             |
| ------------ | ------------------------ |
| `help`       | Shows available commands |
| `create`     | Creates a new object     |
| `show`       | Displays an object       |
| `update`     | Modifies an object       |
| `destroy`    | Deletes an object        |
|`all`         | Lists objects            |
|`count`       | Counts objects           |
|`quit / EOF`  | Exits the console        |


Authors

-Shakilla Uwamahoro s.uwamahoro1@alustudent.com
-Liliane Uwase l.uwase@alustudent.com

