class Question:
    """
    A class representing a question in a quiz.

    Attributes:
    - text (str): The text of the question.
    - answer (str): The correct answer to the question.

    Methods:
    - None
    """

    def __init__(self, q_text, q_answer):
        """
        Initializes a Question instance.

        Parameters:
        - q_text (str): The text of the question.
        - q_answer (str): The correct answer to the question.
        """
        self.text = q_text
        self.answer = q_answer
