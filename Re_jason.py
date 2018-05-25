import re
import tkinter as tk
from tkinter import filedialog


a = input("press enter to select the file to parse")
if a == "":
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
try:
    fileurl = open(file_path, 'r')
    fileurl = (fileurl.read())
except Exception:
    print("An error has occurred, verify that the path exists")
    exit(1)
    
urls = re.findall(r'(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', fileurl)
print(urls)
