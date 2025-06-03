# CHECK THE FILE EXISTS OR NOT :
import os.path
from pathlib import Path

filepath = r"C:\Users\Admin\PycharmProjects\PythonProject\SDET_Python_Selenium\15_FileHandling_Part_01\abc.txt"

print(os.path.isfile(filepath))    # True
print(os.path.exists(filepath))    # True
print(Path(filepath).exists())    # True








