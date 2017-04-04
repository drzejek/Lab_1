from Parser import *
import glob, os, sys

class LogParser(Parser):
    def __init__(self):
        self.stringToFind = "PrChecker.Downs"
        self.files = ".log"
        self.directName = "logLines"
        self.logFiles = []
        self.findAllFiles()
        self.findline()

    def findline(self):
        for filename in self.logFiles:
            linesInFile = []
            with open(filename, 'r') as fLogRead:
                for line in fLogRead.readlines():
                    if (self.stringToFind in line):
                        linesInFile.append(line)
            fLogRead.close()

            self.saveLinesToFile(filename, linesInFile)



    def changeFileName(self, logFileName):
        newLogFileName = logFileName[:-4] + "_" + self.stringToFind + self.files
        return newLogFileName

    def createDirectory(self, directName):
        if not os.path.exists(directName):
            os.makedirs(directName)

    def saveLinesToFile(self, logFileName, linesInFile):
        self.createDirectory(self.directName)

        filename = self.changeFileName(logFileName)
        path = self.directName
        with open(os.path.join(path,filename), 'w') as fLogWrite:
            fLogWrite.writelines(linesInFile)

    def findAllFiles(self):
        for file in glob.glob('*' + self.files):
            self.logFiles.append(file)
        print("Log files:")
        print(self.logFiles)