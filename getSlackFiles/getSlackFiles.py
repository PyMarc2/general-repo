import re
import os
import tkinter as tk
from tkinter import filedialog
import urllib.request


class GetSlackFiles:

    def __init__(self):
        self.file_path = ""
        self.save_file_path = ""
        self.save_file_path_abs = ""

        self.url_file = ""


        self.url_list = []
        self.filename_list = []
        self.category_list = []
        self.dates_list = []

        self.non_trouve = 0
        self.flag = 1
        self.root = tk.Tk()

    def selectFile2Parse(self):
        while self.flag == 1:
            self.confirm = input("Press <Enter> to select the file to parse")
            if self.confirm == "":
                self.root.withdraw()
                self.root.attributes('-topmost', 1)
                self.file_path = filedialog.askopenfilename()
                if not self.file_path:
                    exit(0)
                self.flag = 0

    def openFile2Parse(self):
        try:
            self.url_file = open(self.file_path, 'r')
            self.url_file = self.url_file.read()
        except Exception:
            print("An error has occurred, verify that the path exists or that the file extension is parsable.")
            exit(1)

    def findURL(self):
        self.url_list = (re.findall(r'''https?:[\\/]+.+/download.+\..+\?[^"]+''', self.url_file))
        for i in range(len(self.url_list)):
            self.url_list[i] = self.url_list[i].replace("\\", "")
        print(len(self.url_list))

    def findFilename(self):
        self.filename_list = re.findall(r'''/download.+\..+\?''', self.url_file)
        for i in range(len(self.filename_list)):
            self.filename_list[i] = self.filename_list[i].replace("/download\\/", "")
            self.filename_list[i] = self.filename_list[i].replace("?", "")
        print(len(self.filename_list))

    def findCategory(self):
        pass

    def findDates(self):
        pass

    def selectSaveFolder(self):
        print("Where do you want to save your %d files ?" % len(self.url_list))
        self.save_file_path = filedialog.askdirectory()
        self.save_file_path_abs = os.path.abspath(self.save_file_path)
        if not self.save_file_path:
            exit(0)

    def saveAllFiles(self):
        for i in range(len(self.url_list)):
            print(str(i + 1) + '/' + str(len(self.url_list)), self.filename_list[i])

            try:
                request = urllib.request.Request(self.url_list[i])
                response = urllib.request.urlopen(request)
                file = response.read()
            except urllib.error.HTTPError:
                self.nonTrouve += self.nonTrouve
                print("ERROR FILE NOT FOUND")
                continue

            output = open(os.path.join(self.save_file_path_abs, "%s" % (self.filename_list[i])), "wb")
            output.write(file)
            output.close()

        print("%d files couldn't be found" % self.nonTrouve)
        print("%d files were saved" % (len(self.url_list) - self.nonTrouve))


BSFG = GetSlackFiles()  # BliqSlackFilesGetter

BSFG.selectFile2Parse()
BSFG.openFile2Parse()

BSFG.findURL()
BSFG.findFilename()
BSFG.findCategory()
BSFG.findDates()

BSFG.selectSaveFolder()
BSFG.saveAllFiles()
