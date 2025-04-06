import unittest
from quiz import Question, QUizBrain

class TestQuestion(unittest.TestCase):
    def test_question(self):

class TestQuizBrain(unittest.TestCase):
    def setUp(self):

    def test_initialization(self):

    def test_still_has_question(self):

    def test_next_question(self):

    def test_check_correct_answer(self):

    def test_incorrect_answer(self):

    # add assertion here


if __name__ == '__main__':
    unittest.main()
