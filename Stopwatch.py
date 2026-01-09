import time
import sys
import select

class StopWatch:
    def __init__(self):
        self.startTime = None
        self.elapsedTime = 0
        self.isRunning = False

    def startWatch(self):
        if not self.isRunning:
            self.startTime = time.perf_counter()
            self.isRunning = True
            print('Watch has started')

    def stopWatch(self):
        if self.isRunning:
            self.elapsedTime = time.perf_counter() - self.startTime
            self.isRunning = False
            print('Watch has stopped')

    def resetWatch(self):
        self.elapsedTime = 0
        self.isRunning = False
        print('Watch has reset')

    def logWatch(self):
        totalTime = self.elapsedTime
        if self.isRunning:
            totalTime += time.perf_counter() - self.startTime
        print(f"Time: {totalTime:.2f} seconds")
    

stopwatch= StopWatch()

while True:
    command= input("Choose one of the options...\nS:start\nP:stop\nR:reset\nQ:quit\n\n>")
    if (command== "S"):
        stopwatch.startWatch()
    elif (command== "P"):
        stopwatch.stopWatch()
    elif (command== "R"):
        stopwatch.resetWatch()
    elif (command== "Q"):
        break
    else:
        print("Invalid command. Please try again")

    while stopwatch.isRunning:
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            break
        stopwatch.logWatch()
        time.sleep(1)