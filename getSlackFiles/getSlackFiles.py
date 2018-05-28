import re
import os
import tkinter as tk
from tkinter import filedialog
import urllib.request


flag = 1

while flag == 1:
    confirm = input("Press <Enter> to select the file to parse")
    if confirm == "":
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', 1)
        file_path = filedialog.askopenfilename()
        if not file_path:
            exit(0)
        flag = 0


try:
    url_file = open(file_path, 'r')
    url_file = url_file.read()
except Exception:
    print("An error has occurred, verify that the path exists or that the file extension is parsable.")
    exit(1)


url_list = (re.findall(r'''https?:[\\/]+.+/download.+\..+\?[^"]+''', url_file))
for i in range(len(url_list)):
    url_list[i] = url_list[i].replace("\\", "")
print(len(url_list))

filename_list = re.findall(r'''/download.+\..+\?''', url_file)
for i in range(len(filename_list)):
    filename_list[i] = filename_list[i].replace("/download\\/", "")
    filename_list[i] = filename_list[i].replace("?", "")
print(len(filename_list))

for i in range(len(filename_list)):
    if filename_list[i] not in url_list[i]:
        print("WRONG")

print("Where do you want to save your %d files ?" % len(url_list))
save_file_path = filedialog.askdirectory()
save_file_path_abs = os.path.abspath(save_file_path)
if not save_file_path:
    exit(0)


nonTrouve = 0

for i in range(len(url_list)):
    print(str(i+1)+'/'+str(len(url_list)), filename_list[i])

    try:
        request = urllib.request.Request(url_list[i])
        response = urllib.request.urlopen(request)
        file = response.read()
    except urllib.error.HTTPError:
        nonTrouve += nonTrouve
        print("ERROR FILE NOT FOUND")
        continue

    output = open(os.path.join(save_file_path_abs, "%s" % (filename_list[i])), "wb")
    output.write(file)
    output.close()

print("%d files couldn't be found" % nonTrouve)
print("%d files were saved" % (len(url_list)-nonTrouve))
