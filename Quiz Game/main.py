"""
Quiz Application

This program implements a simple quiz game that loads questions from a data source,
presents them to the user, and tracks their score. It demonstrates object-oriented
programming principles by using separate classes for questions and quiz logic.

The program uses three main components:
- Question: A class that represents individual quiz questions
- QuizBrain: A class that handles the quiz logic and scoring
- question_data: A data structure containing the quiz questions and answers

Usage:
    Run this script directly to start the quiz. Questions will be presented one at a time,
    and the final score will be displayed upon completion.

Dependencies:
    - question_model.py: Contains the Question class definition
    - data.py: Contains the question_data list of dictionaries
    - quiz_brain.py: Contains the QuizBrain class definition
"""

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Initialize an empty list to store Question objects
question_bank = []

# Convert raw question data into Question objects
for question in question_data:
    # Extract question text and correct answer from the data dictionary
    question_text = question["question"]
    question_answer = question["correct_answer"]
    
    # Create a new Question object with the extracted data
    new_question = Question(question_text, question_answer)
    
    # Add the Question object to our question bank
    question_bank.append(new_question)

# Initialize the quiz with our prepared question bank
quiz = QuizBrain(question_bank)

# Main quiz loop - continue as long as there are questions remaining
while quiz.still_has_questions():
    quiz.next_question()  # Present the next question to the user

# Quiz completion messages
print("You've completed the quiz")  # Inform user that the quiz is finished
print(f"Your final score was: {quiz.score}/{quiz.question_number}")  # Display final score
