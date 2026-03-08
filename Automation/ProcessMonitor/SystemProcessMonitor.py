import psutil
import os
import time
import schedule

def CreateLog(FolderName):
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)

    timestamp = time.ctime()
    timestamp = timestamp.replace(" ","")
    timestamp = timestamp.replace(":","_")
    timestamp = timestamp.replace("/","_")

    FileName = os.path.join(FolderName, "Marvellous%s.log" %(timestamp))

    fobj = open(FileName, "w")

    Border = "-" * 80
    fobj.write(Border)
    fobj.write("\n\t\tMarvellous Infosystems Process Log\n")
    fobj.write("\t\tLog file is created at :" +time.ctime()+"\n")
    fobj.write(Border)

    Data = ProcessScan()

    for value in Data:
        fobj.write("%s \n\n" %value)
    fobj.write(Border)
    
    fobj.close()

def ProcessScan():
    listprocess = []
    
    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=['pid','name','username'])
            info['vms'] = proc.memory_info().vms / (1024 * 1024)
            listprocess.append(info)
        except Exception:
            print("Exception occured")
   
    return listprocess

def main():
    Foldername = input()
    Timeinterval = int(input())
    schedule.every(Timeinterval).minutes.do(CreateLog, Foldername)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()