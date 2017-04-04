from WordCounter import *

def main():
    print("Word counter")
    print("Please type name your file to count it words.")

    filename = input()

    while(WordCounter.isNameFile(filename)):
        filename = input()

    wc = WordCounter(filename)
    wc.countWordsInFile()


if __name__ == '__main__':
    main()