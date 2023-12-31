class QuizBrain:
    """
    A class representing a quiz game.

    Attributes:
    - question_number (int): The current question number.
    - score (int): The player's score.
    - question_list (list): A list of Question objects.

    Methods:
    - still_has_questions(): Checks if there are still questions in the quiz.
    - next_question(): Presents the next question to the player.
    - check_answer(user_answer, correct_answer): Checks if the user's answer is correct and updates the score.
    """

    def __init__(self, q_list):
        """
        Initializes a QuizBrain instance.

        Parameters:
        - q_list (list): A list of Question objects representing the quiz questions.
        """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        """
        Checks if there are still questions in the quiz.

        Returns:
        - bool: True if there are more questions, False otherwise.
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Presents the next question to the player and checks the answer.

        Displays the current question number and prompts the player for an answer.

        Calls the check_answer method to evaluate the user's response.

        Prints the correct answer, the player's current score, and a newline.
        """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """
        Checks if the user's answer is correct and updates the score.

        Parameters:
        - user_answer (str): The user's response to the current question.
        - correct_answer (str): The correct answer to the current question.

        Prints a message indicating whether the answer is correct, the correct answer,
        and the player's current score.
        """
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
