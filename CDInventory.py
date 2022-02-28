#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
#Artem Lamnin, 2022-Feb-26, Added functionality and modified script to use dictionaries
#------------------------------------------#

# Declare variables

strChoice = '' # User input
# replaced list of lists with list of dicts
dictTbl=[] #initialize list of dictionaries to hold data
dictRow={} #dictionary row
textdata=[] 
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        # Added the functionality of loading existing data
        objFile=open(strFileName,'r') 
        for row in objFile:
            textdata=row.strip().split(',')
            strID=textdata[0]
            intID=int(strID)
            strTitle=textdata[1]
            strArtist=textdata[2]
            dictRow={'ID':intID, 'CD Title':strTitle, 'Artist Name':strArtist}
            dictTbl.append(dictRow)
        objFile.close()
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dictRow={'ID':intID, 'CD Title':strTitle, 'Artist Name':strArtist}
        dictTbl.append(dictRow)
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        for row in dictTbl:
            print(row)
    elif strChoice == 'd':
        # Added functionality of deleting an entry
        entry_delete_id=int(input('Enter ID to be deleted:'))
        dictTbl.remove(dictTbl[entry_delete_id-1]) 
        
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a')
        index=0
        while index < len(dictTbl):
            strRow=str(dictTbl[index]['ID'])+','+dictTbl[index]['CD Title']+','+dictTbl[index]['Artist Name']
            objFile.write(strRow+'\n')
            index+=1
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

