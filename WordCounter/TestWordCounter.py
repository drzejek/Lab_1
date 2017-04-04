from unittest import TestCase
import WordCounter

class TestWordCounter(TestCase):
    def test_countWordsInFile(self):
        filename = "Test.txt"
        wc = WordCounter.WordCounter(filename)
        expectWordNumber = 7
        self.assertEqual(wc.countWordsInFile(), expectWordNumber)

    def test_isNameFile(self):
        filename = "Test.txt"
        wc = WordCounter.WordCounter(filename)
        isFileName = True
        self.assertEqual(wc.isNameFile(filename), isFileName)

if __name__ == '__main__':
    TestCase.main()
