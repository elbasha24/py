import os
import signal

# os.sched_get_priority_max()
max_priority = os.sched_get_priority_max(os.SCHED_FIFO)
print(f"Maximum priority for SCHED_FIFO: {max_priority}")

# os.sched_get_priority_min()
min_priority = os.sched_get_priority_min(os.SCHED_FIFO)
print(f"Minimum priority for SCHED_FIFO: {min_priority}")

# os.sched_yield()
os.sched_yield()

# os.scandir()
with os.scandir('/path/to/directory') as entries:
    for entry in entries:
        print(entry.name)

# os.sync()
os.sync()

# os.sysconf()
page_size = os.sysconf(os.SC_PAGE_SIZE)
print(f"Page size: {page_size}")

# os.sendfile()
source_fd = os.open('/path/to/source.txt', os.O_RDONLY)
destination_fd = os.open('/path/to/destination.txt', os.O_WRONLY | os.O_CREAT)
os.sendfile(destination_fd, source_fd, 0, os.path.getsize('/path/to/source.txt'))
os.close(source_fd)
os.close(destination_fd)

# os.sched_setparam()
pid = os.getpid()
param = os.sched_param(10)  # Example priority value
os.sched_setparam(pid, param)

# os.sysconf_names
conf_var = "SC_PAGE_SIZE"
name = os.sysconf_names[conf_var]
print(f"Integer value corresponding to {conf_var}: {name}")
value = os.sysconf(name)
print(f"Configuration value corresponding to {name}: {value}")
