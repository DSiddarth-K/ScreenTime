from datetime import datetime
import numpy
from win32gui import GetWindowText, GetForegroundWindow
import time

def getActiveWindow():
    currTask = GetWindowText(GetForegroundWindow())
    windowInfo = currTask.split("- ")
    windowInfo = numpy.flipud(windowInfo)
    application = windowInfo[0]
    try:
        appInfo = windowInfo[1]
        #print(appInfo,windowInfo,len(windowInfo))
    except IndexError:
        pass
    if application == "Google Chrome":
        if "YouTube" in appInfo:
            return(appInfo)
        elif "Google Docs" in appInfo:
            return(appInfo)
        else:
            return(application)
    else:
        return(application)

def addProcesses(processes):
    c = 1
    activeWindow = getActiveWindow()
    for i in range(len(processes)):
        if activeWindow in processes[i][0]:
            c = 0
            processes[i][1] += int(timer())
    if c == 1:
        processes.append([activeWindow,timer()])
    return(processes)

def timer():
    activeWindow = getActiveWindow()
    start = time.time()
    while activeWindow == getActiveWindow():
       pass
    end = time.time()
    elapsedTime = end - start
    return(elapsedTime)
    
def main():
    i = 0
    processes = []
    while(True):
        print(addProcesses(processes))

main()

