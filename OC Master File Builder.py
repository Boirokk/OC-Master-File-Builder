# Searches for existing oc folders and updates them with new order confirmations
# Written by Chad C. 2016-05-18
import os, re, shutil
search = []

# Get OC #'s for search and append to list
for folder in os.listdir(r"S:\_TDS\TDS JOB MASTER FILES"):
    oc = re.findall(r'^\d{5}', folder)
    search.append(oc)

# Search directory for OC #'s
for folder_name, subfolder, file_name in os.walk(r"S:\Yachts\ORDER CONF\2016"):
    for file in file_name:
        oc = re.findall(r'^OC\d{5}|^OC\s\d{5}', file)
        ocz = re.findall(r'\d{5}', str(oc))
        for i in search:
            if i != []:
                if ocz == i:
                    print('Copying ' + os.path.join(folder_name, file))
                    shutil.copy(os.path.join(folder_name, file), r"C:\Users\cczilli\Desktop\ocfiles")




# Search directory for OC #'s
for folder_name, subfolder, file_name in os.walk(r"S:\Yachts\Dept. Xfer file"):
    for file in file_name:
        if file.endswith('.xls') or file.endswith('.xlsx'):
            oc = re.findall(r'^OC\d{5}|^OC\s\d{5}', file)
            ocz = re.findall(r'\d{5}', str(oc))
            for i in search:
                if i != []:
                    if ocz == i:
                        print('Copying ' + os.path.join(folder_name, file))
                        shutil.copy(os.path.join(folder_name, file), r"C:\Users\cczilli\Desktop\ocfiles3")



for folder in os.listdir(r"S:\_TDS\TDS JOB MASTER FILES\13152-SEA FORCE IX 71.5\02- ORDER CONFIRMATION & PO"):
    pass


print('Done...')