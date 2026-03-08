import os
import sys
import hashlib
import time

def CalculatecheckSum(path, BlockSize = 1024):
    fobj = open(path, "rb") 
    
    hobj = hashlib.md5()

    buffer = fobj.read(BlockSize)
    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)

    fobj.close()

    return hobj.hexdigest()
    
def Directorywatcher(DirectoryName = "Marvellous"):
    
    flag = os.path.isabs(DirectoryName)
    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)
    if(flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)
    if(flag == False):
        print("Path is valid but the target is not a Directory")
        exit()

    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            fname = os.path.join(FolderName, fname)
            checksum = CalculatecheckSum(fname)
            print("Filename :", fname)
            print("Checksum :", checksum)
            print()
    
    timestam = time.ctime()

    FileName = "MarvellousLog%s.log" %(timestam)
    FileName = FileName.replace(" ","_")
    FileName = FileName.replace(":","_")

    fobj = open(FileName, "w")
    
    Border = "-" * 54
    
    fobj.write(Border)
    fobj.write("\nThis is a log file of Marvellous Automation Script\n")
    fobj.write("\nThis is a Directory Cleaner Script\n")
    fobj.write(Border+"\n")

    fobj.write("\n\n\n\n\n")
    fobj.write(Border+"\n")
    fobj.write("This file is created at \n"+timestam+"\n")
    fobj.write(Border+"\n")

def FindDuplicate(DirectoryName = "Marvellous"):
    
    flag = os.path.isabs(DirectoryName)
    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)
    if(flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)
    if(flag == False):
        print("Path is valid but the target is not a Directory")
        exit()

    Duplicate = {}

    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            fname = os.path.join(FolderName, fname)
            checksum = CalculatecheckSum(fname)

            if checksum in Duplicate:
                Duplicate[checksum].append(fname)
            else:
                Duplicate[checksum] = [fname]
    
    return Duplicate

def DisplayResult(MyDict):
    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))
    
    Count = 0

    for value in Result:
        for subvalue in value:
            Count += 1 
            print(subvalue)
        print("------------------------------")
        print("Value of count is :", Count)
        print("------------------------------")
        Count = 0

def DeleteDuplicate(MyDict):
    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))
    
    Count = 0
    cnt = 0

    for value in Result:
        for subvalue in value:
            Count += 1 
            if (Count > 1):
                print("Delected File :", subvalue)
                os.remove(subvalue)
                cnt += 1
        Count = 0

    print("Total Deleted file :", cnt)   

def Main():
    border = '_' * 55
    print(border)
    print("---------- Marvellous Automation ----------")
    print(border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h") or (sys.argv[1] == "--H"):
            print("This Application is used to perform Directory Cleaning")
            
        elif(sys.argv[1] == "--u") or (sys.argv[1] == "--U"):
            print("Use the given script as : ")
            print("ScriptName.py NameOfDirectory")
            print("Please provide valid Directory Path")

        else:
            result = FindDuplicate(sys.argv[1])
            DeleteDuplicate(result)

    else:
        print("Invalid no od commanline argument")
        print("Use the given flags as :")
        print("--h : used to display the help")
        print("--u : used to display the usage")

    print(border)
    print("--------- Thanks for using our Script ----------")
    print("---------- Marvellous Infosystem ---------")

if __name__ == "__main__":
    Main()