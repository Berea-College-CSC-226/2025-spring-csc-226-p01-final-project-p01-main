class Question:
    def __init__(self, text, options, answer):
        """
        Creates a quiz question

        :param text: The text question
        :param options: A list of the answer options
        :param answer: The corrext answer from the options
        :return: None
        """
        self.text = text
        self.options = options
        self.answer = answer
