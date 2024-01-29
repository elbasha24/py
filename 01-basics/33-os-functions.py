os.get_blocking()

import os

file_path = '/path/to/file.txt'

blocking = os.get_blocking(file_path)
print(f"Blocking mode: {blocking}")

os.set_blocking()

import os

file_path = '/path/to/file.txt'

# Set blocking mode to non-blocking
os.set_blocking(file_path, False)
print("Blocking mode set to non-blocking")

os.get_exec_path()

import os

exec_path = os.get_exec_path()
print(f"Executable path: {exec_path}")

os.get_inheritable()

import os

file_descriptor = 3

inheritable = os.get_inheritable(file_descriptor)
print(f"Inheritable: {inheritable}")

os.get_terminal_size()

import os

terminal_size = os.get_terminal_size()
print(f"Terminal size: {terminal_size.columns} columns x {terminal_size.lines} lines")

os.getcwd()

import os

current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

os.getcwdb()

import os

current_directory_bytes = os.getcwdb()
print(f"Current working directory (bytes): {current_directory_bytes}")

os.getegid()

import os

effective_group_id = os.getegid()
print(f"Effective group ID: {effective_group_id}")

os.getenv()

import os

environment_variable = os.getenv('ENV_VARIABLE')
print(f"Value of ENV_VARIABLE: {environment_variable}")

os.geteuid()

import os

effective_user_id = os.geteuid()
print(f"Effective user ID: {effective_user_id}")

os.getgid()

import os

group_id = os.getgid()
print(f"Group ID: {group_id}")

os.getgrouplist()

import os

user = 'username'
group = 'groupname'

group_list = os.getgrouplist(user, group)
print(f"Group list: {group_list}")

os.getgroups()

import os

groups = os.getgroups()
print(f"Groups: {groups}")

os.getloadavg()

import os

load_average = os.getloadavg()
print(f"Load average: {load_average}")

os.getlogin()

import os

login = os.getlogin()
print(f"Login: {login}")

os.getpgid()

import os

process_id = os.getpid()
process_group_id = os.getpgid(process_id)
print(f"Process group ID: {process_group_id}")

os.getpgrp()

import os

process_group_id = os.getpgrp()
print(f"Process group ID: {process_group_id}")

os.getppid()

import os

parent_process_id = os.getppid()
print(f"Parent process ID: {parent_process_id}")

os.getpriority()

import os

process_id = os.getpid()
priority = os.getpriority(os.PRIO_PROCESS, process_id)
print(f"Priority: {priority}")

os.getsid()

import os

process_id = os.getpid()
session_id = os.getsid(process_id)
print(f"Session ID: {session_id}")


