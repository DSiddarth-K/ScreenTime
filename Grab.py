import psutil 
from datetime import datetime
import pandas as pd 
import time 
import os 
import wmi
import numpy
from win32gui import GetWindowText, GetForegroundWindow

def tasks():
    processes = []
    for process in psutil.process_iter():
        with process.oneshot():
                pid = process.pid
                if pid == 0:
                    continue
                name = process.name()
                try:
                    create_time = datetime.fromtimestamp(process.create_time())
                except OSError:
            
                    create_time = datetime.fromtimestamp(psutil.boot_time())
                status = process.status()
    processes.append({
            'pid': pid, 'name': name, 'create_time': create_time,
            'status': status})
    return processes

def wmiTasks():
    f = wmi.WMI()
    for process in f.Win32_Process():
        print(f"{process.ProcessId:<10} {process.Name}")

def getActiveWindow():
    tasks=[]
    currTask = GetWindowText(GetForegroundWindow())
    windowInfo = currTask.split("- ")
    windowInfo = numpy.flipud(windowInfo)
    application = windowInfo[0]
    try:
        appInfo = windowInfo[1]
        print(appInfo,windowInfo,len(windowInfo))
    except IndexError:
        pass
    
    


def main():
    while(True):
        getActiveWindow()


main()

