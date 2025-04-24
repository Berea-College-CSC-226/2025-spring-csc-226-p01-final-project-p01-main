import html

class QuizBrain:
    def __init__(self, q_list):
        """
        Initializes the QuizBrain with a list of questions.

        :param q_list: A list of Question objects.
        :return: None
        """
        self.score = 0
        self.question_number = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_question(self):
        """
        Checks to see if there are more questions left.

        :return: True if there are more questions, False if not.
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Gets the next question and its options.

        :return: Question text, and list of options.
        """
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return q_text, self.current_question.options

    def check_answer(self, user_answer):
        """
        Checks the user's answer and updates the score if it's correct.

        :param user_answer: The answer given by the user.
        :return: True if the answer is correct, False if not.
        """
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
