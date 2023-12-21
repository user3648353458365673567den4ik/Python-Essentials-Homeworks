import unittest
from main import TEXT, analyze_text


class AnalyzeTextTest(unittest.TestCase):
    def setUp(self):
        self.analyze_text = analyze_text
        self.text = TEXT

    def test_symbols_count(self):
        self.assertEqual(self.analyze_text(self.text)["symbols"], len(self.text)) # тест на кол-во символов

    def test_symbols_without_space_count(self):
        self.assertEqual(self.analyze_text(self.text)["symbols_without_space"], len(self.text.replace(' ', ''))) # тест на кол-во символов без учета пробелов

    def test_words_count(self):
        self.assertEqual(self.analyze_text(self.text)["words"], len(self.text.split(' ')))  # тест на кол-во слов

    def test_senteces_count(self):
        self.assertEqual(self.analyze_text(self.text)["sentences"], len(self.text.split('.'))) # тест на кол-во предложений

    def test_for_another_datatype(self): # тест на возможность работы с другими типами данных
        self.assertEqual(self.analyze_text(5555)["symbols"], 4)
        self.assertEqual(self.analyze_text(False)["symbols"], 5)
        self.assertEqual(self.analyze_text(5.55)["symbols"], 4)
        self.assertEqual(self.analyze_text({'hello': 'world'})["symbols"], 18)
        self.assertEqual(self.analyze_text(['text'])["symbols"], 8)


if __name__ == "__main__":
    unittest.main()
