# Searches for existing oc folders and updates them with new order confirmations
# Written by Chad C. 2016-05-18
import os, re, shutil

# CONSTANTS
MASTER_FILE_PATH = r"S:\_TDS\TDS JOB MASTER FILES"
DEPT_TRANFER_PATH = r"S:\Yachts\Dept. Xfer file"
ORDER_CONF_2016 = r"S:\Yachts\ORDER CONF\2016"

# LISTS
search = []
oc2016key = []
oc2016value = []
transkey = []
transvalue = []

# DICTIONARY
masterdictionary = {}

# COUNTERS FOR THE LISTS INDEX
count1 = 0
count2 = 0


# Get OC numbers's for search and append to list
for folder in os.listdir(MASTER_FILE_PATH):
    oc = re.findall(r'^\d{5}', folder) # Find 5 digits in the front of the string
    search.append(oc) # Add the 5 digits to the search list for a reference

# Search directory for OC numbers's
for folder_name, subfolder, file_name in os.walk(ORDER_CONF_2016):
    for file in file_name:
        oc = re.findall(r'^OC\d{5}|^OC\s\d{5}', file) # Look for oc5digits or oc 5digits in the file name and save to oc variable
        ocz = re.findall(r'\d{5}', str(oc)) # Strip the oc from the 5 digits and save to ocz variable
        for i in search:
            if i != []: # If search list has a 5 digit number in the element.
                if ocz == i: # If the 5 digit file number matches the 5 digit master file number
                    value = os.path.join(folder_name, file) # Save the file path to value variable
                    oc2016key.append(''.join(ocz)) # Add the 5 digit number to a list
                    oc2016value.append(''.join(value)) # Add the file path that matches the 5 digit number to a list

# Search directory for OC numbers's
for folder_name, subfolder, file_name in os.walk(DEPT_TRANFER_PATH):
    for file in file_name:
        if file.endswith('.xls') or file.endswith('.xlsx'):
            oc = re.findall(r'^OC\d{5}|^OC\s\d{5}', file)
            ocz = re.findall(r'\d{5}', str(oc))
            for i in search:
                if i != []: # If search list has a 5 digit number in the element.
                    if ocz == i: # If the 5 digit file number matches the 5 digit master file number
                        value = os.path.join(folder_name, file) # Save the file path to value variable
                        transkey.append(''.join(ocz)) # Add the 5 digit number to a list
                        transvalue.append(''.join(value)) # Add the file path that matches the 5 digit number to a list

 # Search directory
for folder in os.listdir(MASTER_FILE_PATH):
    oc = re.findall(r'^\d{5}', folder) # Look for 5digits in the begining of file name and save to oc variable
    keystring = ''.join(oc) # Convert oc list (5 digit number) to a string and name it keystring
    # Add the keystring (5 digit number) as the key to the dictionary and the root path as the value for the key
    masterdictionary[keystring] = MASTER_FILE_PATH + os.sep + folder + os.sep + "02- ORDER CONFIRMATION & PO"
    
for key1 in oc2016key:
    for key2 in masterdictionary:
        if key1 == key2:
            shutil.copy(oc2016value[count1], masterdictionary[key1])
            print('Copy ', oc2016value[count1], ' to ', masterdictionary[key1])
    count1 += 1
    
for key1 in transkey:
    for key2 in masterdictionary:
        if key1 == key2:
            shutil.copy(transvalue[count2], masterdictionary[key1])
            print('Copy ', transvalue[count2], ' to ', masterdictionary[key1])
    count2 += 1

print('Done...')
print('All files have been copied to there destination folder.')
