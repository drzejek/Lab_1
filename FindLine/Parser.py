from abc import ABC, abstractmethod

class Parser:
    @abstractmethod
    def findline(self):
        pass

    @abstractmethod
    def saveLinesToFile(self, logFileName, linesInFile):
        pass

    @abstractmethod
    def findAllFiles(self):
        pass

    @abstractmethod
    def changeFileName(self, logFileName):
        pass

