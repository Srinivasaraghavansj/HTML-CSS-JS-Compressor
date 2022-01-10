#pip install css-html-js-minify
import os
import shutil
import requests
from css_html_js_minify import html_minify, css_minify
from jsmin import jsmin
from tqdm import tqdm

folder_name = "POC Latest"

old_dir = f"/Volumes/GoogleDrive-114081981939626733457/My Drive/EDUCUBOT POC SRINI DEV FILES/{folder_name}"
new_dir = f"/Users/srinivasaraghavan/Downloads/ECB POC Production/{folder_name}"+" Production"

url = 'https://www.toptal.com/developers/javascript-minifier/raw'

dirNames = []
entries = []
def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = []
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        dirNames.append(dirName)
        entries.append(entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
    return allFiles

def copy_file(source,destination,verbose = False):
    try:
        shutil.copyfile(source, destination)
        print("File copied successfully.") if verbose else True
    except shutil.SameFileError:
        print("Source and destination represents the same file.") if verbose else True
    except IsADirectoryError:
        print("Destination is a directory.") if verbose else True
    except PermissionError:
        print("Permission denied.") if verbose else True
    except:
        print("Error occurred while copying file.") if verbose else True

dirName = old_dir
all_files = getListOfFiles(dirName)
source_files = []
for i in all_files:
    source_files.append(i.replace(dirName,""))

unique_dirs = set()
for i in dirNames:
    unique_dirs.add(i.replace(dirName,""))
unique_dirs.remove("")

for i in unique_dirs:
    path = new_dir+i
    os.makedirs(path, exist_ok=True)

for i in tqdm(all_files):
    file_ = i.replace(old_dir,"")
    i_ = i.split(".")
    if i_[-1] == "js" and not (i_[-2]== "min" or "compressed" in i_[-2]):
        with open(i, 'r') as f:
            data = f.read()
            with open(new_dir+file_,'w') as w:
                w.write(jsmin(data))

    elif i_[-1] == "css" and not (i_[-2]== "min" or "compressed" in i_[-2]):
        with open(i, 'r') as f:
            data = f.read()
            with open(new_dir+file_,'w') as w:
                w.write(css_minify(data))

    elif i_[-1] == "html" and not (i_[-2]== "min" or "compressed" in i_[-2]):
        with open(i, 'r') as f:
            data = f.read()
            with open(new_dir+file_,'w') as w:
                w.write(html_minify(data))
    else:
        copy_file(i,new_dir+file_)