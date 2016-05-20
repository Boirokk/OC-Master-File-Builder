# Searches for existing oc folders and updates them with new order confirmations
# Written by Chad C. 2016-05-18
import os, re, shutil

search = []
oc2016key = []
oc2016value = []
transkey = []
transvalue = []
masterdictionary = {}
count1 = 0
count2 = 0
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
                    value = os.path.join(folder_name, file)
                    oc2016key.append(''.join(ocz))
                    oc2016value.append(''.join(value))

                    #print('Copying ' + os.path.join(folder_name, file))
                    #shutil.copy(os.path.join(folder_name, file), r"C:\Users\cczilli\Desktop\ocfiles")




# Search directory for OC #'s
for folder_name, subfolder, file_name in os.walk(r"S:\Yachts\Dept. Xfer file"):
    for file in file_name:
        if file.endswith('.xls') or file.endswith('.xlsx'):
            oc = re.findall(r'^OC\d{5}|^OC\s\d{5}', file)
            ocz = re.findall(r'\d{5}', str(oc))
            for i in search:
                if i != []:
                    if ocz == i:
                        value = os.path.join(folder_name, file)
                        transkey.append(''.join(ocz))
                        transvalue.append(''.join(value))

                        #print('Copying ' + os.path.join(folder_name, file))
                        #shutil.copy(os.path.join(folder_name, file), r"C:\Users\cczilli\Desktop\ocfiles3")



#r"S:\_TDS\TDS JOB MASTER FILES\13152-SEA FORCE IX 71.5\02- ORDER CONFIRMATION & PO")
for folder in os.listdir(r"S:\_TDS\TDS JOB MASTER FILES"):
    oc = re.findall(r'^\d{5}', folder)
    keystring = ''.join(oc)
    masterdictionary[keystring] = r"S:\_TDS\TDS JOB MASTER FILES" + os.sep + folder + os.sep + "02- ORDER CONFIRMATION & PO"
for key1 in oc2016key:
    #print(key1)
    for key2 in masterdictionary:
        if key1 == key2:
            shutil.copy(oc2016value[count1], masterdictionary[key1])
            print('Copy ', oc2016value[count1], ' to ', masterdictionary[key1])
    count1 += 1
for key1 in transkey:
    for key2 in masterdictionary:
        #print(key1)
        if key1 == key2:
            shutil.copy(transvalue[count2], masterdictionary[key1])
            print('Copy ', transvalue[count2], ' to ', masterdictionary[key1])
    count2 += 1

print('Done...')