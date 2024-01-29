import os
import sys

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
