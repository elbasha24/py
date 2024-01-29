import os

# os.chdir()
os.chdir('/path/to/directory')

# os.execvp()
os.execvp('ls', ['ls', '-l'])

# os.execv()
os.execv('/bin/ls', ['/bin/ls', '-l'])

# os._exit()
os._exit(0)

# os.umask()
umask = os.umask(0o22)
print(f"Umask: {umask}")

# os.putenv()
os.putenv('ENV_VARIABLE', 'value')

# os.abort()
os.abort()

# os.access()
file_path = '/path/to/file.txt'
access = os.access(file_path, os.R_OK)
print(f"Read access: {access}")

# os.chown()
file_path = '/path/to/file.txt'
os.chown(file_path, 1001, 1001)

# os.chmod()
file_path = '/path/to/file.txt'
os.chmod(file_path, 0o755)

# os.chroot()
os.chroot('/path/to/new/root')

# os.close()
file_descriptor = 3
os.close(file_descriptor)

# os.closerange()
fd_start = 3
fd_end = 5
os.closerange(fd_start, fd_end)

# os.copy_file_range()
src_fd = os.open('/path/to/source.txt', os.O_RDONLY)
dst_fd = os.open('/path/to/destination.txt', os.O_WRONLY | os.O_CREAT)
os.copy_file_range(src_fd, None, dst_fd, None, 1024)
os.close(src_fd)
os.close(dst_fd)

# os.cpu_count()
cpu_count = os.cpu_count()
print(f"CPU count: {cpu_count}")

# os.curdir()
current_directory = os.curdir
print(f"Current directory: {current_directory}")

# os._EnvironCodeFunc()
environ_code = os._EnvironCodeFunc()
print(f"Environ code: {environ_code}")

# os.defpath()
def_path = os.defpath
print(f"Default path: {def_path}")

# os.device_encoding()
device_encoding = os.device_encoding(1)
print(f"Device encoding: {device_encoding}")

# os.DirEntry()
with os.scandir('/path/to/directory') as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.name)

# os.fstat()
file_descriptor = os.open('/path/to/file.txt', os.O_RDONLY)
file_stat = os.fstat(file_descriptor)
print(f"File size: {file_stat.st_size}")
os.close(file_descriptor)

# os.fchmod()
file_descriptor = os.open('/path/to/file.txt', os.O_WRONLY)
os.fchmod(file_descriptor, 0o755)
os.close(file_descriptor)

# os.fsync()
file_descriptor = os.open('/path/to/file.txt', os.O_WRONLY)
os.fsync(file_descriptor)
os.close(file_descriptor)

# os.rename()
old_file_path = '/path/to/old_file.txt'
new_file_path = '/path/to/new_file.txt'
os.rename(old_file_path, new_file_path)

# os.unlink()
file_path = '/path/to/file.txt'
os.unlink(file_path)

# os.fork()
child_pid = os.fork()
if child_pid == 0:
    print("Child process")
else:
    print("Parent process")

# os.fchdir()
file_descriptor = os.open('/path/to/directory', os.O_RDONLY)
os.fchdir(file_descriptor)
os.close(file_descriptor)

# os.fchmod()
file_descriptor = os.open('/path/to/file.txt', os.O_WRONLY)
os.fchmod(file_descriptor, 0o755)
os.close(file_descriptor)

# os.forkpty()
pid, fd = os.forkpty()
if pid == 0:
    os.execvp('ls', ['ls', '-l'])
else:
    os.waitpid(pid, 0)

# os.fpathconf()
file_descriptor = os.open('/path/to/file.txt', os.O_RDONLY)
pathconf_value = os.fpathconf(file_descriptor, os.PC_NAME_MAX)
print(f"Pathconf value: {pathconf_value}")
os.close(file_descriptor)

# os.fsdecode()
encoded_path = b'/path/to/file.txt'
decoded_path = os.fsdecode(encoded_path)
print(f"Decoded path: {decoded_path}")

# os.fspath()
path = '/path/to/file.txt'
fspath = os.fspath(path)
print(f"Fspath: {fspath}")

# os.get_blocking()
file_path = '/path/to/file.txt'
blocking = os.get_blocking(file_path)
print(f"Blocking mode: {blocking}")

# os.set_blocking()
file_path = '/path/to/file.txt'
os.set_blocking(file_path, False)
print("Blocking mode set to non-blocking")

# os.get_exec_path()
exec_path = os.get_exec_path()
print(f"Executable path: {exec_path}")

# os.get_inheritable()
file_descriptor = 3
inheritable = os.get_inheritable(file_descriptor)
print(f"Inheritable: {inheritable}")

# os.get_terminal_size()
terminal_size = os.get_terminal_size()
print(f"Terminal size: {terminal_size.columns} columns x {terminal_size.lines} lines")

# os.getcwd()
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

# os.getcwdb()
current_directory_bytes = os.getcwdb()
print(f"Current working directory (bytes): {current_directory_bytes}")

# os.getegid()
effective_group_id = os.getegid()
print(f"Effective group ID: {effective_group_id}")

# os.getenv()
environment_variable = os.getenv('ENV_VARIABLE')
print(f"Value of ENV_VARIABLE: {environment_variable}")

# os.geteuid()
effective_user_id = os.geteuid()
print(f"Effective user ID: {effective_user_id}")

# os.getgid()
group_id = os.getgid()
print(f"Group ID: {group_id}")

# os.getgrouplist()
user = 'username'
group = 'groupname'
group_list = os.getgrouplist(user, group)
print(f"Group list: {group_list}")

# os.getgroups()
groups = os.getgroups()
print(f"Groups: {groups}")

# os.getloadavg()
load_average = os.getloadavg()
print(f"Load average: {load_average}")

# os.getlogin()
login = os.getlogin()
print(f"Login: {login}")

# os.getpgid()
process_id = os.getpid()
process_group_id = os.getpgid(process_id)
print(f"Process group ID: {process_group_id}")

# os.getpgrp()
process_group_id = os.getpgrp()
print(f"Process group ID: {process_group_id}")

# os.getppid()
parent_process_id = os.getppid()
print(f"Parent process ID: {parent_process_id}")

# os.getpriority()
process_id = os.getpid()
priority = os.getpriority(os.PRIO_PROCESS, process_id)
print(f"Priority: {priority}")

# os.getsid()
process_id = os.getpid()
session_id = os.getsid(process_id)
print(f"Session ID: {session_id}")
