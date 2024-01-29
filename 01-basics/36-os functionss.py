import os
import signal

# os.kill()
pid = 12345
os.kill(pid, signal.SIGTERM)

# os.killpg()
pgid = os.getpgid(os.getpid())
os.killpg(pgid, signal.SIGTERM)

# os.lchown()
file_path = '/path/to/file.txt'
os.lchown(file_path, 1001, 1001)

# os.link()
source = '/path/to/source.txt'
destination = '/path/to/destination.txt'
os.link(source, destination)

# os.listdir()
directory_path = '/path/to/directory'
files = os.listdir(directory_path)
print(f"Files in directory: {files}")

# os.listxattr()
file_path = '/path/to/file.txt'
xattrs = os.listxattr(file_path)
print(f"Extended attributes: {xattrs}")

# os.lockf()
file_descriptor = os.open('/path/to/file.txt', os.O_RDWR)
os.lockf(file_descriptor, os.F_LOCK, 0)
# Perform operations on the locked file
os.lockf(file_descriptor, os.F_ULOCK, 0)
os.close(file_descriptor)

# os.lstat()
file_info = os.lstat('/path/to/file.txt')
print(f"File info: {file_info}")

# os.lseek()
file_descriptor = os.open('/path/to/file.txt', os.O_RDONLY)
os.lseek(file_descriptor, 0, os.SEEK_SET)
os.close(file_descriptor)

# os.makedirs()
os.makedirs('/path/to/new/directory')

# os.mkdir()
os.mkdir('/path/to/new/directory')

# os.major()
st = os.lstat('/path/to/file.txt')
major_device_number = os.major(st.st_dev)
print(f"Major device number: {major_device_number}")

# os.mkfifo()
os.mkfifo('/path/to/fifo')

# os.name()
print(f"Operating system name: {os.name}")

# os.open()
file_descriptor = os.open('/path/to/file.txt', os.O_RDONLY)
# Perform operations using the file descriptor
os.close(file_descriptor)

# os.openpty()
master, slave = os.openpty()
print(f"Master PTY: {master}, Slave PTY: {slave}")

# os.pardir()
print(f"Parent directory: {os.pardir}")

# os.path()
file_path = '/path/to/file.txt'
print(f"Normalized path: {os.path(file_path)}")

# os.pathconf()
max_path_length = os.pathconf('/', 'PC_PATH_MAX')
print(f"Maximum path length: {max_path_length}")

# os.pathsep()
print(f"Path separator: {os.pathsep}")

# os.popen()
output = os.popen('ls -l').read()
print(output)

# os.pread()
file_descriptor = os.open('/path/to/file.txt', os.O_RDONLY)
data = os.pread(file_descriptor, 1024, 0)
os.close(file_descriptor)

# os.pwrite()
file_descriptor = os.open('/path/to/file.txt', os.O_WRONLY)
os.pwrite(file_descriptor, b'data', 0)
os.close(file_descriptor)
