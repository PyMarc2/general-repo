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
        flag = 0


try:
    url_file = open(file_path, 'r')
    url_file = url_file.read()
except Exception:
    print("An error has occurred, verify that the path exists or that the file extension is parsable.")
    exit(1)
    
url_list = re.findall(r'''https?:[\\/]+?[^"]+''', url_file)
extension_list = re.findall(r'''\.(m4a|png|xlsx|txt|tif|jpg|gif|pdf|doc|zip|ppt)''', url_file)
#extension_list = re.findall(r'''\.\w{4}''', url_file)
print(set(extension_list))


print("Where do you want to save your %d files ?" % len(url_list))
save_file_path = os.path.abspath(filedialog.askdirectory())

# try:
#      os.mkdir(save_file_path+"\slack_files")
#      print("Creating the folder 'slack_files' in %s." % save_file_path)
# except FileExistsError:
#      print("Your files will be added to the existing 'slack_files' folder.")

nonTrouve = 0
i = 1

for eachUrl in url_list:
    eachUrl = eachUrl.replace("\\", "")
    print(str(i)+'/'+str(len(url_list)))

    try:
        request = urllib.request.Request(eachUrl)
        response = urllib.request.urlopen(request)
        file = response.read()
    except urllib.error.HTTPError:
        nonTrouve += nonTrouve
        continue

    output = open(os.path.join(save_file_path, "file%d.%s" % (i, extension_list[i-1])), "wb")
    output.write(file)
    output.close()
    i += 1

print("%d files couldn't be found" % nonTrouve)
print("%d files where saved" % (len(url_list)-nonTrouve))
