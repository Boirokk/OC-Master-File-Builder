# Searches for existing oc folders and updates them with new order confirmations
# Written by Chad C. 2016-05-18
import os, re, subprocess
search = []

# Get OC #'s for search and append to list
for folder in os.listdir(r"S:\_TDS\TDS JOB MASTER FILES"):
    oc = re.findall(r'^\d{5}', folder)
    search.append(folder)

# Search directory for OC #'s
for file in os.listdir(r"S:\Yachts\ORDER CONF\2016"):
    print(os.path.realpath(file))
    oc = re.findall(r'^OC\d{5}|^OC\s\d{5}', file)
    ocz = re.findall(r'\d{5}', str(oc))



# Search directory for OC #'s
for file in os.listdir(r"S:\Yachts\Dept. Xfer file"):
    oc = re.findall(r'^OC\d{5}|^OC\s\d{5}', file)
    ocz = re.findall(r'\d{5}', str(oc))



for folder in os.listdir(r"S:\_TDS\TDS JOB MASTER FILES\13152-SEA FORCE IX 71.5\02- ORDER CONFIRMATION & PO"):
    pass

