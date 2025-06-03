# GETTING FILE INFO :-

import os
import time

with open("file1.txt","w") as f:
    f.write("Getting file information...\n" * 15)


info = os.stat("file1.txt")

print(info.st_size)   # 435
print(info.st_mtime)   # 1748893010.9766648
print(info.st_atime)   # 1748893010.9766648
print(info.st_ctime)   # 1748892851.5171266

# mtime, atime, ctime are Unix Epoch Time (from 1 Jan 1970)
# mtime --> modified time = last time file contents was modified.
# atime --> access time = last time file opened.
# ctime --> changed time = last time file inode was modified

# We can convert Unix Epoch time to normal time
print(time.ctime(info.st_mtime))   # Tue Jun  3 01:12:48 2025
print(time.ctime(info.st_atime))   # Tue Jun  3 01:13:29 2025
print(time.ctime(info.st_ctime))   # Tue Jun  3 01:04:11 2025



