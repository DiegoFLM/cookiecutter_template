import os
import datetime
import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"


def replace_year_in_files():
    """Replace the placeholder for the year in files with the current year."""
    current_year = str(datetime.datetime.now().year)
    for dirpath, dirnames, filenames in os.walk('.'):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            with open(filepath, 'r') as file:
                filedata = file.read()
            if '[[year]]' in filedata:
                filedata = filedata.replace('[[year]]', current_year)
                with open(filepath, 'w') as file:
                    file.write(filedata)

replace_year_in_files()



print(f"{MESSAGE_COLOR}Almost done!")
print(f"Initializing a git repository...{RESET_ALL}")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

print(
    f"{MESSAGE_COLOR}The beginning of your destiny is defined now! "
    f"Create and have fun!{RESET_ALL}"
)
