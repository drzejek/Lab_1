import glob
from Exceptions import *

class WordCounter:
    def __init__(self, filename):
        self.filename = filename

    def countWordsInFile(self):
        count=0
        with open(self.filename, 'r') as file:
            count = len(file.read().split())

        print("In file " + self.filename)
        print("Are "+ str(count) +" words")
        return count

    @staticmethod
    def isNameFile(filename):
        try:
            for file in glob.glob('*.*'):
                if file == filename:
                    return False
            raise NoSuchFileException
        except:
            print("I'm sorry there is no such file on this directory")
            return True
