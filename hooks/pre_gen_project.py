import os
import sys
import re

project_slug = "{{ cookiecutter.project_slug }}"

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"


# Check if the project_slug starts with a number
if project_slug[0].isdigit():
    print(f"{ERROR_COLOR}ERROR: {project_slug=} is not a valid name for this template. Project names should not start with a number.{RESET_ALL}")
    sys.exit(1)


# Check if the project_slug contains invalid characters
valid_characters = set("abcdefghijklmnopqrstuvwxyz0123456789_-")
if not all(char in valid_characters for char in project_slug):
    print(f"{ERROR_COLOR}ERROR: {project_slug=} is not a valid name for this template. Project names should only contain lowercase letters, numbers, hyphens, and underscores.{RESET_ALL}")
    sys.exit(1)


# Check if the project_slug is already a directory
if os.path.isdir(project_slug):
    print(f"{ERROR_COLOR}ERROR: A directory with the name '{project_slug}' already exists in the current directory. Please choose a different project name.{RESET_ALL}")    
    sys.exit(1)

print(f"{MESSAGE_COLOR}Let's do it! You're going to create something awesome!")
print(f"Creating project at { os.getcwd() }{RESET_ALL}")