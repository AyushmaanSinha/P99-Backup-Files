import time
import os
import shutil

path = "/path/to/directory"
days = 30

time_in_seconds = time.time() - (days * 24 * 60 * 60)

if os.path.exists(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.stat(file_path).st_ctime < time_in_seconds:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
else:
    print("Path not found.")