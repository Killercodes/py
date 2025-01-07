import tkinter as tk
import os
import json
from tkinter import simpledialog

# Sample JSON data as provided
json_data = """
{
    "docker system df": {
        "cmd": "docker system df"
    },
    "docker info": {
        "cmd": "docker info"
    },
    "docker stop": {
        "cmd": "docker stop <container_id>",
        "parameter": "<container_id>"
    },
    "docker ps": {
        "cmd": "docker ps"
    },
    "docker build": {
        "cmd": "docker build <path>",
        "parameter": "<path>"
    },
    "docker images": {
        "cmd": "docker images"
    },
    "docker pull": {
        "cmd": "docker pull <image_name>",
        "parameter": "<image_name>"
    },
    "docker push": {
        "cmd": "docker push <image_name>",
        "parameter": "<image_name>"
    },
    "docker run": {
        "cmd": "docker run <image_name>",
        "parameter": "<image_name>"
    },
    "docker exec": {
        "cmd": "docker exec <container_id> <command>",
        "parameter": "<container_id>"
    },
    "docker logs": {
        "cmd": "docker logs <container_id>",
        "parameter": "<container_id>"
    },
    "docker rm": {
        "cmd": "docker rm <container_id>",
        "parameter": "<container_id>"
    },
    "docker rmi": {
        "cmd": "docker rmi <image_id>",
        "parameter": "<image_id>"
    },
    "docker network ls": {
        "cmd": "docker network ls"
    },
    "docker volume ls": {
        "cmd": "docker volume ls"
    },
    "docker pause": {
        "cmd": "docker pause <container_id>",
        "parameter": "<container_id>"
    },
    "docker unpause": {
        "cmd": "docker unpause <container_id>",
        "parameter": "<container_id>"
    },
    "docker stats": {
        "cmd": "docker stats"
    },
    "docker inspect": {
        "cmd": "docker inspect <container_or_image_id>",
        "parameter": "<container_or_image_id>"
    },
    "docker tag": {
        "cmd": "docker tag <source_image> <target_image>",
        "parameter": "<source_image>"
    },
    "docker login": {
        "cmd": "docker login <registry>",
        "parameter": "<registry>"
    },
    "docker logout": {
        "cmd": "docker logout <registry>",
        "parameter": "<registry>"
    },
    "docker version": {
        "cmd": "docker version"
    },
    "docker help": {
        "cmd": "docker help"
    }
}
"""

# Parse the JSON string
data = json.loads(json_data)

def create_button(command, cmd_details, row, column):
    button = tk.Button(button_frame, text=command, command=lambda: run_command(cmd_details))
    button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
    return button

def run_command(cmd_details):
    command = cmd_details["cmd"]
    
    if "parameter" in cmd_details:
        parameter = cmd_details["parameter"]
        input_value = simpledialog.askstring("Input", f"Enter value for {parameter}:")
        if input_value:
            command = command.replace(parameter, input_value)

    print(f"Executing command: {command}")

    try:
        os.system(command)
    except Exception as e:
        print(f"Error: {e}")

def create_dynamic_buttons(data):
    row = 0
    column = 0
    max_columns = 4  # Adjust this value based on your preference
    
    for command, details in data.items():
        create_button(command, details, row, column)
        column += 1
        if column >= max_columns:
            column = 0
            row += 1

root = tk.Tk()
root.title("Docker Command Executor")
root.geometry("800x600")

# Create a frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(expand=True, fill="both")

# Configure the grid to auto-adjust
for i in range(4):  # Adjust based on max_columns
    button_frame.columnconfigure(i, weight=1)

create_dynamic_buttons(data)

root.mainloop()
