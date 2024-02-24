import html

class QuizBrain:
    """
    A class to represent the brain of the quiz game.

    Attributes:
        question_number (int): The current question number.
        score (int): The current score of the player.
        question_list (list): A list containing Question objects.
        current_question (Question): The current question being asked.
    """

    def __init__(self, q_list):
        """
        Initialize the QuizBrain.

        Args:
            q_list (list): A list of Question objects.
        """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """
        Check if there are still questions remaining.

        Returns:
            bool: True if there are still questions, False otherwise.
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Get the next question from the question list.

        Returns:
            str: The formatted text of the next question.
        """
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        # Unescape HTML entities in the question text
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer):
        """
        Check if the user's answer is correct.

        Args:
            user_answer (str): The user's answer to the question.

        Returns:
            bool: True if the answer is correct, False otherwise.
        """
        correct_answer = self.current_question.answer
        # Convert both answers to lowercase for case-insensitive comparison
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
